import discord
import asyncio
from Jaegermore import stats
from Jaegermore import questions
from Jaegermore import personalities

class Game():
    def __init__(self, client):
        self.client = client
        self.state = stats.State()
        self.client.loop.create_task(self.timeout())

    async def msg_handler(self, message):
        if message.content in self.state.question.EC and self.state.question.curplayer != None and (message.author.id == self.state.question.curplayer.id):
            chosen_option = self.state.question.EC[message.content]
            if chosen_option in self.state.question.choices[0]:
                if message.author == self.state.question.curplayer:
                    msg_content = self.state.question.question_handler(chosen_option)
                    await message.channel.send(msg_content)
                else:
                    await message.channel.send('Someone else is currently taking the assessment! Please wait for your turn.')


        # Resets the game
        if message.content.startswith('~reset'):
            self.state.game_reset()
            await message.channel.send(embed = self.state.question.reset_msg)
        
        # Plays the intro message
        if message.content.startswith('~intro'):
            await message.channel.send(self.state.question.intro_msg)

        # Starts game
        if message.content.lower().startswith('~start'):
            if (self.state.question.cur_qn[0] == 0 or self.state.question.cur_qn[0] == 'result' or self.state.question.cur_qn[0] == 'result2'):
                messagebox = message.content.split(' ')
                if len(messagebox) == 1:
                    self.state.game_reset()
                    self.state.question.curplayer = message.author
                    self.state.game_channel = message.channel
                    self.state.question.num_qns = 10
                    response = 'Beginning assessment for cadet **' + self.state.question.curplayer.name + '**!'
                elif messagebox[1] == 'full':
                    self.state.game_reset()
                    self.state.question.curplayer = message.author
                    self.state.game_channel = message.channel
                    self.state.question.num_qns = 40
                    response = 'Beginning full assessment for cadet **' + self.state.question.curplayer.name + '**!'
                
                await message.channel.send(response)
                await asyncio.sleep(1)

                msg_content = self.state.question.question_handler(0)
                await message.channel.send(msg_content)
            else:
                await message.channel.send('Someone else is currently taking the assessment! Please wait for your turn.')

        # Reminder to use the emoji to answer
        if message.content in ['1','2','3','4','5','6'] and self.state.question.curplayer != None and message.author.id == self.state.question.curplayer.id:
            await message.channel.send('Make your response using the emoji corresponding to your chosen option. E.g. Reply with `:one:` instead of "1".')

        # Obtains result
        if message.content.startswith('~result') and self.state.question.cur_qn[0] == 'result':
            character = self.state.scores.highest_char()
            # Update records
            self.state.update_records(character)
            player = self.state.question.curplayer
            msg_content = personalities.all_results[character](player)
            self.state.question.cur_qn[0] = 'result2'
            await message.channel.send(embed = msg_content)
            await asyncio.sleep(2)
            await message.channel.send('**If you\'re ready, type `~start` to begin a new assessment.**')

        # Returns detailed personality info for the current test result
        if message.content.startswith('~stats') and self.state.question.cur_qn[0] == 'result2':
            stats_info = self.state.get_info()
            await message.channel.send(embed = stats_info)

        # Player profile
        if message.content.startswith('~profile') or message.content.startswith('~info'):
            messagebox = message.content.split(' ')
            if len(messagebox) == 1:
                player_obj = message.author
            elif message.mentions:
                player_obj = message.mentions[0]
            profile = self.state.get_profile(player_obj)
            await message.channel.send(embed = profile)

        # Shows the leaderboard
        if message.content.startswith('~leaderboard') or message.content.startswith('~lb'):
            messagebox = message.content.split(' ')
            if len(messagebox) == 1:
                leaderboard = self.state.get_leaderboard(message.guild)
            else:
                character = messagebox[1]
                leaderboard = self.state.get_leaderboard(message.guild, character=character)
            await message.channel.send(embed = leaderboard)

        # Returns overall game statistics
        if message.content.startswith('~gamestats'):
            game_stats = self.state.get_stats()
            await message.channel.send(embed = game_stats)
        
        # Returns list of commands
        if message.content.startswith('~help') or message.content.startswith('~commands'):
            commands = self.state.get_commands()
            await message.channel.send(embed = commands)

        # Explains similarity percentage calculation
        if message.content.startswith('~similarity'):
            similarity_embed = self.state.similarity_explanation()
            await message.channel.send(embed = similarity_embed)

        # Testing command
        if message.content.startswith('~test'):
            test = discord.Embed(title = 'Test', description = 'testing')
            test.set_thumbnail(url = 'https://imageshack.com/a/img924/8553/WILQOo.png')
            await message.channel.send(embed = test)

    async def timeout(self):
        await self.client.wait_until_ready()
        await asyncio.sleep(1)
        while not self.client.is_closed():
            prev_qn = self.state.question.cur_qn[0]
            await asyncio.sleep(60)
            if self.state.question.choices[0] != [] and self.state.question.cur_qn[0] == prev_qn:
                self.state.timer += 1
                if self.state.timer >= 10:
                    await self.state.game_channel.send('This test has timed out after not getting new replies for 10 minutes. Type `~start` to begin a new test.')
                    self.state.game_reset()
            else:
                self.state.timer = 0
