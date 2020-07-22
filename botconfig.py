import discord
import asyncio
import ChooseYourAdventure.commands
import Jaegermore.commands
import WarriorsvsSoldiers.commands
import AttackonWikia.commands
from openpyxl import load_workbook

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
            if instance.channel_id == str(message.channel.id):
                return instance

    return None

def get_config_msg(cur_game):
    config_msg = 'Which game would you like to enable for this channel?'
    if cur_game:
        config_msg += '\n(Current game: ' + cur_game.game_name + ')'
    config_msg += '\n\n:one: Choose Your Adventure\n\n\
:two: Jaegermore\n\n\
:three: Warriors vs Soldiers\n\n\
:four: Attack on Wikia'
    return config_msg

def config_bot(config_msg, client):
    # Configures bot for the channel and return embed message
    if config_msg == None:
        return discord.Embed(title = 'Config has timed out after 60 seconds. Type `~config` to start again.', colour=0xE5D2BB)
    else:
        options = {
            '1️⃣':'Choose Your Adventure', 
            '2️⃣':'Jaegermore', 
            '3️⃣':'Warriors vs Soldiers', 
            '4️⃣':'Attack on Wikia'
        }
        chosen_game = options[config_msg.content]

        # Swap game if found in instances, otherwise append to it
        # For excel sheet
        wb = load_workbook("config.xlsx")
        instance_data = wb['Instances']
        i = 0
        inside = False
        for row in instance_data:
            i += 1
            if row[0].value == 'Server IDs':
                continue
            if row[1].value == str(config_msg.channel.id):
                instance_data['C' + str(i)] = chosen_game
                inside = True
                break
        if inside == False:
            instance_data.append([str(config_msg.guild.id), str(config_msg.channel.id), chosen_game])
        
        wb.save("config.xlsx")

        # For instances
        inside2 = False
        for instance in instances:
            if instance.channel_id == str(config_msg.channel.id):
                instance.game = instance.create_game(chosen_game)
                instance.game_name = chosen_game
                inside2 = True
                break
        if inside2 == False:
            instances.append(Instance(str(config_msg.guild.id), str(config_msg.channel.id), chosen_game, client))

        config_embed = discord.Embed(title = chosen_game + ' has been enabled for this channel!', colour=0xE5D2BB)
        return config_embed