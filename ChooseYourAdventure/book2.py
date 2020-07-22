import discord

class Book():
    def __init__(self, state):
        # Constants
        self.intro_msg = 'Welcome to the Attack on Titan adventure game!\n\n\
This is Book 2.\n\n\
**If you\'re ready, type `~start` to begin.**'

        self.reset_msg = discord.Embed(title = 'Game Reset!', description = 'Type **`~start`** to start a new game.\nType **`~intro`** for more information about the game.', colour=0xE5D2BB)

        self.EC = {'0️⃣':0, '1️⃣':1, '2️⃣':2, '3️⃣':3, '4️⃣':4, '5️⃣':5, '6️⃣':6, '7️⃣':7, '8️⃣':8, '9️⃣':9, '🔟':10, '⏩':11, '㊙':'s'}
        self.EC2 = {0:'0️⃣', 1:'1️⃣', 2:'2️⃣', 3:'3️⃣', 4:'4️⃣', 5:'5️⃣', 6:'6️⃣', 7:'7️⃣', 8:'8️⃣', 9:'9️⃣', 10:'🔟', 11:'⏩', 's':'㊙'}

        self.secrets = {}

        self.all_pages = {1:self.P1}

        self.endings = {}

        # Variables
        self.cur_page = [1]
        self.choices = [[]]
        self.response2 = ['']
        self.state = state

    def page_flipper(self, option):
        self.all_pages[self.cur_page[0]](option)
        return self.all_pages[self.cur_page[0]]()

    def P1(self, *option):
        if option == ():
            response = 'This is Book 2.\n\n\
❗Tip: Type **~stats** to bring up the battle report card.\n\n\
❗Tip: Type **~help** to see the list of available commands.\n\n\
Type 1⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 2