import discord
import random
import math
import sqlite3


class State():
    def __init__(self):
        # Constants
        self.intro_msg = discord.Embed(
            title = 'Welcome to ⚔ Warriors vs Soldiers 🛡!',
            description = 'In this Attack on Titan themed party game for 5-10 players, the Soldiers of the Survey Corps embark on expeditions to reach the Basement, which they believe \
holds the secrets about the world.\n\n\
However, the Titan shifters known as Warriors have infiltrated their ranks, and will do anything it takes to sabotage the expeditions and destroy the Walls.\n\n\
As a participant in this game, your abilities of logical deduction, deception, and teamwork will be put to the ultimate test.\n\n\
Will the Soldiers reach the Basement and find out the truth about the world? \
Or will the Warriors destroy the Walls and wipe out humanity? You decide!\n\n\
❗Type `~host` to begin a new game.\n\n\
❗Type `~rules` to view the game rules.\n\n\
❗Type `~help` to see the full list of commands.',  
            colour=0x0013B4)

        self.reset_msg = discord.Embed(title = 'Game Reset!', description = 'Type **`~host`** to create a new lobby.\nType **`~intro`** for more information about the game.', colour=0x0013B4)

        self.start_msg = 'Assigning roles...'
        self.roles_assigned_msg = 'Roles assigned!\n\nWhen everyone is ready, type `~next` to begin the first expedition.'

        self.player_roles = {5: ['soldier','soldier','warrior','warrior','coordinate'], 
                             6: ['soldier','soldier','soldier','warrior','warrior','coordinate'],
                             7: ['soldier','soldier','soldier','warrior','warrior','warrior','coordinate'], 
                             8: ['soldier','soldier','soldier','soldier','warrior','warrior','warrior','coordinate'], 
                             9: ['soldier','soldier','soldier','soldier','soldier','warrior','warrior','warrior','coordinate'], 
                             10: ['soldier','soldier','soldier','soldier','soldier','warrior','warrior','warrior','warrior','coordinate']}
        self.warrior_roles = ['warrior','warchief','false king','ymir','spy']
        self.expedition_sizes = {5:[2,3,2,3,3], 6:[2,3,4,3,4], 7:[2,3,3,4,4], 8:[3,3,4,4,5], 9:[3,4,4,5,5], 10:[3,3,4,5,5]}
        self.expedition_advantages = {5:-50, 6:50, 7:-100, 8:0, 9:100, 10:-150}
        self.roles_advantages = {'queen': {5:150, 6:130, 7:120, 8:100, 9:80, 10:70},
                                 'ackerman': {5:100, 6:120, 7:150, 8:160, 9:180, 10:200},
                                 'mike': {5:160, 6:140, 7:120, 8:100, 9:90, 10:80},
                                 'scout': {5:-120, 6:-90, 7:-80, 8:-60, 9:-40, 10:-40},
                                 'warchief': {5:-120, 6:-110, 7:-90, 8:-80, 9:-60, 10:-50},
                                 'false king': {5:-140, 6:-120, 7:-100, 8:-80, 9:-60, 10:-40},
                                 'ymir': {5:100, 6:90, 7:60, 8:50, 9:50, 10:30},
                                 'spy': {5:-140, 6:-160, 7:-180, 8:-200, 9:-220, 10:-240}}
        self.blessing_advantages = {5:150, 6:120, 7:100, 8:80, 9:60, 10:50}
        self.funds_advantages = {5:-50, 6:-60, 7:-70, 8:-80, 9:-90, 10:-100}


        self.number_games_achievements = {10:'Bronze', 25:'Silver', 50:'Gold', 100:'Platinum', 250:'Diamond', 500:'Master', 1000:'Grandmaster'}
        self.consecutive_wins_achievements = {2:'Bronze', 3:'Silver', 5:'Gold', 7:'Platinum', 10:'Diamond', 15:'Master', 20:'Grandmaster'}
        self.soldier_wins_achievements = {3:'Bronze', 8:'Silver', 15:'Gold', 25:'Platinum', 50:'Diamond', 100:'Master', 200:'Grandmaster'}
        self.warrior_wins_achievements = {3:'Bronze', 8:'Silver', 15:'Gold', 25:'Platinum', 50:'Diamond', 100:'Master', 200:'Grandmaster'}
        self.coordinate_wins_achievements = {3:'Bronze', 8:'Silver', 15:'Gold', 25:'Platinum', 50:'Diamond', 100:'Master', 200:'Grandmaster'}
        self.queen_wins_achievements = {3:'Bronze', 8:'Silver', 15:'Gold', 25:'Platinum', 50:'Diamond', 100:'Master', 200:'Grandmaster'}
        self.warchief_wins_achievements = {3:'Bronze', 8:'Silver', 15:'Gold', 25:'Platinum', 50:'Diamond', 100:'Master', 200:'Grandmaster'}

        self.achievement_rewards = {'Bronze': 20, 'Silver': 40, 'Gold': 60, 'Platinum': 80, 'Diamond': 100, 'Master': 150, 'Grandmaster': 250}
        self.badge_emojis = {'Bronze': '🥉', 'Silver': '🥈', 'Gold': '🥇', 'Platinum': '💠', 'Diamond': '💎', 'Master': '👑', 'Grandmaster': '🎓'}

        # Variables
        self.status = 'waiting for game' # waiting for players, assigning roles, expedition selection, expedition approval, expedition decision, expedition over, choose coordinate, game ended

        self.game_channel = None
        self.server = None
        self.game_host = None
        self.reset_confirmation = False
        self.gametype = 'Ranked'
        self.gamespeed = 'Normal'
        self.players = [] # each player is a list of two elements: the player object and the player's role (str)
        self.message_box = []
        self.newroles = []
        self.ymir_blessing = False
        self.blessed = []
        self.currently_blessed = None
        self.randomroles = False
        self.paths = False
        self.paths_holders = []
        self.funds_enabled = False
        self.funds = 5
        self.kenny = False
        self.kenny_hit_list = []
        self.num_targets = 1
        
        self.cur_expedition = 0
        self.expedition_squad = []
        self.expedition_approval = []
        self.votes_flipped = False
        self.flipping_votes = False
        self.expedition_result = []

        self.expedition_history = []
        self.successful_expeditions = 0
        self.walls_destroyed = 0
        self.wall_secured = False

    def host(self, player, server, fast, ranked):
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        self.server = server
           
        if self.status == 'waiting for players':
            return '**' + self.game_host.name + '** is already the host!'
        elif self.status == 'waiting for game' or self.status == 'game ended':
            self.gametype = 'Ranked'
            if ranked == False:
                self.gametype = 'Casual'
            self.gamespeed = 'Normal'
            if fast == True:
                self.gamespeed = 'Fast'
            self.game_host = player
            self.reset_confirmation = False
            self.status = 'waiting for players'
            self.players = [[player, None]]
            self.newroles = []
            self.ymir_blessing = False
            self.blessed = []
            self.currently_blessed = None
            self.randomroles = False
            self.paths = False
            self.paths_holders = []
            self.funds_enabled = False
            self.funds = 5
            self.kenny = False
            self.kenny_hit_list = []
            self.num_targets = 1

            self.cur_expedition = 0
            self.expedition_squad = []
            self.expedition_approval = []
            self.votes_flipped = False
            self.flipping_votes = False
            self.expedition_result = []

            self.expedition_history = []
            self.successful_expeditions = 0
            self.walls_destroyed = 0
            self.wall_secured = False

            msg = '**' + player.name + '** has started a new lobby! Type `~join` to join the game!'

            # Get total players in server
            player_rankings_query = 'SELECT player, rating FROM players'
            cursor.execute(player_rankings_query)
            player_rankings = cursor.fetchall()
            
            # Sort by Exp from biggest to smallest
            player_rankings.sort(key = lambda x: x[1], reverse = True)

            # Get players in server
            server_users = list(map(lambda y: y.id, server.members))
            server_players = list(filter(lambda x:x[0] in server_users, player_rankings))

            conn.close()

            for person in server_players:
                if person[0] == player.id:
                    msg = '👑 | Humanity\'s strongest soldier ' + msg
                break

            return msg
        else:
            return 'The game has already started!'

    def join(self, player, server):
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        if self.status == 'waiting for players':
            if player in list(map(lambda x:x[0], self.players)):
                return 'You are already in the lobby!'
            elif len(self.players) >= 10:
                return 'Lobby is full! (Maximum of 10 players)'
            else:
                self.players.append([player, None])
                msg = '**' + player.name + '** has joined the game!'

                # Get total players in server
                player_rankings_query = 'SELECT player, rating FROM players'
                cursor.execute(player_rankings_query)
                player_rankings = cursor.fetchall()
                
                # Sort by Exp from biggest to smallest
                player_rankings.sort(key = lambda x: x[1], reverse = True)

                # Get players in server
                server_users = list(map(lambda y: y.id, server.members))
                server_players = list(filter(lambda x:x[0] in server_users, player_rankings))

                conn.close()

                for person in server_players:
                    if person[0] == player.id:
                        msg = '👑 | Humanity\'s strongest soldier ' + msg
                    break

                return msg

        elif self.status == 'waiting for game' or self.status.startswith('game ended'):
            return 'There is no open lobby at the moment!'
        else:
            return 'The game has already started!'

    def leave(self, player):
        if self.status == 'waiting for players':
            if player not in list(map(lambda x:x[0], self.players)):
                return 'You are not in the lobby!'
            # Resets if no one is left
            elif len(self.players) == 1:
                self.reset(player)
                return '**' + player.name + '** has left the lobby! Lobby closed.'
            # Also resets if host leaves
            elif player == self.game_host:
                self.reset(player)
                return 'The host, **' + player.name + '**, has left the lobby! Lobby closed.'
            else:
                self.players.remove([player, None])
                return '**' + player.name + '** has left the lobby!'
        elif self.status == 'waiting for game' or self.status.startswith('game ended'):
            return 'There is no open lobby at the moment!'
        else:
            return 'The game has already started!'

    def kick(self, author, player):
        if self.status == 'waiting for players':
            if author != self.game_host and author.id != 238808836075421697:
                return 'Only the host can kick other players!'
            elif player not in list(map(lambda x:x[0], self.players)):
                return '**' + player.name + '** is not in the lobby!'
            elif player == self.game_host:
                return 'You can\'t kick yourself!'
            else:
                self.players.remove([player, None])
                return '**' + player.name + '** has been removed from the lobby!'
        elif self.status == 'waiting for game':
            return 'There is no open lobby at the moment!'
        else:
            return 'The game has already started!'

    def add_with_role_count_check(self, role):
        soldier_dict = {'queen': '👼**Queen**👼',
                        'ackerman': '💂**Ackerman**💂',
                        'mike': '<:aotSmirk:571740978377916416>**Mike Zacharias** <:aotSmirk:571740978377916416>',
                        'scout': '🏇**Scout**🏇'}

        warrior_dict = {'warchief': '🦹‍♂️**Warchief**🦹‍♂️',
                        'ymir': '🤷‍♀️**Ymir**🤷‍♀️',
                        'false king': '🕴**False King**🕴',
                        'spy': '🕵️‍♀️**Spy**🕵️‍♀️'}
        
        if role in soldier_dict:
            soldier_role_count = len(list(filter(lambda role:role not in self.warrior_roles, self.newroles)))
            if soldier_role_count >= 3:
                if len(self.players) >= 8:
                    self.newroles.append(role)
                    return 'The role {} has been added to the game!'.format(soldier_dict[role])
                else:
                    return 'At least 8 players are needed to add another optional soldier role!'
            elif soldier_role_count >= 2:
                if len(self.players) >= 6:
                    self.newroles.append(role)
                    return 'The role {} has been added to the game!'.format(soldier_dict[role])
                else:
                    return 'At least 6 players are needed to add another optional soldier role!'
            else:
                self.newroles.append(role)
                return 'The role {} has been added to the game!'.format(soldier_dict[role])

        elif role in warrior_dict:
            warrior_role_count = len(list(filter(lambda role:role in self.warrior_roles, self.newroles)))
            if warrior_role_count >= 3:
                if len(self.players) >= 10:
                    self.newroles.append(role)
                    return 'The role {} has been added to the game!'.format(warrior_dict[role])
                else:
                    return 'At least 10 players are needed to add another optional warrior role!'
            elif warrior_role_count >= 2:
                if len(self.players) >= 7:
                    self.newroles.append(role)
                    return 'The role {} has been added to the game!'.format(warrior_dict[role])
                else:
                    return 'At least 7 players are needed to add another optional warrior role!'
            else:
                self.newroles.append(role)
                return 'The role {} has been added to the game!'.format(warrior_dict[role])

    def addrole(self, role, player, randomroles=False):
        if self.status == 'waiting for players' or randomroles == True:
            if player == self.game_host or player.id == 238808836075421697:
                if role == 'blessing' or role == 'ymir\'s blessing' or role == 'ymirs blessing' or role == 'ymir blessing':
                    if self.ymir_blessing == False:
                        self.ymir_blessing = True
                        return '🔮**Ymir\'s Blessing**🔮 has been enabled!'
                    else:
                        return '🔮**Ymir\'s Blessing**🔮 has already been enabled!'

                elif role == 'paths':
                    if self.paths == False:
                        self.paths = True
                        return 'The power of the 📢**Paths**📢 has been enabled!'
                    else:
                        return 'The power of the 📢**Paths**📢 has already been enabled!'

                elif role == 'funds' or role == 'limited funds':
                    if self.funds_enabled == False:
                        self.funds_enabled = True
                        return '💰**Limited Funds**💰 for expeditions has been enabled!'
                    else:
                        return '💰**Limited Funds**💰 for expeditions has already been enabled!'

                elif role == 'kenny' or role == 'kenny the ripper':
                    if self.kenny == False:
                        self.kenny = True
                        return '<:kennytheripper:768310628506402887> **Kenny the Ripper** <:kennytheripper:768310628506402887> has been enabled!'
                    else:
                        return '<:kennytheripper:768310628506402887> **Kenny the Ripper** <:kennytheripper:768310628506402887> has already been enabled!'

                elif role == 'queen':
                    if role not in self.newroles:
                        return self.add_with_role_count_check('queen')
                    else:
                        return 'The 👼**Queen**👼 role is already in the game!'

                elif role == 'ackerman':
                    if role not in self.newroles:
                        return self.add_with_role_count_check('ackerman')
                    else:
                        return 'The 💂**Ackerman**💂 role is already in the game!'

                elif role == 'mike' or role == 'mike zacharias' or role == 'zacharias':
                    role = 'mike'
                    if role not in self.newroles:
                        return self.add_with_role_count_check('mike')
                    else:
                        return '<:aotSmirk:571740978377916416>**Mike Zacharias** <:aotSmirk:571740978377916416> is already in the game!'

                elif role == 'scout':
                    if role not in self.newroles:
                        return self.add_with_role_count_check('scout')
                    else:
                        return 'The 🏇**Scout**🏇 role is already in the game!'
                    
                elif role == 'warchief':
                    if role not in self.newroles:
                        return self.add_with_role_count_check('warchief')
                    else:
                        return 'The 🦹‍♂️**Warchief**🦹‍♂️ role is already in the game!'

                elif role == 'ymir':
                    if role not in self.newroles:
                        return self.add_with_role_count_check('ymir')
                    else:
                        return 'The 🤷‍♀️**Ymir**🤷‍♀️ role is already in the game!'

                elif role == 'false king':
                    if role not in self.newroles:
                        if 'queen' not in self.newroles:
                            return 'The 👼**Queen**👼 role needs to be added first!'

                        return self.add_with_role_count_check('false king')
                    else:
                        return 'The 🕴**False King**🕴 role is already in the game!'

                elif role == 'spy':
                    if role not in self.newroles:
                        return self.add_with_role_count_check('spy')
                    else:
                        return 'The 🕵️‍♀️**Spy**🕵️‍♀️ role is already in the game!'

                else:
                    return 'Invalid role!'
            else:
                return 'Only the host can add or remove optional roles!'
        else:
            return 'There is no open lobby at the moment!'

    def removerole(self, role, player):
        if self.status == 'waiting for players':
            if player == self.game_host or player.id == 238808836075421697:
                if role == 'blessing' or role == 'ymir\'s blessing' or role == 'ymirs blessing' or role == 'ymir blessing':
                    if self.ymir_blessing == True:
                        self.ymir_blessing = False
                        return '🔮**Ymir\'s Blessing**🔮 has been disabled!'
                    else:
                        return '🔮**Ymir\'s Blessing**🔮 is not currently enabled!'

                elif role == 'paths':
                    if self.paths == True:
                        self.paths = False
                        return 'The power of the 📢**Paths**📢 has been disabled!'
                    else:
                        return 'The power of the 📢**Paths**📢 is not currently enabled!'

                elif role == 'funds' or role == 'limited funds':
                    if self.funds_enabled == True:
                        self.funds_enabled = False
                        return '💰**Limited Funds**💰 for expeditions has been disabled!'
                    else:
                        return '💰**Limited Funds**💰 for expeditions is not currently enabled!'

                elif role == 'kenny' or role == 'kenny the ripper':
                    if self.kenny == True:
                        self.kenny = False
                        return '<:kennytheripper:768310628506402887> **Kenny the Ripper** <:kennytheripper:768310628506402887> has been disabled!'
                    else:
                        return '<:kennytheripper:768310628506402887> **Kenny the Ripper** <:kennytheripper:768310628506402887> is not currently enabled!'

                elif role == 'queen':
                    if role in self.newroles:
                        self.newroles.remove('queen')
                        if 'false king' in self.newroles:
                            self.newroles.remove('false king')
                        return 'The role 👼**Queen**👼 has been removed from the game!'
                    else:
                        return 'The 👼**Queen**👼 role is not in the game!'

                elif role == 'ackerman':
                    if role in self.newroles:
                        self.newroles.remove('ackerman')
                        return 'The role 💂**Ackerman**💂 has been removed from the game!'
                    else:
                        return 'The 💂**Ackerman**💂 role is not in the game!'

                elif role == 'mike' or role == 'mike zacharias' or role == 'zacharias':
                    role = 'mike'
                    if role in self.newroles:
                        self.newroles.remove('mike')
                        return '<:aotSmirk:571740978377916416>**Mike Zacharias** <:aotSmirk:571740978377916416> has been removed from the game!'
                    else:
                        return '<:aotSmirk:571740978377916416>**Mike Zacharias** <:aotSmirk:571740978377916416> is not in the game!'

                elif role == 'scout':
                    if role in self.newroles:
                        self.newroles.remove('scout')
                        return 'The role 🏇**Scout**🏇 has been removed from the game!'
                    else:
                        return 'The 🏇**Scout**🏇 role is not in the game!'
                    
                elif role == 'warchief':
                    if role in self.newroles:
                        self.newroles.remove('warchief')
                        return 'The role 🦹‍♂️**Warchief**🦹‍♂️ has been removed from the game!'
                    else:
                        return 'The 🦹‍♂️**Warchief**🦹‍♂️ role is not in the game!'

                elif role == 'ymir':
                    if role in self.newroles:
                        self.newroles.remove('ymir')
                        return 'The role 🤷‍♀️**Ymir**🤷‍♀️ has been removed from the game!'
                    else:
                        return 'The 🤷‍♀️**Ymir**🤷‍♀️ role is not in the game!'

                elif role == 'false king':
                    if role in self.newroles:
                        self.newroles.remove('false king')
                        return 'The role 🕴**False King**🕴 has been removed from the game!'
                    else:
                        return 'The 🕴**False King**🕴 role is not in the game!'

                elif role == 'spy':
                    if role in self.newroles:
                        self.newroles.remove('spy')
                        return 'The role 🕵️‍♀️**Spy**🕵️‍♀️ has been removed from the game!'
                    else:
                        return 'The 🕵️‍♀️**Spy**🕵️‍♀️ role is not in the game!'

                else:
                    return 'Invalid role!'
            else:
                return 'Only the host can add or remove optional roles!'
        else:
            return 'There is no open lobby at the moment!'

    def toggle_randomroles(self, player):
        if self.status == 'waiting for players':
            if player == self.game_host or player.id == 238808836075421697:
                if self.randomroles:
                    self.randomroles = False
                    return 'Random roles have been disabled!'
                else:
                    self.randomroles = True
                    return 'Random roles have been enabled!'
            else:
                return 'Only the host can add or remove optional roles!'
        else:
            return 'There is no open lobby at the moment!'

    def toggle_gametype(self, player, gametype):
        if self.status == 'waiting for players':
            if player == self.game_host or player.id == 238808836075421697:
                if gametype == 'fast':
                    if self.gamespeed == 'Fast':
                        return 'The game speed is already set to **Fast**!'
                    else:
                        self.gamespeed = 'Fast'
                        return 'The game speed has been set to **Fast**!'

                elif gametype == 'normal':
                    if self.gamespeed == 'Normal':
                        return 'The game speed is already set to **Normal**!'
                    else:
                        self.gamespeed = 'Normal'
                        return 'The game speed has been set to **Normal**!'
                
                elif gametype == 'casual':
                    if self.gametype == 'Casual':
                        return 'The game is already in **Casual** mode!'
                    else:
                        self.gametype = 'Casual'
                        return '**Casual** mode has been enabled!'
                    
                elif gametype == 'ranked':
                    if self.gametype == 'Ranked':
                        return 'The game is already in **Ranked** mode!'
                    else:
                        self.gametype = 'Ranked'
                        return '**Ranked** mode has been enabled!'
                
            else:
                return 'Only the host can change the game type!'
        else:
            return 'There is no open lobby at the moment!'


    def display_lobby(self):
        players_in_lobby = ''
        for person in self.players:
            if person[0] == self.game_host:
                players_in_lobby = players_in_lobby + '**' + person[0].mention + '** (Host)\n'
            else:
                players_in_lobby = players_in_lobby + '**' + person[0].mention + '**\n'

        lobby = discord.Embed(title = 'Current lobby', colour=0x0013B4)
        lobby.add_field(name = 'Game Type', value = '**' + self.gamespeed + ' ' + self.gametype + '**')
        lobby.add_field(name = 'Advantage', value = '⚖️ **Perfectly balanced!** ⚖️' if self.calculate_advantage() == '**None**' else self.calculate_advantage())
        lobby.add_field(name = '**' + str(len(self.players)) + '** player' + ('s' if len(self.players) > 1 else '') + ' in lobby', value = players_in_lobby, inline = False)
        lobby.add_field(name = 'Random Roles', value = '🎲' if self.randomroles else '⬛', inline=False)
        lobby.add_field(name = 'Optional Soldier Roles', value = self.get_newroles('soldier'))
        lobby.add_field(name = '⠀', value = '⠀', inline = True)
        lobby.add_field(name = 'Optional Warrior Roles', value = self.get_newroles('warrior'))
        lobby.add_field(name = 'In-Game Effects', value = self.get_effects('effects1'), inline = True)
        lobby.add_field(name = '⠀', value = '⠀', inline = True)
        lobby.add_field(name = '⠀', value = self.get_effects('effects2'), inline = True)
        return lobby

    def get_newroles(self, team):
        if team == 'soldier':
            queencheck = '✅' if 'queen' in self.newroles else '✖'
            ackermancheck = '✅' if 'ackerman' in self.newroles else '✖'
            mikecheck = '✅' if 'mike' in self.newroles else '✖'
            scoutcheck = '✅' if 'scout' in self.newroles else '✖'
            role_msg = queencheck + ' 👼**Queen**👼\n\n' + ackermancheck + ' 💂**Ackerman**💂\n\n' + \
                mikecheck + ' <:aotSmirk:571740978377916416>**Mike Zacharias** <:aotSmirk:571740978377916416>\n\n' + scoutcheck + ' 🏇**Scout**🏇'
            return role_msg
        elif team == 'warrior':
            warchiefcheck = '✅' if 'warchief' in self.newroles else '✖'
            falsekingcheck = '✅' if 'false king' in self.newroles else '✖'
            ymircheck = '✅' if 'ymir' in self.newroles else '✖'
            spycheck = '✅' if 'spy' in self.newroles else '✖'
            role_msg = warchiefcheck + ' 🦹‍♂️**Warchief**🦹‍♂️\n\n' + falsekingcheck + ' 🕴**False King**🕴\n\n' + ymircheck + ' 🤷‍♀️**Ymir**🤷‍♀️\n\n' + spycheck + ' 🕵️‍♀️**Spy**🕵️‍♀️'
            return role_msg
    
    def get_effects(self, effect):
        if effect == 'effects1':
            ymirblessingcheck = '🔮' if self.ymir_blessing else '◼'
            fundscheck = '💰' if self.funds_enabled else '◼'
            role_msg = ymirblessingcheck + ' **Ymir\'s Blessing** ' + ymirblessingcheck + '\n\n' + fundscheck + ' **Limited Funds** ' + fundscheck
            return role_msg
        elif effect == 'effects2':
            pathscheck = '📢' if self.paths else '◼'
            kennycheck = '<:kennytheripper:768310628506402887>' if self.kenny else '◼'
            role_msg = pathscheck + ' **Paths** ' + pathscheck + '\n\n' + kennycheck + ' **Kenny the Ripper** ' + kennycheck
            return role_msg

    def randomize_roles(self):
        self.newroles = []
        rolelist = ['queen', 'ackerman', 'mike', 'scout', 'warchief', 'false king', 'ymir', 'spy']
        for role in rolelist:
            to_add = random.randint(0, 1)
            if to_add:
                self.addrole(role, self.game_host, randomroles=True)

    def start(self, player):
        if self.status == 'waiting for players':
            if player == self.game_host or player.id == 238808836075421697:
                if len(self.players) >= 5:
                    self.message_box = []
                    self.status = 'assigning roles' # First input is selection of expedition members by commander

                    # Randomize roles
                    if self.randomroles:
                        self.randomize_roles()

                    # Add optional roles
                    all_player_roles = self.player_roles[len(self.players)].copy()
                    if 'queen' in self.newroles:
                        for i in range(len(all_player_roles)):
                            if all_player_roles[i] == 'soldier':
                                all_player_roles[i] = 'queen'
                                break
                    if 'ackerman' in self.newroles:
                        for i in range(len(all_player_roles)):
                            if all_player_roles[i] == 'soldier':
                                all_player_roles[i] = 'ackerman'
                                break
                    if 'mike' in self.newroles:
                        for i in range(len(all_player_roles)):
                            if all_player_roles[i] == 'soldier':
                                all_player_roles[i] = 'mike'
                                break
                    if 'scout' in self.newroles:
                        for i in range(len(all_player_roles)):
                            if all_player_roles[i] == 'soldier':
                                all_player_roles[i] = 'scout'
                                break
                    if 'warchief' in self.newroles:
                        for i in range(len(all_player_roles)):
                            if all_player_roles[i] == 'warrior':
                                all_player_roles[i] = 'warchief'
                                break
                    if 'ymir' in self.newroles:
                        for i in range(len(all_player_roles)):
                            if all_player_roles[i] == 'warrior':
                                all_player_roles[i] = 'ymir'
                                break
                    if 'false king' in self.newroles:
                        for i in range(len(all_player_roles)):
                            if all_player_roles[i] == 'warrior':
                                all_player_roles[i] = 'false king'
                                break
                    if 'spy' in self.newroles:
                        for i in range(len(all_player_roles)):
                            if all_player_roles[i] == 'warrior':
                                all_player_roles[i] = 'spy'
                                break
                    
                    self.players.sort(key = lambda x: random.randint(1,100)) # Randomizes player list
                    for i in range(len(self.players)): # Assigns roles to players
                        self.players[i][1] = all_player_roles[i]
                    self.players.sort(key = lambda x: random.randint(1,100)) # Randomizes player list again to get commander

                    if self.paths:
                        self.paths_holders = list(map(lambda x: x[0], self.players))
                        self.paths_holders.sort(key = lambda x: random.randint(1,100))

                    if self.kenny:
                        self.kenny_hit_list = [player[0] for player in self.players]
                        self.kenny_hit_list.sort(key = lambda x: random.randint(1,100))
                        if len(self.players) >= 9:
                            self.num_targets = 2

                    self.cur_expedition += 1
                    return 'Starting game with **' + str(len(self.players)) + '** players!'

                else:
                    return 'Need more players (at least 5 total) to start the game!'
            else:
                return 'Only the host, **' + self.game_host.mention + '**, can start the game!'

        elif self.status == 'waiting for game' or self.status.startswith('game ended'):
            return 'There is no open lobby at the moment!'
        else:
            return 'The game has already started!'

    def reset(self, player):
        if (player == self.game_host or player.id == 238808836075421697) or (self.game_host == None) or (self.status == 'waiting for players') or (self.status.startswith('game ended')):
            if not ((self.game_host == None) or (self.status == 'waiting for players') or (self.status.startswith('game ended'))) and \
                (player == self.game_host or player.id == 238808836075421697) and self.reset_confirmation == False:
                self.reset_confirmation = True
                return player.mention + ', are you sure you want to reset the game? Type `~reset` again to confirm.'

            self.status = 'waiting for game'

            self.game_host = None
            self.reset_confirmation = False
            self.gametype = 'Ranked'
            self.gamespeed = 'Normal'
            self.players = []
            self.message_box = []
            self.newroles = []
            self.ymir_blessing = False
            self.blessed = []
            self.currently_blessed = None
            self.randomroles = False
            self.paths = False
            self.paths_holders = []
            self.funds_enabled = False
            self.funds = 5
            self.kenny = False
            self.kenny_hit_list = []
            self.num_targets = 1

            self.cur_expedition = 0
            self.expedition_squad = []
            self.expedition_approval = []
            self.votes_flipped = False
            self.flipping_votes = False
            self.expedition_result = []

            self.expedition_history = []
            self.successful_expeditions = 0
            self.walls_destroyed = 0
            self.wall_secured = False

            return self.reset_msg

        else:
            return 'Only the host of the current game, **' + self.game_host.name + '**, can reset the game!'

    def get_role_msg(self, player_lst):
        soldier_msg = 'You are a **Soldier**!\n\n\
As a member of the Survey Corps, you have been tasked with the responsibility of finding the secrets to the world \
by reaching the basement.\n\n\
Your task is to find out who the traitors within the military are, reach the basement before they destroy all 3 Walls, and help protect the identity \
of the Coordinate.'

        warrior_msg = 'You are a **Warrior**!\n\n\
You are a Titan shifter who has infiltrated the Walls and are now working undercover to undermine the military\'s efforts. Working with your \
fellow Warriors, you seek to destroy the Walls and wipe out humanity. \n\n\
Your task is to conceal your identity from the Soldiers, and persuade them to allow you into their expeditions. At the same time, you need to try and identify the Coordinate within the ranks of the Soldiers.\n\n\
Your fellow Warriors are:\n'
        for warrior in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
            if warrior == player_lst or warrior[1] == 'ymir':
                continue
            else:
                warrior_msg = warrior_msg + '**' + warrior[0].name + '**\n'
        if 'ymir' in self.newroles:
            warrior_msg = warrior_msg + '\n❗*You do not know **Ymir\'s** identity.*'

        coordinate_msg = 'You are the **Coordinate**!\n\n\
You possess the special ability to sense Titan powers, which allows you to know who the Warriors are. However, due to the powers you possess, \
you are also their prime target, and so you must endeavour to remain hidden while aiding the Soldiers as much as you can. \n\n\
Your task is to help the Soldiers achieve victory using your knowledge of the Warriors\' identities, while keeping your identity as the Coordinate a secret from the Warriors.\n\n\
The Warriors are:\n'
        for warrior in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
            if warrior[1] == 'warchief':
                continue
            else:
                coordinate_msg = coordinate_msg + '**' + warrior[0].name + '**\n'
        if 'warchief' in self.newroles:
            coordinate_msg = coordinate_msg + '\n❗*The identity of the **Warchief** is hidden from you*.'

        queen_msg = 'You are the **Queen**!\n\n\
As Queen of the Walls, you possess the ability to sense the Coordinate\'s powers. Use this knowledge wisely to help the Soldiers achieve victory.\n\n\
Your task is to protect the Coordinate by using your knowledge of their identity to deceive the Warriors into thinking you are the Coordinate.\n\n'
        if 'false king' not in self.newroles:
            queen_msg = queen_msg + 'The Coordinate is:\n**' + list(filter(lambda x:x[1] == 'coordinate', self.players))[0][0].name + '**'
        else:
            queen_msg = queen_msg + 'The Coordinate is one of the following two players. The other is the False King:\n'
            coord_list = ['coordinate', 'false king']
            coord_list.sort(key = lambda x: random.randint(1,100))
            for role in coord_list:
                queen_msg = queen_msg + '**' + list(filter(lambda x:x[1] == role, self.players))[0][0].name + '**\n'

        ackerman_msg = 'You are the **Ackerman**!\n\n\
As one of humanity\'s strongest soldiers, you have been tasked with the responsibility of protecting the Walls.\n\n\
You have the ability to **secure** the Walls on one expedition if you\'re in it. This prevents any Warriors on the expedition from destroying it.\n\n\
However, doing so also alerts any Warriors on the expedition of your identity as the Ackerman, making it easier for them to identity the Coordinate. Use this ability wisely.'

        mike_msg = 'You are **Mike Zacharias**!\n\n\
Using your incredible sense of smell, you have the ability to sniff out Titans in expeditions.\n\n\
During the approval phase of every expedition you are in, you will be told how many Titans the expedition team contains, if any. Both Warriors and the Coordinate are considered Titans.\n\n\
Your task is to aid the Soldiers discreetly without giving away this information to the Warriors.'

        scout_msg = 'You are the **Scout**!\n\n\
As the guide of the expedition, you will fire a signal flare in any expedition that you are in, alerting all to your presence.\n\n\
Your task is to guide the Soldiers to pick the correct team for expeditions, while also hiding your identity from the Warriors to help protect the Coordinate.'

        warchief_msg = 'You are the **Warchief**!\n\n\
As the leader of the Warriors, you have the unique ability of concealing your Titan powers from the Coordinate. Use this extra layer of anonymity to infiltrate deep into the Soldiers\' \
ranks and ensure the Warriors emerge victorious.\n\n\
Your task is the same as your fellow Warriors: Destroy the Walls by getting into expeditions, and try to identify the Coordinate.\n\n\
Your fellow Warriors are:\n'
        for warrior in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
            if warrior == player_lst or warrior[1] == 'ymir':
                continue
            else:
                warchief_msg = warchief_msg + '**' + warrior[0].name + '**\n'
        if 'ymir' in self.newroles:
            warchief_msg = warchief_msg + '\n❗*You do not know **Ymir\'s** identity.*'

        ymir_msg = 'You are **Ymir**!\n\n\
While you are on the Warriors\' side, you do not know of their identities, nor do they know of yours. To achieve success, be sure to keep a close watch \
for potential comrades during expeditions.\n\n\
Your task is to identify your fellow Warriors, and work with them to destroy the Walls.'

        falseking_msg = 'You are the **False King**!\n\n\
You appear as the Coordinate to the Queen, in addition to the real Coordinate. Use this ability to confuse her by acting as the Coordinate, to \
help turn the tide in the Warriors\' favor.\n\n\
Your task is the same as your fellow Warriors: Destroy the Walls by getting into expeditions, and try to identify the Coordinate.\n\n\
Your fellow Warriors are:\n'
        for warrior in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
            if warrior == player_lst or warrior[1] == 'ymir':
                continue
            else:
                falseking_msg = falseking_msg + '**' + warrior[0].name + '**\n'
        if 'ymir' in self.newroles:
            falseking_msg = falseking_msg + '\n❗*You do not know **Ymir\'s** identity.*'

        spy_msg = 'You are the **Spy**!\n\n\
As the Warriors\' most skilled infiltrator, you have the ability to flip the votes during the approval phase of an expedition once.\n\n\
Your task is to help swing the expeditions in the Warriors\' favor at the right time, to achieve your goal of destroying the Walls.\n\n\
Your fellow Warriors are:\n'
        for warrior in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
            if warrior == player_lst or warrior[1] == 'ymir':
                continue
            else:
                spy_msg = spy_msg + '**' + warrior[0].name + '**\n'
        if 'ymir' in self.newroles:
            spy_msg = spy_msg + '\n❗*You do not know **Ymir\'s** identity.*'

        player_role = player_lst[1]
        role_msgs = {
            'soldier': soldier_msg, 
            'warrior': warrior_msg, 
            'coordinate': coordinate_msg,
            'queen': queen_msg, 
            'ackerman': ackerman_msg,
            'mike': mike_msg,
            'scout': scout_msg,
            'warchief': warchief_msg, 
            'ymir': ymir_msg, 
            'false king': falseking_msg,
            'spy': spy_msg
        }
        allegiances = {
            'soldier': 'soldier', 
            'warrior': 'warrior', 
            'coordinate': 'soldier',
            'queen': 'soldier', 
            'ackerman': 'soldier',
            'mike': 'soldier',
            'scout': 'soldier',
            'warchief': 'warrior', 
            'ymir': 'warrior', 
            'false king': 'warrior',
            'spy': 'warrior'
        }

        allegiance = allegiances[player_role]
        role_msg = role_msgs[player_role]

        titles = {
            'soldier': '🛡 Soldier 🛡',
            'warrior': '⚔ Warrior ⚔',
            'coordinate': '🗺 Coordinate 🗺',
            'queen': '👼 Queen 👼',
            'ackerman': '💂 Ackerman 💂',
            'mike': '<:aotSmirk:571740978377916416> Mike Zacharias <:aotSmirk:571740978377916416>',
            'scout': '🏇 Scout 🏇',
            'warchief': '🦹‍♂️ Warchief 🦹‍♂️',
            'ymir': '🤷‍♀️ Ymir 🤷‍♀️',
            'false king': '🕴 False King 🕴',
            'spy': '🕵️‍♀️ Spy 🕵️‍♀️'
        }
        thumbnails = {
            'soldier': 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/shield_1f6e1.png', 
            'warrior': 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/crossed-swords_2694.png'
        }
        allegiance_colours = {
            'soldier': 0x00C9FF,
            'warrior': 0xB23E00
        }

        role_embed = discord.Embed(title=titles[player_role], description=role_msg, colour=allegiance_colours[allegiance])
        role_embed.set_thumbnail(url=thumbnails[allegiance])
        return role_embed

    def get_player_role(self, player = None):
        if player == None:
            # Game hasn't started yet
            if self.status == 'waiting for players' or self.status == 'waiting for game' or self.status.startswith('game ended'):
                # Lists all roles available in the game
                soldier_roles = '\n'.join(['🛡**Soldier**🛡', '🗺**Coordinate**🗺', '👼**Queen**👼', '💂**Ackerman**💂', 
                '<:aotSmirk:571740978377916416>**Mike Zacharias** <:aotSmirk:571740978377916416>', '🏇**Scout**🏇'])
                warrior_roles = '\n'.join(['⚔**Warrior**⚔', '🦹‍♂️**Warchief**🦹‍♂️', '🕴**False King**🕴', '🤷‍♀️**Ymir**🤷‍♀️', '🕵️‍♀️**Spy**🕵️‍♀️'])
                
                list_of_roles = discord.Embed(title = 'List of roles available', description = 'Type ~help <role> for more information about a role.', colour=0x0013B4)
                list_of_roles.add_field(name = 'Soldier roles', value = soldier_roles, inline = True)
                list_of_roles.add_field(name = 'Warrior roles', value = warrior_roles, inline = True)
                return list_of_roles
            else:
                # Lists all roles currently in the game
                all_roles = [player[1] for player in self.players]

                def role_ordering(role_name):
                    role_map = {'soldier': 0, 'warrior': 1, 'coordinate': 2, 'queen': 3, 'ackerman': 4, 'mike': 5, 'scout': 6, 'warchief': 7, 'false king': 8, 'ymir': 9, 'spy': 10}
                    return role_map[role_name]

                all_roles.sort(key = role_ordering)
                display_roles = ''
                display_role_map = {'soldier': '🛡**Soldier**🛡', 'queen': '👼**Queen**👼', 'ackerman': '💂**Ackerman**💂', 
                'mike': '<:aotSmirk:571740978377916416>**Mike Zacharias** <:aotSmirk:571740978377916416>', 'scout': '🏇**Scout**🏇', 'coordinate': '🗺**Coordinate**🗺', 
                'warrior': '⚔**Warrior**⚔', 'warchief': '🦹‍♂️**Warchief**🦹‍♂️', 'false king': '🕴**False King**🕴', 'ymir': '🤷‍♀️**Ymir**🤷‍♀️', 'spy': '🕵️‍♀️**Spy**🕵️‍♀️'}
                for role in all_roles:
                    display_roles += display_role_map[role] + '\n'

                list_of_roles = discord.Embed(title = 'Current list of roles in game', description = display_roles, colour=0xF9FF41)
                return list_of_roles

        else:
            # DM player their role
            if player not in list(map(lambda x: x[0], self.players)):
                return 'You need to be in a game to have a role!'
            elif self.status == 'waiting for players':
                return 'Roles are only assigned after the game has started!'
            else:
                player_role = list(filter(lambda x: player == x[0], self.players))[0][1]

                soldier_msg = 'You are a **Soldier**!'

                warrior_msg = 'You are a **Warrior**!\n\nYour fellow Warriors are:\n'
                for warrior in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
                    if warrior[0] == player or warrior[1] == 'ymir':
                        continue
                    else:
                        warrior_msg = warrior_msg + '**' + warrior[0].name + '**\n'
                if 'ymir' in self.newroles:
                    warrior_msg = warrior_msg + '\n❗*You do not know **Ymir\'s** identity.*'

                warchief_msg = 'You are the **Warchief**!\n\nYour fellow Warriors are:\n'
                for warrior in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
                    if warrior[0] == player or warrior[1] == 'ymir':
                        continue
                    else:
                        warchief_msg = warchief_msg + '**' + warrior[0].name + '**\n'
                if 'ymir' in self.newroles:
                    warchief_msg = warchief_msg + '\n❗*You do not know **Ymir\'s** identity.*'

                queen_msg = 'You are the **Queen**!\n\n'
                if 'false king' not in self.newroles:
                    queen_msg = queen_msg + 'The Coordinate is:\n**' + list(filter(lambda x:x[1] == 'coordinate', self.players))[0][0].name + '**'
                else:
                    queen_msg = queen_msg + 'The Coordinate is one of the following two players. The other is the False King:\n'
                    coord_list = ['coordinate', 'false king']
                    coord_list.sort(key = lambda x: random.randint(1,100))
                    for role in coord_list:
                        queen_msg = queen_msg + '**' + list(filter(lambda x:x[1] == role, self.players))[0][0].name + '**\n'

                ackerman_msg = 'You are the **Ackerman**!'

                mike_msg = 'You are **Mike Zacharias**!'

                scout_msg = 'You are the **Scout**!'
                
                coordinate_msg = 'You are the **Coordinate**!\n\nThe Warriors are:\n'
                for warrior in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
                    if warrior[1] == 'warchief':
                        continue
                    else:
                        coordinate_msg = coordinate_msg + '**' + warrior[0].name + '**\n'
                if 'warchief' in self.newroles:
                    coordinate_msg = coordinate_msg + '\n❗*The identity of the **Warchief** is hidden from you*.'

                ymir_msg = 'You are **Ymir**!'

                falseking_msg = 'You are the **False King**!\n\nYour fellow Warriors are:\n'
                for warrior in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
                    if warrior[0] == player or warrior[1] == 'ymir':
                        continue
                    else:
                        falseking_msg = falseking_msg + '**' + warrior[0].name + '**\n'
                if 'ymir' in self.newroles:
                    falseking_msg = falseking_msg + '\n❗*You do not know **Ymir\'s** identity.*'

                spy_msg = 'You are the **Spy**!\n\nYour fellow Warriors are:\n'
                for warrior in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
                    if warrior[0] == player or warrior[1] == 'ymir':
                        continue
                    else:
                        spy_msg = spy_msg + '**' + warrior[0].name + '**\n'
                if 'ymir' in self.newroles:
                    spy_msg = spy_msg + '\n❗*You do not know **Ymir\'s** identity.*'

                role_msgs = {
                    'soldier': soldier_msg, 
                    'warrior': warrior_msg, 
                    'coordinate': coordinate_msg,
                    'queen': queen_msg, 
                    'ackerman': ackerman_msg, 
                    'mike': mike_msg, 
                    'scout': scout_msg,
                    'warchief': warchief_msg, 
                    'ymir': ymir_msg, 
                    'false king': falseking_msg,
                    'spy': spy_msg
                }
                allegiances = {
                    'soldier': 'soldier', 
                    'warrior': 'warrior', 
                    'coordinate': 'soldier',
                    'queen': 'soldier', 
                    'ackerman': 'soldier',
                    'mike': 'soldier',
                    'scout': 'soldier',
                    'warchief': 'warrior', 
                    'ymir': 'warrior', 
                    'false king': 'warrior',
                    'spy': 'warrior'
                }

                allegiance = allegiances[player_role]
                role_msg = role_msgs[player_role]

                titles = {
                    'soldier': '🛡 Soldier 🛡',
                    'warrior': '⚔ Warrior ⚔',
                    'coordinate': '🗺 Coordinate 🗺',
                    'queen': '👼 Queen 👼',
                    'ackerman': '💂 Ackerman 💂',
                    'mike': '<:aotSmirk:571740978377916416> Mike Zacharias <:aotSmirk:571740978377916416>',
                    'scout': '🏇 Scout 🏇',
                    'warchief': '🦹‍♂️ Warchief 🦹‍♂️',
                    'ymir': '🤷‍♀️ Ymir 🤷‍♀️',
                    'false king': '🕴 False King 🕴',
                    'spy': '🕵️‍♀️ Spy 🕵️‍♀️'
                }
                thumbnails = {
                    'soldier': 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/shield_1f6e1.png', 
                    'warrior': 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/crossed-swords_2694.png'
                }
                allegiance_colours = {
                    'soldier': 0x00C9FF,
                    'warrior': 0xB23E00
                }

                role_embed = discord.Embed(title=titles[player_role], description=role_msg, colour=allegiance_colours[allegiance])
                role_embed.set_thumbnail(url=thumbnails[allegiance])
                return role_embed

    def pick(self, player):
        if player in list(map(lambda x: x[0], self.players)):
            if player in self.expedition_squad:
                return '**' + player.name + '** is already part of the expedition team!'
            else:
                self.expedition_squad.append(player)
                return '**' + player.name + '** has joined the expedition team!'
        else:
            return '**' + player.name + '** is not in the game!'

    def get_ymir_blessing(self):
        if self.currently_blessed == None:
            self.currently_blessed = random.choice(list(filter(lambda x: x not in self.blessed, list(map(lambda x: x[0], self.players)))))
        return self.currently_blessed.mention + ' has received Ymir\'s blessing!'
    
    def get_player_allegiance(self, player):
        if player in list(map(lambda x:x[0], list(filter(lambda x:x[1] in self.warrior_roles, self.players)))):
            return '⚔**Warriors**⚔!'
        else:
            return '🛡**Soldiers**🛡!'

    def get_expedition_size(self):
        expedition_size = self.expedition_sizes[len(self.players)][self.cur_expedition-1]
        return expedition_size

    def next_commander(self):
        prev_commander = self.players.pop(0)
        self.players.append(prev_commander)
        self.message_box = []
        if self.kenny:
            self.update_kenny_hit_list()

    def update_kenny_hit_list(self):
        for _ in range(self.num_targets):
            prev_target = self.kenny_hit_list.pop(0)
            self.kenny_hit_list.append(prev_target)

        if len(self.players) == 7 or len(self.players) == 8:
            if self.num_targets == 1:
                self.num_targets = 2
            elif self.num_targets == 2:
                self.num_targets = 1

    def selection_players(self):
        players_in_expedition = ''
        for person in self.expedition_squad:
            players_in_expedition = players_in_expedition + '**' + person.name + '**\n'
        selection_state = discord.Embed(title = '**' + str(len(self.expedition_squad)) + '**/**' + str(self.get_expedition_size()) + 
        '** players in expedition team', description = players_in_expedition, colour=0xF9FF41)
        return selection_state

    def begin_approval_phase(self):
        self.status = 'expedition approval'
        self.message_box = []
        return '--**Expedition #' + str(self.cur_expedition) + ': Approval phase**--'

    def get_expedition_approval_msg(self, player):
        if self.kenny and player in self.kenny_hit_list[:self.num_targets]:
            kenny_targeted_msg = '💥 Bang! Bang! You have been targeted by Kenny, preventing you from voting!'
            kenny_targeted_embed = discord.Embed(title = 'Expedition Approval', description = kenny_targeted_msg, colour=0xC0C0C0)
            return kenny_targeted_embed
            
        approval_msg = 'The proposed expedition team consists of the following members:\n'

        for member in self.expedition_squad:
            approval_msg += '**' + member.name + '**\n'

        # Warn Mike if there are titans inside
        if player in list(map(lambda x: x[0], list(filter(lambda x: x[1] == 'mike', self.players)))) and player in self.expedition_squad:
            detectable_titans = self.warrior_roles + ['coordinate']
            num_titans = len(list(filter(lambda x: x in list(map(lambda z: z[0], list(filter(lambda y: y[1] in detectable_titans, self.players)))),
                                            self.expedition_squad)))
            if num_titans >= 1:
                approval_msg += '\n❗You smell **%s** Titan%s in this expedition!❗\n' % (
                    str(num_titans), 's' if num_titans >= 2 else '')
            else:
                approval_msg += '\n✅ You do not smell any Titans in this expedition! ✅\n'

        approval_msg += '\nDo you approve of this expedition team proposal?\n' + \
            '✅ Type `y` to approve the proposal.\n' + \
            '❌ Type `n` to reject the proposal.\n'

        # Add flipping option for Spy
        if player in list(map(lambda x: x[0], list(filter(lambda x: x[1] == 'spy', self.players)))) and self.votes_flipped == False:
            approval_msg += '🔄 Type `f` to flip the votes.'

        approval_embed = discord.Embed(title = 'Expedition Approval', description = approval_msg, colour=0xC0C0C0)
        return approval_embed

    def approval_players(self):
        approval_status = ''
        for player in list(map(lambda x:x[0], self.players)):
            if player in list(map(lambda x:x[0], self.expedition_approval)):
                approval_status = approval_status + '**' + player.name + '**\n'
            else:
                approval_status = approval_status + player.name + '\n'
        expedition_approval_status = discord.Embed(title = 'Expedition approval', description = approval_status, colour=0xF9FF41)
        return expedition_approval_status
    
    def approval_add_remainder(self):
        for player in list(map(lambda x:x[0], self.players)):
            if player not in list(map(lambda x:x[0], self.expedition_approval)):
                self.expedition_approval.append([player, 'yes'])

    def get_flip_msg(self, player):
        if player in list(map(lambda x: x[0], list(filter(lambda x: x[1] == 'spy', self.players)))):
            if self.votes_flipped == False:
                self.votes_flipped = True
                self.flipping_votes = True
                flip_msg = 'The votes for this expedition will be flipped! You may now cast your vote (pre-flip):\n\n' + \
                    '✅ Type `y` to approve the proposal.\n' + \
                    '❌ Type `n` to reject the proposal.\n'
                flip_embed = discord.Embed(title = 'Expedition Approval', description = flip_msg, colour=0xC0C0C0)
                return flip_embed
            else:
                return 'You have already used your ability to flip the votes!'
        else:
            return 'Only a Spy may flip the votes!'

    def flip_votes(self):
        for player in self.expedition_approval:
            if player[1] == 'yes':
                player[1] = 'no'
            elif player[1] == 'no':
                player[1] = 'yes'

        self.flipping_votes = False

    def get_approval_result(self):
        self.reset_confirmation = False
        approval_result = ''
        self.expedition_approval.sort(key = lambda x: random.randint(1,100))
        for player in self.expedition_approval:
            if player[1] == 'yes':
                approval_result = approval_result + '**' + player[0].name + '** ✅\n'
            elif player[1] == 'no':
                approval_result = approval_result + '**' + player[0].name + '** ❌\n'
            elif player[1] == 'none':
                approval_result = approval_result + '**' + player[0].name + '** ➖\n'
        
        expedition_result = discord.Embed(title = 'Expedition approval result', description = approval_result, colour=0xF9FF41)
        return expedition_result

    def get_decision_msg(self, player):
        # Warrior
        if player in list(map(lambda x: x[0], list(filter(lambda x: x[1] in self.warrior_roles, self.players)))):
            decision_msg = 'Do you allow the expedition to succeed?\n\n' + \
                '✅ Type `y` to let the expedition succeed.\n' + \
                '❌ Type `n` to sabotage the expedition and destroy the Wall.'
            decision_embed = discord.Embed(title = 'Expedition Decision', description = decision_msg, colour=0xFFF700)
            return decision_embed
        # Soldier
        else:
            decision_msg = '✅ Type `y` to participate in the expedition.\n'
            # If person is an Ackerman
            if player in list(map(lambda x: x[0], list(filter(lambda x: x[1] == 'ackerman', self.players)))) and self.wall_secured == False:
                decision_msg += '🛡 Type `s` to secure the Walls.'
            decision_embed = discord.Embed(title = 'Expedition Decision', description = decision_msg, colour=0x2EFF00)
            return decision_embed

    def decision_players(self):
        decision_status = str(len(list(filter(lambda x: x in list(map(lambda x:x[0], self.expedition_result)), self.expedition_squad)))) + \
            '/' + str(len(self.expedition_squad)) + ' players'

        expedition_decision_status = discord.Embed(title = 'Expedition decision', description = decision_status, colour=0xF9FF41)
        return expedition_decision_status

    def scout_in_expedition(self):
        players_in_expedition_squad = list(filter(lambda x: x[0] in self.expedition_squad, self.players))
        return 'scout' in list(map(lambda x: x[1], players_in_expedition_squad))

    def get_expedition_result(self):
        self.status = ''
        decision_result = ''
        self.expedition_result.sort(key = lambda x: random.randint(1,100))
        if 'secure' in list(map(lambda x:x[1], self.expedition_result)):
            for player in self.expedition_result:
                decision_result = decision_result + '✅\n'
        else:
            for player in self.expedition_result:
                if player[1] == 'yes':
                    decision_result = decision_result + '✅\n'
                elif player[1] == 'no':
                    decision_result = decision_result + '❌\n'
        
        expedition_result = discord.Embed(title = 'Expedition Result', description = decision_result, colour=0xF9FF41)
        return expedition_result

    def test_expedition_success(self):
        num_fails = len(list(filter(lambda x: x[1] == 'no', self.expedition_result)))
        if 'secure' in list(map(lambda x:x[1], self.expedition_result)):
            num_fails = 0

        if len(self.players) >= 7 and self.cur_expedition == 4:
            if num_fails >= 2:
                return False
            else:
                return True
        else:
            if num_fails >= 1:
                return False
            else:
                return True

    def expedition_success_update(self):
        self.successful_expeditions += 1
        self.cur_expedition += 1
        self.expedition_history.append('🛡')
        self.expedition_squad = []
        self.expedition_result = []
        return '✅The expedition was a success!✅'

    def expedition_failure_update(self):
        self.walls_destroyed += 1
        self.cur_expedition += 1
        self.expedition_history.append('⚔')
        self.expedition_squad = []
        self.expedition_result = []

        result_msg = 'The expedition was a failure!\n\n'
        if self.walls_destroyed == 1:
            result_msg = result_msg + '💥Wall **Maria** has been destroyed!💥'
        elif self.walls_destroyed == 2:
            result_msg = result_msg + '💥Wall **Rose** has been destroyed!💥'
        elif self.walls_destroyed == 3:
            result_msg = result_msg + '💥Wall **Sina** has been destroyed!💥'
        return result_msg

    def reach_basement(self):
        self.status = 'choose coordinate'
        basement_msg = 'The Soldiers have reached the Basement! The Warriors have one last chance to seize victory by capturing the Coordinate. Any Warrior may type `~kidnap <@name>` \
to select who they believe is the Coordinate.\n\nThe Warriors are:\n'
        for person in list(filter(lambda x:x[1] in self.warrior_roles, self.players)):
            basement_msg += '**' + person[0].name + '**\n'
        return basement_msg

    def addendum(self, number):
        if self.cur_expedition == number:
            return '🏇'
        elif self.cur_expedition < number:
            return ''
        elif self.cur_expedition > number:
            return self.expedition_history[number-1]

    def add2fails(self):
        if len(self.players) >= 7:
            return '(2 Warriors to fail)'
        else:
            return ''

    def get_status(self):
        if self.status == 'waiting for game' or self.status == 'waiting for players':
            return None
        else:
            status = discord.Embed(title='Current Game Information', description= 'Number of players: **' + str(len(self.players)) + '**\n**' + 
            str(len(list(filter(lambda x:x[1] not in self.warrior_roles, self.players)))) + 
            '** Soldiers vs **' + str(len(list(filter(lambda x:x[1] in self.warrior_roles, self.players)))) + '** Warriors', colour=0xF9FF41)

            if self.successful_expeditions == 0:
                basement_progress = '￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵￶￵ \u2001\u2001\u20011⃣\n\u2001\u2001\u2001\u2001\u20012⃣\n\u2001\u2001\u2001\u2001\u20013⃣🏁'
            elif self.successful_expeditions == 1:
                basement_progress = '￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵￶￵ \u2001\u2001\u2001✅\n\u2001\u2001\u2001\u2001\u20012⃣\n\u2001\u2001\u2001\u2001\u20013⃣🏁'
            elif self.successful_expeditions == 2:
                basement_progress = '￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵￶￵ \u2001\u2001\u2001✅\n\u2001\u2001\u2001\u2001\u2001✅\n\u2001\u2001\u2001\u2001\u20013⃣🏁'
            elif self.successful_expeditions == 3:
                basement_progress = '￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵￶￵ \u2001\u2001\u2001✅\n\u2001\u2001\u2001\u2001\u2001✅\n\u2001\u2001\u2001\u2001\u2001✅🏁'

            if self.walls_destroyed == 0:
                wall_status = '￶￵ ￶￵  ￶￵ ￶￵ ￶￵ ￶￵ \u200A\u200A\u2000🏠🇲🏠\n\u2001\u2000\u2000🏦🇷🏦\n\u2001\u2000\u2000🏰🇸🏰'
            elif self.walls_destroyed == 1:
                wall_status = '￶￵ ￶￵  ￶￵ ￶￵ ￶￵ ￶￵ \u200A\u200A\u2000🏚💥🏚\n\u2001\u2000\u2000🏦🇷🏦\n\u2001\u2000\u2000🏰🇸🏰'
            elif self.walls_destroyed == 2:
                wall_status = '￶￵ ￶￵  ￶￵ ￶￵ ￶￵ ￶￵ \u200A\u200A\u2000🏚💥🏚\n\u2001\u2000\u2000🏚💥🏚\n\u2001\u2000\u2000🏰🇸🏰'
            elif self.walls_destroyed >= 3:
                wall_status = '￶￵ ￶￵  ￶￵ ￶￵ ￶￵ ￶￵ \u200A\u200A\u2000🏚💥🏚\n\u2001\u2000\u2000🏚💥🏚\n\u2001\u2000\u2000🏚💥🏚'

            expedition_info = 'Expedition 1: **' + str(self.expedition_sizes[len(self.players)][0]) + '** members ' + self.addendum(1) + '\n\n\
Expedition 2: **' + str(self.expedition_sizes[len(self.players)][1]) + '** members ' + self.addendum(2) + '\n\n\
Expedition 3: **' + str(self.expedition_sizes[len(self.players)][2]) + '** members ' + self.addendum(3) + '\n\n\
Expedition 4: **' + str(self.expedition_sizes[len(self.players)][3]) + '** members ' + self.add2fails() + self.addendum(4) + '\n\n\
Expedition 5: **' + str(self.expedition_sizes[len(self.players)][4]) + '** members ' + self.addendum(5)

            status.add_field(name = 'Progress towards Basement', value = basement_progress, inline = True)
            status.add_field(name = 'Status of the Walls', value = wall_status, inline = True)
            status.add_field(name = 'Expedition Info', value = expedition_info, inline = False)

            if self.funds_enabled:
                funds_info = ''
                for _ in range(self.funds):
                    funds_info += '💰 '
                for _ in range(5 - self.funds):
                    funds_info += '❌ '
                status.add_field(name = 'Funds', value = funds_info, inline = False)

            return status
    
    def get_players(self):
        if self.status != 'waiting for game' and self.status != 'waiting for players':
            all_players = ''
            for player in self.players:
                if player == self.players[0]:
                    all_players = all_players + '**' + player[0].mention + '** 👑\n'
                else:
                    all_players = all_players + '**' + player[0].mention + '**' + '\n'
            players = discord.Embed(title = 'List of players (in queue to become Commander)', description = all_players, colour=0xF9FF41)
            return players
        elif self.status == 'waiting for players':
            return self.display_lobby()
        else:
            return None

    def get_kenny_hit_list(self):
        all_players = ''
        for player in self.kenny_hit_list:
            if player in self.kenny_hit_list[:self.num_targets]:
                all_players = all_players + '**' + player.mention + '** <:crosshairs:768322832349528104>\n'
            else:
                all_players = all_players + '**' + player.mention + '**' + '\n'
        players = discord.Embed(title = '<:kennytheripper:768310628506402887> Kenny\'s Hit List <:kennytheripper:768310628506402887>', description = all_players, colour=0xF9FF41)
        return players

    def get_summary(self):
        summary = discord.Embed(title = 'Game Summary', description = 'Number of players: **' + str(len(self.players)) + '**\n**' + 
str(len(list(filter(lambda x:x[1] not in self.warrior_roles, self.players)))) + 
'** Soldiers vs **' + str(len(list(filter(lambda x:x[1] in self.warrior_roles, self.players)))) + '** Warriors', colour=0xF9FF41)

        all_soldiers = ''
        all_warriors = ''
        for person in self.players:
            if person[1] == 'soldier':
                all_soldiers += person[0].name + '\n'
            elif person[1] == 'warrior':
                all_warriors += person[0].name + '\n'

        if all_soldiers:
            summary.add_field(name = '🛡Soldiers🛡', value = all_soldiers)
        if all_warriors:
            summary.add_field(name = '⚔Warriors⚔', value = all_warriors)
        summary.add_field(name = '🗺Coordinate🗺', value = list(filter(lambda x:x[1] == 'coordinate', self.players))[0][0].name)
        if 'queen' in self.newroles:
            summary.add_field(name = '👼Queen👼', value = list(filter(lambda x:x[1] == 'queen', self.players))[0][0].name)
        if 'ackerman' in self.newroles:
            summary.add_field(name = '💂Ackerman💂', value = list(filter(lambda x:x[1] == 'ackerman', self.players))[0][0].name)
        if 'mike' in self.newroles:
            summary.add_field(name = '<:aotSmirk:571740978377916416> Mike Zacharias <:aotSmirk:571740978377916416>', value = list(filter(lambda x:x[1] == 'mike', self.players))[0][0].name)    
        if 'scout' in self.newroles:
            summary.add_field(name = '🏇Scout🏇', value = list(filter(lambda x:x[1] == 'scout', self.players))[0][0].name)
        if 'warchief' in self.newroles:
            summary.add_field(name = '🦹‍♂️Warchief🦹‍♂️', value = list(filter(lambda x:x[1] == 'warchief', self.players))[0][0].name)
        if 'false king' in self.newroles:
            summary.add_field(name = '🕴False King🕴', value = list(filter(lambda x:x[1] == 'false king', self.players))[0][0].name)
        if 'ymir' in self.newroles:
            summary.add_field(name = '🤷‍♀️Ymir🤷‍♀️', value = list(filter(lambda x:x[1] == 'ymir', self.players))[0][0].name)
        if 'spy' in self.newroles:
            summary.add_field(name = '🕵️‍♀️Spy🕵️‍♀️', value = list(filter(lambda x:x[1] == 'spy', self.players))[0][0].name)

        return summary

    def calculate_advantage(self, write=True, emblems=True):
        num_players = max(len(self.players), 5)
        expedition_advantage = self.expedition_advantages[num_players]
        roles_advantage = 0
        for role in self.newroles:
            roles_advantage += self.roles_advantages[role][num_players]
        advantage_score = roles_advantage + expedition_advantage
        if self.ymir_blessing:
            advantage_score += self.blessing_advantages[num_players]
        if self.funds_enabled:
            advantage_score += self.funds_advantages[num_players]

        if write == False:
            return advantage_score
        if advantage_score == 0:
            return '**None**'
        elif advantage_score > 0:
            if emblems:
                return '🛡 **Soldiers (+%d)** 🛡' % advantage_score
            else:
                return '**Soldiers (+%d)**' % advantage_score
        else:
            if emblems:
                return '⚔ **Warriors (+%d)** ⚔' % -advantage_score
            else:
                return '**Warriors (+%d)**' % -advantage_score

    def update_server_records(self):
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        get_server_data_query = 'SELECT * FROM servers WHERE server = ?'
        cursor.execute(get_server_data_query, (self.server.id,))
        server_data = cursor.fetchone()

        role_index_map = {'soldier':[19,20], 'warrior':[21,22], 'coordinate':[23,24], 'queen':[25,26], 'warchief':[27,28], 'ymir':[29,30], 'false king':[31,32],
        'ackerman':[33,34], 'mike':[35,36], 'scout':[37,38], 'spy':[39,40]}
        role_col_map = {
            'soldier': ['soldier_wins', 'soldier_games'],
            'queen': ['queen_wins', 'queen_games'],
            'ackerman': ['ackerman_wins', 'ackerman_games'],
            'mike': ['mike_wins', 'mike_games'],
            'scout': ['scout_wins', 'scout_games'],
            'coordinate': ['coordinate_wins', 'coordinate_games'],
            'warrior': ['warrior_wins', 'warrior_games'],
            'warchief': ['warchief_wins', 'warchief_games'],
            'ymir': ['ymir_wins', 'ymir_games'],
            'false king': ['false_king_wins', 'false_king_games'],
            'spy': ['spy_wins', 'spy_games']
        }

        if server_data:
            server_data = list(server_data)
            num_players_index = len(self.players) - 5
            soldiers_wins, warriors_walls, warriors_kidnap = server_data[3 * num_players_index + 1], server_data[3 * num_players_index + 2], server_data[3 * num_players_index + 3]
            if self.status == 'game ended soldiers':
                soldiers_wins += 1
                role_win_updates = list(map(lambda y:y[1], list(filter(lambda x:x[1] not in self.warrior_roles, self.players))))
            elif self.status == 'game ended warriors wall':
                warriors_walls += 1
                role_win_updates = list(map(lambda y:y[1], list(filter(lambda x:x[1] in self.warrior_roles, self.players))))
            elif self.status == 'game ended warriors coord':
                warriors_kidnap += 1
                role_win_updates = list(map(lambda y:y[1], list(filter(lambda x:x[1] in self.warrior_roles, self.players))))

            update_cols = ['soldiers_' + str(len(self.players)), 'warriors_walls_' + str(len(self.players)), 'warriors_kidnap_' + str(len(self.players))]
            update_server_data_query = 'UPDATE servers SET {} = ?, {} = ?, {} = ? WHERE server = ?'.format(*update_cols)
            update_server_data = [soldiers_wins, warriors_walls, warriors_kidnap, self.server.id]
            cursor.execute(update_server_data_query, update_server_data)

            for role in role_win_updates:
                server_data[role_index_map[role][0]] += 1
                update_role_data_query = 'UPDATE servers SET {} = ? WHERE server = ?'.format(role_col_map[role][0])
                cursor.execute(update_role_data_query, (server_data[role_index_map[role][0]], self.server.id))

            role_updates = list(map(lambda y:y[1], self.players))
            for role in role_updates:
                server_data[role_index_map[role][1]] += 1
                update_role_data_query = 'UPDATE servers SET {} = ? WHERE server = ?'.format(role_col_map[role][1])
                cursor.execute(update_role_data_query, (server_data[role_index_map[role][1]], self.server.id))

        else:
            num_players_index = len(self.players) - 5
            soldiers_wins, warriors_walls, warriors_kidnap = 0, 0, 0
            if self.status == 'game ended soldiers':
                soldiers_wins += 1
                role_win_updates = list(map(lambda y:y[1], list(filter(lambda x:x[1] not in self.warrior_roles, self.players))))
            elif self.status == 'game ended warriors wall':
                warriors_walls += 1
                role_win_updates = list(map(lambda y:y[1], list(filter(lambda x:x[1] in self.warrior_roles, self.players))))
            elif self.status == 'game ended warriors coord':
                warriors_kidnap += 1
                role_win_updates = list(map(lambda y:y[1], list(filter(lambda x:x[1] in self.warrior_roles, self.players))))

            insert_server_data_query = 'INSERT INTO servers VALUES ({})'.format(','.join('?' * 41))
            insert_server_data = [self.server.id] + [0] * 40
            for i, score in enumerate([soldiers_wins, warriors_walls, warriors_kidnap]):
                insert_server_data[3 * num_players_index + i + 1] = score

            for role in role_win_updates:
                insert_server_data[role_index_map[role][0]] += 1

            role_updates = list(map(lambda y:y[1], self.players))
            for role in role_updates:
                insert_server_data[role_index_map[role][1]] += 1

            cursor.execute(insert_server_data_query, insert_server_data)
        
        conn.commit()
        conn.close()

    def update_rating(self):
        # Updates rating of all players after game ends, and returns it in an embed. Updates game records as well.
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        # Update server records
        self.update_server_records()

        # Update game records
        get_game_data_query = 'SELECT * FROM global'
        cursor.execute(get_game_data_query)
        game_data = cursor.fetchall()

        num_players = len(self.players)
        if self.status == 'game ended soldiers':
            update_game_data_query = 'UPDATE global SET soldiers = ? WHERE number_of_players = ?'
            update_game_data = [game_data[num_players - 5][1] + 1, num_players]
            cursor.execute(update_game_data_query, update_game_data)
            
        elif self.status == 'game ended warriors wall':
            update_game_data_query = 'UPDATE global SET warriors_walls = ? WHERE number_of_players = ?'
            update_game_data = [game_data[num_players - 5][2] + 1, num_players]
            cursor.execute(update_game_data_query, update_game_data)

        elif self.status == 'game ended warriors coord':
            update_game_data_query = 'UPDATE global SET warriors_kidnap = ? WHERE number_of_players = ?'
            update_game_data = [game_data[num_players - 5][3] + 1, num_players]
            cursor.execute(update_game_data_query, update_game_data)

        conn.commit()

        # Update player ratings
        ratings = []
        # Obtain original ratings
        for player in self.players:
            player_data_query = 'SELECT player, rating FROM players WHERE player = ?'
            cursor.execute(player_data_query, (player[0].id,))
            player_data = cursor.fetchone()

            # [id, rating, role]
            if player_data:
                ratings.append([player_data[0], player_data[1], player[1]]) 
            else:
                insert_player_data_query = 'INSERT INTO players VALUES ({})'.format(','.join('?' * 26))
                insert_player_data = [player[0].id, 1500] + 24 * [0]
                cursor.execute(insert_player_data_query, insert_player_data)
                conn.commit()

                ratings.append([player[0].id, 1500, player[1]])
        
        avg_s = sum(map(lambda y: y[1], (filter(lambda x: x[2] not in self.warrior_roles, ratings)))) / len(list(filter(lambda x: x[2] not in self.warrior_roles, ratings)))
        avg_w = sum(map(lambda y: y[1], (filter(lambda x: x[2] in self.warrior_roles, ratings)))) / len(list(filter(lambda x: x[2] in self.warrior_roles, ratings)))
        sr_modifier = self.calculate_advantage(write=False)

        # Calculate rating transfer amount
        K = 64
        exp = 1 / (1 + 10 ** ((avg_w - avg_s - sr_modifier)/800))
        if self.status == 'game ended soldiers':
            rating_transfer = K * (1 - exp)
        else:
            rating_transfer = K * exp

        rating_transfer = max(10, rating_transfer)

        # Apply rating transfers and update player records
        rating_changes = [] # [id, old rating, new rating, role]
        for player in ratings:
            if self.status == 'game ended soldiers':
                if player[2] not in self.warrior_roles:
                    new_rating = player[1] + rating_transfer
                    win = True
                else:
                    new_rating = player[1] - rating_transfer
                    win = False
            else:
                if player[2] not in self.warrior_roles:
                    new_rating = player[1] - rating_transfer
                    win = False
                else:
                    new_rating = player[1] + rating_transfer
                    win = True

            rating_changes.append([player[0], player[1], new_rating, player[2]])
            
            # Update rating, win/played stats
            role_to_column_map = {
                'soldier': ['soldier_wins', 'soldier_games'],
                'queen': ['queen_wins', 'queen_games'],
                'ackerman': ['ackerman_wins', 'ackerman_games'],
                'mike': ['mike_wins', 'mike_games'],
                'scout': ['scout_wins', 'scout_games'],
                'coordinate': ['coordinate_wins', 'coordinate_games'],
                'warrior': ['warrior_wins', 'warrior_games'],
                'warchief': ['warchief_wins', 'warchief_games'],
                'ymir': ['ymir_wins', 'ymir_games'],
                'false king': ['false_king_wins', 'false_king_games'],
                'spy': ['spy_wins', 'spy_games']
            }
            get_player_role_query = 'SELECT {},{} FROM players WHERE player = ?'.format(*role_to_column_map[player[2]])
            cursor.execute(get_player_role_query, (player[0],))
            player_role_columns = cursor.fetchone()

            update_player_data_query = 'UPDATE players SET rating = ?, {} = ?, {} = ? WHERE player = ?'.format(*role_to_column_map[player[2]])
            player_wins = player_role_columns[0]
            player_games = player_role_columns[1] + 1
            if win == True:
                player_wins += 1

            update_player_data = [new_rating, player_wins, player_games, player[0]]
            cursor.execute(update_player_data_query, update_player_data)
            conn.commit()
        
        conn.close()

        # Embed skill rating changes
        new_ratings = discord.Embed(title = 'Skill Rating (SR) Update', 
                                    description = 'Advantage: ' + self.calculate_advantage(emblems=False) + '\nSoldiers: **' + str(int(round(avg_s, 0))) + '** | Warriors: **' + str(int(round(avg_w, 0))) + '**', 
                                    colour=0xF9FF41)

        soldier_ratings = ''
        warrior_ratings = ''
        for player in self.players:
            if player[1] not in self.warrior_roles:
                player_info = list(filter(lambda x:x[0] == player[0].id, rating_changes))[0]
                if self.status == 'game ended soldiers':
                    sign = '+'
                else:
                    sign = '-'
                soldier_ratings += player[0].name + ': **' + str(int(round(player_info[1], 0))) + '** -> **' + str(int(round(player_info[2], 0))) + '** (' + sign + str(int(round(rating_transfer, 0))) + ')\n'

            else:
                player_info = list(filter(lambda x:x[0] == player[0].id, rating_changes))[0]
                if self.status == 'game ended soldiers':
                    sign = '-'
                else:
                    sign = '+'
                warrior_ratings += player[0].name + ': **' + str(int(round(player_info[1], 0))) + '** -> **' + str(int(round(player_info[2], 0))) + '** (' + sign + str(int(round(rating_transfer, 0))) + ')\n'

        new_ratings.add_field(name = '🛡Soldiers🛡', value = soldier_ratings, inline = False)
        new_ratings.add_field(name = '⚔Warriors⚔', value = warrior_ratings, inline = False)
        return new_ratings

    def update_achievements(self):
        achievements_msgs = []
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        for cur_player in self.players:
            player_data_query = 'SELECT * FROM players WHERE player = ?'
            cursor.execute(player_data_query, (cur_player[0].id,))
            player_data = cursor.fetchone()

            # Player exists in the records (definitely, after updating rating)
            if self.status == 'game ended soldiers':
                if cur_player[1] not in self.warrior_roles:
                    win = True
                else:
                    win = False
            else:
                if cur_player[1] not in self.warrior_roles:
                    win = False
                else:
                    win = True

            # Update consecutive wins and add SR, achievement msg if needed
            player_sr = player_data[1]
            current_streak = player_data[2]
            best_streak = player_data[3]
            if win == True:
                current_streak += 1

                if current_streak > best_streak:
                    # New win streak
                    best_streak = current_streak
                    if best_streak in self.consecutive_wins_achievements:
                        # Achievement msg
                        consecutive_wins_msg = self.badge_emojis[self.consecutive_wins_achievements[best_streak]] + ' | Congratulations ' + cur_player[0].mention + \
                        '! You have obtained a **' + self.consecutive_wins_achievements[best_streak] + '** badge for winning **' + \
                        str(best_streak) + '** games in a row! **(+' + str(self.achievement_rewards[self.consecutive_wins_achievements[best_streak]]) + ' SR)**'

                        achievements_msgs.append(consecutive_wins_msg)

                        # Add SR
                        update_rating_query = 'UPDATE players SET rating = ? WHERE player = ?'
                        rating_gain = self.achievement_rewards[self.consecutive_wins_achievements[best_streak]]
                        player_sr += rating_gain
                        update_rating = [player_sr, cur_player[0].id]
                        cursor.execute(update_rating_query, update_rating)
                        conn.commit()
            else:
                current_streak = 0

            update_streak_query = 'UPDATE players SET current_streak = ?, best_streak = ? WHERE player = ?'
            update_streak = [current_streak, best_streak, cur_player[0].id]
            cursor.execute(update_streak_query, update_streak)
            conn.commit()

            # Add SR, achievement msgs for games played
            games_played = player_data[5] + player_data[7] + player_data[9] + player_data[11] + player_data[13] + player_data[15] + player_data[17] + player_data[19] + \
                player_data[21] + player_data[23] + player_data[25]
            if games_played in self.number_games_achievements:
                # Achievement msg
                games_played_msg = self.badge_emojis[self.number_games_achievements[games_played]] + ' | Congratulations ' + cur_player[0].mention + \
                '! You have obtained a **' + self.number_games_achievements[games_played] + '** badge for having played **' + \
                str(games_played) + '** games! **(+' + str(self.achievement_rewards[self.number_games_achievements[games_played]]) + ' SR)**'

                achievements_msgs.append(games_played_msg)

                # Add SR
                update_rating_query = 'UPDATE players SET rating = ? WHERE player = ?'
                rating_gain = self.achievement_rewards[self.number_games_achievements[games_played]]
                player_sr += rating_gain
                update_rating = [player_sr, cur_player[0].id]
                cursor.execute(update_rating_query, update_rating)
                conn.commit()

            # Add SR, achievement msgs for games won as role
            if win == True:
                if cur_player[1] == 'soldier':
                    soldier_wins = player_data[4]
                    if soldier_wins in self.soldier_wins_achievements:
                        # Achievement msg
                        soldiers_win_msg = self.badge_emojis[self.soldier_wins_achievements[soldier_wins]] + ' | Congratulations ' + cur_player[0].mention + \
                        '! You have obtained a **' + self.soldier_wins_achievements[soldier_wins] + '** badge for winning **' + \
                        str(soldier_wins) + '** games as a 🛡**Soldier**🛡! **(+' + str(self.achievement_rewards[self.soldier_wins_achievements[soldier_wins]]) + ' SR)**'

                        achievements_msgs.append(soldiers_win_msg)

                        # Add SR
                        update_rating_query = 'UPDATE players SET rating = ? WHERE player = ?'
                        rating_gain = self.achievement_rewards[self.soldier_wins_achievements[soldier_wins]]
                        player_sr += rating_gain
                        update_rating = [player_sr, cur_player[0].id]
                        cursor.execute(update_rating_query, update_rating)
                        conn.commit()

                elif cur_player[1] == 'warrior':
                    warrior_wins = player_data[6]
                    if warrior_wins in self.warrior_wins_achievements:
                        # Achievement msg
                        warriors_win_msg = self.badge_emojis[self.warrior_wins_achievements[warrior_wins]] + ' | Congratulations ' + cur_player[0].mention + \
                        '! You have obtained a **' + self.warrior_wins_achievements[warrior_wins] + '** badge for winning **' + \
                        str(warrior_wins) + '** games as a ⚔**Warrior**⚔! **(+' + str(self.achievement_rewards[self.warrior_wins_achievements[warrior_wins]]) + ' SR)**'

                        achievements_msgs.append(warriors_win_msg)

                        # Add SR
                        update_rating_query = 'UPDATE players SET rating = ? WHERE player = ?'
                        rating_gain = self.achievement_rewards[self.warrior_wins_achievements[warrior_wins]]
                        player_sr += rating_gain
                        update_rating = [player_sr, cur_player[0].id]
                        cursor.execute(update_rating_query, update_rating)
                        conn.commit()

                elif cur_player[1] == 'coordinate':
                    coordinate_wins = player_data[8]
                    if coordinate_wins in self.coordinate_wins_achievements:
                        # Achievement msg
                        coordinate_win_msg = self.badge_emojis[self.coordinate_wins_achievements[coordinate_wins]] + ' | Congratulations ' + cur_player[0].mention + \
                        '! You have obtained a **' + self.coordinate_wins_achievements[coordinate_wins] + '** badge for winning **' + \
                        str(coordinate_wins) + '** games as the 🗺**Coordinate**🗺! **(+' + str(self.achievement_rewards[self.coordinate_wins_achievements[coordinate_wins]]) + ' SR)**'

                        achievements_msgs.append(coordinate_win_msg)

                        # Add SR
                        update_rating_query = 'UPDATE players SET rating = ? WHERE player = ?'
                        rating_gain = self.achievement_rewards[self.coordinate_wins_achievements[coordinate_wins]]
                        player_sr += rating_gain
                        update_rating = [player_sr, cur_player[0].id]
                        cursor.execute(update_rating_query, update_rating)
                        conn.commit()

                elif cur_player[1] == 'queen' or cur_player[1] == 'ackerman' or cur_player[1] == 'mike' or cur_player[1] == 'scout':
                    optional_soldier_wins = player_data[10] + player_data[18] + player_data[20] + player_data[22]
                    if optional_soldier_wins in self.queen_wins_achievements:
                        # Achievement msg
                        queen_win_msg = self.badge_emojis[self.queen_wins_achievements[optional_soldier_wins]] + ' | Congratulations ' + cur_player[0].mention + \
                        '! You have obtained a **' + self.queen_wins_achievements[optional_soldier_wins] + '** badge for winning **' + \
                        str(optional_soldier_wins) + '** games with an optional Soldier role! **(+' + \
                        str(self.achievement_rewards[self.queen_wins_achievements[optional_soldier_wins]]) + ' SR)**'

                        achievements_msgs.append(queen_win_msg)

                        # Add SR
                        update_rating_query = 'UPDATE players SET rating = ? WHERE player = ?'
                        rating_gain = self.achievement_rewards[self.queen_wins_achievements[optional_soldier_wins]]
                        player_sr += rating_gain
                        update_rating = [player_sr, cur_player[0].id]
                        cursor.execute(update_rating_query, update_rating)
                        conn.commit()

                elif cur_player[1] == 'warchief' or cur_player[1] == 'false king' or cur_player[1] == 'ymir' or cur_player[1] == 'spy':
                    optional_warrior_wins = player_data[12] + player_data[14] + player_data[16] + player_data[24]
                    if optional_warrior_wins in self.warchief_wins_achievements:
                        # Achievement msg
                        warchief_win_msg = self.badge_emojis[self.warchief_wins_achievements[optional_warrior_wins]] + ' | Congratulations ' + cur_player[0].mention + \
                        '! You have obtained a **' + self.warchief_wins_achievements[optional_warrior_wins] + '** badge for winning **' + \
                        str(optional_warrior_wins) + '** games with an optional Warrior role! **(+' + str(self.achievement_rewards[self.warchief_wins_achievements[optional_warrior_wins]]) + ' SR)**'

                        achievements_msgs.append(warchief_win_msg)

                        # Add SR
                        update_rating_query = 'UPDATE players SET rating = ? WHERE player = ?'
                        rating_gain = self.achievement_rewards[self.warchief_wins_achievements[optional_warrior_wins]]
                        player_sr += rating_gain
                        update_rating = [player_sr, cur_player[0].id]
                        cursor.execute(update_rating_query, update_rating)
                        conn.commit()

        conn.close()

        return achievements_msgs

    def award_sr(self, player, awarded_sr):
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        player_data_query = 'SELECT * FROM players WHERE player = ?'
        cursor.execute(player_data_query, (player.id,))
        player_data = cursor.fetchone()
        player_sr = player_data[1]

        if player_data:
            update_rating_query = 'UPDATE players SET rating = ? WHERE player = ?'
            player_sr += awarded_sr
            update_rating = [player_sr, player.id]
            cursor.execute(update_rating_query, update_rating)
            conn.commit()
        
        conn.close()
        return '🏅 | ' + player.mention + ' has been awarded **' + ('+' if awarded_sr >= 0 else '') + str(awarded_sr) + ' SR!**'

    @staticmethod
    async def update_role(player, client, first_join=False):
        # Updates role based on games played
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        player_data_query = 'SELECT * FROM players WHERE player = ?'
        cursor.execute(player_data_query, (player.id,))
        player_data = cursor.fetchone()

        if player_data:
            games_played = player_data[5] + player_data[7] + player_data[9] + player_data[11] + player_data[13] + player_data[15] + \
            player_data[17] + player_data[19] + player_data[21] + player_data[23] + player_data[25]
        else:
            games_played = 0
        
        conn.close()

        server = client.get_guild(748080644340318299)

        roles_map = [
            [0, 749524096328400936],
            [5, 749524141308117022],
            [10, 749524180696956949],
            [25, 751426544148152441],
            [50, 751426716697755658],
            [100, 751426972474671144],
            [250, 749524159574442005], 
            [500, 749525061136023603]
        ]

        member = server.get_member(player.id)
        if member:
            cur_role_id = 0
            for threshold in roles_map:
                if games_played >= threshold[0]:
                    cur_role_id = threshold[1]
                    if first_join:
                        await member.add_roles(server.get_role(cur_role_id))
                else:
                    break

            await member.add_roles(server.get_role(cur_role_id))

    @staticmethod
    async def update_top_roles(client):
        # Updates #1 and top 10 roles
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        player_data_query = 'SELECT player, rating FROM players'
        cursor.execute(player_data_query)
        player_data = cursor.fetchall()

        conn.close()

        server = client.get_guild(748080644340318299)

        player_rankings = {} # {player id: sr, ...}
        # Put all players into a dictionary
        for row in player_data:
            player_rankings[row[0]] = row[1]

        server_members = server.members
        server_players = []
        for member in server_members:
            if member.id in player_rankings:
                server_players.append([member, player_rankings[member.id]])
        
        # Sort by SR from biggest to smallest
        server_players.sort(key = lambda x: x[1], reverse = True)

        top_role = server.get_role(756429927200587888)
        top10_role = server.get_role(756430896092938322)

        # Update roles
        for i, member in enumerate(server_players):
            member_role_ids = [role.id for role in member[0].roles]
            if i == 0:
                if 756429927200587888 not in member_role_ids:
                    await member[0].add_roles(top_role)
            else:
                if 756429927200587888 in member_role_ids:
                    await member[0].remove_roles(top_role)
                if i < 10:
                    if 756430896092938322 not in member_role_ids:
                        await member[0].add_roles(top10_role)
                else:
                    if 756430896092938322 in member_role_ids:
                        await member[0].remove_roles(top10_role)

    def get_profile(self, player, server):
        # Returns the rating and game stats of given player in an embed
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        player_data_query = 'SELECT * FROM players WHERE player = ?'
        cursor.execute(player_data_query, (player.id,))
        player_data = cursor.fetchone()
        
        if player_data:
            player_sr = player_data[1]
            stats = {'win as soldier': player_data[4], 'played as soldier': player_data[5], 'win as warrior': player_data[6], 'played as warrior': player_data[7], 
            'win as coord': player_data[8], 'played as coord': player_data[9], 'win as queen': player_data[10], 'played as queen': player_data[11], 'win as warchief': player_data[12], 
            'played as warchief': player_data[13], 'win as ymir': player_data[14], 'played as ymir': player_data[15], 'win as false king':player_data[16], 'played as false king': player_data[17], 
            'win as ackerman': player_data[18], 'played as ackerman': player_data[19], 'win as mike': player_data[20], 'played as mike': player_data[21], 'win as scout': player_data[22], 
            'played as scout': player_data[23], 'win as spy': player_data[24], 'played as spy': player_data[25]}

            stats['soldier wins'] = stats['win as soldier'] + stats['win as coord'] + stats['win as queen'] + stats['win as ackerman'] + stats['win as mike'] + stats['win as scout']
            stats['soldier games'] = stats['played as soldier'] + stats['played as coord'] + stats['played as queen'] + stats['played as ackerman'] + stats['played as mike'] + stats['played as scout']
            stats['warrior wins'] = stats['win as warrior'] + stats['win as warchief'] + stats['win as ymir'] + stats['win as false king'] + stats['win as spy']
            stats['warrior games'] = stats['played as warrior'] + stats['played as warchief'] + stats['played as ymir'] + stats['played as false king'] + stats['played as spy']
            stats['wins'] = stats['soldier wins'] + stats['warrior wins']
            stats['games'] = stats['soldier games'] + stats['warrior games']

        else:
            # Add player data into player records
            player_sr = 1500
            insert_player_data_query = 'INSERT INTO players VALUES ({})'.format(','.join('?' * 26))
            insert_player_data = [player.id, 1500] + 24 * [0]
            cursor.execute(insert_player_data_query, insert_player_data)
            conn.commit()

            stats = {'wins': 0, 'games': 0, 'soldier wins': 0, 'soldier games': 0, 'warrior wins': 0, 'warrior games': 0, 'win as soldier': 0, 'played as soldier': 0, 'win as warrior': 0, 'played as warrior': 0, 
            'win as coord': 0, 'played as coord': 0, 'win as queen': 0, 'played as queen': 0, 'win as warchief': 0, 'played as warchief': 0, 'win as ymir': 0, 'played as ymir':0, 'win as false king':0, 
            'played as false king': 0, 'win as ackerman': 0, 'played as ackerman': 0, 'win as mike': 0, 'played as mike': 0, 'win as scout': 0, 'played as scout': 0, 'win as spy': 0, 'played as spy': 0}

        # Get total players in server
        player_rankings_query = 'SELECT player, rating FROM players'
        cursor.execute(player_rankings_query)
        player_rankings = cursor.fetchall()
        
        # Sort by Exp from biggest to smallest
        player_rankings.sort(key = lambda x: x[1], reverse = True)

        # Get players in server
        server_users = list(map(lambda y: y.id, server.members))
        server_players = list(filter(lambda x:x[0] in server_users, player_rankings))
        total_players = len(server_players)

        # Get ranking
        i = 0
        for person in server_players:
            i += 1
            if person[0] == player.id:
                rank = i
                break

        conn.close()

        profile = discord.Embed(title = player.name + '\'s Profile', description = 'Skill Rating (SR): **' + str(int(round(player_sr, 0))) + '**', colour=0x0013B4)
        profile.set_thumbnail(url = player.avatar_url)

        profile.add_field(name = 'Rank', value = str(rank) + '/' + str(total_players), inline = False)
        profile.add_field(name = 'Games played', value = str(stats['games']))
        won_games = str(stats['wins'])
        if stats['games'] > 0:
            won_games += ' (' + str(round(100 * stats['wins'] / stats['games'], 1)) + '%)'
        profile.add_field(name = 'Games won', value = won_games)

        won_soldiers = '🛡 Soldiers: ' + str(stats['soldier wins']) + ' wins' + ' / ' + str(stats['soldier games']) + ' games'
        if stats['soldier games'] > 0:
            won_soldiers += ' **(' + str(round(100 * stats['soldier wins'] / stats['soldier games'], 1)) + '%)**'
        won_soldiers += ' 🛡'

        soldier_wins = 'Soldier: ' + str(stats['win as soldier']) + '/' + str(stats['played as soldier'])
        if stats['played as soldier'] > 0:
            soldier_wins += ' (' + str(round(100 * stats['win as soldier'] / stats['played as soldier'], 1)) + '%)'

        soldier_wins += '\nQueen: ' + str(stats['win as queen']) + '/' + str(stats['played as queen'])
        if stats['played as queen'] > 0:
            soldier_wins += ' (' + str(round(100 * stats['win as queen'] / stats['played as queen'], 1)) + '%)'

        soldier_wins += '\nAckerman: ' + str(stats['win as ackerman']) + '/' + str(stats['played as ackerman'])
        if stats['played as ackerman'] > 0:
            soldier_wins += ' (' + str(round(100 * stats['win as ackerman'] / stats['played as ackerman'], 1)) + '%)'

        soldier_wins += '\nMike Zacharias: ' + str(stats['win as mike']) + '/' + str(stats['played as mike'])
        if stats['played as mike'] > 0:
            soldier_wins += ' (' + str(round(100 * stats['win as mike'] / stats['played as mike'], 1)) + '%)'

        soldier_wins += '\nScout: ' + str(stats['win as scout']) + '/' + str(stats['played as scout'])
        if stats['played as scout'] > 0:
            soldier_wins += ' (' + str(round(100 * stats['win as scout'] / stats['played as scout'], 1)) + '%)'

        soldier_wins += '\nCoordinate: ' + str(stats['win as coord']) + '/' + str(stats['played as coord'])
        if stats['played as coord'] > 0:
            soldier_wins += ' (' + str(round(100 * stats['win as coord'] / stats['played as coord'], 1)) + '%)'

        won_warriors = '⚔ Warriors: ' + str(stats['warrior wins']) + ' wins' + ' / ' + str(stats['warrior games']) + ' games'
        if stats['warrior games'] > 0:
            won_warriors += ' **(' + str(round(100 * stats['warrior wins'] / stats['warrior games'], 1)) + '%)**'
        won_warriors += ' ⚔'

        warrior_wins = '\nWarrior: ' + str(stats['win as warrior']) + '/' + str(stats['played as warrior'])
        if stats['played as warrior'] > 0:
            warrior_wins += ' (' + str(round(100 * stats['win as warrior'] / stats['played as warrior'], 1)) + '%)'

        warrior_wins += '\nWarchief: ' + str(stats['win as warchief']) + '/' + str(stats['played as warchief'])
        if stats['played as warchief'] > 0:
            warrior_wins += ' (' + str(round(100 * stats['win as warchief'] / stats['played as warchief'], 1)) + '%)'

        warrior_wins += '\nFalse King: ' + str(stats['win as false king']) + '/' + str(stats['played as false king'])
        if stats['played as false king'] > 0:
            warrior_wins += ' (' + str(round(100 * stats['win as false king'] / stats['played as false king'], 1)) + '%)'
        
        warrior_wins += '\nYmir: ' + str(stats['win as ymir']) + '/' + str(stats['played as ymir'])
        if stats['played as ymir'] > 0:
            warrior_wins += ' (' + str(round(100 * stats['win as ymir'] / stats['played as ymir'], 1)) + '%)'
        
        warrior_wins += '\nSpy: ' + str(stats['win as spy']) + '/' + str(stats['played as spy'])
        if stats['played as spy'] > 0:
            warrior_wins += ' (' + str(round(100 * stats['win as spy'] / stats['played as spy'], 1)) + '%)'

        profile.add_field(name = won_soldiers, value = soldier_wins, inline = False)
        profile.add_field(name = won_warriors, value = warrior_wins, inline = False)
        
        return profile

    def get_achievements(self, player):
        # Returns achievements of player in an embed
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        # Extract data
        player_data_query = 'SELECT * FROM players WHERE player = ?'
        cursor.execute(player_data_query, (player.id,))
        player_data = cursor.fetchone()

        if player_data:
            # [Name, No. games played, Current win streak, Max win streak, Soldier wins, Warrior wins, Coordinate wins, Queen/Ackerman/Mike/Scout wins, Warchief/False King/Ymir/Spy wins]
            games_played = player_data[5] + player_data[7] + player_data[9] + player_data[11] + player_data[13] + player_data[15] + player_data[17] + player_data[19] + \
                player_data[21] + player_data[23] + player_data[25]
            optional_soldier_wins = player_data[10] + player_data[18] + player_data[20] + player_data[22]
            optional_warrior_wins = player_data[12] + player_data[14] + player_data[16] + player_data[24]
            badges = [player.name, games_played, player_data[2], player_data[3], player_data[4], player_data[6], player_data[8], optional_soldier_wins, optional_warrior_wins]
        else:
            # Add player data into player records
            insert_player_data_query = 'INSERT INTO players VALUES ({})'.format(','.join('?' * 26))
            insert_player_data = [player.id, 1500] + 24 * [0]
            cursor.execute(insert_player_data_query, insert_player_data)
            conn.commit()

            badges = [player.name, 0, 0, 0, 0, 0, 0, 0, 0]

        conn.close()

        # Put info into embed
        num_badges = 0

        number_games_played = badges[1]
        number_games_badges = ''
        number_games_next = str(number_games_played)
        for step in sorted(list(self.number_games_achievements)):
            if number_games_played < step:
                number_games_next = str(number_games_played) + '/' + str(step)
                break
            number_games_badges += self.badge_emojis[self.number_games_achievements[step]]
            num_badges += 1

        cur_streak = badges[2]
        max_streak = badges[3]
        consecutive_wins_badges = ''
        consecutive_next = str(max_streak)
        for step in sorted(list(self.consecutive_wins_achievements)):
            if max_streak < step:
                consecutive_next = str(cur_streak) + '/' + str(step)
                break
            consecutive_wins_badges += self.badge_emojis[self.consecutive_wins_achievements[step]]
            num_badges += 1

        soldier_wins = badges[4]
        soldier_wins_badges = ''
        soldier_wins_next = str(soldier_wins)
        for step in sorted(list(self.soldier_wins_achievements)):
            if soldier_wins < step:
                soldier_wins_next = str(soldier_wins) + '/' + str(step)
                break
            soldier_wins_badges += self.badge_emojis[self.soldier_wins_achievements[step]]
            num_badges += 1

        warrior_wins = badges[5]
        warrior_wins_badges = ''
        warrior_wins_next = str(warrior_wins)
        for step in sorted(list(self.warrior_wins_achievements)):
            if warrior_wins < step:
                warrior_wins_next = str(warrior_wins) + '/' + str(step)
                break
            warrior_wins_badges += self.badge_emojis[self.warrior_wins_achievements[step]]
            num_badges += 1

        coordinate_wins = badges[6]
        coordinate_wins_badges = ''
        coordinate_wins_next = str(coordinate_wins)
        for step in sorted(list(self.coordinate_wins_achievements)):
            if coordinate_wins < step:
                coordinate_wins_next = str(coordinate_wins) + '/' + str(step)
                break
            coordinate_wins_badges += self.badge_emojis[self.coordinate_wins_achievements[step]]
            num_badges += 1

        queen_wins = badges[7]
        queen_wins_badges = ''
        queen_wins_next = str(queen_wins)
        for step in sorted(list(self.queen_wins_achievements)):
            if queen_wins < step:
                queen_wins_next = str(queen_wins) + '/' + str(step)
                break
            queen_wins_badges += self.badge_emojis[self.queen_wins_achievements[step]]
            num_badges += 1

        warchief_wins = badges[8]
        warchief_wins_badges = ''
        warchief_wins_next = str(warchief_wins)
        for step in sorted(list(self.warchief_wins_achievements)):
            if warchief_wins < step:
                warchief_wins_next = str(warchief_wins) + '/' + str(step)
                break
            warchief_wins_badges += self.badge_emojis[self.warchief_wins_achievements[step]]
            num_badges += 1

        player_achievements = discord.Embed(title = 'Badges for Warriors vs Soldiers', description = 'Number of badges collected: **' + str(num_badges) + '**', colour = 0xC0C0C0)
        player_achievements.set_author(name = player.name, icon_url = player.avatar_url)
        player_achievements.set_thumbnail(url = player.avatar_url)

        player_achievements.add_field(name = 'Number of games played', value = number_games_next)
        player_achievements.add_field(name = 'Badges', value = number_games_badges if number_games_badges != '' else '-')
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Number of wins in a row', value = consecutive_next)
        player_achievements.add_field(name = 'Badges', value = consecutive_wins_badges if consecutive_wins_badges != '' else '-')
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Number of wins as Soldier', value = soldier_wins_next)
        player_achievements.add_field(name = 'Badges', value = soldier_wins_badges if soldier_wins_badges != '' else '-')
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Number of wins as Warrior', value = warrior_wins_next)
        player_achievements.add_field(name = 'Badges', value = warrior_wins_badges if warrior_wins_badges != '' else '-')
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Number of wins as Coordinate', value = coordinate_wins_next)
        player_achievements.add_field(name = 'Badges', value = coordinate_wins_badges if coordinate_wins_badges != '' else '-')
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Number of wins as Optional Soldier role', value = queen_wins_next)
        player_achievements.add_field(name = 'Badges', value = queen_wins_badges if queen_wins_badges != '' else '-')
        player_achievements.add_field(name = '⠀', value='⠀')
        player_achievements.add_field(name = 'Number of wins as Optional Warrior role', value = warchief_wins_next)
        player_achievements.add_field(name = 'Badges', value = warchief_wins_badges if warchief_wins_badges != '' else '-')
        player_achievements.add_field(name = '⠀', value='⠀')

        return player_achievements

    def get_game_stats(self, page_no, server):
        # Returns past game statistics
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        get_server_data_query = 'SELECT * FROM servers WHERE server = ?'
        cursor.execute(get_server_data_query, (server.id,))
        server_data = cursor.fetchone()

        get_game_data_query = 'SELECT * FROM global'
        cursor.execute(get_game_data_query)
        game_data = cursor.fetchall()

        get_player_data_query = 'SELECT * FROM players'
        cursor.execute(get_player_data_query)
        player_data = cursor.fetchall()

        page_descriptions = {1: 'Game Stats ({})'.format(server.name), 2: 'Role Stats ({})'.format(server.name), 3: 'Game Stats (Global)', 4: 'Role Stats (Global)'}

        game_stats = discord.Embed(title = '⚔ Warriors vs Soldiers Stats 🛡 ', description = str(page_no) + '. ' + page_descriptions[page_no], colour=0x0013B4)

        if page_no == 1:
            if server_data:
                # Game stats
                soldiers_wins = sum(server_data[1:19:3])
                warriors_wins =  sum(server_data[2:19:3]) + sum(server_data[3:19:3])
                warriors_walls = sum(server_data[2:19:3])
                warriors_kidnap = sum(server_data[3:19:3])
                games_played = 'Soldiers: ' + str(soldiers_wins)
                if (warriors_wins + soldiers_wins) > 0:
                    games_played += ' (' + str(round(100 * soldiers_wins / (warriors_wins + soldiers_wins), 1)) + '%)'
                games_played += '\nWarriors: ' + str(warriors_wins)
                if (warriors_wins + soldiers_wins) > 0:
                    games_played += ' (' + str(round(100 * warriors_wins / (warriors_wins + soldiers_wins), 1)) + '%)'
                games_played += '\n - Walls: ' + str(warriors_walls)
                if (warriors_wins + soldiers_wins) > 0:
                    games_played += ' (' + str(round(100 * warriors_walls / (warriors_wins + soldiers_wins), 1)) + '%)'
                games_played += '\n - Kidnap: ' + str(warriors_kidnap)
                if (warriors_wins + soldiers_wins) > 0:
                    games_played += ' (' + str(round(100 * warriors_kidnap / (warriors_wins + soldiers_wins), 1)) + '%)'
                game_stats.add_field(name = 'Total games played: ' + str(warriors_wins + soldiers_wins), value = games_played, inline = False)

                for i in range(6):
                    soldiers_wins_n = server_data[3 * i + 1]
                    warriors_wins_n = server_data[3 * i + 2] + server_data[3 * i + 3]
                    warriors_walls_n = server_data[3 * i + 2]
                    warriors_kidnap_n = server_data[3 * i + 3]
                    num_players_stats = 'Soldiers: ' + str(soldiers_wins_n)
                    if (warriors_wins_n + soldiers_wins_n) > 0:
                        num_players_stats += ' (' + str(round(100 * soldiers_wins_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                    num_players_stats += '\nWarriors: ' + str(warriors_wins_n)
                    if (warriors_wins_n + soldiers_wins_n) > 0:
                        num_players_stats += ' (' + str(round(100 * warriors_wins_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                    num_players_stats += '\n - Walls: ' + str(warriors_walls_n)
                    if (warriors_wins_n + soldiers_wins_n) > 0:
                        num_players_stats += ' (' + str(round(100 * warriors_walls_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                    num_players_stats += '\n - Kidnap: ' + str(warriors_kidnap_n)
                    if (warriors_wins_n + soldiers_wins_n) > 0:
                        num_players_stats += ' (' + str(round(100 * warriors_kidnap_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                    game_stats.add_field(name = str(i + 5) + ' Players: ' + str(warriors_wins_n + soldiers_wins_n), value = num_players_stats)
            else:
                insert_server_data_query = 'INSERT INTO servers VALUES ({})'.format(','.join('?' * 41))
                insert_server_data = [server.id] + [0] * 40
                cursor.execute(insert_server_data_query, insert_server_data)
                conn.commit()

                soldiers_wins = 0
                warriors_wins =  0
                warriors_walls = 0
                warriors_kidnap = 0
                games_played = 'Soldiers: ' + str(soldiers_wins)
                if (warriors_wins + soldiers_wins) > 0:
                    games_played += ' (' + str(round(100 * soldiers_wins / (warriors_wins + soldiers_wins), 1)) + '%)'
                games_played += '\nWarriors: ' + str(warriors_wins)
                if (warriors_wins + soldiers_wins) > 0:
                    games_played += ' (' + str(round(100 * warriors_wins / (warriors_wins + soldiers_wins), 1)) + '%)'
                games_played += '\n - Walls: ' + str(warriors_walls)
                if (warriors_wins + soldiers_wins) > 0:
                    games_played += ' (' + str(round(100 * warriors_walls / (warriors_wins + soldiers_wins), 1)) + '%)'
                games_played += '\n - Kidnap: ' + str(warriors_kidnap)
                if (warriors_wins + soldiers_wins) > 0:
                    games_played += ' (' + str(round(100 * warriors_kidnap / (warriors_wins + soldiers_wins), 1)) + '%)'
                game_stats.add_field(name = 'Total games played: ' + str(warriors_wins + soldiers_wins), value = games_played, inline = False)

                for i in range(6):
                    soldiers_wins_n = 0
                    warriors_wins_n = 0
                    warriors_walls_n = 0
                    warriors_kidnap_n = 0
                    num_players_stats = 'Soldiers: ' + str(soldiers_wins_n)
                    if (warriors_wins_n + soldiers_wins_n) > 0:
                        num_players_stats += ' (' + str(round(100 * soldiers_wins_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                    num_players_stats += '\nWarriors: ' + str(warriors_wins_n)
                    if (warriors_wins_n + soldiers_wins_n) > 0:
                        num_players_stats += ' (' + str(round(100 * warriors_wins_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                    num_players_stats += '\n - Walls: ' + str(warriors_walls_n)
                    if (warriors_wins_n + soldiers_wins_n) > 0:
                        num_players_stats += ' (' + str(round(100 * warriors_walls_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                    num_players_stats += '\n - Kidnap: ' + str(warriors_kidnap_n)
                    if (warriors_wins_n + soldiers_wins_n) > 0:
                        num_players_stats += ' (' + str(round(100 * warriors_kidnap_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                    game_stats.add_field(name = str(i + 5) + ' Players: ' + str(warriors_wins_n + soldiers_wins_n), value = num_players_stats)

        elif page_no == 2:
            # Role stats
            if server_data:
                soldier_wins, soldier_games = server_data[19], server_data[20]
                warrior_wins, warrior_games = server_data[21], server_data[22]
                coordinate_wins, coordinate_games = server_data[23], server_data[24]
                queen_wins, queen_games = server_data[25], server_data[26]
                warchief_wins, warchief_games = server_data[27], server_data[28]
                ymir_wins, ymir_games = server_data[29], server_data[30]
                falseking_wins, falseking_games = server_data[31], server_data[32]
                ackerman_wins, ackerman_games = server_data[33], server_data[34]
                mike_wins, mike_games = server_data[35], server_data[36]
                scout_wins, scout_games = server_data[37], server_data[38]
                spy_wins, spy_games = server_data[39], server_data[40]
            else:
                insert_server_data_query = 'INSERT INTO servers VALUES ({})'.format(','.join('?' * 41))
                insert_server_data = [server.id] + [0] * 40
                cursor.execute(insert_server_data_query, insert_server_data)
                conn.commit()

                soldier_wins, soldier_games = 0, 0
                warrior_wins, warrior_games = 0, 0
                coordinate_wins, coordinate_games = 0, 0
                queen_wins, queen_games = 0, 0
                warchief_wins, warchief_games = 0, 0
                ymir_wins, ymir_games = 0, 0
                falseking_wins, falseking_games = 0, 0
                ackerman_wins, ackerman_games = 0, 0
                mike_wins, mike_games = 0, 0
                scout_wins, scout_games = 0, 0
                spy_wins, spy_games = 0, 0

            soldier_stats = 'Games: ' + str(soldier_games)
            soldier_stats += '\nWins: ' + str(soldier_wins)
            if soldier_wins > 0:
                soldier_stats += ' (' + str(round(100 * soldier_wins / soldier_games, 1)) + '%)'
            game_stats.add_field(name = '🛡Soldier🛡', value = soldier_stats)

            warrior_stats = 'Games: ' + str(warrior_games)
            warrior_stats += '\nWins: ' + str(warrior_wins)
            if warrior_wins > 0:
                warrior_stats += ' (' + str(round(100 * warrior_wins / warrior_games, 1)) + '%)'
            game_stats.add_field(name = '⚔Warrior⚔', value = warrior_stats)

            coordinate_stats = 'Games: ' + str(coordinate_games)
            coordinate_stats += '\nWins: ' + str(coordinate_wins)
            if coordinate_wins > 0:
                coordinate_stats += ' (' + str(round(100 * coordinate_wins / coordinate_games, 1)) + '%)'
            game_stats.add_field(name = '🗺Coordinate🗺', value = coordinate_stats)

            queen_stats = 'Games: ' + str(queen_games)
            queen_stats += '\nWins: ' + str(queen_wins)
            if queen_wins > 0:
                queen_stats += ' (' + str(round(100 * queen_wins / queen_games, 1)) + '%)'
            game_stats.add_field(name = '👼Queen👼', value = queen_stats)

            warchief_stats = 'Games: ' + str(warchief_games)
            warchief_stats += '\nWins: ' + str(warchief_wins)
            if warchief_wins > 0:
                warchief_stats += ' (' + str(round(100 * warchief_wins / warchief_games, 1)) + '%)'
            game_stats.add_field(name = '🦹‍♂️Warchief🦹‍♂️', value = warchief_stats)

            ymir_stats = 'Games: ' + str(ymir_games)
            ymir_stats += '\nWins: ' + str(ymir_wins)
            if ymir_wins > 0:
                ymir_stats += ' (' + str(round(100 * ymir_wins / ymir_games, 1)) + '%)'
            game_stats.add_field(name = '🤷‍♀️Ymir🤷‍♀️', value = ymir_stats)

            falseking_stats = 'Games: ' + str(falseking_games)
            falseking_stats += '\nWins: ' + str(falseking_wins)
            if falseking_wins > 0:
                falseking_stats += ' (' + str(round(100 * falseking_wins / falseking_games, 1)) + '%)'
            game_stats.add_field(name = '🕴False King🕴', value = falseking_stats)

            ackerman_stats = 'Games: ' + str(ackerman_games)
            ackerman_stats += '\nWins: ' + str(ackerman_wins)
            if ackerman_wins > 0:
                ackerman_stats += ' (' + str(round(100 * ackerman_wins / ackerman_games, 1)) + '%)'
            game_stats.add_field(name = '💂Ackerman💂', value = ackerman_stats)

            mike_stats = 'Games: ' + str(mike_games)
            mike_stats += '\nWins: ' + str(mike_wins)
            if mike_wins > 0:
                mike_stats += ' (' + str(round(100 * mike_wins / mike_games, 1)) + '%)'
            game_stats.add_field(name = '<:aotSmirk:571740978377916416>Mike Zacharias <:aotSmirk:571740978377916416>', value = mike_stats)

            scout_stats = 'Games: ' + str(scout_games)
            scout_stats += '\nWins: ' + str(scout_wins)
            if scout_wins > 0:
                scout_stats += ' (' + str(round(100 * scout_wins / scout_games, 1)) + '%)'
            game_stats.add_field(name = '🏇Scout🏇', value = scout_stats)

            spy_stats = 'Games: ' + str(spy_games)
            spy_stats += '\nWins: ' + str(spy_wins)
            if spy_wins > 0:
                spy_stats += ' (' + str(round(100 * spy_wins / spy_games, 1)) + '%)'
            game_stats.add_field(name = '🕵️‍♀️Spy🕵️‍♀️', value = spy_stats)

        elif page_no == 3:
            # Game stats
            soldiers_wins = sum([row[1] for row in game_data])
            warriors_wins =  sum([row[2] + row[3] for row in game_data])
            warriors_walls = sum([row[2] for row in game_data])
            warriors_kidnap = sum([row[3] for row in game_data])
            games_played = 'Soldiers: ' + str(soldiers_wins)
            if (warriors_wins + soldiers_wins) > 0:
                games_played += ' (' + str(round(100 * soldiers_wins / (warriors_wins + soldiers_wins), 1)) + '%)'
            games_played += '\nWarriors: ' + str(warriors_wins)
            if (warriors_wins + soldiers_wins) > 0:
                games_played += ' (' + str(round(100 * warriors_wins / (warriors_wins + soldiers_wins), 1)) + '%)'
            games_played += '\n - Walls: ' + str(warriors_walls)
            if (warriors_wins + soldiers_wins) > 0:
                games_played += ' (' + str(round(100 * warriors_walls / (warriors_wins + soldiers_wins), 1)) + '%)'
            games_played += '\n - Kidnap: ' + str(warriors_kidnap)
            if (warriors_wins + soldiers_wins) > 0:
                games_played += ' (' + str(round(100 * warriors_kidnap / (warriors_wins + soldiers_wins), 1)) + '%)'
            game_stats.add_field(name = 'Total games played: ' + str(warriors_wins + soldiers_wins), value = games_played, inline = False)

            for i in range(6):
                soldiers_wins_n = game_data[i][1]
                warriors_wins_n =  game_data[i][2] + game_data[i][3]
                warriors_walls_n = game_data[i][2]
                warriors_kidnap_n = game_data[i][3]
                num_players_stats = 'Soldiers: ' + str(soldiers_wins_n)
                if (warriors_wins_n + soldiers_wins_n) > 0:
                    num_players_stats += ' (' + str(round(100 * soldiers_wins_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                num_players_stats += '\nWarriors: ' + str(warriors_wins_n)
                if (warriors_wins_n + soldiers_wins_n) > 0:
                    num_players_stats += ' (' + str(round(100 * warriors_wins_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                num_players_stats += '\n - Walls: ' + str(warriors_walls_n)
                if (warriors_wins_n + soldiers_wins_n) > 0:
                    num_players_stats += ' (' + str(round(100 * warriors_walls_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                num_players_stats += '\n - Kidnap: ' + str(warriors_kidnap_n)
                if (warriors_wins_n + soldiers_wins_n) > 0:
                    num_players_stats += ' (' + str(round(100 * warriors_kidnap_n / (warriors_wins_n + soldiers_wins_n), 1)) + '%)'
                game_stats.add_field(name = str(i + 5) + ' Players: ' + str(warriors_wins_n + soldiers_wins_n), value = num_players_stats)

        elif page_no == 4:
            # Role stats
            soldier_wins, soldier_games = 0, 0
            warrior_wins, warrior_games = 0, 0
            coordinate_wins, coordinate_games = 0, 0
            queen_wins, queen_games = 0, 0
            warchief_wins, warchief_games = 0, 0
            ymir_wins, ymir_games = 0, 0
            falseking_wins, falseking_games = 0, 0
            ackerman_wins, ackerman_games = 0, 0
            mike_wins, mike_games = 0, 0
            scout_wins, scout_games = 0, 0
            spy_wins, spy_games = 0, 0

            for row in player_data:
                soldier_wins += row[4]
                soldier_games += row[5]
                warrior_wins += row[6]
                warrior_games += row[7]
                coordinate_wins += row[8]
                coordinate_games += row[9]
                queen_wins += row[10]
                queen_games += row[11]
                warchief_wins += row[12]
                warchief_games += row[13]
                ymir_wins += row[14]
                ymir_games += row[15]
                falseking_wins += row[16]
                falseking_games += row[17]
                ackerman_wins += row[18]
                ackerman_games += row[19]
                mike_wins += row[20]
                mike_games += row[21]
                scout_wins += row[22]
                scout_games += row[23]
                spy_wins += row[24]
                spy_games += row[25]

            soldier_stats = 'Games: ' + str(soldier_games)
            soldier_stats += '\nWins: ' + str(soldier_wins)
            if soldier_wins > 0:
                soldier_stats += ' (' + str(round(100 * soldier_wins / soldier_games, 1)) + '%)'
            game_stats.add_field(name = '🛡Soldier🛡', value = soldier_stats)

            warrior_stats = 'Games: ' + str(warrior_games)
            warrior_stats += '\nWins: ' + str(warrior_wins)
            if warrior_wins > 0:
                warrior_stats += ' (' + str(round(100 * warrior_wins / warrior_games, 1)) + '%)'
            game_stats.add_field(name = '⚔Warrior⚔', value = warrior_stats)

            coordinate_stats = 'Games: ' + str(coordinate_games)
            coordinate_stats += '\nWins: ' + str(coordinate_wins)
            if coordinate_wins > 0:
                coordinate_stats += ' (' + str(round(100 * coordinate_wins / coordinate_games, 1)) + '%)'
            game_stats.add_field(name = '🗺Coordinate🗺', value = coordinate_stats)

            queen_stats = 'Games: ' + str(queen_games)
            queen_stats += '\nWins: ' + str(queen_wins)
            if queen_wins > 0:
                queen_stats += ' (' + str(round(100 * queen_wins / queen_games, 1)) + '%)'
            game_stats.add_field(name = '👼Queen👼', value = queen_stats)

            warchief_stats = 'Games: ' + str(warchief_games)
            warchief_stats += '\nWins: ' + str(warchief_wins)
            if warchief_wins > 0:
                warchief_stats += ' (' + str(round(100 * warchief_wins / warchief_games, 1)) + '%)'
            game_stats.add_field(name = '🦹‍♂️Warchief🦹‍♂️', value = warchief_stats)

            ymir_stats = 'Games: ' + str(ymir_games)
            ymir_stats += '\nWins: ' + str(ymir_wins)
            if ymir_wins > 0:
                ymir_stats += ' (' + str(round(100 * ymir_wins / ymir_games, 1)) + '%)'
            game_stats.add_field(name = '🤷‍♀️Ymir🤷‍♀️', value = ymir_stats)

            falseking_stats = 'Games: ' + str(falseking_games)
            falseking_stats += '\nWins: ' + str(falseking_wins)
            if falseking_wins > 0:
                falseking_stats += ' (' + str(round(100 * falseking_wins / falseking_games, 1)) + '%)'
            game_stats.add_field(name = '🕴False King🕴', value = falseking_stats)

            ackerman_stats = 'Games: ' + str(ackerman_games)
            ackerman_stats += '\nWins: ' + str(ackerman_wins)
            if ackerman_wins > 0:
                ackerman_stats += ' (' + str(round(100 * ackerman_wins / ackerman_games, 1)) + '%)'
            game_stats.add_field(name = '💂Ackerman💂', value = ackerman_stats)

            mike_stats = 'Games: ' + str(mike_games)
            mike_stats += '\nWins: ' + str(mike_wins)
            if mike_wins > 0:
                mike_stats += ' (' + str(round(100 * mike_wins / mike_games, 1)) + '%)'
            game_stats.add_field(name = '<:aotSmirk:571740978377916416>Mike Zacharias <:aotSmirk:571740978377916416>', value = mike_stats)

            scout_stats = 'Games: ' + str(scout_games)
            scout_stats += '\nWins: ' + str(scout_wins)
            if scout_wins > 0:
                scout_stats += ' (' + str(round(100 * scout_wins / scout_games, 1)) + '%)'
            game_stats.add_field(name = '🏇Scout🏇', value = scout_stats)

            spy_stats = 'Games: ' + str(spy_games)
            spy_stats += '\nWins: ' + str(spy_wins)
            if spy_wins > 0:
                spy_stats += ' (' + str(round(100 * spy_wins / spy_games, 1)) + '%)'
            game_stats.add_field(name = '🕵️‍♀️Spy🕵️‍♀️', value = spy_stats)

        conn.close()

        return game_stats

    def get_leaderboard(self, server, page=1, player=None):
        # Returns the names of the top players, with 10 per page, in an embed
        conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
        cursor = conn.cursor()

        # Get total players in server
        player_rankings_query = 'SELECT player, rating FROM players'
        cursor.execute(player_rankings_query)
        player_data = cursor.fetchall()

        if player:
            # Check if player exists in db
            player_check_query = 'SELECT * FROM players WHERE player = ?'
            cursor.execute(player_check_query, (player.id,))
            player_check = cursor.fetchone()
            if player_check is None:
                # Add player data into player records
                insert_player_data_query = 'INSERT INTO players VALUES ({})'.format(','.join('?' * 26))
                insert_player_data = [player.id, 1500] + 24 * [0]
                cursor.execute(insert_player_data_query, insert_player_data)
                conn.commit()
                player_data.append(insert_player_data)

        conn.close()

        player_rankings = {} # {player id: sr, ...}
        # Put all players into a dictionary
        for row in player_data:
            player_rankings[row[0]] = row[1]

        server_users = server.members
        server_players = []
        for user in server_users:
            if user.id in player_rankings:
                server_players.append([user.mention, player_rankings[user.id]])
        
        # Sort by SR from biggest to smallest
        server_players.sort(key = lambda x: x[1], reverse = True)

        # Get total number of pages
        num_pages = math.ceil(len(server_players) / 10)

        # Top 10x players
        try: 
            page_no = int(page)
        except:
            page_no = 1

        # Wrap-around for leaderboard page flipping
        if page_no > num_pages:
            page_no = 1
        if page_no < 1:
            page_no = num_pages

        # Get page_no of player rank
        if player:
            player_rank = 0
            for person in server_players:
                player_rank += 1
                if person[0] == player.mention:
                    break
            page_no = math.ceil(player_rank / 10)

        # Put names into embed
        all_names = ''
        all_sr = ''
        nums = {1:'1⃣', 2:'2⃣', 3:'3⃣', 4:'4⃣', 5:'5⃣', 6:'6⃣', 7:'7⃣', 8:'8⃣', 9:'9⃣', 10:'🔟'}
        for rank in range((page_no - 1) * 10 + 1, min(len(server_players) + 1, page_no * 10 + 1)):
            if rank == 1:
                all_names += '🥇 '
            elif rank == 2:
                all_names += '🥈 '
            elif rank == 3:
                all_names += '🥉 '
            elif rank <= 10:
                all_names += str(nums[rank]) + ' '
            else:
                all_names += '#' + str(rank) + ' '
            all_names += server_players[rank-1][0] + '\n'
            if rank <= 10:
                all_sr += '￶￵ ￶￵  ￶￵ 🔹 ' + str(int(round(server_players[rank-1][1], 0))) + ' 🔹' + '\n'
            else:
                all_sr += ' ￶￵ ￶￵ ￶￵  ￶￵ ￶￵ ￶￵  ￶￵ ￶￵ ￶￵ ￶￵ ' + str(int(round(server_players[rank-1][1], 0))) + '\n'

        lb_info = 'Page ' + str(page_no) + '/' + str(num_pages)
        leaderboard = discord.Embed(title = 'Leaderboard for Warriors vs Soldiers', description = lb_info, colour=0x0013B4)
        if player:
            leaderboard.add_field(name = player.name + '\'s Rank', value = str(player_rank) + '/' + str(len(server_players)), inline = False)
        leaderboard.add_field(name = 'Player', value = all_names)
        leaderboard.add_field(name = 'Skill Rating (SR)', value = all_sr)
        return leaderboard, page_no

    def get_commands(self, *command_query):
        soldier_info = '🛡**Soldier**🛡\n\n\
The most common role in the game, the Soldier represents the uninformed majority. Their role is find out who the traitors within the military are, reach the basement before they destroy all 3 Walls, \
and help protect the identity of the Coordinate.\n\n\
**Tip:** The Soldier is simultaneously the weakest and strongest role in the game. Even though the Soldier has no knowledge of any one else\'s identity, a Soldier has \
no need to conceal their identity and are free to act however they want.'
        warrior_info = '⚔**Warrior**⚔\n\n\
The Warrior is the spy within the ranks of the military. Their role is to avoid being discovered by the Soldiers, persuade them to allow you into their expeditions, and sabotage them. If that fails, \
they can still win by identifying the Coordinate within the ranks of the soldiers.\n\n\
**Tip:** The Warrior relies on deception and cunning to succeed. Teamwork and coordination with other Warriors is essential, to prevent your identities \
from being exposed. This must be done discreetly, however, as using DMs to communicate with other Warriors is against the rules and spirit of the game.'
        coordinate_info = '🗺**Coordinate**🗺\n\n\
The Coordinate holds the greatest power in the game, but with it comes a heavy responsibility. The Coordinate is aware of the Warriors\' identities from the start, but has to find \
a way to communicate this information to the Soldiers without being noticed by the Warriors, who can kidnap the Coordinate if the Soldiers reach the Basement.\n\n\
**Tip:** The Coordinate\'s playstyle can change depending on the situation. For example, if the other Soldiers are doing a good job identifying the Warriors, it would be advisable to focus on \
deflecting suspicion away from themselves instead.'
        queen_info = '👼**Queen**👼\n\n\
The Queen has the unique position of knowing the Coordinate\'s identity, which allows her to make better decisions during expeditions at no added risk. Her role is to protect \
the Coordinate using this information by acting like they would.\n\n\
**Tip:** While the Queen has the advantage of knowing the Coordinate\'s identity, she also has to be careful not to accidentally reveal the Coordinate\'s identity by favoring them on expeditions too much.'
        ackerman_info = '💂**Ackerman**💂\n\n\
The Ackerman has the ability to secure the Walls in **one** expedition that they\'re in. This prevents any Warriors on the expedition from destroying it. However, doing so also \
alerts any Warriors in the expedition of the Ackerman\'s identity, making it easier for them to identity the Coordinate.\n\n\
**Tip:** Knowing if and when to secure the Walls is key to playing an Ackerman well. For example, if the Soldiers are winning, it might be best to not secure the Walls at all, reducing the chances \
of the Warriors kidnapping the Coordinate at the end.'
        mike_info = '<:aotSmirk:571740978377916416>**Mike Zacharias** <:aotSmirk:571740978377916416>\n\n\
Humanity\'s 2nd strongest soldier **Mike Zacharias** has the incredible ability to sniff out Titans in expeditions <:aotSmirk:571740978377916416>. \
During the approval phase of all the expeditions that he is in, Mike will be told how many Titans the expedition contains, if any. Both Warriors and the Coordinate are considered Titans.\n\n\
**Tip:** The knowledge of how many Titans are in an expedition can be very valuable to both Soldiers and Warriors. Be careful what you do with that information. \
Prove yourself worthy of the title of humanity\'s 2nd strongest soldier!'
        scout_info = '🏇**Scout**🏇\n\n\
The Scout is the guiding light of an expedition. If the Scout is in an expedition, they will automatically fire a signal flare, alerting everyone of their presence in the expedition.\n\n\
**Tip:** The knowledge of the Scout\'s identity can benefit both sides in the game. The Scout should try to help the Soldiers identify them correctly, while working with their fellow Soldiers \
to confuse the Warriors as to who they are.'
        falseking_info = '🕴**False King**🕴\n\n\
The False King appears as the Coordinate to the Queen, in addition to the real Coordinate. This gives him the ability to confuse her by acting as the Coordinate, which can \
help turn the tide in the Warriors\' favor.\n\n\
**Tip:** As the False King, it can be especially advantageous to succeed expeditions which you are in, solely to gain the Queen\'s trust.'
        warchief_info = '🦹‍♂️**Warchief**🦹‍♂️\n\n\
The Warchief has the ability to conceal his identity from the Coordinate. This allows more possibilities to sow confusion within the Soldiers\' ranks without worrying about the \
Coordinate stepping in.\n\n\
**Tip:** The Warchief\'s role acts like a double-edged blade. Without the Coordinate\'s knowing the Warchief\'s identity, he can more easily gain the Soldiers\' trust. \
However, the very fact that the Coordinate is unaware of the Warchief\'s identity can make it harder for the Warriors to identify the Coordinate.'
        ymir_info = '🤷‍♀️**Ymir**🤷‍♀️\n\n\
Ymir is also on the Warriors\' side, but does not know of their identities, nor do they know hers. To achieve success, she must keep a close watch \
for potential comrades during expeditions.\n\n\
**Tip:** In smaller expeditions, it can be risky to choose to destroy the Walls, as there might be another Warrior in your group which would give both of you away. \
It is usually a good idea to wait until the later (and larger) expeditions to make your move.'
        spy_info = '🕵️‍♀️**Spy**🕵️‍♀️\n\n\
A highly skilled infiltrator, the Spy has the ability to flip the votes during the approval phase of an expedition. \
She may only do this once, however, as everyone will be alerted that the votes have been flipped.\n\n\
**Tip:** The Spy needs to be strategic about when to flip the votes to favor the Warriors, as it can easily backfire if people do not vote the way you expect.'
        blessing_info = '🔮**Ymir\'s Blessing**🔮\n\n\
Ymir\'s Blessing allows a player who has it to check another player\'s true allegiance (Warriors or Soldiers). At the start of the 3rd expedition, a random player will be given Ymir\'s blessing. \
They may use it on another player to find out their allegiance (will be DMed to them in private).\n\n\
Ymir\'s blessing will then be passed onto the player who was investigated, who can use it at the start of the next expedition, and so on. \
However, anyone who has had Ymir\'s blessing previously is granted immunity to being investigated by future holders of it.'
        paths_info = '📢**Paths**📢\n\n\
The Paths ability allows players to make an announcement anonymously to everyone in the game. When activated, a random person will be designated as the Paths holder at the start of every expedition. \
They will then be able to send a single message to the game channel without revealing their role or identity.'
        funds_info = '💰**Limited Funds**💰\n\n\
A more realistic take on the game, enabling this option will give the Soldiers limited funds for each expedition. \
If 5 proposals in a row are rejected, the Soldiers will run out of funds for the next expedition, handing the win to the Warriors by default.\n\n\
Enabling this effect could help reduce the frequency of gridlocks while adding an additional element of strategy for both sides.'
        kenny_info = '<:kennytheripper:768310628506402887> **Kenny the Ripper** <:kennytheripper:768310628506402887>\n\n\
Kenny the Ripper is a serial mass-murderer who has the ability to hunt down anyone!\n\n\
Kenny has a hit-list which rotates between players in the game. Each voting round, he will target a number of players from the top of the list, preventing them from voting.\n\n\
The number of players Kenny will target depends on the size of the game:\n\n\
5-6 players - 1 target\n\
7-8 players - 1-2 targets\n\
9-10 players - 2 targets'

        if command_query:
            commands_dict = {'host':'Creates a new lobby with you as the host. Add `casual` or `fast` to the command to host an unranked or fast game.',
                            'join':'Joins an existing lobby.',
                            'leave':'Leave your current lobby.',
                            'kick':'Removes a player from the lobby (Only the host can kick).',
                            'start':'Starts the game (requires 5-10 players).',
                            'reset':'Stops the existing game or clears the current lobby (only the host can reset once the game starts).',
                            'add':'Adds the specified optional role to the game. (E.g. `~add queen`)',
                            'remove':'Removes the specified optional role from the game. (E.g. `~remove queen`)',
                            'randomroles': 'Toggles randomization of optional roles when starting a game.',
                            'fast': 'Toggles fast mode on, with reduced timer durations for all phases.\n\n\
Voting: 1 min -> 30 secs\nExpedition selection: 5 min -> 2 min\nKidnap: 10 min -> 2 min',
                            'normal': 'Toggles normal mode on, with standard timer durations for all phases.',
                            'casual': 'Toggles casual mode on. SR or badges will not be awarded at the end of a game.',
                            'ranked': 'Toggles ranked mode on, with SR and badges being awarded as usual.',
                            'players':'If game hasn\'t started yet: Brings up the current list of players in the lobby.\n\n\
If game has started: Brings up the current list of players, arranged in order of their position in the queue to be Commander.',
                            'next':'Starts the next expedition after the previous expedition has ended.',
                            'pick':'The command used by the current Commander to select the expedition team. (E.g. `~pick @armin`)',
                            'kidnap': 'Usable if the Soldiers reach the basement, any Warrior can use this command to pick who they think is the Coordinate. (E.g. `~kidnap @eren`)',
                            'status':'Brings up the state of the current game. This includes the number of players, the number of Warriors and Soldiers, the current progress towards the Basement \
and status of the Walls, the results of previous expeditions and information on the current expedition.',
                            'rules':'Provides a breakdown of the game rules and roles, as well as some common tips and strategies.',
                            'profile':'Checks a person\'s profile (E.g. `~profile @levi`).',
                            'badges':'Checks the badges a given user has. Use just `~badges` to check your own badges.',
                            'gamestats':'Brings up the records of all games played.',
                            'leaderboard': 'Brings up the leaderboard, listing the top 10 players on the server. Add a number or tag to see subsequent pages (e.g. `~lb 2`).',
                            'lb': 'Brings up the leaderboard, listing the top 10 players on the server. Add a number or tag to see subsequent pages (e.g. `~lb 2`).',
                            'role': 'Checks your current role with the bot.',
                            'roles': 'If game hasn\'t started yet: Shows the full list of available roles.\n\nIf game has started: Shows the list of roles currently in the game.',
                            'advantage': 'The advantage value tells you how powerful one side is relative to the other. It is calculated by a combination of the roles added and size of the game.\n\n' + \
                                'At the end of the game, the side with the advantage will have the advantage value added to their team\'s average SR when calculating SR changes, ' + \
                                'so as to reflect their stronger position.\n\n' \
                                'This should help compensate for role imbalances by minimizing the penalty to the weaker side while rewarding them for an upset victory.'}

            roles_dict = {'soldier': soldier_info,
                        'warrior': warrior_info,
                        'coordinate': coordinate_info,
                        'queen': queen_info,
                        'ackerman': ackerman_info,
                        'mike': mike_info,
                        'scout': scout_info,
                        'false king': falseking_info,
                        'falseking': falseking_info,
                        'warchief': warchief_info,
                        'ymir': ymir_info,
                        'spy': spy_info,
                        'ymir\'s blessing': blessing_info,
                        'blessing': blessing_info,
                        'paths': paths_info,
                        'limited funds': funds_info,
                        'funds': funds_info,
                        'kenny': kenny_info,
                        'kenny the ripper': kenny_info}

            if command_query[0] in commands_dict:
                return discord.Embed(title = '`~' + command_query[0] + '`', description = commands_dict[command_query[0]], colour = 0x0013B4)
            elif command_query[0] in roles_dict:
                return discord.Embed(description = roles_dict[command_query[0]], colour = 0x0013B4)

        else:
            lobby_commands = '`~host`\n\
`~join`\n\
`~leave`\n\
`~kick <@person>`\n\
`~start`\n\
`~reset`\n\
`~add <role>`\n\
`~remove <role>`\n\
`~roles`\n\
`~randomroles`\n\
`~fast`\n\
`~normal`\n\
`~casual`\n\
`~ranked`\n\
`~players`\n\
`~advantage`'

            game_commands = '`~role`\n\
`~roles`\n\
`~next`\n\
`~pick <@person>`\n\
`~kidnap <@person>`\n\
`~status`\n\
`~players`\n\
`~advantage`'

            other_commands = '`~rules`\n\
`~profile <@person>`\n\
`~badges <@person>`\n\
`~gamestats`\n\
`~leaderboard`'

            commands = discord.Embed(title = 'List of commands for Warriors vs Soldiers', colour=0x0013B4)
            general_commands = '`~config` : Lets you select the game for each channel\n' + \
                '`~credits` : Who made me/Get support\n' + \
                '`~invite` : Link to invite me'
            commands.add_field(name = 'General', value = general_commands, inline = False)
            commands.add_field(name = 'Warriors vs Soldiers', value = 'For more information about a specific command, type `~help <command>`. (E.g. `~help kidnap`)', inline = False)
            commands.add_field(name = 'Lobby commands', value = lobby_commands)
            commands.add_field(name = 'In-game commands', value = game_commands)
            commands.add_field(name = 'Other commands', value = other_commands)
            return commands

    def tutorial(self, page_num):
        if page_num < 1:
            page_num = 17
        elif page_num > 17:
            page_num = 1

        if page_num == 1:
            tutorial1_intro = 'Warriors vs Soldiers is a party game for 5-10 players. It is based on the tabletop game The Resistance: Avalon, ' + \
            'with a similar concept to other deception games like Werewolf, Mafia, and Among Us.\n\u200B'
            tutorial1_embed = discord.Embed(title = 'Rules Summary', description = tutorial1_intro, colour=0x0013B4)

            tutorial1_teams = 'There are two teams, Warriors and Soldiers. The Soldiers will always outnumber the Warriors in a game. ' + \
            'However, the Soldiers do not know anyone\'s identities, while the Warriors know each other\'s identities.\n\u200B'
            tutorial1_embed.add_field(name = 'The Teams', value = tutorial1_teams, inline = False)

            tutorial1_objective = 'The objective of the game is to score 3 points for your team before the opposing team does.\n\u200B'
            tutorial1_embed.add_field(name = 'The Objective', value = tutorial1_objective, inline = False)

            tutorial1_selection = 'There can be up to 5 rounds (called Expeditions) in a game. Players take turns to pick a team (of varying size) to embark on each expedition.\n\u200B'
            tutorial1_embed.add_field(name = 'Team Selection', value = tutorial1_selection, inline = False)

            tutorial1_expedition = 'If a team is comprised of all Soldiers, then the expedition succeeds and Soldiers gain a point. ' + \
            'However, if there is a Warrior in the team, they may choose to sabotage the expedition, giving Warriors a point instead.\n\u200B'
            tutorial1_embed.add_field(name = 'The Expedition', value = tutorial1_expedition, inline = False)

            tutorial1_coordinate = 'The Coordinate is a special Soldier role who knows the Warriors\' identities from the beginning. ' + \
            'However, if the Soldiers score 3 points first, the Warriors have a last chance to win by identifying the Coordinate correctly at the end of the game.'
            tutorial1_embed.add_field(name = 'The Coordinate', value = tutorial1_coordinate, inline = False)

            tutorial1_details = 'For more detailed information on the game (including in-game screenshots!), click on ▶ below.'
            tutorial1_embed.add_field(name = '\u200B', value = tutorial1_details, inline = False)

            return None, tutorial1_embed, page_num

        if page_num == 2:
            tutorial2 = '**📖Backstory📖**\n\n\
The Year 850 was a pivotal year in the world of Attack on Titan. Around this time, it was discovered that Titan shifters who call themselves "Warriors" have infiltrated the Walls, \
and are attempting to wipe out the remainder of humanity by either destroying the Walls with their Titan powers or capturing the Coordinate, an unimaginable source of power.\n\n\
At approximately the same time, the Survey Corps, soldiers who have dedicated their lives to the survival of humanity, are on the verge of a major breakthrough. \
They have discovered that a certain basement in the border town of Shiganshina contains valuable secrets about the Titans, secrets that could allow them to overcome the Titan menace once and for all. \
Acting on that information, the Survey Corps prepare to embark on a series of expeditions to reach the Basement and secure this secret.\n\n\
This game puts you and your friends at the centre of this conflict. In a race against time, whichever side reaches their objectives first will decide the fate of humanity.\n\n\
Click on ▶ below to see the in-game rules.'
            return tutorial2, None, page_num

        if page_num == 3:
            tutorial3 = '**📌Game Rules📌**\n\n\
:one: Messaging another player in private (DM) is not allowed while in a game.\n\n\
:two: Revealing your role via screenshot is not allowed.\n\n\
:three: To invite people to join, you can ping `@Warriors vs. Soldiers`. Do not abuse pings, and do not ping other roles or random people.\n\n\
:four: Be civil and respectful to others when playing, keeping in mind these rules and the server rules.\n\n\
Click on ▶ below for more detailed information on gameplay.'
            return tutorial3, None, page_num

        elif page_num == 4:
            tutorial4 = '**🎲Gameplay🎲**\n\n\
At the start of the game, each player is secretly assigned a role (through DMs).\n\n\
The Warriors are made aware of each other without the Soldiers knowing - \
the only thing the Soldiers know is how many Warriors exist, not who they are. The player with the Coordinate role is also made aware of the Warriors\' identities.\n\n\
Below is an example of what a role message for a Warrior might look like:\n\u200B'
            warrior_msg = 'You are a **Warrior**!\n\n\
You are a Titan shifter who has infiltrated the Walls and are now working undercover to undermine the military\'s efforts. Working with your \
fellow Warriors, you seek to destroy the Walls and wipe out humanity. \n\n\
Your task is to conceal your identity from the Soldiers, and persuade them to allow you into their expeditions. At the same time, you need to try and identify the Coordinate within the ranks of the Soldiers.\n\n\
Your fellow Warriors are:\n**Reiner**\n**Bertolt**'
            tutorial4_embed = discord.Embed(title = '⚔ Warrior ⚔', description=warrior_msg, colour=0xB23E00)
            tutorial4_embed.set_thumbnail(url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/crossed-swords_2694.png')
            return tutorial4, tutorial4_embed, page_num

        elif page_num == 5:
            tutorial5 = '**🏠 Game Status 🏠**\n\n\
The game consists of up to 5 expeditions, each consisting of 3 phases to decide its success or failure.\n\n\
At any point during the game, you may type `~status` to bring up the current state of the game.\n\n\
This is what the game state looks like at the start of the game:\n\u200B'
            tutorial5_embed = discord.Embed(title='Current Game Information', description= 'Number of players: **5**\n**3** Soldiers vs **2** Warriors', colour=0xF9FF41)
            basement_progress = '￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵ ￶￵￶￵ \u2001\u2001\u20011⃣\n\u2001\u2001\u2001\u2001\u20012⃣\n\u2001\u2001\u2001\u2001\u20013⃣🏁'
            wall_status = '￶￵ ￶￵  ￶￵ ￶￵ ￶￵ ￶￵ \u200A\u200A\u2000🏠🇲🏠\n\u2001\u2000\u2000🏦🇷🏦\n\u2001\u2000\u2000🏰🇸🏰'

            expedition_info = 'Expedition 1: **2** members ' + '🏇' + '\n\n\
Expedition 2: **3** members ' + '\n\n\
Expedition 3: **2** members ' + '\n\n\
Expedition 4: **3** members ' + '\n\n\
Expedition 5: **3** members '

            tutorial5_embed.add_field(name = 'Progress towards Basement', value = basement_progress, inline = True)
            tutorial5_embed.add_field(name = 'Status of the Walls', value = wall_status, inline = True)
            tutorial5_embed.add_field(name = 'Expedition Info', value = expedition_info, inline = False)
            return tutorial5, tutorial5_embed, page_num

        elif page_num == 6:
            tutorial6 = '**🔹Planning Phase🔹**\n\n\
At the start of this phase, one of the players (either a Soldier or Warrior) is selected, based on a randomized queue implemented at the start of the game, to be the Commander. \
The Commander selects a number of players (which can include the Commander) to form the expedition team.\n\u200B'
            tutorial6_msg = 'Here, it is Armin\'s turn to be the Commander, and he selects Eren, Reiner, and himself to be in the expedition.'
            tutorial6_embed = discord.Embed(description=tutorial6_msg, colour=0x0013B4)
            tutorial6_embed.set_image(url='https://cdn.discordapp.com/attachments/266949919821135872/751345113992527882/selection_phase.PNG')
            return tutorial6, tutorial6_embed, page_num

        elif page_num == 7:
            tutorial7 = '**🔹Approval Phase🔹**\n\n\
After the Commander has picked the expedition team, all of the players discuss the Commander\'s choice, and vote in private (via DMs) whether or not to accept the proposed team.\n\n\
If a majority of players votes no to the proposal or if it\'s a tie, the Commander position passes on to the next player in line, who proposes their own expedition team.\n\n\
This continues until a majority of players agree with the current expedition team, at which point the round moves to the Action Phase.\n\u200B'
            tutorial7_msg = 'Everyone votes on the proposed expedition team (left), and the results are revealed after everyone has voted (right).\n\n' + \
            'As everyone with the exception of Eren approved of the expedition, the round progresses to the Action Phase.'
            tutorial7_embed = discord.Embed(description=tutorial7_msg, colour=0x0013B4)
            tutorial7_embed.set_image(url='https://cdn.discordapp.com/attachments/266949919821135872/751355515736424448/approval-phase-combined5.png')
            return tutorial7, tutorial7_embed, page_num

        elif page_num == 8:
            tutorial8 = '**🔹Action Phase🔹**\n\n\
Once an expedition team is agreed upon, the players in the expedition team then embark on the expedition. A Soldier must choose to help the expedition succeed, while a Warrior may either \
help the expedition succeed, or secretly sabotage the expedition.\n\n\
If all the players choose to succeed the expedition, the Soldiers advance one step closer to the Basement. \
But if a Warrior sabotages the expedition, the outermost Wall is destroyed and the Warriors move one step closer to victory.\n\u200B'
            tutorial8_msg = 'This 3-player expedition has been sabotaged by a Warrior within, resulting in a loss of a Wall.'
            tutorial8_embed = discord.Embed(description=tutorial8_msg, colour=0x0013B4)
            tutorial8_embed.set_image(url='https://cdn.discordapp.com/attachments/266949919821135872/751345083193753610/decision_phase.PNG')
            return tutorial8, tutorial8_embed, page_num

        elif page_num == 9:
            tutorial9 = '**🏆 Win conditions and the Coordinate 🏆**\n\n\
If the Warriors manage to destroy all 3 Walls before the Soldiers reach the Basement (3 successful expeditions), then Warriors win.\n\n\
If the Soldiers manage to reach the Basement first, the Warriors have one last chance to win by correctly identifying and kidnapping the Coordinate, who knows their identities. \
If they choose the wrong person, then Soldiers win.\n\u200B'
            tutorial9_msg = 'In this game, the Soldiers have reached the Basement by succeeding 3 expeditions.\n\n' + \
            'However, the Warriors correctly managed to identify the Coordinate, Eren, resulting in a win for the Warriors.'
            tutorial9_embed = discord.Embed(description=tutorial9_msg, colour=0x0013B4)
            tutorial9_embed.set_image(url='https://cdn.discordapp.com/attachments/266949919821135872/751345102492008458/kidnap_phase2.PNG')
            tutorial9_embed.set_footer(text='It was kind of obvious who it was, really...')
            return tutorial9, tutorial9_embed, page_num

        elif page_num == 10:
            tutorial10 = '💡**Tips and Strategies**💡\n\n\
💭 A common strategy used by the Warriors is to succeed the first couple of expeditions. This allows them to maintain their cover for a longer period, but also \
gives the Soldiers a significant headstart. Be tactful about when to do this (for example, if people are starting to suspect you).\n\n\
💭 Warriors can often find clues on who the Coordinate is by looking at past Commanders\' decisions and the voting rounds. As the Coordinate knows the Warriors\' identities, \
they rarely ever pick or vote incorrectly.\n\n\
💭 It can be helpful to also do weird and crazy things occasionally and be known as the guy/gal who just does unexpected things sometimes. This might be arrogantly displaying how they \
are randomly voting for an expedition for fun, vehemently accusing someone of being a Warrior with no solid evidence, or being mute \
for a game. This kind of randomness will help cover up slip-ups in games because it can be shrugged off as, "but he/she just always does that kind of thing".\n\n\
💭 Remember that at the end of the day, this is just a game! Lying and deception are part-and-parcel of the game; don\'t take it too seriously, and you\'ll have a great time!'
            return tutorial10, None, page_num

        elif page_num == 11:
            tutorial11_soldier = 'The most common role in the game, the Soldier represents the uninformed majority. \
Their role is find out who the traitors within the military are, reach the basement before they destroy all 3 Walls, and help protect the identity of the Coordinate.\n\n\
**Tip:** The Soldier is simultaneously the weakest and strongest role in the game. Even though the Soldier has no knowledge of any one else\'s identity, a Soldier has \
no need to conceal their identity and are free to act however they want.\n\u200B'
            tutorial11_warrior = 'The Warrior is the infiltrator within the ranks of the military. \
Their role is to avoid discovery by the Soldiers, persuade them to allow you into their expeditions, and sabotage them. If that fails, \
they can still win by identifying the Coordinate within the ranks of the Soldiers.\n\n\
**Tip:** The Warrior relies on deception and cunning to succeed. Teamwork and coordination with other Warriors is essential, to prevent your identities \
from being exposed. This must be done discreetly, however, as using DMs to communicate with other Warriors is against the rules and spirit of the game.\n\u200B'
            tutorial11_coordinate = 'The Coordinate holds the greatest power in the game, but with it comes a heavy responsibility. \
The Coordinate is aware of the Warriors\' identities from the start, but has to find \
a way to communicate this information to the Soldiers without being noticed by the Warriors, who can kidnap the Coordinate if the Soldiers reach the Basement.\n\n\
**Tip:** The Coordinate\'s playstyle can change depending on the situation. For example, if the other Soldiers are doing a good job identifying the Warriors, it would be advisable to focus on \
deflecting suspicion away from themselves instead.'

            tutorial11_embed = discord.Embed(title='Basic Roles', colour=0x0013B4)
            tutorial11_embed.add_field(name = '🛡Soldier🛡', value = tutorial11_soldier, inline = False)
            tutorial11_embed.add_field(name = '⚔Warrior⚔', value = tutorial11_warrior, inline = False)
            tutorial11_embed.add_field(name = '🗺Coordinate🗺', value = tutorial11_coordinate, inline = False)
            return None, tutorial11_embed, page_num

        elif page_num == 12:
            tutorial12_queen = 'The Queen has the unique position of knowing the Coordinate\'s identity, which allows her to make better decisions during expeditions at no added risk. Her role is to protect \
the Coordinate using this information by acting like they would.\n\n\
**Tip:** While the Queen has the advantage of knowing the Coordinate\'s identity, she also has to be careful not to accidentally reveal the Coordinate\'s identity by favoring them on expeditions too much.\n\u200B'
            tutorial12_ackerman = 'The Ackerman has the ability to secure the Walls in **one** expedition that they\'re in. This prevents any Warriors on the expedition from destroying it. However, doing so also \
alerts any Warriors in the expedition of the Ackerman\'s identity, making it easier for them to identity the Coordinate.\n\n\
**Tip:** Knowing if and when to secure the Walls is key to playing an Ackerman well. For example, if the Soldiers are winning, it might be best to not secure the Walls at all, keeping your identity hidden.'

            tutorial12_embed = discord.Embed(title='Optional Soldier Roles (1)', colour=0x0013B4)
            tutorial12_embed.add_field(name = '👼Queen👼', value = tutorial12_queen, inline = False)
            tutorial12_embed.add_field(name = '💂Ackerman💂', value = tutorial12_ackerman, inline = False)
            return None, tutorial12_embed, page_num

        elif page_num == 13:
            tutorial13_mike = 'Humanity\'s 2nd strongest soldier Mike Zacharias has the incredible ability to sniff out Titans in expeditions. \
During the approval phase of the expeditions he is in, Mike will be told how many Titans the expedition contains. Both Warriors and the Coordinate are considered Titans.\n\n\
**Tip:** The knowledge of how many Titans are in an expedition can be very valuable to both Warriors and Soldiers. Be careful not to reveal information that might help the Warriors identify the Coordinate.\n\u200B'
            tutorial13_scout = 'The Scout is the guiding light of an expedition. If the Scout is in an expedition, they will automatically fire a signal flare, alerting everyone of their presence in the expedition.\n\n\
**Tip:** The knowledge of the Scout\'s identity can benefit both sides in the game. The Scout should try to help the Soldiers identify them correctly, while working with their fellow Soldiers \
to confuse the Warriors as to who they are.'

            tutorial13_embed = discord.Embed(title='Optional Soldier Roles (2)', colour=0x0013B4)
            tutorial13_embed.add_field(name = '<:aotSmirk:571740978377916416>Mike Zacharias <:aotSmirk:571740978377916416>', value = tutorial13_mike, inline = False)
            tutorial13_embed.add_field(name = '🏇Scout🏇', value = tutorial13_scout, inline = False)
            return None, tutorial13_embed, page_num

        elif page_num == 14:
            tutorial14_falseking = 'The False King appears as the Coordinate to the Queen, in addition to the real Coordinate. \
This gives him the ability to confuse her by acting as the Coordinate, which can help turn the tide in the Warriors\' favor.\n\n\
**Tip:** As the False King, it can be especially advantageous to succeed expeditions which you are in, solely to gain the Queen\'s trust.\n\u200B'
            tutorial14_warchief = 'The Warchief has the ability to conceal his identity from the Coordinate. \
This allows more possibilities to sow confusion within the Soldiers\' ranks without worrying about the Coordinate stepping in.\n\n\
**Tip:** The Warchief\'s role acts like a double-edged blade. Without the Coordinate\'s knowing the Warchief\'s identity, he can more easily gain the Soldiers\' trust. \
However, the very fact that the Coordinate is unaware of the Warchief\'s identity can make it harder for the Warriors to identify the Coordinate.'

            tutorial14_embed = discord.Embed(title='Optional Warrior Roles (1)', colour=0x0013B4)
            tutorial14_embed.add_field(name = '🕴False King🕴', value = tutorial14_falseking, inline = False)
            tutorial14_embed.add_field(name = '🦹‍♂️Warchief🦹‍♂️', value = tutorial14_warchief, inline = False)
            return None, tutorial14_embed, page_num

        elif page_num == 15:
            tutorial15_ymir = 'Ymir is also on the Warriors\' side, but does not know of their identities, nor do they know hers. To achieve success, she must keep a close watch \
for potential comrades during expeditions.\n\n\
**Tip:** In smaller expeditions, it can be risky to choose to destroy the Walls, as there might be another Warrior in your group which would give both of you away. \
It is usually a good idea to wait until the later (and larger) expeditions to make your move.\n\u200B'
            tutorial15_spy = 'A highly skilled infiltrator, the Spy has the ability to flip the votes during the approval phase of an expedition. \
She may only do this once, however, as everyone will be alerted that the votes have been flipped.\n\n\
**Tip:** The Spy needs to be strategic about when to flip the votes to favor the Warriors, as it can easily backfire if people do not vote the way you expect.'

            tutorial15_embed = discord.Embed(title='Optional Warrior Roles (2)', colour=0x0013B4)
            tutorial15_embed.add_field(name = '🤷‍♀️Ymir🤷‍♀️', value = tutorial15_ymir, inline = False)
            tutorial15_embed.add_field(name = '🕵️‍♀️Spy🕵️‍♀️', value = tutorial15_spy, inline = False)
            return None, tutorial15_embed, page_num

        elif page_num == 16:
            tutorial16_blessing = 'Ymir\'s Blessing allows a player who has it to check another player\'s true allegiance (Warriors or Soldiers). \
At the start of the 3rd expedition, a random player will be given Ymir\'s blessing. \
They may use it on another player to find out their allegiance (will be DMed to them in private).\n\n\
Ymir\'s blessing will then be passed onto the player who was investigated, who can use it at the start of the next expedition, and so on. \
Anyone who has had Ymir\'s blessing previously is granted immunity to being investigated by future holders of it.\n\u200B'
            tutorial16_funds = 'A more realistic take on the game, enabling this option will give the Soldiers limited funds for each expedition. \
If 5 proposals in a row are rejected, the Soldiers will run out of funds for the next expedition, handing the win to the Warriors by default.\n\n\
Enabling this effect could help reduce the frequency of gridlocks while adding an additional element of strategy for both sides.'
            tutorial16_embed = discord.Embed(title='In-Game Effects (1)', colour=0x0013B4)
            tutorial16_embed.add_field(name = '🔮Ymir\'s Blessing🔮', value = tutorial16_blessing, inline = False)
            tutorial16_embed.add_field(name = '💰Limited Funds💰', value = tutorial16_funds, inline = False)
            return None, tutorial16_embed, page_num

        elif page_num == 17:
            tutorial17_paths = 'The Paths ability allows players to make an announcement anonymously to everyone in the game. \
When activated, a random person will be designated as the Paths holder at the start of every expedition. \
They will then be able to send a single message to the game channel without revealing their role or identity.\n\u200B'
            tutorial17_kenny = 'Kenny the Ripper is a serial mass-murderer who has the ability to hunt down anyone!\n\n\
Kenny has a hit-list which rotates between players in the game. Each voting round, he will target a number of players from the top of the list, preventing them from voting.\n\n\
The number of players Kenny will target depends on the size of the game:\n\n\
5-6 players - 1 target\n\
7-8 players - 1-2 targets\n\
9-10 players - 2 targets'
            tutorial17_embed = discord.Embed(title='In-Game Effects (2)', colour=0x0013B4)
            tutorial17_embed.add_field(name = '📢Paths📢', value = tutorial17_paths, inline = False)
            tutorial17_embed.add_field(name = '<:kennytheripper:768310628506402887> **Kenny the Ripper** <:kennytheripper:768310628506402887>', value = tutorial17_kenny, inline = False)
            return None, tutorial17_embed, page_num
