import discord
import asyncio
from ChooseYourAdventure import stats
from ChooseYourAdventure import book
from ChooseYourAdventure import book2

class Game():
    def __init__(self, client):
        self.client = client
        self.state = stats.State()
        self.client.loop.create_task(self.timeout())

    async def msg_handler(self, message):
        if message.content in self.state.book.EC:
            chosen_option = self.state.book.EC[message.content]
            if chosen_option in self.state.book.choices[0]:
                if message.author.id == self.state.cur_player_id:
                    # Handles secrets for Annie's path
                    if chosen_option == 's' and self.state.book.cur_page[0] in self.state.book.annie_secrets:
                        msg_content = self.state.get_annie_secrets(message.author)
                        if msg_content.startswith('Nice'):
                            await message.channel.send(msg_content)
                        else:
                            self.state.book.new_msg = await message.channel.send(msg_content)

                    # Flips page normally
                    else:
                        msg_content = self.state.book.page_flipper(chosen_option)
                        self.state.book.new_msg = await message.channel.send(msg_content)

                    # Adds choices as reactions
                    for option in self.state.book.choices[0]:
                        await self.state.book.new_msg.add_reaction(self.state.book.EC2[option])

                    # Logs the ending the player achieved, if any
                    if self.state.book.cur_page[0] in self.state.book.endings:
                        promotion_info = self.state.log_ending(message.author)
                        if promotion_info != None:
                            await asyncio.sleep(2)
                            await message.channel.send(embed = promotion_info)
                        
                    # For endings with videos
                    if self.state.book.response2[0] != '':
                        await asyncio.sleep(1)
                        await message.channel.send(self.state.book.response2[0])
                
                else:
                    await message.channel.send('Someone else is currently playing the game! Please wait for your turn.')

        # GAMEPLAY
        # Resets the game
        if message.content.startswith('~reset'):
            self.state.reset_game()
            await message.channel.send(embed = self.state.book.reset_msg)

        # Plays the intro message
        if message.content.startswith('~intro'):
            await message.channel.send(self.state.book.intro_msg)

        # List of commands
        if message.content.startswith('~help') or message.content.startswith('~commands'):
            commands = self.state.get_commands()
            await message.channel.send(embed = commands)
        
        # Starts game
        if message.content.startswith('~start'):
            if self.state.book.cur_page[0] == 1 or self.state.book.choices[0] == []:
                self.state.reset_game()
                self.state.game_channel = message.channel
                self.state.cur_player_id = message.author.id

                # Book selection
                # Access to Book 2, go to book selection
                if self.state.check_book(message.author):
                    self.state.select_book = True
                    select_msg = await message.channel.send('📖 | Please select the story you would like to participate in:\n\n' + \
                    ':one: Book 1 - The Battle for Trost\n\n' + \
                    ':two: Book 2 - Hunt for the Female Titan')
                    for rxn in ['1️⃣', '2️⃣']:
                        await select_msg.add_reaction(rxn)
                    
                # No access to Book 2, start Book 1 straight away
                else:
                    new_msg = await message.channel.send(self.state.book.P1())
                    for option in self.state.book.choices[0]:
                        await new_msg.add_reaction(self.state.book.EC2[option])
            else:
                await message.channel.send('There is already a game ongoing!')

        # Book selection
        if self.state.select_book == True and message.content in self.state.book.EC:
            chosen_option = self.state.book.EC[message.content]
            # Changes state for book 2, otherwise starts book 1 (default state)
            if chosen_option == 2:
                self.state.switch_book(2)

            if chosen_option == 1 or chosen_option == 2:
                self.state.select_book = False
                new_msg = await message.channel.send(self.state.book.P1())
                for option in self.state.book.choices[0]:
                    await new_msg.add_reaction(self.state.book.EC2[option])

        # Reminder to use the emoji to answer
        if (self.state.book.cur_page[0] == 1 or self.state.book.cur_page[0] == 2) and (self.state.book.choices[0] != [] and message.content in ['1','2','3']):
            reminder_msg = '❗Make your response using the emoji corresponding to your chosen option. E.g. Reply with `:one:` instead of "1".'
            await message.channel.send(reminder_msg)
    
        # Secret handler (add reaction)
        if message.content.lower() in self.state.book.secrets:
            if self.state.book.secrets[message.content.lower()] == self.state.book.cur_page[0]:
                self.state.book.choices[0].append('s')
                await self.state.book.new_msg.add_reaction(self.state.book.EC2['s'])
        
        # INFORMATION
        # Displays the current game state
        if message.content.startswith('~stats'):
            stats_info = self.state.get_stats()
            await message.channel.send(embed = stats_info)

        # Brings up the progress info of player
        if message.content.startswith('~info') or message.content.startswith('~profile'):
            messagebox = message.content.split(' ')
            book_no = 1
            if len(messagebox) == 1:
                user_obj = message.author
            elif message.mentions:
                user_obj = message.mentions[0]
            else:
                user_obj = message.author
                book_no = messagebox[1]
                
            progress_info = self.state.get_profile(user_obj, book_no=book_no)
            profile_msg = await message.channel.send(embed = progress_info)

            def reaction_check(reaction, user):
                return user != self.client.user and (reaction.emoji == '1️⃣' or reaction.emoji == '2️⃣') and (reaction.message.id == profile_msg.id)

            await profile_msg.add_reaction('1️⃣')
            await profile_msg.add_reaction('2️⃣')

            while True:
                rxn, user = await self.client.wait_for('reaction_add', check = reaction_check)

                if rxn.emoji == '1️⃣':
                    book_no = 1
                elif rxn.emoji == '2️⃣':
                    book_no = 2

                progress_info = self.state.get_profile(user_obj, book_no=book_no)
                await profile_msg.edit(embed=progress_info)
                await rxn.remove(user)
                await asyncio.sleep(0.1)

        # Shows the leaderboard
        if message.content.startswith('~leaderboard') or message.content.startswith('~lb'):
            messagebox = message.content.split(' ')
            if len(messagebox) == 1:
                leaderboard, cur_page = self.state.get_leaderboard(message.guild)
            elif message.mentions:
                player_profile = message.mentions[0]
                leaderboard, cur_page = self.state.get_leaderboard(message.guild, player=player_profile)
            else:
                page_no = messagebox[1]
                leaderboard, cur_page = self.state.get_leaderboard(message.guild, page=page_no)
            leaderboard_msg = await message.channel.send(embed = leaderboard)

            def reaction_check(reaction, user):
                return user != self.client.user and (reaction.emoji == '◀' or reaction.emoji == '▶') and (reaction.message.id == leaderboard_msg.id)

            await leaderboard_msg.add_reaction('◀')
            await leaderboard_msg.add_reaction('▶')

            while True:
                rxn, user = await self.client.wait_for('reaction_add', check = reaction_check)

                if rxn.emoji == '◀':
                    cur_page -= 1
                elif rxn.emoji == '▶':
                    cur_page += 1

                leaderboard, cur_page = self.state.get_leaderboard(message.guild, page=cur_page)
                await leaderboard_msg.edit(embed=leaderboard)
                await rxn.remove(user)
                await asyncio.sleep(0.1)

        # Returns overall game statistics
        if message.content.startswith('~gamestats'):
            messagebox = message.content.split(' ')
            book_no = 1
            if len(messagebox) > 1:
                book_no = messagebox[1]
            gamestats = self.state.get_gamestats(book_no=book_no)
            gamestats_msg = await message.channel.send(embed = gamestats)

            def reaction_check(reaction, user):
                return user != self.client.user and (reaction.emoji == '1️⃣' or reaction.emoji == '2️⃣') and (reaction.message.id == gamestats_msg.id)

            await gamestats_msg.add_reaction('1️⃣')
            await gamestats_msg.add_reaction('2️⃣')

            while True:
                rxn, user = await self.client.wait_for('reaction_add', check = reaction_check)

                if rxn.emoji == '1️⃣':
                    book_no = 1
                elif rxn.emoji == '2️⃣':
                    book_no = 2

                gamestats = self.state.get_gamestats(book_no=book_no)
                await gamestats_msg.edit(embed=gamestats)
                await rxn.remove(user)
                await asyncio.sleep(0.1)

        # Testing command
        if message.content.startswith('~test'):
            promotion_info = discord.Embed(title='🎖Entropi has been promoted to Squad Captain!🎖', colour=0xE5D2BB)
            promotion_info.set_thumbnail(url = message.author.avatar_url)
            promotion_info.add_field(name = 'Congratulations!', value =  '**Squad Leader** ➡ **Squad Captain**')
            await message.channel.send(embed = promotion_info)

    async def timeout(self):
        await self.client.wait_until_ready()
        await asyncio.sleep(1)
        while not self.client.is_closed():
            prev_page = self.state.book.cur_page[0]
            await asyncio.sleep(60)
            if self.state.book.choices[0] != [] and self.state.book.cur_page[0] == prev_page:
                self.state.timer += 1
                if self.state.timer >= 10:
                    await self.state.game_channel.send('This session has timed out after not getting new replies for 10 minutes. Type `~start` to begin a new game.')
                    self.state.reset_game()
            else:
                self.state.timer = 0
        