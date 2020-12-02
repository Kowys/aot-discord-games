import discord
import math
import sqlite3
from ChooseYourAdventure import book
from ChooseYourAdventure import book2


class Affinities():
    def __init__(self, book):
        if book == 1:
            self.eren = 0
            self.mikasa = 0
            self.armin = 0
            self.jean = 0
            self.krista = 0
            self.sasha = 0
        elif book == 2:
            self.eren = 0
            self.mikasa = 0
            self.armin = 0
            self.jean = 0
            self.krista = 0
            self.sasha = 0
            self.hanji = 0
            self.levi = 0
            self.annie = 0

class Statuses():
    def __init__(self, book):
        if book == 1:
            self.eren = 'Alive'
            self.mikasa = 'Alive'
            self.armin = 'Alive'
            self.jean = 'Alive'
            self.krista = 'Alive'
            self.sasha = 'Alive'
            self.marco = 'Alive'
            self.franz = 'Alive'
            self.hannah = 'Alive'
            self.squad34 = 'Alive'
            self.levi = 'Alive'
            self.rico = 'Alive'
            self.ian = 'Alive'
            self.mitabi = 'Alive'
        elif book == 2:
            self.eren = 'Alive'
            self.mikasa = 'Alive'
            self.armin = 'Alive'
            self.jean = 'Alive'
            self.krista = 'Alive'
            self.sasha = 'Alive'
            self.levi = 'Alive'
            self.hanji = 'Alive'
            self.annie = 'Alive'
            self.petra = 'Alive'
            self.oluo = 'Alive'
            self.gunther = 'Alive'
            self.eld = 'Alive'
            self.dieter = 'Alive'
            self.lukesiss = 'Alive'

class Flags():
    def __init__(self, book):
        if book == 1:
            self.flagD = 'No'
            self.flagL = 'No'
            self.levihelp = 'No'
            self.witheren = 'No'
            self.sashaeaten = 'No'
            self.armindressed = 'No'
            self.armintutorial = 'No'
            self.memelevel = 0
        elif book == 2:
            self.keyA = 'No'
            self.keyY = 'No'
            self.keyR = 'No'
            self.keyS = 'No'
            self.killcount = 0

class State():
    def __init__(self):
        # Initialize as Book 1
        self.book = book.Book(self)
        self.book_no = 1
        self.affinities = Affinities(1)
        self.statuses = Statuses(1)
        self.flags = Flags(1)
        self.cur_player_id = None
        self.select_book = False
        self.timer = 0
        self.game_channel = None

    def reset_game(self):
        self.book = book.Book(self)
        self.book_no = 1
        self.affinities = Affinities(1)
        self.statuses = Statuses(1)
        self.flags = Flags(1)
        self.cur_player_id = None
        self.select_book = False
        self.timer = 0
        self.game_channel = None

    def switch_book(self, book_num):
        books = {1:book, 2:book2}
        self.book = books[book_num].Book(self)
        self.book_no = book_num
        self.affinities = Affinities(book_num)
        self.statuses = Statuses(book_num)
        self.flags = Flags(book_num)

    def check_book(self, player):
        conn = sqlite3.connect('ChooseYourAdventure/cya_db.db')
        cursor = conn.cursor()

        get_endings_query = 'SELECT * FROM endings WHERE player = ?'
        cursor.execute(get_endings_query, (player.id,))
        endings_data = cursor.fetchone()

        if endings_data and sum(endings_data[1:]) > 0:
            return True

        return False

    def get_annie_secrets(self, user_obj):
        conn = sqlite3.connect('ChooseYourAdventure/cya_db.db')
        cursor = conn.cursor()

        get_annie_query = 'SELECT * FROM annie_progress WHERE player = ?'
        cursor.execute(get_annie_query, (user_obj.id,))
        annie_data = cursor.fetchone()

        cur_progress = self.book.annie_secrets[self.book.cur_page[0]]

        if annie_data:
            annie_progress = annie_data[1]
            if cur_progress > annie_progress + 1:
                return 'Nice try, ' + user_obj.mention + ', but you do not have access to this secret yet!'
            elif cur_progress == annie_progress + 1:
                # Update annie progress
                update_annie_query = 'UPDATE annie_progress SET progress = ? WHERE player = ?'
                update_annie = [cur_progress, user_obj.id]
                cursor.execute(update_annie_query, update_annie)
                conn.commit()
                # Go to secret page and return content
                return self.book.page_flipper('s')
            else:
                # Go to secret page and return content
                return self.book.page_flipper('s')
        else:
            if cur_progress > 1:
                return 'Nice try, ' + user_obj.mention + ', but you do not have access to this secret yet!'
            else:
                # Insert annie progress
                insert_annie_query = 'INSERT INTO annie_progress VALUES (?,?)'
                insert_annie = [user_obj.id, 1]
                cursor.execute(insert_annie_query, insert_annie)
                conn.commit()

                # Go to secret page and return content
                return self.book.page_flipper('s')

        conn.close()

    def log_ending(self, author):
        conn = sqlite3.connect('ChooseYourAdventure/cya_db.db')
        cursor = conn.cursor()

        # Add ending to game statistics
        get_global_query = 'SELECT * FROM global'
        cursor.execute(get_global_query)
        global_stats = cursor.fetchall()
        
        ending = self.book.endings[self.book.cur_page[0]]
        ending_map = {'Trial of Eren and Mikasa': 14, 'A Soldier\'s Duty': 15, 'An Ordinary Moment of Happiness': 2, 'Failure of the Reclamation Plan': 16, 'Jean Kirstein of the Survey Corps': 3, 
        'A Narrow Victory': 4, 'Armin Arlert\'s Dream': 5, 'A Regular Soldier': 17, '104th Annihilated at HQ': 18, 'Junior High': 24, 'The Fall of Wall Rose': 19, 
        'Failure to Reclaim Trost District': 20, 'A Moment\'s Peace': 21, 'Eren Flees': 22, 'Captain Levi\'s Recruit': 6, 'Mikasa\'s True Face': 7, 'Nameless Hero': 8, 'Eren Yeager\'s Hand': 9, 
        'Sasha Blouse\'s Promise': 10, 'The Girl Who Hid Her True Self': 11, 'The Death of a Merchant': 23, 'No Regrets': 12, 'Jean of the Military Police': 13, 'Joining the Garrison': 1}

        endings_db_map = {'Joining the Garrison':'joining_the_garrison', 'An Ordinary Moment of Happiness':'an_ordinary_moment_of_happiness', 
        'Jean Kirstein of the Survey Corps':'jean_kirstein_of_the_survey_corps', 'A Narrow Victory':'a_narrow_victory', 'Armin Arlert\'s Dream':'armin_arlerts_dream',
        'Captain Levi\'s Recruit':'captain_levis_recruit', 'Mikasa\'s True Face':'mikasas_true_face', 'Nameless Hero':'nameless_hero', 'Eren Yeager\'s Hand':'eren_yeagers_hand', 
        'Sasha Blouse\'s Promise':'sasha_blouses_promise', 'The Girl Who Hid Her True Self':'the_girl_who_hid_her_true_self', 'No Regrets':'no_regrets', 
        'Jean of the Military Police':'jean_of_the_military_police', 'Trial of Eren and Mikasa':'trial_of_eren_and_mikasa', 'A Soldier\'s Duty':'a_soldiers_duty', 
        'Failure of the Reclamation Plan':'failure_of_the_reclamation_plan', 'A Regular Soldier':'a_regular_soldier','104th Annihilated at HQ':'annihilated_at_hq', 
        'The Fall of Wall Rose':'the_fall_of_wall_rose', 'Failure to Reclaim Trost District':'failure_to_reclaim_trost_district', 'A Moment\'s Peace':'a_moments_peace', 
        'Eren Flees':'eren_flees', 'The Death of a Merchant':'the_death_of_a_merchant','Junior High':'junior_high'}

        update_index = ending_map[ending]
        update_global_query = 'UPDATE global SET count = ? WHERE ending = ?'
        cursor.execute(update_global_query, [global_stats[update_index][1] + 1, ending])
        conn.commit()

        # Logs the ending the player achieved
        get_player_query = 'SELECT * FROM endings WHERE player = ?'
        cursor.execute(get_player_query, (author.id,))
        raw_player_endings = cursor.fetchone()

        if raw_player_endings:
            player_endings = raw_player_endings[1:]
            former_ending_count = len(list(filter(lambda x: x > 0, player_endings)))

            # Add ending the player got
            update_ending = endings_db_map[ending]
            update_player_query = 'UPDATE endings SET {} = ? WHERE player = ?'.format(update_ending)

            new_ending_value = raw_player_endings[update_index] + 1
            update_player = [new_ending_value, author.id]

            cursor.execute(update_player_query, update_player)

        else:
            former_ending_count = 0

            insert_ending_query = 'INSERT INTO endings VALUES ({})'.format(','.join('?' * 25))
            insert_position = update_index - 1
            insert_data = [author.id] + [0] * insert_position + [1] + [0] * (25 - 2 - insert_position)
            cursor.execute(insert_ending_query, insert_data)

        conn.commit()

        # Inform player of rank ups
        get_player_query = 'SELECT * FROM endings WHERE player = ?'
        cursor.execute(get_player_query, (author.id,))
        raw_player_endings = cursor.fetchone()
        player_endings = raw_player_endings[1:]
        ending_count = len(list(filter(lambda x: x > 0, player_endings)))

        conn.close()

        rank_ups = {1: ['Trainee', 'Recruit'], 2: ['Recruit', 'Private'], 3: ['Private', 'Soldier'], 5: ['Soldier', 'Elite Soldier'], 8: ['Elite Soldier', 'Officer'], 10: ['Officer', 'Team Leader'], 
        13: ['Team Leader', 'Senior Team Leader'], 15: ['Senior Team Leader', 'Squad Leader'], 20: ['Squad Leader', 'Squad Captain'], 24: ['Squad Captain', 'Commander']}
        
        if (ending_count > former_ending_count) and (ending_count in rank_ups):
            new_rank = rank_ups[ending_count][1]
            former_rank = rank_ups[ending_count][0]

            # Rank-up message
            promotion_info = discord.Embed(title='🎖' + author.name + ' has been promoted to ' + new_rank + '!🎖', colour=0xE5D2BB)
            promotion_info.set_thumbnail(url = author.avatar_url)
            promotion_info.add_field(name = 'Congratulations!', value =  '**' + former_rank + '** ➡ **' + new_rank + '**')

            return promotion_info

        # If no promotion
        else:
            return None

    def get_stats(self):
        stats_info = discord.Embed(title='Battle information\n', colour=0xE5D2BB)

        if self.book_no == 1:
            stats_info.add_field(name = '**Statuses**', value = 'Eren: ' + self.statuses.eren + \
            '\nMikasa: ' + self.statuses.mikasa + \
            '\nArmin: ' + self.statuses.armin + \
            '\nJean: ' + self.statuses.jean + \
            '\nKrista: ' + self.statuses.krista + \
            '\nSasha: ' + self.statuses.sasha + \
            '\nMarco: ' + self.statuses.marco + \
            '\nFranz: ' + self.statuses.franz + \
            '\nHannah: ' + self.statuses.hannah + \
            '\nSquad 34: ' + self.statuses.squad34 + \
            '\nLevi: ' + self.statuses.levi + \
            '\nRico: ' + self.statuses.rico + \
            '\nIan: ' + self.statuses.ian + \
            '\nMitabi: ' + self.statuses.mitabi) 

            stats_info.add_field(name = '**Affinities**', value = 'Eren: ' + str(self.affinities.eren) + \
            '\nMikasa: ' + str(self.affinities.mikasa) + \
            '\nArmin: ' + str(self.affinities.armin) + \
            '\nJean: ' + str(self.affinities.jean) + \
            '\nKrista: ' + str(self.affinities.krista) + \
            '\nSasha: ' + str(self.affinities.sasha))
            
            stats_info.add_field(name = '**Flags**', value = 'Flag D : ' + self.flags.flagD + \
            '\nFlag L: ' + self.flags.flagL)

        elif self.book_no == 2:
            stats_info.add_field(name = '**Statuses**', value = 'Eren: ' + self.statuses.eren + \
            '\nMikasa: ' + self.statuses.mikasa + \
            '\nArmin: ' + self.statuses.armin + \
            '\nJean: ' + self.statuses.jean + \
            '\nKrista: ' + self.statuses.krista + \
            '\nSasha: ' + self.statuses.sasha + \
            '\nLevi: ' + self.statuses.levi + \
            '\nHanji: ' + self.statuses.hanji + \
            '\nAnnie: ' + self.statuses.annie + \
            '\nPetra: ' + self.statuses.petra + \
            '\nOluo: ' + self.statuses.oluo + \
            '\nGunther: ' + self.statuses.gunther + \
            '\nEld: ' + self.statuses.eld + \
            '\nDieter Ness: ' + self.statuses.dieter + \
            '\nLuke Siss: ' + self.statuses.lukesiss) 

            stats_info.add_field(name = '**Affinities**', value = 'Eren: ' + str(self.affinities.eren) + \
            '\nMikasa: ' + str(self.affinities.mikasa) + \
            '\nArmin: ' + str(self.affinities.armin) + \
            '\nJean: ' + str(self.affinities.jean) + \
            '\nKrista: ' + str(self.affinities.krista) + \
            '\nSasha: ' + str(self.affinities.sasha) + \
            '\nHanji: ' + str(self.affinities.hanji) + \
            '\nLevi: ' + str(self.affinities.levi) + \
            '\nAnnie: ' + str(self.affinities.annie))

            keys = ''
            if self.flags.keyA == 'Yes':
                keys += 'Key A\n'
            if self.flags.keyY == 'Yes':
                keys += 'Key Y\n'
            if self.flags.keyR == 'Yes':
                keys += 'Key R\n'
            if self.flags.keyS == 'Yes':
                keys += 'Key S\n'

            stats_info.add_field(name = '**Keys**', value = keys if keys else '-')

            stats_info.add_field(name = '**Kill Count**', value = str(self.flags.killcount))

        return stats_info

    def get_profile(self, user_obj):
        conn = sqlite3.connect('ChooseYourAdventure/cya_db.db')
        cursor = conn.cursor()

        player_endings_query = 'SELECT * FROM endings WHERE player = ?'
        cursor.execute(player_endings_query, (user_obj.id,))
        raw_endings = cursor.fetchone()
        if raw_endings:
            my_endings = raw_endings[1:]
            ending_count = len(list(filter(lambda x: x > 0, my_endings)))
        else:
            my_endings = [0] * 24
            ending_count = 0
            insert_player_query = 'INSERT INTO endings VALUES ({})'.format(','.join('?' * 25))
            cursor.execute(insert_player_query, [user_obj.id] + my_endings)
            conn.commit()

        if ending_count == 0:
            my_rank = '**Trainee 🔸**'
        elif ending_count == 1:
            my_rank = '**Recruit 🔸🔸**'
        elif ending_count == 2:
            my_rank = '**Private 🔸🔸🔸**'
        elif ending_count < 5:
            my_rank = '**Soldier 🔹**'
        elif ending_count < 8:
            my_rank = '**Elite Soldier 🔹🔹**'
        elif ending_count < 10:
            my_rank = '**Officer 🔹🔹🔹**'
        elif ending_count < 13:
            my_rank = '**Team Leader 💠**'
        elif ending_count < 15:
            my_rank = '**Senior Team Leader 💠🔹**'
        elif ending_count < 20:
            my_rank = '**Squad Leader ⭐**'
        elif ending_count < 24:
            my_rank = '**Squad Captain 🌟**'
        elif ending_count == 24:
            my_rank = '**Commander 👑**'
        desc = 'Rank: ' + my_rank + '\n' + 'Number of endings obtained: ' + str(ending_count) + '/24'
        progress_info = discord.Embed(title='Player information\n', description = desc, colour=0xE5D2BB)
        # Include number of games played, and other interesting stats?

        username, user_url = user_obj.name, user_obj.avatar_url
        progress_info.set_author(name = username, icon_url = user_url)
        progress_info.set_thumbnail(url = user_url)

        endings_index_map = {0:'Joining the Garrison', 1:'An Ordinary Moment of Happiness', 2:'Jean Kirstein of the Survey Corps', 3:'A Narrow Victory', 4:'Armin Arlert\'s Dream',
        5:'Captain Levi\'s Recruit', 6:'Mikasa\'s True Face', 7:'Nameless Hero', 8:'Eren Yeager\'s Hand', 9:'Sasha Blouse\'s Promise', 10:'The Girl Who Hid Her True Self',
        11:'No Regrets', 12:'Jean of the Military Police', 13:'Trial of Eren and Mikasa', 14:'A Soldier\'s Duty', 15:'Failure of the Reclamation Plan', 16:'A Regular Soldier',
        17:'104th Annihilated at HQ', 18:'The Fall of Wall Rose', 19:'Failure to Reclaim Trost District', 20:'A Moment\'s Peace', 21:'Eren Flees', 22:'The Death of a Merchant',
        23:'Junior High'}

        endings = [['An Ordinary Moment of Happiness', 'Jean Kirstein of the Survey Corps', 'A Narrow Victory', 'Armin Arlert\'s Dream', 'Captain Levi\'s Recruit', 'Mikasa\'s True Face', 'Nameless Hero', 
        'Eren Yeager\'s Hand', 'Sasha Blouse\'s Promise', 'The Girl Who Hid Her True Self', 'No Regrets', 'Jean of the Military Police', 'Joining the Garrison'], 
        ['Trial of Eren and Mikasa', 'A Soldier\'s Duty', 'Failure of the Reclamation Plan', 'A Regular Soldier', '104th Annihilated at HQ', 'The Fall of Wall Rose', 'Failure to Reclaim Trost District',
        'A Moment\'s Peace', 'Eren Flees', 'The Death of a Merchant'],
        ['Junior High']]

        good_endings, bad_endings, secret_endings = '', '', ''
        for i in range(len(my_endings)):
            if my_endings[i] > 0:
                ending = endings_index_map[i]
                if ending in endings[0]:
                    good_endings += ending + '\n'
                elif ending in endings[1]:
                    bad_endings += ending + '\n'
                elif ending in endings[2]:
                    secret_endings += ending + '\n'

        conn.close()

        progress_info.add_field(name = '**Good Endings**', value = '-' if good_endings == '' else good_endings) 
        progress_info.add_field(name = '**Bad Endings**', value = '-' if bad_endings == '' else bad_endings)
        progress_info.add_field(name = '**Secret Endings**', value = '-' if secret_endings == '' else secret_endings, inline = False)

        return progress_info

    def get_leaderboard(self, server, page=1, player=None):
        conn = sqlite3.connect('ChooseYourAdventure/cya_db.db')
        cursor = conn.cursor()

        player_endings_query = 'SELECT * FROM endings'
        cursor.execute(player_endings_query)
        all_endings = cursor.fetchall()

        # server_users_ids = {member.id: [member.id, member.name] for member in server.members}
        server_endings = []
        for row in all_endings:
            unique_ending_count = len(list(filter(lambda x: x > 0, row[1:])))
            server_endings.append([row[0], unique_ending_count])

        conn.close()

        # Sort according to ending count
        server_endings.sort(key = lambda x: x[1], reverse = True)

        total_pages = math.ceil(len(server_endings) / 10)

        # Sanitize page input
        try: 
            page_no = int(page)
        except:
            page_no = 1

        # Clips inputs that are too high or too low
        if page_no < 1:
            page_no = 1
        if page_no > total_pages:
            page_no = total_pages

        # Get page_no of player rank
        if player:
            player_rank = 0
            for person in server_endings:
                player_rank += 1
                if person[0] == player.id:
                    break
            page_no = math.ceil(player_rank / 10)

        leaderboard = discord.Embed(title = '🏆 Leaderboard for Choose Your Adventure 🏆', colour=0xE5D2BB)
        leaderboard.set_footer(text = 'Page ' + str(page_no) + '/' + str(total_pages))
        if player:
            leaderboard.add_field(name = player.name + '\'s Rank', value = str(player_rank) + '/' + str(len(server_endings)), inline = False)

        for rank in range((page_no - 1) * 10 + 1, min(len(server_endings) + 1, page_no * 10 + 1)):
            ending_count = server_endings[rank-1][1]
            if ending_count == 0:
                insignia = '🔸'
            elif ending_count == 1:
                insignia = '🔸🔸'
            elif ending_count == 2:
                insignia = '🔸🔸🔸'
            elif ending_count < 5:
                insignia = '🔹'
            elif ending_count < 8:
                insignia = '🔹🔹'
            elif ending_count < 10:
                insignia = '🔹🔹🔹'
            elif ending_count < 13:
                insignia = '💠'
            elif ending_count < 15:
                insignia = '💠🔹'
            elif ending_count < 20:
                insignia = '⭐'
            elif ending_count < 24:
                insignia = '🌟'
            elif ending_count == 24:
                insignia = '👑'
            leaderboard.add_field(name = insignia + ' | #' + str(rank) + ' | Endings: ￵**' + str(server_endings[rank-1][1]) + '**', 
                                  value = '<@' + str(server_endings[rank-1][0]) + '>',
                                  inline = False)

        return leaderboard

    def get_gamestats(self):
        # Returns overall game statistics
        conn = sqlite3.connect('ChooseYourAdventure/cya_db.db')
        cursor = conn.cursor()

        game_stats_query = 'SELECT * FROM global'
        cursor.execute(game_stats_query)
        game_data = cursor.fetchall()

        endings_list = []
        for row in game_data:
            if row[0] == 'Total':
                continue
            endings_list.append([row[0], row[1]])

        endings_list.sort(key = lambda x: x[1], reverse = True)

        all_endings = ''
        for ending in endings_list:
            all_endings += ending[0] + ': ' + str(ending[1]) + '\n'

        game_stats = discord.Embed(title = '🔦 Choose Your Adventure Stats', colour=0xE5D2BB)
        game_stats.add_field(name = 'Total Number Of Endings Obtained', value = '**' + str(game_data[0][1]) + '**', inline = False)
        game_stats.add_field(name = 'Endings', value = all_endings)

        conn.close()

        return game_stats

    def get_commands(self):
        # Returns the list of commands
        commands_list = discord.Embed(title = 'List of commands for Choose Your Adventure', colour=0xE5D2BB)
        general_commands = '`~credits` : Who made me/Get support\n' + \
            '`~patreon` : Support the creator!'
        commands_list.add_field(name = 'General', value = general_commands, inline = False)

        cya_commands = '`~start`\n Starts a new game.\n' + \
        '`~intro`\n Gives a short introduction to the game.\n' + \
        '`~reset`\n Resets the game.\n' + \
        '`~stats`\n Brings up the Battle Report Card during a game.\n' + \
        '`~profile <@person>`\n Checks the profile of a given user.\n' + \
        '`~leaderboard/~lb`\n Shows the leaderboard, listing the top 10 players on the server. Add a number to see subsequent pages (e.g. `~lb 2`).\n' + \
        '`~gamestats`\n Brings up the overall game statistics.'
        commands_list.add_field(name = 'Choose Your Adventure', value = cya_commands)
        return commands_list