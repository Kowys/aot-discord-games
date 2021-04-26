import discord
import time
import random
import math
import sqlite3
import urllib
import numpy as np
import cv2
import os
from AttackonWikia import fetchURL

class State():
    def __init__(self):
        # Variables
        self.question_no = 0
        self.question_set = None
        self.clue_no = 0
        self.used_bonus_clue = False
        self.game_channel = None
        self.image = None
        self.image_hint = 0
        self.challenge = False
        self.hangman_challenge = False
        self.image_challenge = False
        self.players = []
        self.scores = [0,0]
        self.timer = 0
        self.correct = False
        self.letters_guessed = ''
        self.wrong_answers = 0
        self.wrong_letter = False
        self.extra_life = False

        # Constants
        self.intro_msg = discord.Embed(title = 'Game Reset!', description = 'Type `~new` to start a new puzzle.\n' + \
            'Type `~hangman` to start a new hangman game.\n' + \
            'Type `~image` to guess a new image.\n\n' + \
            'Type `~help` to see the list of available commands.', colour = 0xC0C0C0)
        # Appropriate msgs when ending question
        # Add "Type `~answer` during a question to reveal the correct answer."

        self.levelling_system = ([1,0],[2,1],[3,2],[4,3],[5,5],[6,7],[7,10],[8,13],[9,16],[10,20],[11,24],[12,28],[13,32],[14,36],[15,40],[16,45],[17,50],[18,55],[19,60],[20,66],[21,72],[22,78],[23,85],[24,92],[25,100],
        [26,108],[27,116],[28,124],[29,132],[30,141],[31,150],[32,160],[33,170],[34,180],[35,190],[36,200],[37,215],[38,230],[39,245],[40,260],[41,280],[42,300],[43,320],[44,350],[45,380],[46,410],[47,440],
        [48,480],[49,520],[50,560],[51,600],[52,650],[53,700],[54,750],[55,800],[56,875],[57,950],[58,1025],[59,1100],[60,1200],[61,1300],[62,1400],[63,1500],[64,1625],[65,1750],[66,1875],[67,2000],
        [68,2150],[69,2300],[70,2500],[71,2725],[72,2950],[73,3175],[74,3400],[75,3650],[76,3900],[77,4150],[78,4425],[79,4700],[80,5000],[81,5450],[82,5900],[83,6350],[84,6800],[85,7300],[86,7800],
        [87,8300],[88,8850],[89,9400],[90,10000],[91,10900],[92,11800],[93,12700],[94,13600],[95,14600],[96,15600],[97,16600],[98,17700],[99,18800],[100,20000],
        [101,21200],[102,21500],[103,22800],[104,24100],[105,24500],[106,25900],[107,27300],[108,28800],[109,30300],[110,31800],
        [111,33400],[112,35000],[113,36700],[114,38400],[115,40200],[116,42000],[117,43900],[118,45800],[119,47800],[120,50000])

        self.one_clue_achievements = {10:'Bronze', 25:'Silver', 80:'Gold', 150:'Platinum', 400:'Diamond', 750:'Master', 1500:'Grandmaster'}
        self.consecutive_days_achievements = {5:'Bronze', 14:'Silver', 30:'Gold', 60:'Platinum', 100:'Diamond', 200:'Master', 365:'Grandmaster'}
        self.challenge_achievements = {5:'Bronze', 15:'Silver', 30:'Gold', 50:'Platinum', 80:'Diamond', 150:'Master', 300:'Grandmaster'}
        self.hangman_achievements = {5:'Bronze', 15:'Silver', 50:'Gold', 100:'Platinum', 250:'Diamond', 500:'Master', 1000:'Grandmaster'}
        self.image_achievements = {5:'Bronze', 15:'Silver', 50:'Gold', 100:'Platinum', 250:'Diamond', 500:'Master', 1000:'Grandmaster'}

        self.achievement_rewards = {'Bronze': 20, 'Silver': 50, 'Gold': 100, 'Platinum': 150, 'Diamond': 300, 'Master':500, 'Grandmaster':1000}
        self.badge_emojis = {'Bronze': '🥉', 'Silver': '🥈', 'Gold': '🥇', 'Platinum': '💠', 'Diamond': '💎', 'Master': '👑', 'Grandmaster':'🎓'}

    # Methods
    def game_reset(self):
        self.question_no = 0
        self.question_set = None
        self.clue_no = 0
        self.used_bonus_clue = False
        self.game_channel = None
        self.image = None
        self.image_hint = 0
        self.challenge = False
        self.hangman_challenge = False
        self.image_challenge = False
        self.players = []
        self.scores = [0,0]
        self.timer = 0
        self.correct = False
        self.letters_guessed = ''
        self.wrong_answers = 0
        self.wrong_letter = False
        self.extra_life = False

    def game_active(self):
        return self.question_set != None or self.image != None or \
            self.challenge == True or self.hangman_challenge == True or self.image_challenge == True

    def get_new_question(self, msg_channel):
        self.game_reset()
        self.game_channel = msg_channel
        self.question_set = fetchURL.new_question()
        self.clue_no = 1
        # +1 to record of questions asked
        self.new_question()
        clue_contents = self.question_set['clues'][0] 
        fixed_clue_contents = clue_contents[1:] if clue_contents.startswith(' ') else clue_contents
        clue_msg = fixed_clue_contents + '\n\n' + 'Type `~clue` for the next hint. Type `~answer` to reveal the answer.'
        clue_embed = discord.Embed(title = 'Clue 1', description = clue_msg, colour = 0xC0C0C0)

        return clue_embed

    def get_clue(self):
        if self.question_set == None:
            return 'No puzzle is currently active!'
        elif len(self.question_set) == 2:
            return 'You can\'t use that in a hangman game!'
        elif 'clues' not in self.question_set:
            return 'You can\'t use that when guessing the image!'
        elif self.clue_no >= 5:
            return 'You have used up all the available clues!'
        else:
            self.clue_no += 1
            clue_contents = self.question_set['clues'][self.clue_no - 1]
            fixed_clue_contents = clue_contents[1:] if clue_contents.startswith(' ') else clue_contents
            if self.clue_no < 5:
                clue_msg = fixed_clue_contents + '\n\n' + 'Type `~clue` for the next hint. Type `~answer` to reveal the answer.'
            elif self.clue_no == 5:
                clue_msg = fixed_clue_contents + '\n\n' + 'Type `~answer` to reveal the answer.'
            clue_embed = discord.Embed(title = 'Clue ' + str(self.clue_no), description = clue_msg, colour = 0xC0C0C0)
            return clue_embed

    def get_bonus_clue(self, player):
        if self.question_set == None:
            return 'No puzzle is currently active!'
        elif len(self.question_set) == 2:
            return 'You can\'t use that in a hangman game!'
        elif 'clues' not in self.question_set:
            return 'You can\'t use that when guessing the image!'
        else:
            cur_level = self.get_player_level(player)
            if cur_level < 50 and player.id != 238808836075421697:
                return 'You need to be **Level 50** to use the bonus clue! (Type `~profile` to see your current level)'

            self.used_bonus_clue = True
            clue_contents = self.question_set['clues'][5]
            fixed_clue_contents = clue_contents[1:] if clue_contents.startswith(' ') else clue_contents
            if self.clue_no < 5:
                clue_msg = fixed_clue_contents + '\n\n' + 'Type `~clue` for the next hint. Type `~answer` to reveal the answer.'
            elif self.clue_no == 5:
                clue_msg = fixed_clue_contents + '\n\n' + 'Type `~answer` to reveal the answer.'
            clue_embed = discord.Embed(title = 'Bonus Clue', description = clue_msg, colour = 0xC0C0C0)
            return clue_embed

    def get_player_level(self, player):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        # Extract data
        get_player_data = 'SELECT * FROM players WHERE player = ?'
        cursor.execute(get_player_data, (player.id,))
        player_info = cursor.fetchone()

        if player_info is None:
            insert_player_data = 'INSERT INTO players VALUES (?,?,?,?,?,?,?)'
            player_data = [player.id, 0, 0, 0, 0, 0, 0]
            cursor.execute(insert_player_data, player_data)
            conn.commit()

            player_info = [player.id, 0, 0, 0, 0, 0, 0]

        conn.close()

        # Put info into embed
        for level in self.levelling_system:
            if player_info[1] < level[1]:
                next_exp = level[1] - player_info[1]
                break
            player_level = level[0]

        return player_level

    def populate_crops(self, img):
        # 4 different sizes: 0.2, 0.4, 0.6, 1.0
        # Corresponds to 3 hints
        folder_path = "AttackonWikia/images/{}".format(self.game_channel.id)
        os.makedirs(folder_path, exist_ok=True)

        filepath = os.path.join(folder_path, "image.jpg")
        cv2.imwrite(filepath, img)

        starting_coords = (random.uniform(0,1), random.uniform(0,1))
        for i, scale in enumerate([0.1, 0.2, 0.3]):
            x1, x2 = starting_coords[0] - scale, starting_coords[0] + scale
            if x1 < 0:
                x2 -= x1
                x1 = 0
            elif x2 > 1:
                x1 -= x2 - 1
                x2 = 1
            y1, y2 = starting_coords[1] - scale, starting_coords[1] + scale
            if y1 < 0:
                y2 -= y1
                y1 = 0
            elif y2 > 1:
                y1 -= y2 - 1
                y2 = 1

            h, w = img.shape[0], img.shape[1]
            crop_img = img[int(y1*h):int(y2*h), int(x1*w):int(x2*w)]
            filepath = os.path.join(folder_path, "image{}.jpg".format(i+1))
            cv2.imwrite(filepath, crop_img)

    def get_crop_image(self):
        folder_path = "AttackonWikia/images/{}".format(self.game_channel.id)
        filename = "image{}.jpg".format(self.image_hint + 1) if self.image_hint < 3 else "image.jpg"
        filepath = os.path.join(folder_path, filename)
        img_file = discord.File(filepath, filename=filename)
        return img_file

    def blacklistUrl(self, image_url):
        shortened_image_url = image_url.split('/')[-1]
        os.makedirs(os.path.join("AttackonWikia", "blacklist", shortened_image_url), exist_ok=True)

    def urlBlacklisted(self, image_url):
        base_path = "AttackonWikia/blacklist"
        os.makedirs(base_path, exist_ok=True)
        shortened_image_url = image_url.split('/')[-1]
        if shortened_image_url in os.listdir(base_path):
            return True
        else:
            return False

    def fromImageCache(self, image_url):
        os.makedirs("AttackonWikia/image_cache", exist_ok=True)

        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        image_cache_query = 'SELECT filename FROM cache WHERE url = ?'
        cursor.execute(image_cache_query, (image_url,))
        filename = cursor.fetchone()
        conn.commit()
        conn.close()

        if filename:
            filepath = os.path.join("AttackonWikia", "image_cache", filename[0])
            img = cv2.imread(filepath)
            return img
        else:
            return None

    def saveToCache(self, img, image_url):
        filename = image_url.split('/')[-1]
        filepath = os.path.join("AttackonWikia", "image_cache", filename)
        cv2.imwrite(filepath, img)

        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        image_cache_query = 'INSERT INTO cache VALUES (?,?)'
        image_values = [image_url, filename]
        cursor.execute(image_cache_query, image_values)
        conn.commit()
        conn.close()

    def populate_cache(self):
        for _ in range(10):
            self.question_set = fetchURL.new_image()
            image_url = self.question_set['image']
            if self.urlBlacklisted(image_url):
                continue

            img = self.fromImageCache(image_url)
            if img is None:
                try:
                    url_response = urllib.request.urlopen(image_url)
                except:
                    # Blacklist url
                    self.blacklistUrl(image_url)
                    return None
                try:
                    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                except:
                    self.blacklistUrl(image_url)
                    return None
                if img is None:
                    self.blacklistUrl(image_url)
                    return None
                
                self.saveToCache(img, image_url)

            return None
        
    def get_image(self, image_url):
        img = self.fromImageCache(image_url)
        if img is None:
            try:
                url_response = urllib.request.urlopen(image_url)
            except:
                # Blacklist url
                self.blacklistUrl(image_url)
                return None

            img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            if img is None:
                self.blacklistUrl(image_url)
                return None

            self.saveToCache(img, image_url)

        self.populate_crops(img)

        return self.get_crop_image()

    def fetch_new_image(self):
        self.question_set, image_file = None, None
        for _ in range(10):
            self.question_set = fetchURL.new_image()
            image_url = self.question_set['image']
            if self.urlBlacklisted(image_url):
                continue

            image_file = self.get_image(image_url)
            if self.question_set and image_file:
                break

        return image_file

    def get_new_image(self, msg_channel):
        self.game_reset()
        self.game_channel = msg_channel
        image_file = self.fetch_new_image()

        self.new_image_update()

        if self.image_hint < 3:
            hint_msg = 'Type `~hint` to reveal more of the image.\n'
        else:
            hint_msg = ''

        image_embed = discord.Embed(title = 'Guess the image!', description = hint_msg + 'Type `~answer` to reveal the answer.', colour = 0xC0C0C0)
        image_embed.set_image(url = "attachment://image1.jpg")
        return image_file, image_embed

    def get_image_hint(self):
        if self.question_set == None:
            return None, 'No puzzle is currently active!'
        elif len(self.question_set) == 2:
            return None, 'You can\'t use that in a hangman game!'
        elif 'clues' in self.question_set:
            return None, 'You can\'t use that in a regular puzzle!'
        elif self.image_hint >= 3:
            return None, 'You have already revealed the entire image!'
        else:
            self.image_hint += 1
            image_file = self.get_crop_image()

            if self.image_hint < 3:
                hint_msg = 'Type `~hint` to reveal more of the image.\n'
            else:
                hint_msg = ''

            image_embed = discord.Embed(title = 'Guess the image!', description = hint_msg + 'Type `~answer` to reveal the answer.', colour = 0xC0C0C0)
            image_embed.set_image(url = "attachment://{}".format(image_file.filename))
            return image_file, image_embed

    def get_new_image_challenge(self):
        image_file = self.get_image(self.question_set['image'])
        image_embed = discord.Embed(title = 'Image Mode', colour = 0xC0C0C0)
        image_embed.set_image(url = "attachment://image1.jpg")
        return image_file, image_embed

    def get_image_challenge_image(self):
        image_file = self.get_crop_image()
        image_embed = discord.Embed(title = 'Image Mode', colour = 0xC0C0C0)
        image_embed.set_image(url = "attachment://{}".format(image_file.filename))
        return image_file, image_embed

    def get_new_hangman(self, msg_channel):
        self.game_reset()
        self.game_channel = msg_channel
        self.question_set = fetchURL.new_hangman()
        # +1 to record of questions asked
        self.new_hangman_question()
        current_word = self.get_hangman_word()
        hangman_status = self.get_hangman_status()
        hangman_embed = discord.Embed(title = 'Hangman Mode', description = current_word + '\n\n' + hangman_status, colour = 0xC0C0C0)
        return hangman_embed

    def get_new_hangman_challenge(self):
        self.letters_guessed = ''
        current_word = self.get_hangman_word()
        hangman_embed = discord.Embed(title = 'Hangman Mode', description = current_word, colour = 0xC0C0C0)
        return hangman_embed

    def get_hangman_challenge_word(self):
        current_word = self.get_hangman_word()
        hangman_embed = discord.Embed(title = 'Hangman Mode', description = current_word, colour = 0xC0C0C0)
        return hangman_embed

    def hangman_reveal_letter(self):
        # Updates letters guessed with a randomly chosen letter
        valid_letters = list(filter(lambda x:x not in self.letters_guessed, self.question_set['title'].upper()))
        def remove_duplicates(word):
            all_letters = ''
            for i in word:
                if i not in all_letters:
                    all_letters += i
            return all_letters
        valid_letters = remove_duplicates(valid_letters)
        chosen_letter = valid_letters[random.randint(0, len(valid_letters)-1)]
        self.letters_guessed += chosen_letter + ' '
        
    def letter_guess_check(self, msg):
        if len(msg) != 1 or self.question_set == None:
            return False
        elif len(self.question_set) != 2:
            return False
        else:
            valid_letters = 'abcdefghijklmnopqrstuvwxyz'
            if msg.lower() in valid_letters:
                return True
            else:
                return False

    def letter_guess(self, letter, player):
        # Letter already used
        if letter.upper() in self.letters_guessed:
            self.wrong_letter = True

            description = '🔄 Letter `' + letter.upper() + '` has already been used. Please try again.'
            current_word = self.get_hangman_word()
            hangman_status = self.get_hangman_status()
            hangman_embed = discord.Embed(title = 'Hangman Mode', description = description + '\n' + current_word + '\n\n' + hangman_status, colour = 0xC0C0C0)
            hangman_embed.set_footer(text = self.letters_guessed)
            return hangman_embed
        
        # Correct letter
        elif letter.lower() in self.question_set['title'].lower():
            self.letters_guessed += letter.upper() + ' '
            # Word not completed
            if '◯' in self.get_hangman_word():
                description = '✅ ' + player.mention + ' has guessed a letter `' + letter.upper() + '`!'
                current_word = self.get_hangman_word()
                hangman_status = self.get_hangman_status()
                hangman_embed = discord.Embed(title = 'Hangman Mode', description = description + '\n' + current_word + '\n\n' + hangman_status, colour = 0xC0C0C0)
                hangman_embed.set_footer(text = self.letters_guessed)
                return hangman_embed

            # Word completed
            else:
                return self.correct_answer(player)

        # Wrong letter
        else:
            self.letters_guessed += letter.upper() + ' '
            self.wrong_letter = True
            self.wrong_answers += 1

            if self.wrong_answers < 6 + self.extra_life:
                description = '❌ Letter `' + letter.upper() + '` does not exist. Please try again.'
            else:
                description = '❌ Letter `' + letter.upper() + '` does not exist.'
            current_word = self.get_hangman_word()
            hangman_status = self.get_hangman_status()
            hangman_embed = discord.Embed(title = 'Hangman Mode', description = description + '\n' + current_word + '\n\n' + hangman_status, colour = 0xC0C0C0)
            hangman_embed.set_footer(text = self.letters_guessed)

            return hangman_embed

    def get_extra_life(self, player):
        if self.question_set == None:
            return 'No hangman game is currently active!', None
        elif 'clues' in self.question_set:
            return 'You can\'t use that in a puzzle game!', None
        elif 'image' in self.question_set:
            return 'You can\'t use that when guessing the image!', None
        else:
            cur_level = self.get_player_level(player)
            if cur_level < 75 and player.id != 238808836075421697:
                return 'You need to be **Level 75** to get an extra life! (Type `~profile` to see your current level)', None
            elif self.extra_life:
                return 'The current hangman game already has an extra life!', None

        self.extra_life = True

        current_word = self.get_hangman_word()
        hangman_status = self.get_hangman_status()
        hangman_embed = discord.Embed(title = 'Hangman Mode', description = current_word + '\n\n' + hangman_status, colour = 0xC0C0C0)
        hangman_embed.set_footer(text = self.letters_guessed)

        return 'An extra life has been added to the current hangman game!', hangman_embed

    def get_hangman_word(self):
        title = '`'
        for letter in self.question_set['title'].upper():
            if letter == ' ':
                title += ' \u2001 '
            elif letter in self.letters_guessed:
                title += letter + ' '
            else:
                title += '◯ '
 
        title += '`'
        return title

    def get_hangman_status(self):
        hangman_dict = {
            0: '⠀🇲 \u2001\u2004🇷 \u2001 🇸\n🏡🏡 🏠🏠 🏰🏰',
            1: '⠀🇲 \u2001\u2004🇷 \u2001 🇸\n💥🏡 🏠🏠 🏰🏰',
            2: '⠀🇲 \u2001\u2004🇷 \u2001 🇸\n💥💥 🏠🏠 🏰🏰',
            3: '⠀🇲 \u2001\u2004🇷 \u2001 🇸\n💥💥 💥🏠 🏰🏰',
            4: '⠀🇲 \u2001\u2004🇷 \u2001 🇸\n💥💥 💥💥 🏰🏰',
            5: '⠀🇲 \u2001\u2004🇷 \u2001 🇸\n💥💥 💥💥 💥🏰',
            6: '⠀🇲 \u2001\u2004🇷 \u2001 🇸\n💥💥 💥💥 💥💥',
            7: '⠀🇲 \u2001\u2004🇷 \u2001 🇸\n💥💥 💥💥 💥💥'
        }
        hangman_status = hangman_dict[self.wrong_answers]
        if self.extra_life:
            if self.wrong_answers < 7:
                hangman_status += ' 🏯'
            else:
                hangman_status += ' 💥'
        return hangman_status

    def get_end_question_msg(self):
        if len(self.question_set) == 3:
            if 'image' in self.question_set:
                return 'Type `~image` to guess a new image. Type `~help` to see the list of available commands.'
            else:
                return 'Type `~new` to start a new puzzle. Type `~help` to see the list of available commands.'
        elif len(self.question_set) == 2:
            return 'Type `~hangman` to start a new hangman game. Type `~help` to see the list of available commands.'

    def get_answer(self):
        answer_msgs = []
        if self.question_set == None:
            answer_msgs.append('No puzzle is currently active!')
        else:
            if self.wrong_answers >= 6:
                answer_msgs.append('Hangman! The page is **' + self.question_set['title'] + ' !**')
            else:
                answer_msgs.append('The page is **' + self.question_set['title'] + ' !**')
            answer_msgs.append(self.question_set['url'])
            end_question_msg = self.get_end_question_msg()
            answer_msgs.append(end_question_msg)
            self.game_reset()

        return answer_msgs

    def correct_answer(self, player):
        correct_answer_msgs = []
        correct_answer_msgs.append('Correct! The page is **' + self.question_set['title'] + ' !**')
        correct_answer_msgs.append(self.question_set['url'])

        end_question_msg = self.get_end_question_msg()
        correct_answer_msgs.append(end_question_msg)
        
        # Update player records
        level_update = self.update_player_records(player)
        if level_update != None:
            correct_answer_msgs.append(level_update)

        # Log result in achievements and sends message if obtained achievement
        achievements = self.log_achievements(player)
        for achievement in achievements:
            correct_answer_msgs.append(achievement)

        # Update dailies
        dailies = self.update_dailies(player)
        for daily in dailies:
            correct_answer_msgs.append(daily)

        # +1 to global record of correct questions
        if len(self.question_set) == 3:
            if 'image' in self.question_set:
                self.correct_image()
            else:
                self.correct_question()
        elif len(self.question_set) == 2:
            self.correct_hangman_question()

        self.game_reset()

        return correct_answer_msgs

    def new_challenge(self, msg_channel):
        self.challenge = True
        self.game_channel = msg_channel
        self.question_no = 1
        if self.hangman_challenge == True:
            # clue_no stays at 0
            self.question_set = fetchURL.new_hangman()
        elif self.image_challenge == True:
            self.question_set = fetchURL.new_image()
            self.image_hint = 0
        else:
            self.question_set = fetchURL.new_question()
            self.clue_no = 1

    def next_question(self):
        if self.hangman_challenge == True:
            self.question_set = fetchURL.new_hangman()
        elif self.image_challenge == True:
            self.question_set = fetchURL.new_image()
            self.image_hint = 0
        else:
            self.question_set = fetchURL.new_question()
            self.clue_no = 1
        self.timer = 0
        self.correct = False

    def new_question(self):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        get_question_query = 'SELECT questions_asked FROM overall'
        cursor.execute(get_question_query)
        question_info = cursor.fetchone()

        update_question_query = 'UPDATE overall SET questions_asked = ?'
        cursor.execute(update_question_query, (question_info[0] + 1,))
        
        conn.commit()
        conn.close()

    def correct_question(self):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        get_question_query = 'SELECT questions_correct FROM overall'
        cursor.execute(get_question_query)
        question_info = cursor.fetchone()

        update_question_query = 'UPDATE overall SET questions_correct = ?'
        cursor.execute(update_question_query, (question_info[0] + 1,))
        
        conn.commit()
        conn.close()

    def new_hangman_question(self):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        get_hangman_query = 'SELECT hangman_games_played FROM overall'
        cursor.execute(get_hangman_query)
        hangman_info = cursor.fetchone()

        update_hangman_query = 'UPDATE overall SET hangman_games_played = ?'
        cursor.execute(update_hangman_query, (hangman_info[0] + 1,))
        
        conn.commit()
        conn.close()

    def correct_hangman_question(self):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        get_hangman_query = 'SELECT hangman_games_won FROM overall'
        cursor.execute(get_hangman_query)
        hangman_info = cursor.fetchone()

        update_hangman_query = 'UPDATE overall SET hangman_games_won = ?'
        cursor.execute(update_hangman_query, (hangman_info[0] + 1,))
        
        conn.commit()
        conn.close()

    def new_image_update(self):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        get_image_query = 'SELECT images_generated FROM overall'
        cursor.execute(get_image_query)
        image_info = cursor.fetchone()

        update_image_query = 'UPDATE overall SET images_generated = ?'
        cursor.execute(update_image_query, (image_info[0] + 1,))
        
        conn.commit()
        conn.close()

    def correct_image(self):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        get_image_query = 'SELECT images_correct FROM overall'
        cursor.execute(get_image_query)
        image_info = cursor.fetchone()

        update_image_query = 'UPDATE overall SET images_correct = ?'
        cursor.execute(update_image_query, (image_info[0] + 1,))
        
        conn.commit()
        conn.close()

    def new_challenge_qn(self):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        get_challenge_query = 'SELECT questions_asked, challenge_questions, hangman_games_played, images_generated FROM overall'
        cursor.execute(get_challenge_query)
        challenge_info = cursor.fetchone()

        update_challenge_query = 'UPDATE overall SET questions_asked = ?, challenge_questions = ?, hangman_games_played = ?, images_generated = ?'
        if self.hangman_challenge == True:
            update_challenge_data = [challenge_info[0], challenge_info[1] + 1, challenge_info[2] + 1, challenge_info[3]]
        elif self.image_challenge == True:
            update_challenge_data = [challenge_info[0], challenge_info[1] + 1, challenge_info[2], challenge_info[3] + 1]
        else:
            update_challenge_data = [challenge_info[0] + 1, challenge_info[1] + 1, challenge_info[2], challenge_info[3]]

        cursor.execute(update_challenge_query, update_challenge_data)

        conn.commit()
        conn.close()

    def correct_challenge_qn(self):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        get_challenge_query = 'SELECT questions_correct, challenge_questions_correct, hangman_games_won, images_correct FROM overall'
        cursor.execute(get_challenge_query)
        challenge_info = cursor.fetchone()

        update_challenge_query = 'UPDATE overall SET questions_correct = ?, challenge_questions_correct = ?, hangman_games_won = ?, images_correct = ?'
        if self.hangman_challenge == True:
            update_challenge_data = [challenge_info[0], challenge_info[1] + 1, challenge_info[2] + 1, challenge_info[3]]
        elif self.image_challenge == True:
            update_challenge_data = [challenge_info[0], challenge_info[1] + 1, challenge_info[2], challenge_info[3] + 1]
        else:
            update_challenge_data = [challenge_info[0] + 1, challenge_info[1] + 1, challenge_info[2], challenge_info[3]]

        cursor.execute(update_challenge_query, update_challenge_data)

        conn.commit()
        conn.close()

    def finish_challenge(self):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        get_challenge_query = 'SELECT challenges_completed FROM overall'
        cursor.execute(get_challenge_query)
        challenge_info = cursor.fetchone()

        update_challenge_query = 'UPDATE overall SET challenges_completed = ?'
        cursor.execute(update_challenge_query, (challenge_info[0] + 1,))
        
        conn.commit()
        conn.close()

    def update_player_records(self, user_obj):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        # Extract data
        get_player_data = 'SELECT * FROM players WHERE player = ?'
        cursor.execute(get_player_data, (user_obj.id,))
        player_info = cursor.fetchone()

        if player_info:
            # Old player level
            for level in self.levelling_system:
                if player_info[1] < level[1]:
                    break
                old_player_level = level[0]

            # +1 to exp and correct answers
            update_player_exp = 'UPDATE players SET exp = ? WHERE player = ?'
            cursor.execute(update_player_exp, (player_info[1] + 1, user_obj.id))

            if len(self.question_set) == 3:
                if 'image' in self.question_set:
                    # Image
                    update_player_images = 'UPDATE players SET images_correct = ? WHERE player = ?'
                    cursor.execute(update_player_images, (player_info[6] + 1, user_obj.id))
                else:
                    # Regular
                    update_player_answers = 'UPDATE players SET correct_answers = ? WHERE player = ?'
                    cursor.execute(update_player_answers, (player_info[2] + 1, user_obj.id))
            elif len(self.question_set) == 2:
                # Hangman
                update_player_hangman = 'UPDATE players SET hangman_correct = ? WHERE player = ?'
                cursor.execute(update_player_hangman, (player_info[5] + 1, user_obj.id))

            # New player level
            for level in self.levelling_system:
                if player_info[1] + 1 < level[1]:
                    break
                new_player_level = level[0]

            conn.commit()
            conn.close()

            if new_player_level > old_player_level:
                return '🆙 | Congratulations ' + user_obj.mention + '! You have reached level **' + str(new_player_level) + '**!'
            else:
                return None

        else:
            insert_player = 'INSERT INTO players VALUES (?,?,?,?,?,?,?)'
            if len(self.question_set) == 3:
                if 'image' in self.question_set:
                    # Image
                    player_data = [user_obj.id, 1, 0, 0, 0, 0, 1]
                    cursor.execute(insert_player, player_data)
                else:
                    # Regular
                    player_data = [user_obj.id, 1, 1, 0, 0, 0, 0]
                    cursor.execute(insert_player, player_data)

            elif len(self.question_set) == 2:
                # Hangman
                player_data = [user_obj.id, 1, 0, 0, 0, 1, 0]
                cursor.execute(insert_player, player_data)

            conn.commit()
            conn.close()

            return '🆙 | Congratulations ' + user_obj.mention + '! You have reached level **2**!'

    def get_score(self, num):
        score = self.scores[num]
        if score == 0:
            return '⬛ ⬛ ⬛'
        elif score == 1:
            return '✅ ⬛ ⬛'
        elif score == 2:
            return '✅ ✅ ⬛'
        elif score == 3:
            return '✅ ✅ ✅'

    def get_scoreboard(self):
        scoreboard = discord.Embed(title='Scores\n', colour=0xB4B4B4)
        scoreboard.add_field(name = self.players[0].name, value = self.get_score(0)) 
        scoreboard.add_field(name = self.players[1].name, value = self.get_score(1)) 
        return scoreboard

    def get_winner(self):
        winner_index = 0 if self.scores[0] >= 3 else 1
        loser_index = 1 if self.scores[0] >= 3 else 0
        players = [self.players[winner_index], self.players[loser_index]]

        scoreboard = discord.Embed(title='🏆 The winner is **' + players[0].name + '**! 🏆', colour=0xB4B4B4)
        scoreboard.set_thumbnail(url = players[0].avatar_url)
        scoreboard.add_field(name = self.players[0].name, value = self.get_score(0)) 
        scoreboard.add_field(name = self.players[1].name, value = self.get_score(1)) 
        return scoreboard

    def challenge_update_player_records(self):
        winner_index = 0 if self.scores[0] >= 3 else 1
        loser_index = 1 if self.scores[0] >= 3 else 0
        players = [self.players[winner_index], self.players[loser_index]]

        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        level_updates = []

        j = 0
        for player in players:
            j += 1
            # Extract data
            get_player_data = 'SELECT * FROM players WHERE player = ?'
            cursor.execute(get_player_data, (player.id,))
            player_info = cursor.fetchone()

            if player_info:
                # Old player level
                for level in self.levelling_system:
                    if player_info[1] < level[1]:
                        break
                    old_player_level = level[0]
    
                # Add to exp and challenge won/completed
                update_challenge_stats_query = 'UPDATE players SET exp = ?, challenges_played = ?, challenges_won = ? WHERE player = ?'
                if j == 1:
                    new_exp = player_info[1] + 10
                    update_challenge_stats = [new_exp, player_info[3] + 1, player_info[4] + 1, player.id]
                elif j == 2:
                    new_exp = player_info[1] + 5
                    update_challenge_stats = [new_exp, player_info[3] + 1, player_info[4], player.id]

                cursor.execute(update_challenge_stats_query, update_challenge_stats)
                conn.commit()

                # New player level
                for level in self.levelling_system:
                    if new_exp < level[1]:
                        break
                    new_player_level = level[0]

                if new_player_level > old_player_level:
                    level_updates.append('🆙 | Congratulations ' + player.mention + '! You have reached level **' + str(new_player_level) + '**!') 

            else:
                insert_challenge_stats_query = 'INSERT INTO players VALUES (?,?,?,?,?,?,?)'
                insert_challenge_stats = [player.id, 5, 0, 1, 0, 0, 0]
                cursor.execute(insert_challenge_stats_query, insert_challenge_stats)
                conn.commit()

                level_updates.append('🆙 | Congratulations ' + player.mention + '! You have reached level **5**!')

        conn.close()

        return level_updates

    def update_dailies(self, player=None):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()
        cur_date = str(time.gmtime().tm_year) + '-' + str(time.gmtime().tm_mon) + '-' + str(time.gmtime().tm_mday)
        cur_dailies = []

        if player:
            # Extract data
            get_dailies_query = 'SELECT * FROM dailies WHERE player = ?'
            cursor.execute(get_dailies_query, (player.id,))
            dailies_info = cursor.fetchone()

            get_player_data = 'SELECT * FROM players WHERE player = ?'
            cursor.execute(get_player_data, (player.id,))
            player_data = cursor.fetchone()

            if dailies_info:
                prev_date = dailies_info[1]
                standard_dailies, hangman_dailies, image_dailies = dailies_info[2], dailies_info[3], dailies_info[5]
                # Still same day
                if cur_date == prev_date:
                    if len(self.question_set) == 3:
                        # Image question
                        if 'image' in self.question_set:
                            image_dailies += 1
                            update_image_dailies = 'UPDATE dailies SET image = ? WHERE player = ?'
                            cursor.execute(update_image_dailies, (image_dailies, player.id))
                        # Normal question
                        else:
                            standard_dailies += 1
                            update_standard_dailies = 'UPDATE dailies SET standard = ? WHERE player = ?'
                            cursor.execute(update_standard_dailies, (standard_dailies, player.id))
                    # Hangman
                    else:
                        hangman_dailies += 1
                        update_hangman_dailies = 'UPDATE dailies SET hangman = ? WHERE player = ?'
                        cursor.execute(update_hangman_dailies, (hangman_dailies, player.id))

                    conn.commit()
                        
                    # Award daily if reached 10 points
                    if (len(self.question_set) == 3 and 'image' not in self.question_set and standard_dailies == 10) or \
                    (len(self.question_set) == 2 and hangman_dailies == 10) or \
                    (len(self.question_set) == 3 and 'image' in self.question_set and image_dailies == 10):
                        # Daily reward msg
                        if len(self.question_set) == 3:
                            if 'image' in self.question_set:
                                daily_reward_msg = '☑ | Congratulations, ' + player.mention + ', you have completed the Images daily task! **(+15 Exp)**'
                            else:
                                daily_reward_msg = '☑ | Congratulations, ' + player.mention + ', you have completed the standard games daily task! **(+15 Exp)**'
                        else:
                            daily_reward_msg = '☑ | Congratulations, ' + player.mention + ', you have completed the Hangman daily task! **(+15 Exp)**'
                        cur_dailies.append(daily_reward_msg)

                        # Add exp to player (Assume player data already exists, from update_player_records method)
                        player_exp = player_data[1]
                        # Old player level
                        for level in self.levelling_system:
                            if player_exp < level[1]:
                                break
                            old_player_level = level[0]

                        # Add exp
                        player_exp = player_exp + 15
                        update_player_exp_query = 'UPDATE players SET exp = ? WHERE player = ?'
                        cursor.execute(update_player_exp_query, (player_exp, player.id))
                        conn.commit()

                        # New player level
                        for level in self.levelling_system:
                            if player_exp < level[1]:
                                break
                            new_player_level = level[0]

                        if new_player_level > old_player_level:
                            cur_dailies.append('🆙 | Congratulations ' + player.mention + '! You have reached level **' + str(new_player_level) + '**!')

                # New day, reset
                else:
                    reset_dailies_query = 'UPDATE dailies SET last_play = ?, standard = ?, hangman = ?, challenge = ?, image = ? WHERE player = ?'
                    if len(self.question_set) == 3:
                        if 'image' in self.question_set:
                            reset_dailies = [cur_date, 0, 0, 0, 1, player.id]
                        else:
                            reset_dailies = [cur_date, 1, 0, 0, 0, player.id]
                    else:
                        reset_dailies = [cur_date, 0, 1, 0, 0, player.id]

                    cursor.execute(reset_dailies_query, reset_dailies)
                    conn.commit()

            else:
                insert_player_dailies_query = 'INSERT INTO dailies VALUES (?,?,?,?,?,?)'
                if len(self.question_set) == 3:
                    # Image
                    if 'image' in self.question_set:
                        insert_player_dailies = [player.id, cur_date, 0, 0, 0, 1]
                    # Normal question
                    else:
                        insert_player_dailies = [player.id, cur_date, 1, 0, 0, 0]
                # Hangman
                else:
                    insert_player_dailies = [player.id, cur_date, 0, 1, 0, 0]

                cursor.execute(insert_player_dailies_query, insert_player_dailies)
                conn.commit()

        # Challenge completed, both players
        else:
            for player in self.players:
                # Extract data
                get_dailies_query = 'SELECT * FROM dailies WHERE player = ?'
                cursor.execute(get_dailies_query, (player.id,))
                dailies_info = cursor.fetchone()

                get_player_data = 'SELECT * FROM players WHERE player = ?'
                cursor.execute(get_player_data, (player.id,))
                player_data = cursor.fetchone()

                if dailies_info:
                    prev_date = dailies_info[1]
                    challenge_dailies = dailies_info[4]
                    # Still same day
                    if cur_date == prev_date:
                        challenge_dailies += 1
                        update_challenge_dailies = 'UPDATE dailies SET challenge = ? WHERE player = ?'
                        cursor.execute(update_challenge_dailies, (challenge_dailies, player.id))

                    # New day, reset
                    else:
                        challenge_dailies = 1
                        reset_dailies_query = 'UPDATE dailies SET last_play = ?, standard = ?, hangman = ?, challenge = ?, image = ? WHERE player = ?'
                        reset_dailies = [cur_date, 0, 0, 1, 0, player.id]
                        cursor.execute(reset_dailies_query, reset_dailies)
                    
                    conn.commit()

                    # Award daily, by default
                    if challenge_dailies == 1:
                        daily_reward_msg = '☑ | Congratulations, ' + player.mention + ', you have completed the Challenge daily task! **(+25 Exp)**'
                        cur_dailies.append(daily_reward_msg)

                        # Add exp to player (Assume player data already exists, from update_player_records method)
                        player_exp = player_data[1]
                        # Old player level
                        for level in self.levelling_system:
                            if player_exp < level[1]:
                                break
                            old_player_level = level[0]

                        # Add exp
                        player_exp = player_exp + 25
                        update_player_exp_query = 'UPDATE players SET exp = ? WHERE player = ?'
                        cursor.execute(update_player_exp_query, (player_exp, player.id))
                        conn.commit()

                        # New player level
                        for level in self.levelling_system:
                            if player_exp < level[1]:
                                break
                            new_player_level = level[0]

                        if new_player_level > old_player_level:
                            cur_dailies.append('🆙 | Congratulations ' + player.mention + '! You have reached level **' + str(new_player_level) + '**!')

                else:
                    insert_player_dailies_query = 'INSERT INTO dailies VALUES (?,?,?,?,?,?)'
                    insert_player_dailies = [player.id, cur_date, 0, 0, 1, 0]

                    cursor.execute(insert_player_dailies_query, insert_player_dailies)
                    conn.commit()

                    # Award daily, by default
                    daily_reward_msg = '☑ | Congratulations, ' + player.mention + ', you have completed the Challenge daily task! **(+25 Exp)**'
                    cur_dailies.append(daily_reward_msg)

                    # Add exp to player (Assume player data already exists, from update_player_records method)
                    player_exp = player_data[1]
                    # Old player level
                    for level in self.levelling_system:
                        if player_exp < level[1]:
                            break
                        old_player_level = level[0]

                    # Add exp
                    player_exp = player_exp + 25
                    update_player_exp_query = 'UPDATE players SET exp = ? WHERE player = ?'
                    cursor.execute(update_player_exp_query, (player_exp, player.id))
                    conn.commit()

                    # New player level
                    for level in self.levelling_system:
                        if player_exp < level[1]:
                            break
                        new_player_level = level[0]

                    if new_player_level > old_player_level:
                        cur_dailies.append('🆙 | Congratulations ' + player.mention + '! You have reached level **' + str(new_player_level) + '**!')

        conn.close()

        return cur_dailies
    
    def next_day_check(self, last_date, cur_date):
        endday = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        last = list(map(lambda x: int(x), last_date.split('-')))
        cur = list(map(lambda x: int(x), cur_date.split('-')))
        if cur[2] - last[2] == 1:
            return True
        elif cur[1] - last[1] == 1 and (cur[2] == 1 and last[2] >= endday[last[1]]):
            return True
        elif cur[0] - last[0] == 1 and (cur[1] == 1 and cur[2] == 1) and (last[1] == 12 and last[2] == 31):
            return True
        else:
            return False

    def log_achievements(self, player):
        # Increment achievements progress for questions and returns achievement messages if any
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        # Extract data
        achievements_query = 'SELECT * FROM achievements WHERE player = ?'
        cursor.execute(achievements_query, (player.id,))
        player_achievements = cursor.fetchone()

        player_data_query = 'SELECT player, exp FROM players WHERE player = ?'
        cursor.execute(player_data_query, (player.id,))
        player_data = cursor.fetchone()

        achievement_msgs = []
        # 1 clue
        if self.clue_no == 1 and self.used_bonus_clue == False:
            if player_achievements:
                new_clue_value = player_achievements[1] + 1
                update_clue_achievements_query = 'UPDATE achievements SET one_clue = ? WHERE player = ?'
                cursor.execute(update_clue_achievements_query, (new_clue_value, player.id))
            else:
                new_clue_value = 1
                cur_date = str(time.gmtime().tm_year) + '-' + str(time.gmtime().tm_mon) + '-' + str(time.gmtime().tm_mday)
                insert_clue_achievements_query = 'INSERT INTO achievements VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
                insert_clue_achievements_values = [player.id, new_clue_value, 0, cur_date, 1, 1, 0, 0, 0, 0, 0, 0]
                cursor.execute(insert_clue_achievements_query, insert_clue_achievements_values)

            conn.commit()

            # If achievement earned, add exp and append achievement msg
            if new_clue_value in self.one_clue_achievements or (new_clue_value > 1500 and player_achievements[7] == 0):
                achievement_value = new_clue_value
                if new_clue_value >= 1500 and player_achievements[7] == 0:
                    update_clue_achievements_query = 'UPDATE achievements SET one_clue_gm = ? WHERE player = ?'
                    cursor.execute(update_clue_achievements_query, (1, player.id))
                    conn.commit()
                    achievement_value = 1500

                # Achievement msg
                one_clue = self.badge_emojis[self.one_clue_achievements[achievement_value]] + ' | Congratulations ' + player.mention + \
                '! You have obtained ' + ('a ' if 'Master' not in self.one_clue_achievements[achievement_value] else 'the ') + '**' + \
                self.one_clue_achievements[achievement_value] + (' of Archives' if 'Master' in self.one_clue_achievements[achievement_value] else '') + \
                '** badge for answering **' + str(achievement_value) + '** questions correctly with only 1 clue! **(+' + \
                str(self.achievement_rewards[self.one_clue_achievements[achievement_value]]) + ' Exp)**'
                
                achievement_msgs.append(one_clue)

                # Add exp to player (Assume player data already exists, from update_player_records method)
                player_exp = player_data[1]
                # Old player level
                for level in self.levelling_system:
                    if player_exp < level[1]:
                        break
                    old_player_level = level[0]

                # Add exp
                player_exp = player_exp + self.achievement_rewards[self.one_clue_achievements[achievement_value]]
                update_player_exp_query = 'UPDATE players SET exp = ? WHERE player = ?'
                cursor.execute(update_player_exp_query, (player_exp, player.id))
                conn.commit()

                # New player level
                for level in self.levelling_system:
                    if player_exp < level[1]:
                        break
                    new_player_level = level[0]

                if new_player_level > old_player_level:
                    achievement_msgs.append('🆙 | Congratulations ' + player.mention + '! You have reached level **' + str(new_player_level) + '**!')

        # Perfect hangman
        if len(self.question_set) == 2 and self.wrong_answers == 0 and self.challenge == False:
            if player_achievements:
                new_hangman_value = player_achievements[6] + 1
                update_hangman_achievements_query = 'UPDATE achievements SET perfect_hangman = ? WHERE player = ?'
                cursor.execute(update_hangman_achievements_query, (new_hangman_value, player.id))
            else:
                new_hangman_value = 1
                cur_date = str(time.gmtime().tm_year) + '-' + str(time.gmtime().tm_mon) + '-' + str(time.gmtime().tm_mday)
                insert_hangman_achievements_query = 'INSERT INTO achievements VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
                insert_hangman_achievements_values = [player.id, 0, 0, cur_date, 1, 1, new_hangman_value, 0, 0, 0, 0, 0]
                cursor.execute(insert_hangman_achievements_query, insert_hangman_achievements_values)

            conn.commit()

            # If achievement earned, add exp and append achievement msg
            if new_hangman_value in self.hangman_achievements or (new_hangman_value > 1000 and player_achievements[10] == 0):
                achievement_value = new_hangman_value
                if new_hangman_value >= 1000 and player_achievements[10] == 0:
                    update_hangman_achievements_query = 'UPDATE achievements SET hangman_gm = ? WHERE player = ?'
                    cursor.execute(update_hangman_achievements_query, (1, player.id))
                    conn.commit()
                    achievement_value = 1000

                # Achievement msg
                hangman_msg = self.badge_emojis[self.hangman_achievements[achievement_value]] + ' | Congratulations ' + player.mention + \
                '! You have obtained ' + ('a ' if 'Master' not in self.hangman_achievements[achievement_value] else 'the ') + '**' + \
                self.hangman_achievements[achievement_value] + (' of Hangman' if 'Master' in self.hangman_achievements[achievement_value] else '') + \
                '** badge for winning **' + str(achievement_value) + '** hangman games without any mistakes! **(+' + \
                str(self.achievement_rewards[self.hangman_achievements[achievement_value]]) + ' Exp)**'
                
                achievement_msgs.append(hangman_msg)

                # Add exp to player (Assume player data already exists, from update_player_records method)
                player_exp = player_data[1]
                # Old player level
                for level in self.levelling_system:
                    if player_exp < level[1]:
                        break
                    old_player_level = level[0]

                # Add exp
                player_exp = player_exp + self.achievement_rewards[self.hangman_achievements[achievement_value]]
                update_player_exp_query = 'UPDATE players SET exp = ? WHERE player = ?'
                cursor.execute(update_player_exp_query, (player_exp, player.id))
                conn.commit()

                # New player level
                for level in self.levelling_system:
                    if player_exp < level[1]:
                        break
                    new_player_level = level[0]

                if new_player_level > old_player_level:
                    achievement_msgs.append('🆙 | Congratulations ' + player.mention + '! You have reached level **' + str(new_player_level) + '**!')

        # No hint image 
        if 'image' in self.question_set and self.image_hint == 0:
            if player_achievements:
                new_image_value = player_achievements[11] + 1
                update_image_achievements_query = 'UPDATE achievements SET no_hint_image = ? WHERE player = ?'
                cursor.execute(update_image_achievements_query, (new_image_value, player.id))
            else:
                new_image_value = 1
                cur_date = str(time.gmtime().tm_year) + '-' + str(time.gmtime().tm_mon) + '-' + str(time.gmtime().tm_mday)
                insert_image_achievements_query = 'INSERT INTO achievements VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
                insert_image_achievements_values = [player.id, 0, 0, cur_date, 1, 1, 0, 0, 0, 0, 0, new_image_value]
                cursor.execute(insert_image_achievements_query, insert_image_achievements_values)

            conn.commit()

            # If achievement earned, add exp and append achievement msg
            if new_image_value in self.image_achievements:
                achievement_value = new_image_value
                # Achievement msg
                image_msg = self.badge_emojis[self.image_achievements[achievement_value]] + ' | Congratulations ' + player.mention + \
                '! You have obtained ' + ('a ' if 'Master' not in self.image_achievements[achievement_value] else 'the ') + '**' + \
                self.image_achievements[achievement_value] + (' of Images' if 'Master' in self.image_achievements[achievement_value] else '') + \
                '** badge for guessing **' + str(achievement_value) + '** images correctly without any hints! **(+' + \
                str(self.achievement_rewards[self.image_achievements[achievement_value]]) + ' Exp)**'
                
                achievement_msgs.append(image_msg)

                # Add exp to player (Assume player data already exists, from update_player_records method)
                player_exp = player_data[1]
                # Old player level
                for level in self.levelling_system:
                    if player_exp < level[1]:
                        break
                    old_player_level = level[0]

                # Add exp
                player_exp = player_exp + self.achievement_rewards[self.image_achievements[achievement_value]]
                update_player_exp_query = 'UPDATE players SET exp = ? WHERE player = ?'
                cursor.execute(update_player_exp_query, (player_exp, player.id))
                conn.commit()

                # New player level
                for level in self.levelling_system:
                    if player_exp < level[1]:
                        break
                    new_player_level = level[0]

                if new_player_level > old_player_level:
                    achievement_msgs.append('🆙 | Congratulations ' + player.mention + '! You have reached level **' + str(new_player_level) + '**!')

        # Consecutive days
        if player_achievements:
            cur_date = str(time.gmtime().tm_year) + '-' + str(time.gmtime().tm_mon) + '-' + str(time.gmtime().tm_mday)
            last_date = player_achievements[3]
            if cur_date != last_date:
                # Update newest date
                update_new_date_query = 'UPDATE achievements SET last_play = ? WHERE player = ?'
                cursor.execute(update_new_date_query, (cur_date, player.id))
                conn.commit()

                # 1 day
                if self.next_day_check(last_date, cur_date):
                    new_streak_value = player_achievements[4] + 1
                    update_streak_achievements_query = 'UPDATE achievements SET current_streak = ? WHERE player = ?'
                    cursor.execute(update_streak_achievements_query, (new_streak_value, player.id))
                    conn.commit()

                    if new_streak_value > player_achievements[5]:
                        # New max streak
                        update_max_streak_achievements_query = 'UPDATE achievements SET max_streak = ? WHERE player = ?'
                        cursor.execute(update_max_streak_achievements_query, (new_streak_value, player.id))
                        conn.commit()
                    
                        # If achievement earned, add exp and append achievement msg
                        if new_streak_value in self.consecutive_days_achievements or (new_streak_value > 365 and player_achievements[9] == 0):
                            achievement_value = new_streak_value
                            if new_streak_value >= 365 and player_achievements[9] == 0:
                                update_streak_gm_achievements_query = 'UPDATE achievements SET streak_gm = ? WHERE player = ?'
                                cursor.execute(update_streak_gm_achievements_query, (1, player.id))
                                conn.commit()
                                achievement_value = 365

                            # Achievement msg
                            consecutive = self.badge_emojis[self.consecutive_days_achievements[achievement_value]] + ' | Congratulations ' + player.mention + \
                            '! You have obtained a **' + self.consecutive_days_achievements[achievement_value] + '** badge for playing the game every day for **' + \
                            str(achievement_value) + '** days! **(+' + str(self.achievement_rewards[self.consecutive_days_achievements[achievement_value]]) + ' Exp)**'
                            
                            achievement_msgs.append(consecutive)

                            # Add exp to player (Assume player data already exists, from update_player_records method)
                            player_exp = player_data[1]
                            # Old player level
                            for level in self.levelling_system:
                                if player_exp < level[1]:
                                    break
                                old_player_level = level[0]

                            # Add exp
                            player_exp = player_exp + self.achievement_rewards[self.consecutive_days_achievements[achievement_value]]
                            update_player_exp_query = 'UPDATE players SET exp = ? WHERE player = ?'
                            cursor.execute(update_player_exp_query, (player_exp, player.id))
                            conn.commit()

                            # New player level
                            for level in self.levelling_system:
                                if player_exp < level[1]:
                                    break
                                new_player_level = level[0]

                            if new_player_level > old_player_level:
                                achievement_msgs.append('🆙 | Congratulations ' + player.mention + '! You have reached level **' + str(new_player_level) + '**!')

                # > 1 day, reset streak
                else:
                    reset_streak_query = 'UPDATE achievements SET last_play = ?, current_streak = 1 WHERE player = ?'
                    cursor.execute(reset_streak_query, (cur_date, player.id))
                    conn.commit()
        else:
            cur_date = str(time.gmtime().tm_year) + '-' + str(time.gmtime().tm_mon) + '-' + str(time.gmtime().tm_mday)
            insert_consecutive_achievements_query = 'INSERT INTO achievements VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
            insert_consecutive_achievements_values = [player.id, 0, 0, cur_date, 1, 1, 0, 0, 0, 0, 0, 0]
            cursor.execute(insert_consecutive_achievements_query, insert_consecutive_achievements_values)
            conn.commit()
        
        conn.close()

        return achievement_msgs

    def log_challenge_achievements(self):
        winner_index = 0 if self.scores[0] >= 3 else 1
        loser_index = 1 if self.scores[0] >= 3 else 0
        players = [self.players[winner_index], self.players[loser_index]]

        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        achievement_msgs = []

        for player in players:
            # Extract data
            get_player_achievements_query = 'SELECT * FROM achievements WHERE player = ?'
            cursor.execute(get_player_achievements_query, (player.id,))
            player_achievements = cursor.fetchone()

            player_data_query = 'SELECT player, exp FROM players WHERE player = ?'
            cursor.execute(player_data_query, (player.id,))
            player_data = cursor.fetchone()

            if player_achievements:
                # Update challenge played
                new_challenge_value = player_achievements[2] + 1
                update_player_achievements_query = 'UPDATE achievements SET challenges_played = ? WHERE player = ?'
                cursor.execute(update_player_achievements_query, (new_challenge_value, player.id))
                conn.commit()

                # If achievement earned, add exp and append achievement msg
                if new_challenge_value in self.challenge_achievements or (new_challenge_value > 300 and player_achievements[8] == 0):
                    achievement_value = new_challenge_value
                    if new_challenge_value >= 300 and player_achievements[8] == 0:
                        update_challenge_gm_query = 'UPDATE achievements SET challenges_gm = ? WHERE player = ?'
                        cursor.execute(update_challenge_gm_query, (1, player.id))
                        conn.commit()
                        achievement_value = 300

                    # Achievement msg
                    challenge = self.badge_emojis[self.challenge_achievements[achievement_value]] + ' | Congratulations ' + player.mention + \
                    '! You have obtained ' + ('a ' if 'Master' not in self.challenge_achievements[achievement_value] else 'the ') + '**' + \
                    self.challenge_achievements[achievement_value] + (' of Challenges' if 'Master' in self.challenge_achievements[achievement_value] else '') + \
                    '** badge for having played **' + str(achievement_value) + \
                    '** challenges! **(+' + str(self.achievement_rewards[self.challenge_achievements[achievement_value]]) + ' Exp)**'
                    
                    achievement_msgs.append(challenge)

                    # Add exp to player (Assume player data already exists, from update_player_records method)
                    player_exp = player_data[1]
                    # Old player level
                    for level in self.levelling_system:
                        if player_exp < level[1]:
                            break
                        old_player_level = level[0]

                    # Add exp
                    player_exp = player_exp + self.achievement_rewards[self.challenge_achievements[achievement_value]]
                    update_player_exp_query = 'UPDATE players SET exp = ? WHERE player = ?'
                    cursor.execute(update_player_exp_query, (player_exp, player.id))
                    conn.commit()

                    # New player level
                    for level in self.levelling_system:
                        if player_exp < level[1]:
                            break
                        new_player_level = level[0]

                    if new_player_level > old_player_level:
                        achievement_msgs.append('🆙 | Congratulations ' + player.mention + '! You have reached level **' + str(new_player_level) + '**!')
            else:
                cur_date = str(time.gmtime().tm_year) + '-' + str(time.gmtime().tm_mon) + '-' + str(time.gmtime().tm_mday)
                insert_challenge_achievements_query = 'INSERT INTO achievements VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
                insert_challenge_achievements_values = [player.id, 0, 1, cur_date, 1, 1, 0, 0, 0, 0, 0, 0]
                cursor.execute(insert_challenge_achievements_query, insert_challenge_achievements_values)
                conn.commit()

        conn.close()

        return achievement_msgs

    def get_profile(self, player, server):
        # Returns profile of player in an embed
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        # Extract data
        get_player_data = 'SELECT * FROM players WHERE player = ?'
        cursor.execute(get_player_data, (player.id,))
        player_info = cursor.fetchone()

        if player_info is None:
            insert_player_data = 'INSERT INTO players VALUES (?,?,?,?,?,?,?)'
            player_data = [player.id, 0, 0, 0, 0, 0, 0]
            cursor.execute(insert_player_data, player_data)
            conn.commit()

            player_info = [player.id, 0, 0, 0, 0, 0, 0]

        # Put info into embed
        for level in self.levelling_system:
            if player_info[1] < level[1]:
                next_exp = level[1] - player_info[1]
                break
            player_level = level[0]

        player_desc = 'Level: **' + str(player_level) + '**\nExperience Points: **' + str(player_info[1]) + '**'
        if len(self.levelling_system) > player_level:
            player_desc += ' (' + str(next_exp) + ' Exp to next level)'

        # Get player records sorted by exp descending
        get_players_ranked = 'SELECT player, exp FROM players ORDER BY exp DESC'
        cursor.execute(get_players_ranked)
        player_rankings = cursor.fetchall()

        # Get players in server
        # server_users = [member.id for member in server.members]
        # server_players = list(filter(lambda x:x[0] in server_users, player_rankings))
        # total_players = len(server_players)

        # Get ranking
        i = 1
        for person in player_rankings:
            if person[0] == player.id:
                rank = i
                break
            else:
                i += 1

        conn.close()

        player_profile = discord.Embed(title = 'Attack on Wikia Profile', description = player_desc, colour = 0xC0C0C0)
        player_profile.set_author(name = player.name, icon_url = player.avatar_url)
        player_profile.set_thumbnail(url = player.avatar_url)

        player_profile.add_field(name = 'Rank', value = str(rank) + '/' + str(len(player_rankings)), inline = False)
        player_profile.add_field(name = 'Questions answered correctly', value = str(player_info[2]), inline = False)
        player_profile.add_field(name = 'Hangman games won', value = str(player_info[5]), inline = False)
        player_profile.add_field(name = 'Images guessed correctly', value = str(player_info[6]), inline = False)
        player_profile.add_field(name = 'Challenges played', value = str(player_info[3]))
        player_profile.add_field(name = 'Challenges won', value = str(player_info[4]))
        
        return player_profile

    def get_achievements(self, player):
        # Returns profile of player in an embed
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        # Extract data
        achievements_query = 'SELECT * FROM achievements WHERE player = ?'
        cursor.execute(achievements_query, (player.id,))
        player_info = cursor.fetchone()

        if player_info:
            badges = [player.name, player_info[1], player_info[2], player_info[4], player_info[5], player_info[6], player_info[11]]
        else:
            cur_date = str(time.gmtime().tm_year) + '-' + str(time.gmtime().tm_mon) + '-' + str(time.gmtime().tm_mday)
            insert_achievements_query = 'INSERT INTO achievements VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
            initial_achievements = [player.id, 0, 0, cur_date, 1, 1, 0, 0, 0, 0, 0, 0]
            cursor.execute(insert_achievements_query, initial_achievements)
            conn.commit()

            badges = [player.name, 0, 0, 1, 1, 0, 0]

        conn.close()

        # Put info into embed
        num_badges = 0

        cur_days = badges[3]
        max_days = badges[4]
        consecutive_badges = ''
        consecutive_next = str(cur_days)
        for step in sorted(list(self.consecutive_days_achievements)):
            if max_days < step:
                consecutive_next = str(cur_days) + '/' + str(step)
                break
            consecutive_badges += self.badge_emojis[self.consecutive_days_achievements[step]]
            num_badges += 1

        one_clue = badges[1]
        one_clue_badges = ''
        one_clue_next = str(one_clue)
        for step in sorted(list(self.one_clue_achievements)):
            if one_clue < step:
                one_clue_next = str(one_clue) + '/' + str(step)
                break
            one_clue_badges += self.badge_emojis[self.one_clue_achievements[step]]
            num_badges += 1

        challenges_played = badges[2]
        challenge_badges = ''
        challenge_next = str(challenges_played)
        for step in sorted(list(self.challenge_achievements)):
            if challenges_played < step:
                challenge_next = str(challenges_played) + '/' + str(step)
                break
            challenge_badges += self.badge_emojis[self.challenge_achievements[step]]
            num_badges += 1

        perfect_hangman = badges[5]
        perfect_hangman_badges = ''
        perfect_hangman_next = str(perfect_hangman)
        for step in sorted(list(self.hangman_achievements)):
            if perfect_hangman < step:
                perfect_hangman_next = str(perfect_hangman) + '/' + str(step)
                break
            perfect_hangman_badges += self.badge_emojis[self.hangman_achievements[step]]
            num_badges += 1

        no_hint_image = badges[6]
        no_hint_image_badges = ''
        no_hint_image_next = str(no_hint_image)
        for step in sorted(list(self.image_achievements)):
            if no_hint_image < step:
                no_hint_image_next = str(no_hint_image) + '/' + str(step)
                break
            no_hint_image_badges += self.badge_emojis[self.image_achievements[step]]
            num_badges += 1

        player_achievements = discord.Embed(title = 'Badges for Attack on Wikia', description = 'Number of badges collected: **' + str(num_badges) + '**', colour = 0xC0C0C0)
        player_achievements.set_author(name = player.name, icon_url = player.avatar_url)
        player_achievements.set_thumbnail(url = player.avatar_url)

        player_achievements.add_field(name = 'Number of consecutive days played', value = consecutive_next)
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Badges', value = consecutive_badges if consecutive_badges != '' else '-')
        player_achievements.add_field(name = 'Correct answers with 1 clue', value = one_clue_next)
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Badges', value = one_clue_badges if one_clue_badges != '' else '-')
        player_achievements.add_field(name = 'Perfect Hangman games', value = perfect_hangman_next)
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Badges', value = perfect_hangman_badges if perfect_hangman_badges != '' else '-')
        player_achievements.add_field(name = 'Images guessed with no hints', value = no_hint_image_next)
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Badges', value = no_hint_image_badges if no_hint_image_badges != '' else '-')
        player_achievements.add_field(name = 'Challenges played', value = challenge_next)
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Badges', value = challenge_badges if challenge_badges != '' else '-')

        return player_achievements

    def get_dailies(self, player):
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        # Extract data
        dailies_query = 'SELECT * FROM dailies WHERE player = ?'
        cursor.execute(dailies_query, (player.id,))
        player_dailies = cursor.fetchone()

        cur_date = str(time.gmtime().tm_year) + '-' + str(time.gmtime().tm_mon) + '-' + str(time.gmtime().tm_mday)

        if player_dailies:
            # B: prev play, C: Standard, D: Hangman, E: Challenge
            prev_date = player_dailies[1]
            if cur_date != prev_date:
                # Reset
                reset_dailies_query = 'UPDATE dailies SET last_play = ?, standard = ?, hangman = ?, challenge = ?, image = ? WHERE player = ?'
                cursor.execute(reset_dailies_query, (cur_date, 0, 0, 0, 0, player.id))
                conn.commit()
                player_dailies = [player.id, cur_date, 0, 0, 0, 0]
        else:
            insert_dailies_query = 'INSERT INTO dailies VALUES (?,?,?,?,?,?)'
            player_dailies = [player.id, cur_date, 0, 0, 0, 0]
            cursor.execute(insert_dailies_query, player_dailies)
            conn.commit()

        conn.close()
                
        def get_time_remaining(cur_hr, cur_min):
            # 24 hrs - current time
            cur_mins = cur_hr * 60 + cur_min
            rem_min = 24 * 60 - cur_mins
            hr = str(rem_min // 60)
            minute = str(rem_min % 60)
            return '[' + hr + 'h ' + minute + 'm]'

        time_remaining = get_time_remaining(time.gmtime().tm_hour, time.gmtime().tm_min)

        standard_daily = ('☑' if player_dailies[2] >= 10 else '⬛') +  ' Complete 10 standard puzzles! **[+15 Exp]**'
        standard_daily2 = '￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵￶￵ - Progress: **' + str(player_dailies[2]) + '/10**'
            
        hangman_daily = ('☑' if player_dailies[3] >= 10 else '⬛') + ' Win 10 Hangman games! **[+15 Exp]**'
        hangman_daily2 = '￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵￶￵ - Progress: **' + str(player_dailies[3]) + '/10**'

        image_daily = ('☑' if player_dailies[5] >= 10 else '⬛') + ' Guess 10 images correctly! **[+15 Exp]**'
        image_daily2 = '￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵￶￵ - Progress: **' + str(player_dailies[5]) + '/10**'

        challenge_daily = ('☑' if player_dailies[4] >= 1 else '⬛') + ' Complete a challenge! **[+25 Exp]**'
        challenge_daily2 = '￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵￶￵ - Progress: **' + str(player_dailies[4]) + '/1**'

        cur_dailies = discord.Embed(colour = 0xC0C0C0)
        cur_dailies.set_author(name = 'Today\'s Dailies ' + time_remaining, icon_url = player.avatar_url)
        cur_dailies.set_thumbnail(url = player.avatar_url)

        cur_dailies.add_field(name = standard_daily, value = standard_daily2, inline = False)
        cur_dailies.add_field(name = hangman_daily, value = hangman_daily2, inline = False)
        cur_dailies.add_field(name = image_daily, value = image_daily2, inline = False)
        cur_dailies.add_field(name = challenge_daily, value = challenge_daily2, inline = False)
        return cur_dailies

    def get_stats(self):
        # Returns overall game stats in an embed
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        game_data_query = 'SELECT * FROM overall'
        cursor.execute(game_data_query)
        game_data = cursor.fetchone()

        total_qns = game_data[0]
        correct_qns = str(game_data[1])
        if total_qns > 0:
            correct_qns += ' (' + str(round(100 * game_data[1] / total_qns, 1)) + '%)'

        hangman_games = game_data[5]
        hangman_won_games = str(game_data[6])
        if hangman_games > 0:
            hangman_won_games += ' (' + str(round(100 * game_data[6] / hangman_games, 1)) + '%)'
        
        images_generated = game_data[7]
        images_correct = str(game_data[8])
        if images_generated > 0:
            images_correct += ' (' + str(round(100 * game_data[8] / images_generated, 1)) + '%)'

        challenge_qns = game_data[3]
        c_correct_qns = str(game_data[4])
        if challenge_qns > 0:
            c_correct_qns += ' (' + str(round(100 * game_data[4] / challenge_qns, 1)) + '%)'

        challenges_played = str(game_data[2])

        conn.close()
        
        game_stats = discord.Embed(title = '📖 Attack on Wikia Stats', colour = 0xC0C0C0)

        game_stats.add_field(name = 'Questions asked', value = str(total_qns))
        game_stats.add_field(name = 'Questions answered correctly', value = correct_qns)
        game_stats.add_field(name = '⠀', value = '⠀')
        game_stats.add_field(name = 'Total Hangman games played', value = str(hangman_games))
        game_stats.add_field(name = 'Total Hangman games won', value = hangman_won_games)
        game_stats.add_field(name = '⠀', value = '⠀')
        game_stats.add_field(name = 'Number of images generated', value = str(images_generated))
        game_stats.add_field(name = 'Images guessed correctly', value = images_correct)
        game_stats.add_field(name = '⠀', value = '⠀')
        game_stats.add_field(name = 'Challenges played', value = challenges_played, inline = False)
        game_stats.add_field(name = 'Challenge questions asked', value = str(challenge_qns))
        game_stats.add_field(name = 'Challenge questions answered correctly', value = c_correct_qns)
        game_stats.add_field(name = '⠀', value = '⠀')
        
        return game_stats

    def get_leaderboard(self, server, page=1, player=None):
        # Returns the names of the top players, with 10 per page, in an embed
        conn = sqlite3.connect('AttackonWikia/aow_db.db')
        cursor = conn.cursor()

        player_rankings_query = 'SELECT player, exp FROM players'
        cursor.execute(player_rankings_query)
        player_rankings = cursor.fetchall()

        if player:
            player_query = 'SELECT * FROM players WHERE player = ?'
            cursor.execute(player_query, (player.id,))
            player_data = cursor.fetchone()
            if player_data is None:
                # Add player data into player records
                insert_player_data = 'INSERT INTO players VALUES (?,?,?,?,?,?,?)'
                player_data = [player.id, 0, 0, 0, 0, 0, 0]
                cursor.execute(insert_player_data, player_data)
                conn.commit()
                player_rankings.append(player_data)

        # player_rankings_map = {}
        # for player_rank in player_rankings:
        #     player_rankings_map[player_rank[0]] = player_rank[1]

        # server_players = []
        # for user in server.members:
        #     if user.id in player_rankings_map:
        #         server_players.append([user.mention, player_rankings_map[user.id]])

        # Sort by Exp from biggest to smallest
        player_rankings.sort(key = lambda x: x[1], reverse = True)

        conn.close()

        total_pages = math.ceil(len(player_rankings) / 10)
        
        # Sanitize page input
        try: 
            page_no = int(page)
        except:
            page_no = 1

        # Clips inputs that are too high or too low
        if page_no < 1:
            page_no = total_pages
        if page_no > total_pages:
            page_no = 1

        # Get page_no of player rank
        if player:
            player_rank = 0
            for person in player_rankings:
                player_rank += 1
                if person[0] == player.id:
                    break
            page_no = math.ceil(player_rank / 10)

        # Put names into embed
        all_names = ''
        all_levels_exp = ''
        nums = {1:'🥇', 2:'🥈', 3:'🥉', 4:'4⃣', 5:'5⃣', 6:'6⃣', 7:'7⃣', 8:'8⃣', 9:'9⃣', 10:'🔟'}
        for rank in range((page_no - 1) * 10 + 1, min(len(player_rankings) + 1, page_no * 10 + 1)):
            rank_emoji = nums[rank] if rank <= 10 else str(rank) + '.'
            all_names += rank_emoji + ' <@' + str(player_rankings[rank-1][0]) + '>\n'
            for level in self.levelling_system:
                if player_rankings[rank-1][1] < level[1]:
                    next_level_exp = level[1]
                    break
                player_level = level[0]
            all_levels_exp += '**' + str(player_level) + '**' + ' (' + str(player_rankings[rank-1][1])
            if player_level < len(self.levelling_system):
                all_levels_exp += '/' + str(next_level_exp)
            all_levels_exp += ')\n'

        leaderboard = discord.Embed(title = 'Leaderboard for Attack on Wikia', colour=0xC0C0C0)
        if not player:
            leaderboard.add_field(name = 'Max Level', value = str(len(self.levelling_system)), inline = False)
        if player:
            leaderboard.add_field(name = player.name + '\'s Rank', value = str(player_rank) + '/' + str(len(player_rankings)), inline = False)
        leaderboard.add_field(name = 'Rank/Name', value = all_names)
        leaderboard.add_field(name = 'Level/Exp', value = all_levels_exp)
        leaderboard.set_footer(text = 'Page ' + str(page_no) + '/' + str(total_pages))

        return leaderboard, page_no

    def get_specials(self):
        specials = '`~bonus`\nGet a bonus clue for the current puzzle! **(Level 50 to unlock)**\n' + \
            '`~life`\nAdds an extra life to the current hangman game! **(Level 75 to unlock)**'
        specials_list = discord.Embed(title = 'Special Commands for Attack on Wikia', description = specials, colour = 0xC0C0C0)
        return specials_list

    def get_commands(self):
        commands_list = discord.Embed(title = 'List of commands for Attack on Wikia', colour = 0xC0C0C0)
        general_commands = '`~credits` : Who made me/Get support\n' + \
            '`~patreon` : Support the creator!'
        commands_list.add_field(name = 'General', value = general_commands, inline = False)

        aow_commands = '`~new`\n Starts a new puzzle.\n' + \
        '`~clue`\n Gives another hint for the current puzzle. There is a maximum of 5 clues per puzzle.\n' + \
        '`~hangman <@person>`\n Starts a new Hangman game. Type `~hangman <@person>` to challenge someone to a Hangman game.\n' + \
        '`~image`\n Starts image mode. Type `~image <@person>` to start an image challenge.\n' + \
        '`~answer`\n Reveals the answer of an active puzzle.\n' + \
        '`~challenge <@person>`\n Sends a challenge to another person, or accepts an incoming challenge.\n' + \
        '`~reset`\n Resets the game.\n' + \
        '`~profile <@person>`\n Checks the profile of a given user.\n' + \
        '`~badges <@person>`\n Checks the badges of a given user.\n' + \
        '`~dailies`\n Checks the progress of your daily rewards.\n' + \
        '`~gamestats`\n Shows the overall game statistics.\n' + \
        '`~leaderboard/~lb <page> <@person>`\n Shows the leaderboard, listing the top 10 players on the server. Add a number or tag to see subsequent pages (e.g. `~lb 2`).\n' + \
        '`~special`\n Shows the list of special commands that require certain levels to access.'
        commands_list.add_field(name = 'Attack on Wikia', value = aow_commands)
        return commands_list