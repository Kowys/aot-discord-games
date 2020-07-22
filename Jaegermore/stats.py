import random
import discord
from Jaegermore import questions
from openpyxl import load_workbook

class Scores():
    def __init__(self):
        self.eren = 0
        self.mikasa = 0
        self.armin = 0
        self.jean = 0
        self.krista = 0
        self.sasha = 0
        self.levi = 0
        self.annie = 0
        self.marco = 0
        self.erwin = 0

    def highest_char(self):
        list_of_scores = [['eren', self.eren], ['mikasa', self.mikasa], ['armin', self.armin], ['jean', self.jean], ['krista', self.krista], ['sasha', self.sasha], ['levi', self.levi],
        ['annie', self.annie], ['erwin', self.erwin]]

        highest_score = max(map(lambda x: x[1], list_of_scores))
        highest_chars = list(filter(lambda x: x[1] == highest_score, list_of_scores))
        index = random.randint(1, len(highest_chars))
        highest_char = highest_chars[index-1][0]

        return highest_char

class State():
    def __init__(self):
        self.question = questions.Question(self)
        self.scores = Scores()
        self.game_channel = None
        self.timer = 0

    def game_reset(self):
        self.question = questions.Question(self)
        self.scores = Scores()
        self.game_channel = None
        self.timer = 0

    def update_records(self, character):
        wb = load_workbook("Jaegermore/records.xlsx")
        player_stats = wb['Players']
        global_stats = wb['Global']
        all_pers = {'eren':'B','mikasa':'C','armin':'D','jean':'E','krista':'F','sasha':'G','levi':'H','annie':'I','erwin':'J'}
        pers_index = all_pers[character]

        global_stats[pers_index + '2'] = global_stats[pers_index + '2'].value + 1
        global_stats['K2'] = global_stats['K2'].value + 1

        inside = False
        i = 0
        for row in player_stats:
            i += 1
            if row[0].value == str(self.question.curplayer.id):
                player_stats[pers_index + str(i)] = player_stats[pers_index + str(i)].value + 1
                wb.save("Jaegermore/records.xlsx")
                inside = True
                break
        if inside == False:
            player_stats.append([str(self.question.curplayer.id)] + 9 * [0])
            player_stats[pers_index + str(i+1)] = player_stats[pers_index + str(i+1)].value + 1
            wb.save("Jaegermore/records.xlsx")

    def get_info(self):
        stats_info = discord.Embed(title='Detailed Personality Info for **' + self.question.curplayer.name + '**', colour=0x5CFFE9)

        stats_info.add_field(name = '**Personality levels**', value = 'Eren: ' + str(self.scores.eren) + '\n\
    Mikasa: ' + str(self.scores.mikasa) + '\n\
    Armin: ' + str(self.scores.armin) + '\n\
    Jean: ' + str(self.scores.jean) + '\n\
    Krista: ' + str(self.scores.krista) + '\n\
    Sasha: ' + str(self.scores.sasha) + '\n\
    Levi: ' + str(self.scores.levi) + '\n\
    Annie: ' + str(self.scores.annie) + '\n\
    Erwin: ' + str(self.scores.erwin)) 

        return stats_info

    def get_profile(self, player):
        wb = load_workbook("Jaegermore/records.xlsx")
        player_stats = wb['Players']

        inside = False
        for row in player_stats:
            if row[0].value == str(player.id):
                all_personalities = list(map(lambda x: x.value, row[1:10]))
                inside = True
                break
        if inside == False:
            player_stats.append([str(player.id)] + 9 * [0])
            all_personalities = 9 * [0]
        
        wb.save("Jaegermore/records.xlsx")

        pers_mappings = {0:'Eren', 1:'Mikasa', 2:'Armin', 3:'Jean', 4:'Krista', 5:'Sasha', 6:'Levi', 7:'Annie', 8:'Erwin'}
        thumbnail_urls = {'Eren':'https://i.imgur.com/AZgDHsm.png',
        'Mikasa':'https://i.imgur.com/DrfMlLN.png',
        'Armin':'https://i.imgur.com/H5SkwLR.jpg',
        'Jean':'https://i.imgur.com/BJdEBiW.jpg',
        'Krista':'https://i.imgur.com/fA9Nmdr.jpg',
        'Sasha':'https://i.imgur.com/8b9BXc7.jpg',
        'Levi':'https://i.imgur.com/6UoSOTQ.png',
        'Annie':'https://i.imgur.com/eDVpxFm.jpg',
        'Erwin':'https://i.imgur.com/MGKlG4x.png'}

        all_pers_text = ''
        for i in range(len(all_personalities)):
            all_pers_text += pers_mappings[i] + ': ' + str(all_personalities[i]) + '\n'

        dominant_personalities = []
        highest = max(all_personalities)
        for i in range(len(all_personalities)):
            if all_personalities[i] == highest:
                dominant_personalities.append(pers_mappings[i])

        index = random.randint(1, len(dominant_personalities))
        dominant_personality = dominant_personalities[index-1]

        pers_title = 'Dominant Personality' if (highest == 0 or len(dominant_personalities) < 2) else 'Dominant Personalities'
        
        pers_text = ''
        for i in range(len(dominant_personalities)):
            if i > 0:
                pers_text += ', **' + dominant_personalities[i] + '**'
            else:
                pers_text += '**' + dominant_personalities[i] + '**'
        if highest == 0:
            pers_text = 'None'

        profile = discord.Embed(title = pers_title, description = pers_text, colour=0x5CFFE9)
        profile.set_author(name = player.name, icon_url = player.avatar_url)
        profile.set_thumbnail(url = thumbnail_urls[dominant_personality] if highest != 0 else 'https://i.imgur.com/AZgDHsm')
        profile.add_field(name = 'Personalities', value = all_pers_text)
        
        return profile

    def get_stats(self):
        wb = load_workbook("Jaegermore/records.xlsx")
        global_stats = wb['Global']
        game_stats = discord.Embed(title = '👥 Jaegermore Stats', colour=0x5CFFE9)
        game_stats.add_field(name = 'Total tests taken', value = str(global_stats['K2'].value), inline = False)
        mapping = {0:'B', 1:'C', 2:'D', 3:'E', 4:'F', 5:'G', 6:'H', 7:'I', 8:'J'}
        for i in range(9):
            game_stats.add_field(name = global_stats[mapping[i] + '1'].value, value = global_stats[mapping[i] + '2'].value, inline = True)
        return game_stats

    def get_commands(self):
        # Returns the list of commands
        commands_list = discord.Embed(title = 'List of commands for Jaegermore', colour = 0x5CFFE9)
        commands_list.add_field(name = '~start', value = 'Starts a new assessment. Use ~start full to take the full assessment.')
        commands_list.add_field(name = '~intro', value = 'Introduces the game.')
        commands_list.add_field(name = '~result', value = 'Reveals your personality at the end of the assessment.')
        commands_list.add_field(name = '~stats', value = 'Provides detailed scores obtained for each character at the end of the assessment.')
        commands_list.add_field(name = '~profile <@person>', value = 'Checks the profile of a given user. Use just ~profile to check your own profile.')
        commands_list.add_field(name = '~gamestats', value = 'Brings up the overall game statistics.')
        return commands_list