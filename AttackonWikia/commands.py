import discord
import asyncio
from AttackonWikia import state

class Game():
    def __init__(self, client):
        self.client = client
        self.state = state.State()
        self.versus_timer_obj = self.client.loop.create_task(self.versus_timer())
        self.game_timeout_obj = self.client.loop.create_task(self.game_timeout())

    async def msg_handler(self, message):
        # Gameplay
        if message.content.startswith('~reset'):
            self.state.game_reset()
            self.versus_timer_obj.cancel()
            self.game_timeout_obj.cancel()
            self.versus_timer_obj = self.client.loop.create_task(self.versus_timer())
            self.game_timeout_obj = self.client.loop.create_task(self.game_timeout())
            await message.channel.send(embed = self.state.intro_msg)

        if self.state.challenge == False:
            # Default gamemode
            if message.content.startswith('~new'):
                if not self.state.game_active():
                    await message.channel.send('Starting new puzzle!')
                    new_qn_msg = self.state.get_new_question(message.channel)
                    if type(new_qn_msg) == str:
                        await message.channel.send(new_qn_msg)
                    else:
                        await message.channel.send(embed=new_qn_msg)
                else:
                    await message.channel.send('There is already an active game being played! Please finish the current game before starting a new one.')

            if message.content.startswith('~clue'):
                clue_msg = self.state.get_clue()
                if type(clue_msg) == str:
                    await message.channel.send(clue_msg)
                else:
                    await message.channel.send(embed=clue_msg)

            if message.content.startswith('~image'):
                if not self.state.game_active():
                    await message.channel.send('Generating new image!')
                    new_image = self.state.get_new_image(message.channel)
                    await message.channel.send(embed = new_image)
                else:
                    await message.channel.send('There is already an active game being played! Please finish the current game before starting a new one.')
            
            if message.content.startswith('~hangman'):
                if not self.state.game_active():
                    if len(message.content.split(' ')) == 1:
                        await message.channel.send('Starting new hangman game!')
                        hangman_msg = self.state.get_new_hangman(message.channel)
                        await message.channel.send(embed = hangman_msg)
                    else:
                        if message.mentions and message.mentions[0] != message.author:
                            if self.state.players == [] or message.author != self.state.players[1]:
                                self.state.players = [message.author, message.mentions[0]]
                                await message.channel.send('**' + self.state.players[0].name + '** has challenged **' + self.state.players[1].name + '** to a game of Hangman!')
                                await message.channel.send('**' + self.state.players[1].name + '**, type ~hangman <@mention> to accept.')

                            elif message.author == self.state.players[1]:
                                # Starts challenge
                                await message.channel.send('**' + self.state.players[0].name + '** vs. **' + self.state.players[1].name + '**! First to 3 wins!')

                                self.state.hangman_challenge = True
                                self.state.new_challenge(message.channel)
                                scoreboard = self.state.get_scoreboard()
                                await message.channel.send(embed = scoreboard)
                                await asyncio.sleep(2)

                                # +1 to record of questions & challenge questions asked
                                self.state.new_challenge_qn()
                                await message.channel.send('**Round 1**')
                                hangman_msg = self.state.get_new_hangman_challenge()
                                await message.channel.send(embed = hangman_msg)
                        else:
                            await message.channel.send('Please specify a user to challenge!')
                else:
                    await message.channel.send('There is already an active game being played! Please finish the current game before starting a new one.')
                
            if message.content.startswith('~answer'):
                answer_msgs = self.state.get_answer()
                for answer_msg in answer_msgs:
                    await message.channel.send(answer_msg)

            # Player guesses correctly
            if self.state.question_set != None and self.state.question_set['title'].lower() in message.content.lower():
                if message.author.id != self.client.user.id and self.state.correct == False:
                    self.state.correct = True
                    correct_answer_msgs = self.state.correct_answer(message.author)
                    for correct_answer_msg in correct_answer_msgs:
                        await message.channel.send(correct_answer_msg)
            
            # Player guesses with a letter
            if self.state.letter_guess_check(message.content) and self.state.wrong_letter == False:
                letter_guess_msgs = self.state.letter_guess(message.content, message.author)
                if type(letter_guess_msgs) != list:
                    # Embed, hangman still in progress
                    await message.channel.send(embed = letter_guess_msgs)
                    if self.state.wrong_answers >= 6:
                        answer_msgs = self.state.get_answer()
                        for answer_msg in answer_msgs:
                            await message.channel.send(answer_msg)
                    elif self.state.wrong_letter == True:
                        await asyncio.sleep(0.5)
                        self.state.wrong_letter = False
                else:
                    # Word completed, equivalent to player guessing correctly
                    for letter_guess_msg in letter_guess_msgs:
                        await message.channel.send(letter_guess_msg)
           
            if message.content.startswith('~challenge'):
                if not self.state.game_active():
                    if message.mentions and message.mentions[0] != message.author:
                        if self.state.players == [] or message.author != self.state.players[1] or message.mentions[0] != self.state.players[0]:
                            self.state.players = [message.author, message.mentions[0]]
                            await message.channel.send('**' + self.state.players[0].name + '** has challenged **' + self.state.players[1].name + '**!')
                            await message.channel.send('**' + self.state.players[1].name + '**, type ~challenge <@mention> to accept.')

                        elif message.author == self.state.players[1] and message.mentions[0] == self.state.players[0]:
                            # Starts challenge
                            await message.channel.send('**' + self.state.players[0].name + '** vs. **' + self.state.players[1].name + '**! First to 3 wins!')

                            self.state.new_challenge(message.channel)
                            scoreboard = self.state.get_scoreboard()
                            await message.channel.send(embed = scoreboard)
                            await asyncio.sleep(2)

                            # +1 to record of questions & challenge questions asked
                            self.state.new_challenge_qn()
                            await message.channel.send('-- **Round 1** --')
                            await asyncio.sleep(1)
                            clue_contents = self.state.question_set['clues'][0] 
                            clue_msg = clue_contents[1:] if clue_contents.startswith(' ') else clue_contents
                            clue_embed = discord.Embed(title = 'Clue 1', description = clue_msg, colour = 0xC0C0C0)
                            await message.channel.send(embed = clue_embed)                 
                    
                    else:
                        await message.channel.send('Please specify a user to challenge!')
                else:
                    await message.channel.send('There is already an active game being played! Please finish the current game before starting a new one.')
        
        else:
            # Challenge ongoing
            if message.content.startswith('~challenge') or message.content.startswith('~new') or message.content.startswith('~image') or message.content.startswith('~hangman'):
                await message.channel.send('A match is currently underway!')

            # One player gets the right answer
            if self.state.question_set != None and self.state.question_set['title'].lower() in message.content.lower(): 
                if message.author in self.state.players and self.state.correct == False:
                    self.state.correct = True
                    player_no = 0 if message.author == self.state.players[0] else 1
                    self.state.scores[player_no] += 1
                    await message.channel.send('**' + message.author.name + '** is correct! The page is **' + self.state.question_set['title'] + ' !**')
                    await message.channel.send(self.state.question_set['url'])

                    # Updates records for game and player
                    self.state.correct_challenge_qn()
                    level_update = self.state.update_player_records(message.author)
                    if level_update != None:
                        await message.channel.send(level_update)
                    dailies = self.state.update_dailies(message.author)
                    for daily in dailies:
                        await message.channel.send(daily)

                    # Log result in achievements and sends message if obtained achievement
                    achievements = self.state.log_achievements(message.author)
                    for achievement in achievements:
                        await message.channel.send(achievement)

                    # Check if any player has reached 3 points
                    if max(self.state.scores) < 3:
                        await asyncio.sleep(1)
                        scoreboard = self.state.get_scoreboard()
                        await message.channel.send(embed = scoreboard)

                        # Next question
                        self.state.question_no += 1
                        self.state.new_challenge_qn()
                        await asyncio.sleep(2)
                        await message.channel.send('-- **Round ' + str(self.state.question_no) + '** --')
                        await asyncio.sleep(1)

                        self.state.next_question()
                        if self.state.hangman_challenge == False:
                            clue_contents = self.state.question_set['clues'][0] 
                            clue_msg = clue_contents[1:] if clue_contents.startswith(' ') else clue_contents
                            clue_embed = discord.Embed(title = 'Clue 1', description = clue_msg, colour = 0xC0C0C0)
                            await message.channel.send(embed = clue_embed)    
                        else:
                            hangman_msg = self.state.get_new_hangman_challenge()
                            await message.channel.send(embed = hangman_msg)

                    else:
                        # Reveal winner
                        scoreboard = self.state.get_winner()
                        await asyncio.sleep(1)
                        await message.channel.send(embed = scoreboard)

                        # Updates records for game and players
                        self.state.finish_challenge()
                        level_updates = self.state.challenge_update_player_records()
                        for update in level_updates:
                            await message.channel.send(update)

                        # Update daily
                        dailies = self.state.update_dailies()
                        for daily in dailies:
                            await message.channel.send(daily)

                        # Log result in achievements and sends message if obtained achievement
                        achievements = self.state.log_challenge_achievements()
                        for achievement in achievements:
                            await message.channel.send(achievement)

                        # Reset all stats
                        self.state.game_reset()

                        await asyncio.sleep(2)
                        await message.channel.send('Type `~challenge <@person>` to start a new challenge. Type `~help` to see the list of available commands.')

        # Information
        if message.content.startswith('~profile') or message.content.startswith('~rank'):
            messagebox = message.content.split(' ')
            if len(messagebox) == 1:
                player_obj = message.author
            elif message.mentions:
                player_obj = message.mentions[0]
            profile = self.state.get_profile(player_obj, message.guild)
            await message.channel.send(embed = profile)

        if message.content.startswith('~badges') or message.content.startswith('~achievements'):
            messagebox = message.content.split(' ')
            if len(messagebox) == 1:
                player_obj = message.author
            elif message.mentions:
                player_obj = message.mentions[0]
            badges = self.state.get_achievements(player_obj)
            await message.channel.send(embed = badges)

        if message.content.startswith('~dailies') or message.content.startswith('~daily'):
            cur_dailies = self.state.get_dailies(message.author)
            await message.channel.send(embed = cur_dailies)
        
        if message.content.startswith('~gamestats'):
            stats = self.state.get_stats()
            await message.channel.send(embed = stats)

        if message.content.startswith('~leaderboard') or message.content.startswith('~lb'):
            messagebox = message.content.split(' ')
            if len(messagebox) == 1:
                leaderboard = self.state.get_leaderboard(message.guild)
            elif message.mentions:
                player_profile = message.mentions[0]
                leaderboard = self.state.get_leaderboard(message.guild, player=player_profile)
            else:
                page_no = messagebox[1]
                leaderboard = self.state.get_leaderboard(message.guild, page=page_no)
            await message.channel.send(embed = leaderboard)

        if message.content.startswith('~help') or message.content.startswith('~commands'):
            commands = self.state.get_commands()
            await message.channel.send(embed = commands)

        if message.content.startswith('~test'):
            hangman = '`🔄` Letter `A` does not exist. You can guess again in 2 seconds.\n\n'
            hangman += '| \u2004 🇲 \u2001\u2000 🇷 \u2001\u2000 🇸\n'
            hangman += '|💥💥 💥🏠 🏰🏰'
            hangman_embed = discord.Embed(title = 'Hangman Mode', description = hangman, colour = 0xC0C0C0)
            hangman_embed.set_footer(text = 'a b c d e')
            await message.channel.send(embed = hangman_embed)


    async def versus_timer(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(1)
            if self.state.challenge == True:
                if self.state.hangman_challenge == False:
                    # Standard challenge
                    cur_question = self.state.question_no
                    self.state.timer += 10
                    await asyncio.sleep(10)
                    if cur_question == self.state.question_no:
                        if self.state.clue_no < 5:
                            self.state.clue_no += 1
                            clue_contents = self.state.question_set['clues'][self.state.clue_no - 1]
                            clue_msg = clue_contents[1:] if clue_contents.startswith(' ') else clue_contents
                            clue_embed = discord.Embed(title = 'Clue ' + str(self.state.clue_no), description = clue_msg, colour = 0xC0C0C0)
                            await self.state.game_channel.send(embed = clue_embed)

                        else:
                            # Countdown
                            if self.state.timer < 60:
                                await self.state.game_channel.send('**' + str(60 - self.state.timer) + '** seconds remaining!')

                            else:
                                # Time's up, next question
                                await self.state.game_channel.send('Time\'s up! The page is **' + self.state.question_set['title'] + ' !**')
                                await self.state.game_channel.send(self.state.question_set['url'])
                                self.state.question_no += 1
                                self.state.new_challenge_qn()
                                self.state.next_question()

                                await asyncio.sleep(1)
                                scoreboard = self.state.get_scoreboard()
                                await self.state.game_channel.send(embed = scoreboard)

                                await asyncio.sleep(2)
                                await self.state.game_channel.send('-- **Round ' + str(self.state.question_no) + '** --')
                                await asyncio.sleep(1)
                                clue_contents = self.state.question_set['clues'][0]
                                clue_msg = clue_contents[1:] if clue_contents.startswith(' ') else clue_contents
                                clue_embed = discord.Embed(title = 'Clue 1', description = clue_msg, colour = 0xC0C0C0)
                                await self.state.game_channel.send(embed = clue_embed)

                    else:
                        # Someone answered correctly
                        continue

                else:
                    # Hangman challenge
                    cur_question = self.state.question_no
                    await asyncio.sleep(5)
                    if cur_question == self.state.question_no:
                        # Reveal new letter
                        self.state.hangman_reveal_letter()
                        if '◯' in self.state.get_hangman_word():
                            # Not completed
                            hangman_msg = self.state.get_hangman_challenge_word()
                            await self.state.game_channel.send(embed = hangman_msg)
                        else:
                            await asyncio.sleep(5)
                            if cur_question == self.state.question_no:
                                # Reveal answer, move to next question
                                await self.state.game_channel.send('Time\'s up! The page is **' + self.state.question_set['title'] + ' !**')
                                await self.state.game_channel.send(self.state.question_set['url'])
                                self.state.question_no += 1
                                self.state.new_challenge_qn()
                                self.state.next_question()

                                await asyncio.sleep(1)
                                scoreboard = self.state.get_scoreboard()
                                await self.state.game_channel.send(embed = scoreboard)

                                await asyncio.sleep(2)
                                await self.state.game_channel.send('-- **Round ' + str(self.state.question_no) + '** --')
                                await asyncio.sleep(1)
                                hangman_msg = self.state.get_new_hangman_challenge()
                                await self.state.game_channel.send(embed = hangman_msg)

                    else:
                        # Someone answered correctly
                        continue
            
    async def game_timeout(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            await asyncio.sleep(1)
            if self.state.game_active():
                timer = 0
                current_qn = self.state.question_set
                while current_qn == self.state.question_set:
                    await asyncio.sleep(1)
                    timer += 1
                    if current_qn == self.state.question_set and timer == 600:
                        await self.state.game_channel.send('This session has timed out after not getting new replies for 10 minutes.')
                        self.versus_timer_obj.cancel()
                        self.versus_timer_obj = self.client.loop.create_task(self.versus_timer())
                        await self.state.game_channel.send(embed = self.state.intro_msg)
                        self.state.game_reset()

