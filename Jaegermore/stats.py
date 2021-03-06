import random
import math
import discord
import sqlite3
from Jaegermore import questions

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
        conn = sqlite3.connect('Jaegermore/jaegermore_db.db')
        cursor = conn.cursor()

        # Update global stats
        global_stats_query = 'SELECT * FROM global'
        cursor.execute(global_stats_query)
        global_stats = cursor.fetchone()
        
        pers_mappings = {'eren':0, 'mikasa':1, 'armin':2, 'jean':3, 'krista':4, 'sasha':5, 'levi':6, 'annie':7, 'erwin':8}

        update_global_stats_query = 'UPDATE global SET {} = ?, total = ?'.format(character)
        updated_character = global_stats[pers_mappings[character]] + 1
        updated_total = global_stats[9] + 1
        cursor.execute(update_global_stats_query, (updated_character, updated_total))
        conn.commit()

        # Update player stats
        player_stats_query = 'SELECT * FROM players WHERE player = ?'
        cursor.execute(player_stats_query, (self.question.curplayer.id,))
        player_data = cursor.fetchone()

        if player_data:
            update_player_stats_query = 'UPDATE players SET {} = ? WHERE player = ?'.format(character)
            updated_player_character = player_data[pers_mappings[character] + 1] + 1
            cursor.execute(update_player_stats_query, (updated_player_character, self.question.curplayer.id))
        else:
            insert_player_stats_query = 'INSERT INTO players VALUES ({})'.format(','.join('?' * 10))
            insert_player_stats = [self.question.curplayer.id] + [0] * 9
            insert_player_stats[pers_mappings[character] + 1] = 1
            cursor.execute(insert_player_stats_query, insert_player_stats)

        conn.commit()
        conn.close()

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

    def calculate_affinity(self, personality_count, all_personalities_count):
        non_personality_count = (all_personalities_count - personality_count) / 8
        total_count = personality_count + non_personality_count

        if total_count > 0:
            raw_score = personality_count / total_count
        else:
            return 0

        affinity_score = raw_score - (raw_score - 0.5) * (1 / (2 ** math.log(total_count ** 1.75 + 1, 10)))
        return round(affinity_score * 100, 2)

    def get_profile(self, player):
        conn = sqlite3.connect('Jaegermore/jaegermore_db.db')
        cursor = conn.cursor()

        player_stats_query = 'SELECT * FROM players WHERE player = ?'
        cursor.execute(player_stats_query, (player.id,))
        player_data = cursor.fetchone()

        if player_data:
            all_personalities = player_data[1:]
        else:
            all_personalities = [0] * 9
            insert_player_stats_query = 'INSERT INTO players VALUES ({})'.format(','.join('?' * 10))
            insert_player_stats = [player.id] + all_personalities
            cursor.execute(insert_player_stats_query, insert_player_stats)
            conn.commit()

        conn.close()

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
        else:
            affinity_score = self.calculate_affinity(highest, sum(all_personalities))
            pers_text += '\n(Similarity: ' + str(affinity_score) + '%)'

        profile = discord.Embed(title = pers_title, description = pers_text, colour=0x5CFFE9)
        profile.set_author(name = player.name, icon_url = player.avatar_url)
        profile.set_thumbnail(url = thumbnail_urls[dominant_personality] if highest != 0 else 'https://i.imgur.com/AZgDHsm')
        profile.add_field(name = 'Personalities', value = all_pers_text)
        
        return profile

    def get_leaderboard(self, server, character=None):
        conn = sqlite3.connect('Jaegermore/jaegermore_db.db')
        cursor = conn.cursor()

        all_players_query = 'SELECT * FROM players'
        cursor.execute(all_players_query)
        all_players_data = cursor.fetchall()

        # Get server players
        # server_users_ids = {member.id: [member.id, member.name] for member in server.members}
        server_players_data = []
        for row in all_players_data:
            # if row[0] in server_users_ids:
            total_count = sum(row[1:])
            server_players_data.append([row[0]] + list(row[1:]) + [total_count])

        conn.close()
        
        # Sort by characters + total
        highest_rankings = [('Eren', []), ('Mikasa', []), ('Armin', []), ('Jean', []), ('Krista', []), ('Sasha', []), ('Levi', []), ('Annie', []), ('Erwin', []), ('Total', [])]
        for i, _ in enumerate(highest_rankings):
            if i == 9:
                server_players_data.sort(key=lambda row: row[i+1], reverse=True)
            else:
                server_players_data.sort(key=lambda row: self.calculate_affinity(row[i+1], row[-1]), reverse=True)

            for j in range(min(10, len(server_players_data))):
                # Name, affinity, count
                if i == 9:
                    rank_info = [server_players_data[j][0], server_players_data[j][i+1]]
                else:
                    rank_info = [server_players_data[j][0], self.calculate_affinity(server_players_data[j][i+1], server_players_data[j][-1]), server_players_data[j][i+1], server_players_data[j][-1]]
                highest_rankings[i][1].append(rank_info)

        # Display rankings for chosen character
        character_map = {'eren':0, 'mikasa':1, 'armin':2, 'jean':3, 'krista':4, 'sasha':5, 'levi':6, 'annie':7, 'erwin':8, 'total':9}
        thumbnail_urls = {'Eren':'https://i.imgur.com/AZgDHsm.png',
        'Mikasa':'https://i.imgur.com/DrfMlLN.png',
        'Armin':'https://i.imgur.com/H5SkwLR.jpg',
        'Jean':'https://i.imgur.com/BJdEBiW.jpg',
        'Krista':'https://i.imgur.com/fA9Nmdr.jpg',
        'Sasha':'https://i.imgur.com/8b9BXc7.jpg',
        'Levi':'https://i.imgur.com/6UoSOTQ.png',
        'Annie':'https://i.imgur.com/eDVpxFm.jpg',
        'Erwin':'https://i.imgur.com/MGKlG4x.png',
        'Total':'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/trophy_1f3c6.png'}

        if character and character in character_map:
            char_index = character_map[character]
            char_rankings = highest_rankings[char_index]
            player_names = ''
            player_affinities = ''
            char_count = ''
            for i, player in enumerate(char_rankings[1]):
                player_names += '#' + str(i+1) + ' <@' + str(player[0]) + '>\n'
                if char_index < 9:
                    player_affinities += str(player[1]) + '%\n'
                    char_count += str(player[2]) + '/' + str(player[3]) + '\n'
                else:
                    char_count += str(player[1]) + '\n'

            leaderboard = discord.Embed(title = 'Leaderboard for Jaegermore (' + char_rankings[0] + ')', colour=0x5CFFE9)
            leaderboard.add_field(name = 'Player', value = player_names)
            leaderboard.add_field(name = 'Count', value = char_count)
            if char_index < 9:
                leaderboard.set_thumbnail(url = thumbnail_urls[char_rankings[0]])
                leaderboard.add_field(name = 'Similarity', value = player_affinities)
            leaderboard.set_footer(text = 'How is Similarity calculated? Type ~similarity to find out!')

        else:
            leaderboard = discord.Embed(title = '👑 Leaderboard for Jaegermore 👑', colour=0x5CFFE9)
            for i, character_info in enumerate(highest_rankings):
                if i < 9:
                    leaderboard.add_field(name = character_info[0], value = '<@' + str(character_info[1][0][0]) + '>' + '\n' + 'Similarity: ' + str(character_info[1][0][1]) + '%')
                else:
                    leaderboard.add_field(name = character_info[0], value = '<@' + str(character_info[1][0][0]) + '>' + '\n' + 'Count: ' + str(character_info[1][0][1]))
            leaderboard.set_footer(text = 'Add a character name behind the ~lb command to see the leaderboard for each character, e.g. ~lb eren/~lb total.')
        
        return leaderboard


    def get_stats(self):
        conn = sqlite3.connect('Jaegermore/jaegermore_db.db')
        cursor = conn.cursor()

        global_stats_query = 'SELECT * FROM global'
        cursor.execute(global_stats_query)
        global_stats = cursor.fetchone()

        pers_mappings = {0:'Eren', 1:'Mikasa', 2:'Armin', 3:'Jean', 4:'Krista', 5:'Sasha', 6:'Levi', 7:'Annie', 8:'Erwin'}

        game_stats = discord.Embed(title = '👥 Jaegermore Stats', colour=0x5CFFE9)
        game_stats.add_field(name = 'Total tests taken', value = str(global_stats[9]), inline = False)
        for i in range(9):
            game_stats.add_field(name = pers_mappings[i], value = global_stats[i], inline = True)

        conn.close()

        return game_stats

    def get_commands(self):
        # Returns the list of commands
        commands_list = discord.Embed(title = 'List of commands for Jaegermore', colour = 0x5CFFE9)
        general_commands = '`~credits` : Who made me/Get support'
        commands_list.add_field(name = 'General', value = general_commands, inline = False)

        jaegermore_commands = '`~start`\n Starts a new assessment. Use `~start full` to take the full assessment.\n' + \
        '`~intro`\n Introduces the game.\n' + \
        '`~result`\n Reveals your personality at the end of the assessment.\n' + \
        '`~stats`\n Provides detailed scores for each character at the end of the assessment.\n' + \
        '`~profile <@person>`\n Checks the personality scores of a given user.\n' + \
        '`~leaderboard/~lb <personality>`\n Brings up the leaderboard, showing the top player(s) for each personality.\n' + \
        '`~gamestats`\n Brings up the overall game statistics.\n' + \
        '`~similarity`\n Explains how the similarity percentage for a character is calculated.'
        commands_list.add_field(name = 'Jaegermore', value = jaegermore_commands)
        return commands_list

    def similarity_explanation(self):
        similarity_msg = 'Your Similarity score for a given character is calculated based on two factors:\n\n' + \
            '1. The percentage of tests where you obtained that character\n' + \
            '2. The total number of tests taken\n\n' + \
            'What this means is that to increase your Similarity score for a character, you should try to get only that character in as many tests as possible!'
        similarity_embed = discord.Embed(title = 'How is Similarity calculated?', description = similarity_msg, colour = 0x5CFFE9)
        return similarity_embed