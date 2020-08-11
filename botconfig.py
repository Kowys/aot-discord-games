import discord
import asyncio
import config_queries
import ChooseYourAdventure.commands
import Jaegermore.commands
import WarriorsvsSoldiers.commands
import AttackonWikia.commands

# Each instance contains server ID, channel ID, and client as attributes
instances = []

class Instance():
    def __init__(self, server_id, channel_id, game_name, client):
        self.game_name = game_name
        self.server_id = server_id
        self.channel_id = channel_id
        self.client = client
        self.game = self.create_game(game_name)

    def create_game(self, game_name):
        if game_name == 'Choose Your Adventure':
            return ChooseYourAdventure.commands.Game(self.client)
        elif game_name == 'Jaegermore':
            return Jaegermore.commands.Game(self.client)
        elif game_name == 'Warriors vs Soldiers':
            return WarriorsvsSoldiers.commands.Game(self.client)
        elif game_name == 'Attack on Wikia':
            return AttackonWikia.commands.Game(self.client)

    async def msg_handler(self, message):
        # Select the correct game handler to handle the message
        await self.game.msg_handler(message)

def get_cur_game(message):
    # Returns the game state from games corresponding to the channel
    # Returns None if no game is enabled for the channel
    # If private message, return the game state of Warriors vs Soldiers if person is in game
    for instance in instances:
        if str(message.channel.type) == 'private':
            # Players can join only 1 game at a time (Might need to fix later)
            try:
                if message.author in list(map(lambda x:x[0], instance.game.state.players)):
                    return instance
            except:
                continue
        else:
            if instance.channel_id == message.channel.id:
                return instance

    return None

def get_config_msg(cur_game):
    config_msg = 'Which game would you like to enable for this channel?'
    config_msg += '\n(Current game: ' + (cur_game.game_name if cur_game else 'None') + ')'
    config_msg += '\n\n:one: Choose Your Adventure (Locked)\n\n\
:two: Jaegermore (Locked)\n\n\
:three: Warriors vs Soldiers\n\n\
:four: Attack on Wikia (Locked)\n\n\
:zero: None'
    return config_msg

def config_bot(config_msg, client):
    # Configures bot for the channel and return embed message
    if config_msg == None:
        return discord.Embed(description = 'Config has timed out after 60 seconds. Type `~config` to start again.', colour=0xE5D2BB)
    else:
        options = {
            '1️⃣':'Choose Your Adventure',
            '2️⃣':'Jaegermore',
            '3️⃣':'Warriors vs Soldiers',
            '4️⃣':'Attack on Wikia',
            '0️⃣':'None',
            '1':'Choose Your Adventure',
            '2':'Jaegermore',
            '3':'Warriors vs Soldiers',
            '4':'Attack on Wikia',
            '0':'None'
        }
        locked_options = {
            '1️⃣':'Choose Your Adventure',
            '2️⃣':'Jaegermore',
            '4️⃣':'Attack on Wikia',
            '1':'Choose Your Adventure',
            '2':'Jaegermore',
            '4':'Attack on Wikia'
        }
        if config_msg.content in locked_options and config_msg.author.id != 238808836075421697:
            locked_msg = 'If you\'d like to play this game, please join the [Attack on Titan Wiki server](https://discord.gg/attackontitan).'
            locked_embed = discord.Embed(title = 'Game currently unavailable to the public', description = locked_msg, colour=0xE5D2BB)
            return locked_embed

        chosen_game = options[config_msg.content]

        # Update DB
        config_queries.update_config(config_msg.guild.id, config_msg.channel.id, chosen_game)

        # Update instances
        inside = False
        for instance in instances:
            if instance.channel_id == config_msg.channel.id:
                if chosen_game == 'None':
                    instances.remove(instance)
                else:
                    instance.game = instance.create_game(chosen_game)
                    instance.game_name = chosen_game
                inside = True
                break
        if inside == False and chosen_game != 'None':
            instances.append(Instance(config_msg.guild.id, config_msg.channel.id, chosen_game, client))

        if chosen_game == 'None':
            embed_msg = 'All games have been disabled for this channel!'
        else:
            embed_msg = chosen_game + ' has been enabled for this channel!'
        config_embed = discord.Embed(title = embed_msg, colour=0xE5D2BB)
        return config_embed