import discord
import asyncio
import botconfig
import config_queries
import db_backup

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

        # Display servers bot is in
        elif message.content.startswith('~servers') and message.mentions and message.author.id == 238808836075421697:
            if message.mentions[0] == self.user:
                servers = self.guilds
                server_names = '\n'.join(list(map(lambda x: x.name, servers)))
                server_ids = '\n'.join(list(map(lambda x: str(x.id), servers)))
                servers_embed = discord.Embed(title = 'Number of servers: ' + str(len(servers)), colour=0xE5D2BB)
                servers_embed.add_field(name = 'Server names', value = server_names)
                servers_embed.add_field(name = 'Server IDs', value = server_ids)
                await message.channel.send(embed = servers_embed)

        elif message.content.startswith('~botleaveserver') and message.author.id == 238808836075421697:
            server_id = message.content.split(' ')[1]
            servers = self.guilds
            if server_id in list(map(lambda x: str(x.id), servers)):
                server_obj = list(filter(lambda x: str(x.id) == server_id, servers))[0]
                await server_obj.leave()
                await message.channel.send('Left server: **' + server_obj.name + '**')
            else:
                await message.channel.send('I am not in this server!')

        # Deletes a specified number of messages  
        elif message.content.startswith('~clear') and message.author.id == 238808836075421697: 
            number_to_delete = int(message.content.split(' ')[1]) + 1
            await message.channel.purge(limit = number_to_delete)

        elif cur_game:
            await cur_game.msg_handler(message)

        elif message.content.startswith('~') and not '~~' in message.content:
            msg = 'No game is currently enabled in this channel! Type `~config` to select a game.'
            await message.channel.send(embed=discord.Embed(description=msg, colour=0xE5D2BB))