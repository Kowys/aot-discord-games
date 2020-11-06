import discord
import asyncio
from WarriorsvsSoldiers import game


class Game():
    def __init__(self, client):
        self.client = client
        self.state = game.State()
        self.approval_timer_obj = self.client.loop.create_task(self.approval_timer())
        self.decision_timer_obj = self.client.loop.create_task(self.decision_timer())
        self.selection_timer_obj = self.client.loop.create_task(self.selection_timer())
        self.next_expedition_timer_obj = self.client.loop.create_task(self.next_expedition_timer())
        self.blessing_timer_obj = self.client.loop.create_task(self.blessing_timer())
        self.paths_timer_obj = self.client.loop.create_task(self.paths_timer())
        self.saboteur_timer_obj = self.client.loop.create_task(self.saboteur_timer())
        self.kidnap_timer_obj = self.client.loop.create_task(self.kidnap_timer())

    async def msg_handler(self, message):
        # Private messages
        if str(message.channel.type) == 'private':
            response = message.content.lower()

            # Check your own role
            if response.startswith('~role'):
                player_role = self.state.get_player_role(message.author)
                await message.author.dm_channel.send(embed=player_role)

            # Saboteur
            if self.state.status == 'saboteur selection':
                saboteur_msg, public_msg = self.state.saboteur_select(response, message.author)
                if type(saboteur_msg) != str:
                    await message.author.dm_channel.send(embed=saboteur_msg)
                    await self.state.game_channel.send(public_msg)
                    await asyncio.sleep(2)
                    await self.state.game_channel.send(embed=self.state.get_status())
                    await asyncio.sleep(2)
                    await self.state.game_channel.send('When everyone is ready, type `~next` to begin the first expedition.')
                else:
                    await message.author.dm_channel.send(saboteur_msg)

            # Paths phase
            if self.state.status == 'paths announcement' and message.author == self.state.paths_holders[0]:
                self.state.status = 'expedition selection'
                self.state.paths_holders.pop(0)

                announcement_msg = 'An announcement has been sent from the Paths!'
                preface_msg = 'The **Paths Holder** says:\n📢 '
                player_msg = message.content

                await message.author.dm_channel.send(embed=discord.Embed(description='Your message has been sent!', colour=0x4B4B4B))
                await self.state.game_channel.send(announcement_msg)
                await asyncio.sleep(2)

                await self.state.game_channel.send(preface_msg + player_msg)
                await asyncio.sleep(2)

                expedition_msg = '--**Expedition #' + \
                    str(self.state.cur_expedition) + ': Planning phase**--'
                await self.state.game_channel.send(expedition_msg)
                await asyncio.sleep(2)
                self.state.next_commander()
                commander_msg = 'The commander for this expedition is **' + \
                    self.state.players[0][0].mention + '**!'
                await self.state.game_channel.send(commander_msg)

                await asyncio.sleep(2)
                players_msg = self.state.get_players()
                await self.state.game_channel.send(embed=players_msg)

                if self.state.kenny:
                    await asyncio.sleep(2)
                    kenny_hit_list_msg = self.state.get_kenny_hit_list()
                    await self.state.game_channel.send(embed=kenny_hit_list_msg)

                await asyncio.sleep(1)
                commander_msg2 = 'Commander **' + \
                    self.state.players[0][0].name + \
                    '**, please select your team for the expedition. (Type `~pick <@name>` to pick a team member.)'
                await self.state.game_channel.send(commander_msg2)

            # Expedition voting phase
            if self.state.status == 'expedition approval':
                if message.author not in list(map(lambda x: x[0], self.state.expedition_approval)):
                    if response.startswith('y'):
                        self.state.expedition_approval.append([message.author, 'yes'])
                        await message.author.dm_channel.send(embed=discord.Embed(description='Response recorded!', colour=0xC0C0C0))

                    elif response.startswith('n'):
                        self.state.expedition_approval.append([message.author, 'no'])
                        await message.author.dm_channel.send(embed=discord.Embed(description='Response recorded!', colour=0xC0C0C0))

                    elif response.startswith('f'):
                        # Spy only
                        flip_msg = self.state.get_flip_msg(message.author)
                        if type(flip_msg) == str:
                            await message.author.dm_channel.send(flip_msg)
                        else:
                            await message.author.dm_channel.send(embed=flip_msg)

                    if not response.startswith('f'):
                        expedition_approval_status = self.state.approval_players()
                        self.state.message_box.append(await self.state.game_channel.send(embed=expedition_approval_status))
                        # Delete previous approval messages
                        if len(self.state.message_box) > 1:
                            for _ in range(len(self.state.message_box) - 1):
                                delete_msg = self.state.message_box.pop(0)
                                await delete_msg.delete()

                    # After everyone has voted
                    if len(self.state.expedition_approval) == len(self.state.players):
                        if self.state.status != 'expedition approval':
                            pass
                        else:
                            self.state.status = ''
                            await self.state.message_box[0].delete()
                            self.state.message_box = []

                            if self.state.flipping_votes:
                                self.state.flip_votes()
                                await self.state.game_channel.send('🔄 The votes have been flipped by the **Spy**! 🔄')

                            expedition_approval_result = self.state.get_approval_result()
                            await self.state.game_channel.send(embed=expedition_approval_result)

                            # Go to decision phase if vote passes, or back to selection phase otherwise
                            if len(list(filter(lambda x: x[1] == 'yes', self.state.expedition_approval))) > 0.5 * (len(self.state.expedition_approval) - self.state.num_targets):
                                self.state.expedition_approval = []
                                await self.state.game_channel.send('The proposal has passed!')

                                expedition_msg = '--**Expedition #' + \
                                    str(self.state.cur_expedition) + ': Action phase**--'
                                await asyncio.sleep(2)
                                await self.state.game_channel.send(expedition_msg)

                                decision_intro = 'Expedition members, please decide what you\'ll do during the expedition!'
                                await asyncio.sleep(2)
                                await self.state.game_channel.send(decision_intro)

                                for person in self.state.expedition_squad:
                                    decision_msg = self.state.get_decision_msg(person)
                                    try:
                                        await person.dm_channel.send(embed=decision_msg)
                                    except:
                                        private_dms_decision_msg = person.mention + ', you have disabled DMs from server members! ' + \
                                        'As a result, I am unable to process your decision.\n\n' + \
                                        'Please enable DMs from server members to participate in the game.'
                                        await self.state.game_channel.send(private_dms_decision_msg)
                                    await asyncio.sleep(0.1)

                                self.state.status = 'expedition decision'

                            else:
                                self.state.expedition_approval = []
                                self.state.expedition_squad = []
                                self.state.status = 'expedition selection'

                                await self.state.game_channel.send('The proposal has failed!')

                                if self.state.funds_enabled:
                                    self.state.funds -= 1
                                    status = self.state.get_status()
                                    await asyncio.sleep(2)
                                    await self.state.game_channel.send(embed=status)
                                    if self.state.funds == 1:
                                        await self.state.game_channel.send('❗| The Soldiers have funds for only **1** more proposal!')
                                    elif self.state.funds == 0:
                                        self.state.status = 'game ended warriors wall'
                                        warriors_win_msg = '⚔The Soldiers have run out of funds for further expeditions. Warriors win!⚔'
                                        await asyncio.sleep(2)
                                        await self.state.game_channel.send(warriors_win_msg)

                                        end_summary = self.state.get_summary()
                                        await asyncio.sleep(2)
                                        await self.state.game_channel.send(embed=end_summary)

                                        if self.state.gametype == 'Ranked':
                                            rating_changes = self.state.update_rating()
                                            achievements_msgs = self.state.update_achievements()
                                            # Update roles in official WvS server
                                            for player in self.state.players:
                                                await self.state.update_role(player[0], self.client)
                                            await self.state.update_top_roles(self.client)
                                            await asyncio.sleep(2)
                                            await self.state.game_channel.send(embed=rating_changes)
                                            for achievements_msg in achievements_msgs:
                                                await self.state.game_channel.send(achievements_msg)

                                        self.state.status = 'game ended'

                                if not self.state.status == 'game ended':
                                    expedition_msg = '--**Expedition #' + \
                                        str(self.state.cur_expedition) + ': Planning phase**--'
                                    await asyncio.sleep(2)
                                    await self.state.game_channel.send(expedition_msg)

                                    await asyncio.sleep(2)
                                    self.state.next_commander()
                                    commander_msg = 'The commander for this expedition is **' + \
                                        self.state.players[0][0].mention + '**!'
                                    await self.state.game_channel.send(commander_msg)

                                    await asyncio.sleep(2)
                                    players_msg = self.state.get_players()
                                    await self.state.game_channel.send(embed=players_msg)

                                    if self.state.kenny:
                                        await asyncio.sleep(2)
                                        kenny_hit_list_msg = self.state.get_kenny_hit_list()
                                        await self.state.game_channel.send(embed=kenny_hit_list_msg)

                                    await asyncio.sleep(2)
                                    commander_msg2 = 'Commander **' + \
                                        self.state.players[0][0].name + \
                                        '**, please select your team for the expedition. (Type `~pick <@name>` to pick a team member.)'
                                    await self.state.game_channel.send(commander_msg2)
                else:
                    if response.startswith('f') and message.author in list(map(lambda x: x[0], list(filter(lambda x: x[1] == 'spy', self.state.players)))):
                        await message.author.dm_channel.send('You\'ve already voted! You may no longer flip the votes.')
                    elif self.state.kenny and message.author in self.state.kenny_hit_list[:self.state.num_targets]:
                        await message.author.dm_channel.send('You may not vote while being targeted by Kenny!')
                    else:
                        await message.author.dm_channel.send('You\'ve already voted!')

            # Expedition phase
            elif self.state.status == 'expedition decision':
                if message.author in self.state.expedition_squad:
                    if message.author not in list(map(lambda x: x[0], self.state.expedition_result)):
                        if response.startswith('y'):
                            self.state.expedition_result.append([message.author, 'yes'])
                            if message.author in list(map(lambda x: x[0], list(filter(lambda x: x[1] in self.state.warrior_roles, self.state.players)))):
                                embed_colour = 0xFFF700
                            else:
                                embed_colour = 0x2EFF00
                            await message.author.dm_channel.send(embed=discord.Embed(description='Response recorded!', colour=embed_colour))

                        elif response.startswith('n'):
                            # Warriors only
                            if message.author in list(map(lambda x: x[0], list(filter(lambda x: x[1] in self.state.warrior_roles, self.state.players)))):
                                self.state.expedition_result.append([message.author, 'no'])
                                await message.author.dm_channel.send(embed=discord.Embed(description='Response recorded!', colour=0xFFF700))
                            else:
                                await message.author.dm_channel.send('Only a Warrior may sabotage the expedition!')

                        elif response.startswith('s'):
                            # Ackerman only
                            if message.author in list(map(lambda x: x[0], list(filter(lambda x: x[1] == 'ackerman', self.state.players)))):
                                if self.state.wall_secured == False:
                                    self.state.wall_secured = True
                                    self.state.expedition_result.append([message.author, 'secure'])
                                    await message.author.dm_channel.send(embed=discord.Embed(description='Response recorded!', colour=0x2EFF00))
                                else:
                                    await message.author.dm_channel.send('You have already used your ability to secure the Walls!')
                            else:
                                await message.author.dm_channel.send('Only an Ackerman may secure the Walls!')

                        elif response in ['1','2','3','4','5']:
                            # Hunter only
                            if message.author in list(map(lambda x: x[0], list(filter(lambda x: x[1] == 'hunter', self.state.players)))):
                                if self.state.hunter_used == False:
                                    hunter_msg = self.state.track_person(message.author, response)
                                    if hunter_msg.startswith('Response recorded!'):
                                        self.state.expedition_result.append([message.author, 'yes'])
                                        await message.author.dm_channel.send(embed=discord.Embed(description=hunter_msg, colour=0x2EFF00))
                                    else:
                                        await message.author.dm_channel.send(hunter_msg)
                                else:
                                    await message.author.dm_channel.send('You have already used your tracking ability!')
                            else:
                                await message.author.dm_channel.send('Only a Hunter may track people!')

                        expedition_decision_status = self.state.decision_players()
                        self.state.message_box.append(await self.state.game_channel.send(embed=expedition_decision_status))
                        # Delete previous decision messages
                        if len(self.state.message_box) > 1:
                            for _ in range(len(self.state.message_box) - 1):
                                delete_msg = self.state.message_box.pop(0)
                                await delete_msg.delete()

                        # Go to result after everyone has voted
                        if len(self.state.expedition_result) == len(self.state.expedition_squad):
                            if self.state.status != 'expedition decision':
                                pass
                            else:
                                self.state.status = 'awaiting result'
                                self.state.message_box = []
                                if self.state.scout_in_expedition():
                                    await self.state.game_channel.send('💫 A flare has been fired by the **Scout**! 💫')
                                await self.state.game_channel.send('Type `~result` to see the results of the expedition!')
                    else:
                        await message.author.dm_channel.send('You\'ve already made your decision!')
                else:
                    await message.author.dm_channel.send('You are not on the expedition team!')

        # Channel messages
        else:
            # Lobby commands
            if message.content.startswith('~host'):
                # Hosts a new game if status is 'waiting for game', i.e. after a reset or a game just ended
                messagebox = message.content.split(' ')
                fast, ranked = False, True
                if len(messagebox) >= 2:
                    if 'fast' in [word.lower() for word in messagebox]:
                        fast = True
                    if 'casual' in [word.lower() for word in messagebox]:
                        ranked = False
                
                msg = self.state.host(message.author, message.guild, fast, ranked)
                await message.channel.send(msg)
                if 'has started' in msg:
                    lobby = self.state.display_lobby()
                    self.state.message_box.append(await message.channel.send(embed=lobby))
                    # Delete previous lobby messages
                    if len(self.state.message_box) > 1:
                        for _ in range(len(self.state.message_box) - 1):
                            delete_msg = self.state.message_box.pop(0)
                            await delete_msg.delete()

            if message.content.startswith('~join'):
                # Joins an open lobby (status is 'waiting for players') if not full
                msg = self.state.join(message.author, message.guild)
                await message.channel.send(msg)
                if '**' in msg:
                    lobby = self.state.display_lobby()
                    self.state.message_box.append(await message.channel.send(embed=lobby))
                    # Delete previous lobby messages
                    if len(self.state.message_box) > 1:
                        for _ in range(len(self.state.message_box) - 1):
                            delete_msg = self.state.message_box.pop(0)
                            await delete_msg.delete()

            if message.content.startswith('~leave'):
                # Leaves an open lobby
                msg = self.state.leave(message.author)
                await message.channel.send(msg)
                if msg.startswith('**') and len(self.state.players) >= 1:
                    lobby = self.state.display_lobby()
                    self.state.message_box.append(await message.channel.send(embed=lobby))
                    # Delete previous lobby messages
                    if len(self.state.message_box) > 1:
                        for _ in range(len(self.state.message_box) - 1):
                            delete_msg = self.state.message_box.pop(0)
                            await delete_msg.delete()

            if message.content.startswith('~kick'):
                # (Host only) Removes a player from the lobby
                messagebox = message.content.split(' ')
                if message.mentions:
                    player_profile = message.mentions[0]
                    kick_msg = self.state.kick(message.author, player_profile)
                    await message.channel.send(kick_msg)
                    if 'removed from the lobby' in kick_msg and len(self.state.players) >= 1:
                        lobby = self.state.display_lobby()
                        self.state.message_box.append(await message.channel.send(embed=lobby))
                        # Delete previous lobby messages
                        if len(self.state.message_box) > 1:
                            for _ in range(len(self.state.message_box) - 1):
                                delete_msg = self.state.message_box.pop(0)
                                await delete_msg.delete()
                else:
                    await message.channel.send('Please specify a player to kick!')

            if message.content.startswith('~add') or message.content.startswith('~remove'):
                # Adds or removes an optional role
                messagebox = message.content.split(' ')
                if len(messagebox) >= 2:
                    newrole = ' '.join(messagebox[1:]).lower()
                    if message.content.startswith('~add'):
                        if message.mentions and message.mentions[0].id == 188226672279945216:
                            newrole = 'mike'
                        rolemsg = self.state.addrole(newrole, message.author)
                    else:
                        if message.mentions and message.mentions[0].id == 188226672279945216:
                            newrole = 'mike'
                        rolemsg = self.state.removerole(newrole, message.author)
                    await message.channel.send(rolemsg)
                    if 'has been' in rolemsg:
                        lobby = self.state.display_lobby()
                        self.state.message_box.append(await message.channel.send(embed=lobby))
                        # Delete previous lobby messages
                        if len(self.state.message_box) > 1:
                            for _ in range(len(self.state.message_box) - 1):
                                delete_msg = self.state.message_box.pop(0)
                                await delete_msg.delete()
                else:
                    await message.channel.send('Please specify a role to add or remove! E.g. `~add queen`')

            if message.content.lower().startswith('~randomroles') or message.content.lower().startswith('~random roles'):
                randomroles_msg = self.state.toggle_randomroles(message.author)
                await message.channel.send(randomroles_msg)
                if 'have been' in randomroles_msg:
                    lobby = self.state.display_lobby()
                    self.state.message_box.append(await message.channel.send(embed=lobby))
                    # Delete previous lobby messages
                    if len(self.state.message_box) > 1:
                        for _ in range(len(self.state.message_box) - 1):
                            delete_msg = self.state.message_box.pop(0)
                            await delete_msg.delete()
            
            if message.content.lower().startswith('~fast') or message.content.lower().startswith('~normal') or message.content.lower().startswith('~casual') or message.content.lower().startswith('~ranked'):
                if message.content.lower().startswith('~fast'):
                    msg = self.state.toggle_gametype(message.author, 'fast')
                elif message.content.lower().startswith('~normal'):
                    msg = self.state.toggle_gametype(message.author, 'normal')
                elif message.content.lower().startswith('~casual'):
                    msg = self.state.toggle_gametype(message.author, 'casual')
                elif message.content.lower().startswith('~ranked'):
                    msg = self.state.toggle_gametype(message.author, 'ranked')
                await message.channel.send(msg)
                if 'has been' in msg:
                    lobby = self.state.display_lobby()
                    self.state.message_box.append(await message.channel.send(embed=lobby))
                    # Delete previous lobby messages
                    if len(self.state.message_box) > 1:
                        for _ in range(len(self.state.message_box) - 1):
                            delete_msg = self.state.message_box.pop(0)
                            await delete_msg.delete()

            if message.content.startswith('~start'):
                # Only the host can start the game
                start_msg = self.state.start(message.author)
                await message.channel.send(start_msg)

                if start_msg.startswith('Starting game'):
                    self.state.game_channel = message.channel
                    self.reset_timers()
                    await asyncio.sleep(1)
                    await message.channel.send(embed=self.state.get_status())
                    await asyncio.sleep(2)
                    if self.state.randomroles:
                        await message.channel.send(embed=self.state.get_player_role())

                    # Tells players their roles
                    await message.channel.send(self.state.start_msg)
                    await asyncio.sleep(1)
                    for player in self.state.players:
                        if not player[0].dm_channel:
                            await player[0].create_dm()
                        role_msg = self.state.get_role_msg(player)
                        await asyncio.sleep(0.1)
                        try:
                            await player[0].dm_channel.send(embed=role_msg)
                        except:
                            private_dms_msg = player[0].mention + ', you have disabled DMs from server members! ' + \
                            'As a result, I am unable to DM to you your role.\n\n' + \
                            'Please enable DMs from server members, then type `~role` to receive your role.'
                            await message.channel.send(private_dms_msg)
                    await asyncio.sleep(1)
                    await message.channel.send(self.state.get_roles_assigned_msg())

                    if 'saboteur' in self.state.newroles:
                        saboteur_player, saboteur_embed = self.state.get_saboteur_msg()
                        await saboteur_player.dm_channel.send(embed=saboteur_embed)

            # In-game commands
            if message.content.startswith('~reset'):
                # Only the host (or a mod) can reset the game
                msg = self.state.reset(message.author)
                if type(msg) == str:
                    await message.channel.send(msg)
                else:
                    self.reset_timers()

                    await message.channel.send(embed=msg)

            if message.content.startswith('~intro'):
                await message.channel.send(embed=self.state.intro_msg)

            # Check your own role
            if message.content == '~role':
                if not message.author.dm_channel:
                    await message.author.create_dm()
                player_role = self.state.get_player_role(message.author)
                if type(player_role) != str:
                    try:
                        await message.author.dm_channel.send(embed=player_role)
                    except:
                        private_dms_role_msg = message.author.mention + ', you have disabled DMs from server members! ' + \
                        'As a result, I am unable to send you your role.\n\n' + \
                        'Please enable DMs from server members to participate in the game.'
                        await message.channel.send(private_dms_role_msg)
                else:
                    await message.channel.send(player_role)

            # Check roles currently in the game
            if message.content.startswith('~roles'):
                player_roles = self.state.get_player_role()
                if type(player_roles) == str:
                    await message.channel.send(player_roles)
                else:
                    await message.channel.send(embed=player_roles)

            # Checks the advantage of the current game or lobby
            if message.content.startswith('~advantage'):
                advantage_value = self.state.calculate_advantage()
                advantage_embed = discord.Embed(title = 'Advantage', description = '⚖️ **Perfectly balanced!** ⚖️' if advantage_value == '**None**' else advantage_value, colour=0xF9FF41)
                await message.channel.send(embed=advantage_embed)

            if message.content.startswith('~next'):
                # Begin next expedition, commander to pick team
                if (message.author in list(map(lambda x:x[0], self.state.players)) or message.author.id == 238808836075421697):
                    if (self.state.status == 'assigning roles' or self.state.status == 'expedition over'):
                        # Reset timers at the start of each expedition
                        self.reset_timers()

                        if self.state.paths:
                            self.state.status = 'paths announcement'

                            paths_msg = '📢 The power of the Paths now has a new owner! 📢'
                            await message.channel.send(paths_msg)
                            await asyncio.sleep(1)
                            paths_msg2 = '**Paths Holder**, please make your announcement to the world.'
                            await message.channel.send(paths_msg2)

                            paths_holder_msg = '📢You are the **Paths Holder**!📢\n\nType in the message you wish to send to the world now.'
                            if not self.state.paths_holders[0].dm_channel:
                                await self.state.paths_holders[0].create_dm()
                            try:
                                await self.state.paths_holders[0].dm_channel.send(embed=discord.Embed(description=paths_holder_msg, colour=0x4B4B4B))
                            except:
                                print("Error: User cannot receive DM")

                        else:
                            self.state.status = 'expedition selection'

                            expedition_msg = '--**Expedition #' + \
                                str(self.state.cur_expedition) + ': Planning phase**--'
                            await message.channel.send(expedition_msg)
                            await asyncio.sleep(2)
                            self.state.next_commander()
                            commander_msg = 'The commander for this expedition is **' + \
                                self.state.players[0][0].mention + '**!'
                            await message.channel.send(commander_msg)

                            await asyncio.sleep(2)
                            players_msg = self.state.get_players()
                            await message.channel.send(embed=players_msg)

                            if self.state.kenny:
                                await asyncio.sleep(2)
                                kenny_hit_list_msg = self.state.get_kenny_hit_list()
                                await message.channel.send(embed=kenny_hit_list_msg)

                            await asyncio.sleep(2)
                            commander_msg2 = 'Commander **' + \
                                self.state.players[0][0].name + \
                                '**, please select your team for the expedition. (Type `~pick <@name>` to pick a team member.)'
                            await message.channel.send(commander_msg2)
                else:
                    await message.channel.send('You may only start the next expedition if you are in the game!')

            if message.content.startswith('~check'):
                if self.state.status == 'ymir\'s blessing':
                    if message.author == self.state.currently_blessed:
                        if message.mentions:
                            player_obj = message.mentions[0]
                            if player_obj in list(map(lambda x: x[0], self.state.players)):
                                if player_obj not in self.state.blessed:
                                    if player_obj != message.author:
                                        await message.channel.send(message.author.mention + ' has invoked Ymir\'s blessing!')
                                        await asyncio.sleep(1)
                                        blessing_msg = '**' + player_obj.name + '** is fighting on the side of the ' + self.state.get_player_allegiance(player_obj)
                                        blessing_embed = discord.Embed(title='🔮**Ymir\'s Blessing**🔮\n\n', description=blessing_msg, colour=0x9B00D9)
                                        try:
                                            await message.author.dm_channel.send(embed=blessing_embed)
                                            await asyncio.sleep(1)
                                            await message.channel.send('**' + message.author.name + '** now knows **' + player_obj.name + '**\'s true allegiance!')
                                        except:
                                            private_dms_blessing_msg = message.author.mention + ', you have disabled DMs from server members! ' + \
                                            'As a result, I am unable to send you the information.\n\n' + \
                                            'Please enable DMs from server members to participate in the game.'
                                            await message.channel.send(private_dms_blessing_msg)

                                        self.state.status = 'expedition over'
                                        self.state.blessed.append(message.author)
                                        self.state.currently_blessed = player_obj

                                        next_expedition_msg = 'When everyone is ready, type `~next` to begin the next expedition.'
                                        await asyncio.sleep(2)
                                        await message.channel.send(next_expedition_msg)

                                    else:
                                        await message.channel.send('You already know your own allegiance!')
                                else:
                                    await message.channel.send('**' + player_obj.name + '** has been blessed by Ymir previously and is now immune to it! Choose someone else.')
                            else:
                                await message.channel.send('**' + player_obj.name + '** is not in the game!')
                        else:
                            await message.channel.send('Please pick someone to check their allegiance!')
                    else:
                        await message.channel.send('You do not have Ymir\'s blessing!')
                else:
                    await message.channel.send('Ymir\'s blessing is currently not active!')

            if message.content.startswith('~pick'):
                # For commander to pick the expedition team
                if self.state.status == 'expedition selection':
                    if message.author == self.state.players[0][0]:
                        if message.mentions:
                            player_obj = message.mentions[0]
                            selection_msg = self.state.pick(player_obj)
                            await message.channel.send(selection_msg)

                            if 'has joined' in selection_msg:
                                selection_state = self.state.selection_players()
                                self.state.message_box.append(await message.channel.send(embed=selection_state))
                                # Delete previous selection messages
                                if len(self.state.message_box) > 1:
                                    for _ in range(len(self.state.message_box) - 1):
                                        delete_msg = self.state.message_box.pop(0)
                                        await delete_msg.delete()

                            # Enough people: move to approval phase
                            if len(self.state.expedition_squad) == self.state.get_expedition_size():
                                approval_start = self.state.begin_approval_phase()
                                await asyncio.sleep(2)
                                await message.channel.send(approval_start)
                                await asyncio.sleep(1)
                                await message.channel.send('Receiving votes...')

                                for player in self.state.kenny_hit_list[:self.state.num_targets]:
                                    self.state.expedition_approval.append([player, 'none'])

                                for player in list(map(lambda x: x[0], self.state.players)):
                                    if not player.dm_channel:
                                        await player.create_dm()
                                    approval_msg = self.state.get_expedition_approval_msg(player)
                                    try:
                                        await player.dm_channel.send(embed=approval_msg)
                                    except:
                                        private_dms_approval_msg = player.mention + ', you have disabled DMs from server members! ' + \
                                        'As a result, I am unable to process your vote.\n\n' + \
                                        'Please enable DMs from server members to participate in the game.'
                                        await message.channel.send(private_dms_approval_msg)
                                    await asyncio.sleep(0.1)
                        else:
                            await message.channel.send('Please pick someone for the expedition team!')
                    else:
                        await message.channel.send('You are not the Commander!')
                else:
                    await message.channel.send('You may only pick an expedition team during the selection phase of an expedition!')

            if message.content.startswith('~result') and self.state.status == 'awaiting result':
                if self.state.status != 'awaiting result':
                    # In case 2 people type at the same time
                    pass
                else:
                    # Display result
                    expedition_result = self.state.get_expedition_result()
                    await message.channel.send(embed=expedition_result)

                    # Check if expedition is a success or not
                    expedition_success = self.state.test_expedition_success()

                    # Inform all warriors inside expedition of the identity of the Ackerman if the Ackerman secures wall
                    if 'secure' in list(map(lambda x: x[1], self.state.expedition_result)):
                        for warrior in list(filter(lambda x: x in self.state.expedition_squad, list(map(lambda x: x[0], list(filter(lambda x: x[1] in self.state.warrior_roles, self.state.players)))))):
                            ackerman_name = list(filter(lambda x: x[1] == 'ackerman', self.state.players))[
                                0][0].name
                            try:
                                await warrior.dm_channel.send(embed=discord.Embed(description='🛡 The Ackerman, **' + ackerman_name + '**, has prevented you from destroying the Walls!', colour=0x00C9FF))
                            except:
                                print("Error: User cannot receive DM")

                    if self.state.funds_enabled:
                        self.state.funds = 5

                    if expedition_success == True:
                        result_msg = self.state.expedition_success_update()
                        await asyncio.sleep(2)
                        await message.channel.send(result_msg)

                        if self.state.hunter_target != None:
                            hunter_expose_msg = self.state.test_hunter_target()
                            self.state.hunter_target = None
                            if hunter_expose_msg:
                                await asyncio.sleep(2)
                                await message.channel.send(hunter_expose_msg)

                        self.state.expedition_result = []
                        status = self.state.get_status()
                        await asyncio.sleep(2)
                        await message.channel.send(embed=status)

                        if self.state.successful_expeditions == 3:
                            basement_msg = self.state.reach_basement()
                            await asyncio.sleep(1)
                            await message.channel.send(basement_msg)
                        else:
                            if self.state.ymir_blessing == True and self.state.cur_expedition >= 3:
                                self.state.status = 'ymir\'s blessing'
                                blessing_msg = self.state.get_ymir_blessing()
                                await asyncio.sleep(2)
                                await message.channel.send(blessing_msg)
                                await asyncio.sleep(2)
                                await message.channel.send('**' + self.state.currently_blessed.name + '**, please select a player to check their allegiance. (Type `~check <@person>` to pick a person)')

                            else:
                                self.state.status = 'expedition over'
                                next_expedition_msg = 'When everyone is ready, type `~next` to begin the next expedition.'
                                await asyncio.sleep(2)
                                await message.channel.send(next_expedition_msg)

                    elif expedition_success == False:
                        result_msg = self.state.expedition_failure_update()
                        await asyncio.sleep(2)
                        await message.channel.send(result_msg)

                        if self.state.hunter_target != None:
                            hunter_expose_msg = self.state.test_hunter_target()
                            self.state.hunter_target = None
                            if hunter_expose_msg:
                                await asyncio.sleep(2)
                                await message.channel.send(hunter_expose_msg)

                        self.state.expedition_result = []
                        status = self.state.get_status()
                        await asyncio.sleep(2)
                        await message.channel.send(embed=status)

                        if self.state.walls_destroyed == 3:
                            self.state.status = 'game ended warriors wall'
                            warriors_win_msg = '⚔All the Walls have been destroyed and humanity has been wiped out. Warriors win!⚔'
                            await message.channel.send(warriors_win_msg)
                            end_summary = self.state.get_summary()
                            await asyncio.sleep(2)
                            await message.channel.send(embed=end_summary)

                            if self.state.gametype == 'Ranked':
                                rating_changes = self.state.update_rating()
                                achievements_msgs = self.state.update_achievements()
                                # Update roles in official WvS server
                                try:
                                    for player in self.state.players:
                                        await self.state.update_role(player[0], self.client)
                                    await self.state.update_top_roles(self.client)
                                except Exception as e:
                                    print(e)
                                await asyncio.sleep(2)
                                await message.channel.send(embed=rating_changes)
                                for achievements_msg in achievements_msgs:
                                    await message.channel.send(achievements_msg)

                            self.state.status = 'game ended'

                        else:
                            if self.state.ymir_blessing == True and self.state.cur_expedition >= 3:
                                self.state.status = 'ymir\'s blessing'
                                blessing_msg = self.state.get_ymir_blessing()
                                await asyncio.sleep(2)
                                await message.channel.send(blessing_msg)
                                await asyncio.sleep(2)
                                await message.channel.send('**' + self.state.currently_blessed.name + '**, please select a player to check their allegiance. (Type `~check <@person>` to pick a person)')

                            else:
                                self.state.status = 'expedition over'
                                next_expedition_msg = 'When everyone is ready, type `~next` to begin the next expedition.'
                                await asyncio.sleep(2)
                                await message.channel.send(next_expedition_msg)

            if message.content.lower().startswith('~kidnap'):
                # When warriors try to identify coordinate at the end
                if self.state.status == 'choose coordinate':
                    if message.author in list(map(lambda x: x[0], list(filter(lambda x: x[1] in self.state.warrior_roles, self.state.players)))):
                        if message.mentions:
                            player_obj = message.mentions[0]
                            if player_obj in list(map(lambda x: x[0], self.state.players)):
                                if player_obj in list(filter(lambda x: x[1] == 'coordinate', self.state.players))[0]:
                                    self.state.status = 'game ended warriors coord'
                                    warriors_win = '⚔The Warriors have correctly identified the Coordinate, **' + \
                                        player_obj.name + '**! Warriors win!⚔'
                                    await message.channel.send(warriors_win)
                                else:
                                    self.state.status = 'game ended soldiers'
                                    soldiers_win = '🛡The Warriors did not manage to identify the Coordinate. Soldiers win!🛡'
                                    await message.channel.send(soldiers_win)

                                end_summary = self.state.get_summary()
                                await asyncio.sleep(2)
                                await message.channel.send(embed=end_summary)

                                if self.state.gametype == 'Ranked':
                                    rating_changes = self.state.update_rating()
                                    achievements_msgs = self.state.update_achievements()
                                    # Update roles in official WvS server
                                    try:
                                        for player in self.state.players:
                                            await self.state.update_role(player[0], self.client)
                                        await self.state.update_top_roles(self.client)
                                    except Exception as e:
                                        print(e)
                                    await asyncio.sleep(2)
                                    await message.channel.send(embed=rating_changes)
                                    for achievements_msg in achievements_msgs:
                                        await message.channel.send(achievements_msg)

                                self.state.status = 'game ended'

                            else:
                                await message.channel.send('**' + player_obj.name + '** is not in the game!')
                    else:
                        await message.channel.send('Only Warriors are allowed to kidnap people!')
                else:
                    await message.channel.send('You\'re not allowed to kidnap anyone yet!')

            if message.content.startswith('~summary') and message.author.id == 238808836075421697:
                end_summary = self.state.get_summary()
                await message.delete()
                await message.author.dm_channel.send(embed=end_summary)

            if message.content.startswith('~status'):
                # Brings up the game status, containing number of players, current round, and graphics for status of expeditions and walls
                status = self.state.get_status()
                if status != None:
                    await message.channel.send(embed=status)
                await message.channel.send('Current game state: `' + self.state.status + '`')

            if message.content.startswith('~players'):
                # Brings up the player list (tags all players in the game), along with their position in the queue to be commander (special emoji (prob crown) for player who is commander)
                players = self.state.get_players()
                if players != None:
                    await message.channel.send(embed=players)
                else:
                    await message.channel.send('There is no open lobby at the moment!')

            if message.content.startswith('~profile') or message.content == '~rank':
                messagebox = message.content.split(' ')
                if message.mentions:
                    player_profile = message.mentions[0]
                else:
                    player_profile = message.author
                profile = self.state.get_profile(player_profile, message.guild)
                await message.channel.send(embed=profile)

            if message.content.startswith('~badges') or message.content.startswith('~achievements'):
                messagebox = message.content.split(' ') 
                if message.mentions:
                    player_profile = message.mentions[0]
                else:
                    player_profile = message.author
                badges = self.state.get_achievements(player_profile)
                await message.channel.send(embed=badges)

            if message.content.startswith('~leaderboard') or message.content.startswith('~lb'):
                messagebox = message.content.split(' ')
                if 'g' in messagebox or 'global' in messagebox:
                    all_servers = True
                else:
                    all_servers = False

                if len(messagebox) == 1 and all_servers == False or len(messagebox) == 2 and all_servers == True:
                    leaderboard, cur_page = self.state.get_leaderboard(message.guild, all_servers=all_servers)
                elif message.mentions:
                    player_profile = message.mentions[0]
                    leaderboard, cur_page = self.state.get_leaderboard(message.guild, player=player_profile, all_servers=all_servers)
                else:
                    page_no = messagebox[1] if all_servers == False else messagebox[2]
                    leaderboard, cur_page = self.state.get_leaderboard(message.guild, page=page_no, all_servers=all_servers)
                leaderboard_msg = await message.channel.send(embed=leaderboard)

                def reaction_check(reaction, user):
                    return user != self.client.user and (reaction.emoji == '▶' or reaction.emoji == '◀') and (reaction.message.id == leaderboard_msg.id)

                await leaderboard_msg.add_reaction('◀')
                await leaderboard_msg.add_reaction('▶')

                while True:
                    rxn, user = await self.client.wait_for('reaction_add', check = reaction_check)

                    if rxn.emoji == '▶':
                        cur_page += 1
                    elif rxn.emoji == '◀':
                        cur_page -= 1

                    leaderboard, cur_page = self.state.get_leaderboard(message.guild, page=cur_page, all_servers=all_servers)
                    await leaderboard_msg.edit(embed=leaderboard)
                    await rxn.remove(user)
                    await asyncio.sleep(0.1)

            if message.content.startswith('~stats') or message.content.startswith('~gamestats'):
                cur_stat_page = 1
                game_stats_msg = await message.channel.send(embed=self.state.get_game_stats(cur_stat_page, message.guild))
                stats_emojis = {1:'1️⃣', 2:'2️⃣', 3:'3️⃣', 4:'4️⃣'}
                stats_emojis_rev = {'1️⃣':1, '2️⃣':2, '3️⃣':3, '4️⃣':4}
                for emoji in stats_emojis_rev:
                    await game_stats_msg.add_reaction(emoji)

                def reaction_check(reaction, user):
                    return user != self.client.user and (reaction.emoji in stats_emojis_rev) and (reaction.message.id == game_stats_msg.id)

                while True:
                    rxn, user = await self.client.wait_for('reaction_add', check = reaction_check)

                    if rxn.emoji != stats_emojis[cur_stat_page]:
                        cur_stat_page = stats_emojis_rev[rxn.emoji]
                        await game_stats_msg.edit(embed=self.state.get_game_stats(cur_stat_page, message.guild))
                        await rxn.remove(user)
                            
                    await asyncio.sleep(0.1)

            if message.content.startswith('~help') or message.content.startswith('~info'):
                helpbox = message.content.split(' ')
                if len(helpbox) == 1:
                    # For list of commands
                    commands = self.state.get_commands()
                    await message.channel.send(embed=commands)
                else:
                    arguments = ' '.join(helpbox[1:]).lower()
                    # Help commands here
                    command_help = self.state.get_commands(arguments)
                    if command_help:
                        await message.channel.send(embed=command_help)

            if message.content.startswith('~commands'):
                commands = self.state.get_commands()
                await message.channel.send(embed=commands)

            if message.content.startswith('~tutorial') or message.content.startswith('~rules'):
                # For a detailed explanation of the game
                cur_tutorial = 1
                tutorial, tutorial_embed, cur_tutorial = self.state.tutorial(1)
                tutorial_msg = await message.channel.send(content=tutorial, embed=tutorial_embed)
                await tutorial_msg.add_reaction('◀')
                await tutorial_msg.add_reaction('▶')

                def reaction_check(reaction, user):
                    return user != self.client.user and (reaction.emoji == '▶' or reaction.emoji == '◀') and (reaction.message.id == tutorial_msg.id)

                while True:
                    rxn, user = await self.client.wait_for('reaction_add', check = reaction_check)

                    if rxn.emoji == '▶':
                        cur_tutorial += 1
                    elif rxn.emoji == '◀':
                        cur_tutorial -= 1

                    tutorial, tutorial_embed, cur_tutorial = self.state.tutorial(cur_tutorial)
                    await tutorial_msg.edit(content=tutorial, embed=tutorial_embed)
                    await rxn.remove(user)
                    await asyncio.sleep(0.1)

            if message.content.startswith('~award'):
                if message.mentions and message.author.id == 238808836075421697:
                    sr_awarded = int(message.content.split(' ')[-1])
                    player_profile = message.mentions[0]
                    award_msg = self.state.award_sr(player_profile, sr_awarded)
                    await message.channel.send(award_msg)

            # Testing command
            if message.content.startswith('~test') and message.author.id == 238808836075421697:
                server = self.client.get_guild(748080644340318299)
                print('Server:', server)
                for member in server.members:
                    print('Member:', member)

                # status.add_field(name = '\u200B', value='test')
                # status.set_image(url='https://cdn.discordapp.com/attachments/266949919821135872/748958842087538748/annie_vs_kenneeh.PNG')
                # status.set_thumbnail(url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/shield_1f6e1.png')
#                 status = discord.Embed(title='⚔ Warrior ⚔', description=role_msg, colour=0xB23E00)
#                 status.set_thumbnail(url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/crossed-swords_2694.png')
                # await message.channel.send(embed=status)

    def reset_timers(self):
        self.approval_timer_obj.cancel()
        self.decision_timer_obj.cancel()
        self.selection_timer_obj.cancel()
        self.next_expedition_timer_obj.cancel()
        self.blessing_timer_obj.cancel()
        self.paths_timer_obj.cancel()
        self.kidnap_timer_obj.cancel()
        self.saboteur_timer_obj.cancel()

        self.approval_timer_obj = self.client.loop.create_task(self.approval_timer())
        self.decision_timer_obj = self.client.loop.create_task(self.decision_timer())
        self.selection_timer_obj = self.client.loop.create_task(self.selection_timer())
        self.next_expedition_timer_obj = self.client.loop.create_task(self.next_expedition_timer())
        self.blessing_timer_obj = self.client.loop.create_task(self.blessing_timer())
        self.paths_timer_obj = self.client.loop.create_task(self.paths_timer())
        self.saboteur_timer_obj = self.client.loop.create_task(self.saboteur_timer())
        self.kidnap_timer_obj = self.client.loop.create_task(self.kidnap_timer())

    async def next_expedition_timer(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(1)
            if self.state.status == 'assigning roles' or self.state.status == 'expedition over':
                timer = 0
                while self.state.status == 'assigning roles' or self.state.status == 'expedition over':
                    await asyncio.sleep(1)
                    timer += 1
                    if (self.state.gamespeed == 'Normal' and timer == 540 and (self.state.status == 'assigning roles' or self.state.status == 'expedition over')) or \
                    (self.state.gamespeed == 'Fast' and timer == 120 and (self.state.status == 'assigning roles' or self.state.status == 'expedition over')):
                        timer_msg = self.state.game_host.mention + ', you have **60 seconds** to start the next expedition!'
                        await self.state.game_channel.send(timer_msg)

                    if self.state.gamespeed == 'Fast' and timer == 150 and (self.state.status == 'assigning roles' or self.state.status == 'expedition over'):
                        timer_msg = self.state.game_host.mention + ', you have **30 seconds** to start the next expedition!'
                        await self.state.game_channel.send(timer_msg)

                    if (self.state.gamespeed == 'Normal' and timer >= 600 and (self.state.status == 'assigning roles' or self.state.status == 'expedition over')) or \
                    (self.state.gamespeed == 'Fast' and timer >= 180 and (self.state.status == 'assigning roles' or self.state.status == 'expedition over')):
                        times_up_msg = '**' + self.state.game_host.name + \
                            '** did not manage to start the next expedition in time! Resetting game...'
                        await self.state.game_channel.send(times_up_msg)
                        self.state.reset_confirmation = True
                        msg = self.state.reset(self.state.game_host)
                        await self.state.game_channel.send(embed=msg)

    async def approval_timer(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(1)
            if self.state.status == 'expedition approval':
                timer = 0
                while self.state.status == 'expedition approval':
                    await asyncio.sleep(1)
                    timer += 1
                    if self.state.gamespeed == 'Normal' and timer == 30 and self.state.status == 'expedition approval':
                        await self.state.game_channel.send('Participants have **30 seconds** to cast their votes!')
                    if (self.state.gamespeed == 'Normal' and timer >= 60 and self.state.status == 'expedition approval') or \
                    (self.state.gamespeed == 'Fast' and timer >= 30 and self.state.status == 'expedition approval'):
                        self.state.status = ''
                        await self.state.game_channel.send('Time\'s up! Approving the remaining votes...')
                        # Add remaining players into expedition approval ('yes' by default)
                        self.state.approval_add_remainder()

                        # Then proceed as before: with everyone having voted
                        if self.state.message_box:
                            await self.state.message_box[0].delete()
                        self.state.message_box = []

                        if self.state.flipping_votes:
                            self.state.flip_votes()
                            await self.state.game_channel.send('🔄 The votes have been flipped by the Spy! 🔄')

                        expedition_approval_result = self.state.get_approval_result()
                        await self.state.game_channel.send(embed=expedition_approval_result)

                        # Go decision phase if vote passes, or back to selection phase otherwise
                        if len(list(filter(lambda x: x[1] == 'yes', self.state.expedition_approval))) > 0.5 * (len(self.state.expedition_approval) - self.state.num_targets):
                            self.state.expedition_approval = []
                            await self.state.game_channel.send('The proposal has passed!')

                            expedition_msg = '--**Expedition #' + \
                                str(self.state.cur_expedition) + ': Action phase**--'
                            await asyncio.sleep(2)
                            await self.state.game_channel.send(expedition_msg)

                            decision_intro = 'Expedition members, please decide what you\'ll do during the expedition!'
                            await asyncio.sleep(2)
                            await self.state.game_channel.send(decision_intro)

                            for person in self.state.expedition_squad:
                                decision_msg = self.state.get_decision_msg(person)
                                try:
                                    await person.dm_channel.send(embed=decision_msg)
                                except:
                                    private_dms_decision_msg = person.mention + ', you have disabled DMs from server members! ' + \
                                    'As a result, I am unable to process your decision.\n\n' + \
                                    'Please enable DMs from server members to participate in the game.'
                                    await self.state.game_channel.send(private_dms_decision_msg)
                                await asyncio.sleep(0.1)

                            self.state.status = 'expedition decision'

                        else:
                            self.state.expedition_approval = []
                            self.state.expedition_squad = []
                            self.state.status = 'expedition selection'

                            await self.state.game_channel.send('The proposal has failed!')

                            if self.state.funds_enabled:
                                self.state.funds -= 1
                                status = self.state.get_status()
                                await asyncio.sleep(2)
                                await self.state.game_channel.send(embed=status)
                                if self.state.funds == 1:
                                    await self.state.game_channel.send('❗| The Soldiers have funds for only **1** more proposal!')
                                elif self.state.funds == 0:
                                    self.state.status = 'game ended warriors wall'
                                    warriors_win_msg = '⚔The Soldiers have run out of funds for further expeditions. Warriors win!⚔'
                                    await asyncio.sleep(2)
                                    await self.state.game_channel.send(warriors_win_msg)

                                    end_summary = self.state.get_summary()
                                    await asyncio.sleep(2)
                                    await self.state.game_channel.send(embed=end_summary)

                                    if self.state.gametype == 'Ranked':
                                        rating_changes = self.state.update_rating()
                                        achievements_msgs = self.state.update_achievements()
                                        # Update roles in official WvS server
                                        for player in self.state.players:
                                            await self.state.update_role(player[0], self.client)
                                        await self.state.update_top_roles(self.client)
                                        await asyncio.sleep(2)
                                        await self.state.game_channel.send(embed=rating_changes)
                                        for achievements_msg in achievements_msgs:
                                            await self.state.game_channel.send(achievements_msg)

                                    self.state.status = 'game ended'

                            if not self.state.status == 'game ended':
                                expedition_msg = '--**Expedition #' + \
                                    str(self.state.cur_expedition) + ': Planning phase**--'
                                await asyncio.sleep(2)
                                await self.state.game_channel.send(expedition_msg)

                                await asyncio.sleep(2)
                                self.state.next_commander()
                                commander_msg = 'The commander for this expedition is ' + \
                                    self.state.players[0][0].mention + '!'
                                await self.state.game_channel.send(commander_msg)

                                await asyncio.sleep(2)
                                players_msg = self.state.get_players()
                                await self.state.game_channel.send(embed=players_msg)

                                if self.state.kenny:
                                    await asyncio.sleep(2)
                                    kenny_hit_list_msg = self.state.get_kenny_hit_list()
                                    await self.state.game_channel.send(embed=kenny_hit_list_msg)

                                await asyncio.sleep(1)
                                commander_msg2 = 'Commander **' + \
                                    self.state.players[0][0].name + \
                                    '**, please select your team for the expedition. (Type `~pick <@name>` to pick a team member.)'
                                await self.state.game_channel.send(commander_msg2)

    async def decision_timer(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(1)
            if self.state.status == 'expedition decision':
                timer = 0
                while self.state.status == 'expedition decision':
                    await asyncio.sleep(1)
                    timer += 1
                    if self.state.gamespeed == 'Normal' and timer == 30 and self.state.status == 'expedition decision':
                        await self.state.game_channel.send('Expedition team members have **30 seconds** to make their decisions!')
                    if (self.state.gamespeed == 'Normal' and timer >= 60 and self.state.status == 'expedition decision') or \
                    (self.state.gamespeed == 'Fast' and timer >= 30 and self.state.status == 'expedition decision'):
                        self.state.status = ''
                        # Add remaining players into expedition decision
                        for player in self.state.expedition_squad:
                            if player not in list(map(lambda x: x[0], self.state.expedition_result)):
                                self.state.expedition_result.append([player, 'yes'])

                        expedition_decision_status = self.state.decision_players()
                        self.state.message_box.append(await self.state.game_channel.send(embed=expedition_decision_status))
                        if len(self.state.message_box) > 1:
                            for _ in range(len(self.state.message_box) - 1):
                                delete_msg = self.state.message_box.pop(0)
                                await delete_msg.delete()
                        # Then proceed as before
                        if len(self.state.expedition_result) == len(self.state.expedition_squad):
                            self.state.status = 'awaiting result'
                            self.state.message_box = []
                            if self.state.scout_in_expedition():
                                await self.state.game_channel.send('💫 A flare has been fired by the **Scout**! 💫')
                            await self.state.game_channel.send('Type `~result` to see the results of the expedition!')
                        else:
                            await self.state.game_channel.send('Something went wrong! Resetting current expedition...')

                            self.state.message_box = []
                            self.state.expedition_squad = []
                            self.state.expedition_approval = []
                            self.state.expedition_result = []

                            self.state.status = 'expedition selection'

                            # Reset timers at the start of each expedition
                            self.reset_timers()

                            expedition_msg = '--**Expedition #' + \
                                str(self.state.cur_expedition) + ': Planning phase**--'
                            await self.state.game_channel.send(expedition_msg)
                            await asyncio.sleep(2)

                            commander_msg = 'The commander for this expedition is **' + \
                                self.state.players[0][0].mention + '**!'
                            await self.state.game_channel.send(commander_msg)

                            await asyncio.sleep(2)
                            players_msg = self.state.get_players()
                            await self.state.game_channel.send(embed=players_msg)
                            
                            if self.state.kenny:
                                await asyncio.sleep(2)
                                kenny_hit_list_msg = self.state.get_kenny_hit_list()
                                await self.state.game_channel.send(embed=kenny_hit_list_msg)

                            await asyncio.sleep(1)
                            commander_msg2 = 'Commander **' + \
                                self.state.players[0][0].name + \
                                '**, please select your team for the expedition. (Type `~pick <@name>` to pick a team member.)'
                            await self.state.game_channel.send(commander_msg2)

    async def selection_timer(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(1)
            if self.state.status == 'expedition selection':
                timer = 0
                while self.state.status == 'expedition selection' and not self.client.is_closed():
                    await asyncio.sleep(1)
                    timer += 1
                    if (self.state.gamespeed == 'Normal' and timer == 240 and self.state.status == 'expedition selection') or \
                    (self.state.gamespeed == 'Fast' and timer == 60 and self.state.status == 'expedition selection'):
                        timer_msg = 'Commander ' + \
                            self.state.players[0][0].mention + \
                            ', you have **60 seconds** to pick your team!'
                        await self.state.game_channel.send(timer_msg)

                    elif self.state.gamespeed == 'Fast' and timer == 90 and self.state.status == 'expedition selection':
                        timer_msg = 'Commander ' + \
                            self.state.players[0][0].mention + \
                            ', you have **30 seconds** to pick your team!'
                        await self.state.game_channel.send(timer_msg)

                    elif (self.state.gamespeed == 'Normal' and timer >= 300 and self.state.status == 'expedition selection') or \
                    (self.state.gamespeed == 'Fast' and timer >= 120 and self.state.status == 'expedition selection'):
                        timer = 0
                        # Skip to next commander
                        self.state.expedition_squad = []
                        times_up_msg = 'Commander **' + \
                            self.state.players[0][0].name + \
                            '** did not manage to pick their team in time!'
                        await self.state.game_channel.send(times_up_msg)

                        expedition_msg = '--**Expedition #' + \
                            str(self.state.cur_expedition) + ': Planning phase**--'
                        await self.state.game_channel.send(expedition_msg)

                        await asyncio.sleep(2)
                        self.state.next_commander()
                        commander_msg = 'The commander for this expedition is ' + \
                            self.state.players[0][0].mention + '!'
                        await self.state.game_channel.send(commander_msg)

                        await asyncio.sleep(2)
                        players_msg = self.state.get_players()
                        await self.state.game_channel.send(embed=players_msg)

                        if self.state.kenny:
                            await asyncio.sleep(2)
                            kenny_hit_list_msg = self.state.get_kenny_hit_list()
                            await self.state.game_channel.send(embed=kenny_hit_list_msg)

                        await asyncio.sleep(1)
                        commander_msg2 = 'Commander ' + \
                            self.state.players[0][0].name + \
                            ', please select your team for the expedition. (Type `~pick <@name>` to pick a team member.)'
                        await self.state.game_channel.send(commander_msg2)

    async def blessing_timer(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(1)
            if self.state.status == 'ymir\'s blessing':
                timer = 0
                while self.state.status == 'ymir\'s blessing':
                    await asyncio.sleep(1)
                    timer += 1
                    if self.state.gamespeed == 'Normal' and timer == 60 and self.state.status == 'ymir\'s blessing':
                        timer_msg = self.state.currently_blessed.mention + \
                            ', you have **60 seconds** to use Ymir\'s blessing!'
                        await self.state.game_channel.send(timer_msg)

                    if (self.state.gamespeed == 'Normal' and timer == 90 and self.state.status == 'ymir\'s blessing') or \
                    (self.state.gamespeed == 'Fast' and timer == 30 and self.state.status == 'ymir\'s blessing'):
                        timer_msg = self.state.currently_blessed.mention + \
                            ', you have **30 seconds** to use Ymir\'s blessing!'
                        await self.state.game_channel.send(timer_msg)

                    if (self.state.gamespeed == 'Normal' and timer >= 120 and self.state.status == 'ymir\'s blessing') or \
                    (self.state.gamespeed == 'Fast' and timer >= 60 and self.state.status == 'ymir\'s blessing'):
                        times_up_msg = '**' + self.state.currently_blessed.name + '** did not use Ymir\'s blessing in time!'
                        await self.state.game_channel.send(times_up_msg)

                        self.state.status = 'expedition over'
                        self.state.blessed.append(self.state.currently_blessed)
                        self.state.currently_blessed = None

                        next_expedition_msg = 'When everyone is ready, type `~next` to begin the next expedition.'
                        await asyncio.sleep(2)
                        await self.state.game_channel.send(next_expedition_msg)

    async def paths_timer(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(1)
            if self.state.status == 'paths announcement':
                timer = 0
                while self.state.status == 'paths announcement':
                    await asyncio.sleep(1)
                    timer += 1
                    if self.state.gamespeed == 'Normal' and timer == 60 and self.state.status == 'paths announcement':
                        timer_msg = 'The Paths holder has **60 seconds** to make their announcement!'
                        player_timer_msg = 'You have **60 seconds** to send your message!'
                        await self.state.game_channel.send(timer_msg)
                        try:
                            await self.state.paths_holders[0].dm_channel.send(player_timer_msg)
                        except:
                            print("Error: User cannot receive DM")

                    if (self.state.gamespeed == 'Normal' and timer == 90 and self.state.status == 'paths announcement') or \
                    (self.state.gamespeed == 'Fast' and timer == 30 and self.state.status == 'paths announcement'):
                        timer_msg = 'The Paths holder has **30 seconds** to make their announcement!'
                        player_timer_msg = 'You have **30 seconds** to send your message!'
                        await self.state.game_channel.send(timer_msg)
                        try:
                            await self.state.paths_holders[0].dm_channel.send(player_timer_msg)
                        except:
                            print("Error: User cannot receive DM")

                    if (self.state.gamespeed == 'Normal' and timer >= 120 and self.state.status == 'paths announcement') or \
                    (self.state.gamespeed == 'Fast' and timer >= 60 and self.state.status == 'paths announcement'):
                        times_up_msg = 'The Paths holder did not make their announcement in time!'
                        await self.state.game_channel.send(times_up_msg)
                        self.state.paths_holders.pop(0)

                        self.state.status = 'expedition selection'
                        expedition_msg = '--**Expedition #' + \
                            str(self.state.cur_expedition) + ': Planning phase**--'
                        await self.state.game_channel.send(expedition_msg)
                        await asyncio.sleep(2)
                        self.state.next_commander()
                        commander_msg = 'The commander for this expedition is **' + \
                            self.state.players[0][0].mention + '**!'
                        await self.state.game_channel.send(commander_msg)

                        await asyncio.sleep(2)
                        players_msg = self.state.get_players()
                        await self.state.game_channel.send(embed=players_msg)

                        if self.state.kenny:
                            await asyncio.sleep(2)
                            kenny_hit_list_msg = self.state.get_kenny_hit_list()
                            await self.state.game_channel.send(embed=kenny_hit_list_msg)

                        await asyncio.sleep(1)
                        commander_msg2 = 'Commander **' + \
                            self.state.players[0][0].name + \
                            '**, please select your team for the expedition. (Type `~pick <@name>` to pick a team member.)'
                        await self.state.game_channel.send(commander_msg2)

    async def saboteur_timer(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(1)
            if self.state.status == 'saboteur selection':
                timer = 0
                while self.state.status == 'saboteur selection':
                    await asyncio.sleep(1)
                    timer += 1
                    if timer == 60 and self.state.status == 'saboteur selection':
                        timer_msg = 'The Saboteur has **60 seconds** to sabotage an expedition!'
                        player_timer_msg = 'You have **60 seconds** to sabotage an expedition!'
                        await self.state.game_channel.send(timer_msg)
                        try:
                            saboteur_player = list(filter(lambda x: x[1] == 'saboteur', self.state.players))[0][0]
                            await saboteur_player.dm_channel.send(player_timer_msg)
                        except:
                            print("Error: User cannot receive DM")
                    
                    if timer == 90 and self.state.status == 'saboteur selection':
                        timer_msg = 'The Saboteur has **30 seconds** to sabotage an expedition!'
                        player_timer_msg = 'You have **30 seconds** to sabotage an expedition!'
                        await self.state.game_channel.send(timer_msg)
                        try:
                            saboteur_player = list(filter(lambda x: x[1] == 'saboteur', self.state.players))[0][0]
                            await saboteur_player.dm_channel.send(player_timer_msg)
                        except:
                            print("Error: User cannot receive DM")

                    if timer >= 120 and self.state.status == 'saboteur selection':
                        times_up_msg = 'The Saboteur did not sabotage an expedition in time!'
                        await self.state.game_channel.send(times_up_msg)
                        self.state.status = 'assigning roles'
                        await asyncio.sleep(2)
                        await self.state.game_channel.send('When everyone is ready, type `~next` to begin the first expedition.')

    async def kidnap_timer(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(1)
            if self.state.status == 'choose coordinate':
                timer = 0
                while self.state.status == 'choose coordinate':
                    await asyncio.sleep(1)
                    timer += 1
                    if self.state.gamespeed == 'Normal' and timer == 300 and self.state.status == 'choose coordinate':
                        timer_msg = '❗| The Warriors have **5 minutes** to kidnap the Coordinate!'
                        await self.state.game_channel.send(timer_msg)
                    elif self.state.gamespeed == 'Normal' and timer == 480 and self.state.status == 'choose coordinate':
                        timer_msg = '❗| The Warriors have **2 minutes** to kidnap the Coordinate!'
                        await self.state.game_channel.send(timer_msg)
                    elif (self.state.gamespeed == 'Normal' and timer == 540 and self.state.status == 'choose coordinate') or \
                    (self.state.gamespeed == 'Fast' and timer == 60 and self.state.status == 'choose coordinate'):
                        timer_msg = '❗| The Warriors have **60 seconds** to kidnap the Coordinate!'
                        await self.state.game_channel.send(timer_msg)
                    elif (self.state.gamespeed == 'Normal' and timer == 570 and self.state.status == 'choose coordinate') or \
                    (self.state.gamespeed == 'Fast' and timer == 90 and self.state.status == 'choose coordinate'):
                        timer_msg = '❗| The Warriors have **30 seconds** to kidnap the Coordinate!'
                        await self.state.game_channel.send(timer_msg)
                    elif self.state.gamespeed == 'Fast' and timer == 105 and self.state.status == 'choose coordinate':
                        timer_msg = '❗| The Warriors have **15 seconds** to kidnap the Coordinate!'
                        await self.state.game_channel.send(timer_msg)
                    elif (self.state.gamespeed == 'Normal' and timer >= 600 and self.state.status == 'choose coordinate') or \
                    (self.state.gamespeed == 'Fast' and timer >= 120 and self.state.status == 'choose coordinate'):
                        timer = 0
                        # Win for soldiers
                        self.state.status = 'game ended soldiers'
                        times_up_msg = '🛡The Warriors did not manage to kidnap the Coordinate in time. Soldiers win!🛡'
                        await self.state.game_channel.send(times_up_msg)

                        end_summary = self.state.get_summary()
                        await asyncio.sleep(2)
                        await self.state.game_channel.send(embed=end_summary)

                        if self.state.gametype == 'Ranked':
                            rating_changes = self.state.update_rating()
                            achievements_msgs = self.state.update_achievements()
                            # Update roles in official WvS server
                            for player in self.state.players:
                                await self.state.update_role(player[0], self.client)
                            await self.state.update_top_roles(self.client)
                            await asyncio.sleep(2)
                            await self.state.game_channel.send(embed=rating_changes)
                            for achievements_msg in achievements_msgs:
                                await self.state.game_channel.send(achievements_msg)

                        self.state.status = 'game ended'
                        

    # async def vc_timer(self):
    #     await self.client.wait_until_ready()
    #     while not self.client.is_closed():
    #         await asyncio.sleep(1)
    #         if self.state.server and 'Warriors vs. Soldiers VC' in [role.name for role in self.state.server.roles]:
    #             vc_role = [role for role in self.state.server.roles if role.name == 'Warriors vs. Soldiers VC'][0]
    #             vc_users = [player for player in self.state.server.members if 'Warriors vs. Soldiers VC' in [role.name for role in player.roles]]
    #             # Add roles to players currently in the game
    #             for player in [player[0] for player in self.state.players]:
    #                 if 'Warriors vs. Soldiers VC' not in [role.name for role in player.roles] and player not in vc_users:
    #                     await self.client.add_roles(player, vc_role)

    #             # Remove roles from players who are not in the game and not in the recently played list
    #             for player in vc_users:
    #                 if player not in [player[0] for player in self.state.players] and player not in self.state.recently_played:
    #                     await self.client.remove_roles(player, vc_role)

    #         # Increments countdown timer when activated. When reach 10 mins, resets recently played list, stops countdown and resets countdown timer
    #         if self.state.vc_countdown_flag == True:
    #             self.state.vc_countdown += 1
    #             if self.state.vc_countdown >= 600:
    #                 self.state.recently_played = []
    #                 self.state.vc_countdown_flag = False
    #                 self.state.vc_countdown = 0


    # async def colour_change():
    #     colours = [discord.Colour(0xFFFFFF), discord.Colour(0xC0C0C0), discord.Colour(0x808080), discord.Colour(0x000000), discord.Colour(0x800000), discord.Colour(0xFFFF00), discord.Colour(0x808000),
    #     discord.Colour(0x00FF00), discord.Colour(0x008000), discord.Colour(0x00FFFF), discord.Colour(0x008080), discord.Colour(0x0000FF), discord.Colour(0x000080), discord.Colour(0xFF00FF), discord.Colour(0x800080)]
    #     await client.wait_until_ready()
    #     serverID = '401801585803657216'
    #     myserver = list(filter(lambda x: x.id == serverID, client.servers))[0]
    #     rainbow_role = list(filter(lambda x: x.name == 'Rainbow', myserver.roles))[0]
    #     while not client.is_closed():
    #         await asyncio.sleep(1)
    #         colorint = random.randint(1, len(colours))
    #         color = colours[colorint - 1]
    #         try:
    #             await client.edit_role(server = myserver, role = rainbow_role, colour = color)
    #         except:
    #             continue
