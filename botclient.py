import discord
import asyncio
import botconfig
import config_queries
import db_backup
import admin
from WarriorsvsSoldiers import game
from AttackonWikia import populateURLs

class MyClient(discord.Client):
    backup = None
    populate_urls = False

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        # Create all databases and tables if they don't exist (5 dbs in total, backup every week)
        config_queries.initialize_dbs()

        # Begin DB backup loop
        if self.backup:
            db_backup.DBbackup(self)
        
        # Start indexing wikia pages
        if self.populate_urls:
            populateURLs.PopulateURLsObj(self)

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
        cur_games = botconfig.get_cur_game(message)

        if message.author.bot:
            return

        if message.content == '~die' and message.author.id == 238808836075421697:
            print("Terminating")
            raise SystemExit

        # Privacy policy
        elif message.content.startswith('~privacy'):
            privacy_msg = '**Where does the information go?**\n\n' + \
            'All the information is stored in a local SQLite DB. If you want your information removed contact Entropi#3441.\n\n' + \
            '**What information is collected?**\n\n' + \
            '- Guild ID\n' + \
            '- Channel ID\n' + \
            '- User ID\n\n' + \
            '**Why do we collect the information?**\n\n' + \
            'We collect information to maintain game records for players to track their progress and compete on the leaderboards.\n\n' + \
            '**Do we share any information?**\n\n' + \
            'None of the data collected is shared nor ever will be shared.\n\n' + \
            'Support? If you have any problems contact Entropi#3441. Or join the support server: https://discord.gg/sBjKwBp\n\n'
            privacy_embed = discord.Embed(title = 'Privacy Policy for Warriors vs Soldiers', description = privacy_msg, colour=0xE5D2BB)
            await message.channel.send(embed = privacy_embed)

        # Admin commands
        elif message.content.split(' ')[0] in admin.commands_list and message.author.id == 238808836075421697:
            await admin.message_handler(self, message, botconfig.instances)

        # Config
        elif message.content.startswith('~config'):
            if str(message.channel.type) == 'private':
                await message.channel.send('You can only enable games in a public channel!')
            elif message.author.guild_permissions.manage_guild or message.author.id == 238808836075421697:
                current_author_id = message.author.id
                current_channel_id = message.channel.id
                config_embed = botconfig.get_config_msg(cur_games)
                await message.channel.send(embed = config_embed)

                def options(my_msg):
                    return (my_msg.author.id == current_author_id and my_msg.channel.id == current_channel_id) \
                    and (my_msg.author.guild_permissions.manage_guild or my_msg.author.id == 238808836075421697) \
                    and my_msg.content in ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '0️⃣', '1', '2', '3', '4', '0']
                    
                try:
                    config_response = await self.wait_for('message', check = options, timeout = 60)
                except asyncio.TimeoutError:
                    config_response = None

                config_game = botconfig.config_bot(config_response, self)
                await message.channel.send(embed = config_game)
            else:
                await message.channel.send('You require the **Manage Server** permission to configure me!')

        # Deletes a specified number of messages  
        elif message.content.startswith('~clear') and message.author.id == 238808836075421697: 
            number_to_delete = int(message.content.split(' ')[1]) + 1
            await message.channel.purge(limit = number_to_delete)

        elif message.content in ['-help', '-config']:
            await message.channel.send('My prefix is `~`! E.g. type `~help` to see my list of commands.')

        elif message.content.startswith('~credits'):
            credits_msg = 'This bot was made by Entropi#3441. Please DM me if you have any suggestions or bug reports.\n\n'
            patreon_msg = 'If you liked my games, do consider supporting me on [Patreon](https://www.patreon.com/entropi)!'
            credits_embed =  discord.Embed(title = 'Credits', description = credits_msg + patreon_msg, colour=0xE5D2BB)
            await message.channel.send(embed=credits_embed)

        elif message.content.startswith('~invite'):
            invite_msg = '[Click here](https://discord.com/oauth2/authorize?client_id=422033689250234368&scope=bot&permissions=388161) to invite me to your server!\n\n' + \
            'Or join the official [Warriors vs Soldiers server](https://discord.gg/sBjKwBp)!'
            invite_embed =  discord.Embed(title = 'Invite link', description = invite_msg, colour=0xE5D2BB)
            invite_embed.set_thumbnail(url=str(self.user.avatar_url))
            await message.channel.send(embed=invite_embed)

        elif message.channel.id == 751466308079583262:
            if message.content.startswith('~pings') and message.author.id == 238808836075421697:
                pings_msg = 'Type `y` if you want to be pinged.\nType `n` if you no longer want to be pinged.'
                status = discord.Embed(title = 'Would you like to be pinged for games in this server?', description = pings_msg, colour=0x00C9FF)
                await message.channel.send(embed=status)
            elif message.content.lower() == 'y':
                await message.author.add_roles(message.guild.get_role(748084175352889364))
                confirmation_msg = await message.channel.send(embed=discord.Embed(description = message.author.mention + ', you can now be pinged for games in this server!', colour=0x00C9FF))
                await message.delete()
                await asyncio.sleep(15)
                await confirmation_msg.delete()
            elif message.content.lower() == 'n':
                await message.author.remove_roles(message.guild.get_role(748084175352889364))
                confirmation_msg = await message.channel.send(embed=discord.Embed(description = message.author.mention + ', you will no longer be pinged for games in this server!', colour=0x00C9FF))
                await message.delete()
                await asyncio.sleep(15)
                await confirmation_msg.delete()
            elif message.author.id != self.user.id:
                await message.delete()

        elif cur_games:
            if message.mentions and message.mentions[0] == self.user:
                message.mentions = []
                message.content = '~help'

            for game in cur_games:
                await game.msg_handler(message)
        
        elif message.content.startswith('~help') or (message.mentions and message.mentions[0] == self.user):
            commands = discord.Embed(title = 'List of commands', description = 'Here is the list of available commands.', colour=0xE5D2BB)
            general_commands = '`~config` : Lets you select the game for each channel\n' + \
                '`~credits` : Who made me/Get support\n' + \
                '`~invite` : Link to invite me to your server'
            commands.add_field(name = 'General', value = general_commands)
            await message.channel.send(embed=commands)

        elif message.content.lower() in botconfig.commands_list:
            msg = 'No game is currently enabled in this channel! Type `~config` to select a game.'
            await message.channel.send(embed=discord.Embed(description=msg, colour=0xE5D2BB))

    async def on_member_join(self, member):
        if member.guild.id == 748080644340318299:
            # Assign role to member in WvS server
            await game.State.update_role(member, self, first_join=True)
            await game.State.update_top_roles(self)

    async def on_guild_join(self, server):
        logs_channel = self.get_channel(742621514003644507)
        server_info = 'Server ID: ' + str(server.id) + '\n' + '# Members: ' + str(len(server.members))
        await logs_channel.send(embed=discord.Embed(title='Joined server: ' + server.name, description = server_info, colour=0xE5D2BB))

    async def on_guild_remove(self, server):
        for instance in botconfig.instances:
            if instance.server_id == server.id:
                botconfig.instances.remove(instance)
        logs_channel = self.get_channel(742621514003644507)
        server_info = 'Server ID: ' + str(server.id) + '\n' + '# Members: ' + str(len(server.members))
        await logs_channel.send(embed=discord.Embed(title='Left server: ' + server.name, description = server_info, colour=0xE5D2BB))