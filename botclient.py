import discord
import asyncio
import botconfig
import config_queries
import db_backup
import admin

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        # Create all databases and tables if they don't exist (5 dbs in total, backup every week)
        config_queries.initialize_dbs()

        # Begin DB backup loop
        db_backup.DBbackup(self)

        # Set default status for public bot
        bot_status = discord.Game(name = '~help | ~config')
        await self.change_presence(activity = bot_status)

        # Initialize game states for all channels in the config record
        instance_data = config_queries.get_instances()
        botconfig.instances = []
        for row in instance_data:
            new_instance = botconfig.Instance(row[0], row[1], row[2], self)
            botconfig.instances.append(new_instance)

    async def on_message(self, message): # Only one of these allowed
        # Get cur_game, which is the game object consisting of commands and all other relevant states of the game
        cur_game = botconfig.get_cur_game(message)

        if message.content == '~die' and message.author.id == 238808836075421697:
            print("Terminating")
            raise SystemExit

        # Admin commands
        elif message.content.split(' ')[0] in admin.commands_list:
            await admin.message_handler(self, message)

        # Config 
        elif message.content.startswith('~config'):
            if message.author.id == 238808836075421697:
                config_msg = botconfig.get_config_msg(cur_game)
                config_embed = discord.Embed(title = config_msg, colour=0xE5D2BB)
                await message.channel.send(embed = config_embed)

                def options(my_msg):
                    return (message.author.id == message.guild.owner.id or message.author.id == 238808836075421697) \
                    and my_msg.content in ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '0️⃣']
                    
                try:
                    config_response = await self.wait_for('message', check = options, timeout = 60)
                except asyncio.TimeoutError:
                    config_response = None

                config_game = botconfig.config_bot(config_response, self)
                await message.channel.send(embed = config_game)
            else:
                await message.channel.send('Only the bot owner can configure me!')

        # Deletes a specified number of messages  
        elif message.content.startswith('~clear') and message.author.id == 238808836075421697: 
            number_to_delete = int(message.content.split(' ')[1]) + 1
            await message.channel.purge(limit = number_to_delete)

        elif cur_game:
            await cur_game.msg_handler(message)

        elif message.content.startswith('~') and not '~~' in message.content:
            msg = 'No game is currently enabled in this channel! Type `~config` to select a game.'
            await message.channel.send(embed=discord.Embed(description=msg, colour=0xE5D2BB))