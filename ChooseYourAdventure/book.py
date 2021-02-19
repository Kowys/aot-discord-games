import discord

class Book():
    def __init__(self, state):
        # Constants
        self.intro_msg = 'Welcome to the Attack on Titan adventure game!\n\n\
You are a member of the 104th Training Corps, a nameless soldier fighting in the Battle \
of Trost.\n\n\
The battle against the overwhelmingly powerful Titans is not an easy one. A single \
wrong move could lead to your grisly death on the field.\n\n\
However, with careful judgment and appropriate action, you can survive and even contribute to a \
victory. You may even save some of your friends who otherwise would be fated to die.\n\n\
**If you\'re ready, type `~start` to begin.**'

        self.reset_msg = discord.Embed(title = 'Game Reset!', description = 'Type **`~start`** to start a new game.\nType **`~intro`** for more information about the game.', colour=0xE5D2BB)

        self.EC = {'0️⃣':0, '1️⃣':1, '2️⃣':2, '3️⃣':3, '4️⃣':4, '5️⃣':5, '6️⃣':6, '7️⃣':7, '8️⃣':8, '9️⃣':9, '🔟':10, '⏩':11, '㊙️':'s'}
        self.EC2 = {0:'0️⃣', 1:'1️⃣', 2:'2️⃣', 3:'3️⃣', 4:'4️⃣', 5:'5️⃣', 6:'6️⃣', 7:'7️⃣', 8:'8️⃣', 9:'9️⃣', 10:'🔟', 11:'⏩', 's':'㊙️'}

        self.secrets = {'what a terrible state of affairs':146, 'what a terrible state of affairs.':146,
        'survey corps with its wealth of experience':189,
        'he looks around wildly for help':265, 'he looks around wildly for help.':265,
        'the scene seems somehow unreal':198, 'the scene seems somehow unreal.':198,
        'protect their defenseless charge':232, 'protect their defenseless charge.':232,
        'if you had a horse':279, 'if you had a horse,':279,
        'he seems somehow uneasy':243, 'he seems somehow uneasy...':243,
        'marco is lucky':2881, 'marco is lucky.':2881,
        'a way to break this impasse':139,
        'the top students in your trainee class':207,
        'in the midst of a battle rife with cruelty':128,
        'a keen look in her eyes':32,
        'she has a goal in mind':214,
        'a matching codeword':801}

        self.annie_secrets = {139: 1, 207: 2, 128: 3, 32: 4, 214: 5}

        self.all_pages = {1:self.P1, 2:self.P2, 3:self.P3, 4:self.P4, 5:self.P5, 6:self.P6, 7:self.P7, 8:self.P8, 801:self.P801, 8011:self.P8011, 802:self.P802, 9:self.P9, 901:self.P901, 10:self.P10, 
        11:self.P11, 12:self.P12, 13:self.P13, 15:self.P15, 16:self.P16, 17:self.P17, 18:self.P18, 19:self.P19, 20:self.P20, 21:self.P21, 22:self.P22, 23:self.P23, 24:self.P24, 25:self.P25, 
        26:self.P26, 27:self.P27, 28:self.P28, 29:self.P29, 30:self.P30, 31:self.P31, 32:self.P32, 33:self.P33, 34:self.P34, 35:self.P35, 36:self.P36, 
        37:self.P37, 38:self.P38, 39:self.P39, 40:self.P40, 41:self.P41, 42:self.P42, 43:self.P43, 44:self.P44, 45:self.P45, 46:self.P46, 48:self.P48, 49:self.P49, 50:self.P50, 
        51:self.P51, 52:self.P52, 53:self.P53, 54:self.P54, 5411:self.P5411, 55:self.P55, 56:self.P56, 57:self.P57, 58:self.P58, 59:self.P59, 60:self.P60, 
        61:self.P61, 62:self.P62, 63:self.P63, 64:self.P64, 65:self.P65, 66:self.P66, 67:self.P67, 68:self.P68, 69:self.P69, 70:self.P70, 71:self.P71, 
        72:self.P72, 73:self.P73, 74:self.P74, 75:self.P75, 76:self.P76, 77:self.P77, 78:self.P78, 79:self.P79, 80:self.P80, 81:self.P81, 82:self.P82, 83:self.P83,  
        84:self.P84, 85:self.P85, 86:self.P86, 87:self.P87, 88:self.P88, 89:self.P89, 90:self.P90, 91:self.P91, 92:self.P92, 
        93:self.P93, 94:self.P94, 95:self.P95, 96:self.P96, 97:self.P97, 98:self.P98, 99:self.P99, 101:self.P101, 102:self.P102, 103:self.P103, 
        104:self.P104, 105:self.P105, 106:self.P106, 107:self.P107, 108:self.P108, 109:self.P109, 110:self.P110, 111:self.P111, 112:self.P112, 113:self.P113, 
        114:self.P114, 115:self.P115, 116:self.P116, 117:self.P117, 118:self.P118, 1181:self.P1181, 
        119:self.P119, 120:self.P120, 121:self.P121, 122:self.P122, 123:self.P123, 124:self.P124, 125:self.P125, 126:self.P126, 128:self.P128, 129:self.P129, 
        130:self.P130, 131:self.P131, 132:self.P132, 133:self.P133, 134:self.P134, 135:self.P135, 136:self.P136, 137:self.P137, 138:self.P138, 139:self.P139, 140:self.P140, 
        141:self.P141, 142:self.P142, 143:self.P143, 144:self.P144, 145:self.P145, 146:self.P146, 147:self.P147, 148:self.P148, 149:self.P149, 150:self.P150, 
        151:self.P151, 152:self.P152, 153:self.P153, 154:self.P154, 155:self.P155, 156:self.P156, 157:self.P157, 158:self.P158, 159:self.P159, 160:self.P160, 161:self.P161, 162:self.P162, 
        163:self.P163, 165:self.P165, 166:self.P166, 1661:self.P1661, 167:self.P167, 168:self.P168, 169:self.P169, 
        170:self.P170, 171:self.P171, 172:self.P172, 173:self.P173, 174:self.P174, 175:self.P175, 176:self.P176, 177:self.P177, 178:self.P178, 179:self.P179, 180:self.P180, 181:self.P181, 182:self.P182, 
        183:self.P183, 184:self.P184, 185:self.P185, 186:self.P186, 187:self.P187, 188:self.P188, 189:self.P189, 190:self.P190, 
        191:self.P191, 192:self.P192, 193:self.P193, 194:self.P194, 195:self.P195, 196:self.P196, 
        197:self.P197, 1971:self.P1971, 198:self.P198, 199:self.P199, 200:self.P200, 201:self.P201, 202:self.P202, 203:self.P203, 204:self.P204, 
        205:self.P205, 206:self.P206, 2061:self.P2061, 207:self.P207, 208:self.P208, 209:self.P209, 210:self.P210, 
        211:self.P211, 212:self.P212, 213:self.P213, 214:self.P214, 215:self.P215, 216:self.P216, 217:self.P217, 218:self.P218, 219:self.P219, 220:self.P220, 
        221:self.P221, 222:self.P222, 223:self.P223, 224:self.P224, 225:self.P225, 226:self.P226, 227:self.P227, 228:self.P228, 229:self.P229, 230:self.P230, 231:self.P231, 232:self.P232, 
        233:self.P233, 234:self.P234, 235:self.P235, 236:self.P236, 237:self.P237, 238:self.P238, 239:self.P239, 240:self.P240, 241:self.P241, 242:self.P242, 243:self.P243, 
        244:self.P244, 245:self.P245, 246:self.P246, 247:self.P247, 248:self.P248, 250:self.P250, 251:self.P251, 
        252:self.P252, 253:self.P253, 254:self.P254, 255:self.P255, 256:self.P256, 257:self.P257, 258:self.P258, 259:self.P259, 260:self.P260, 261:self.P261, 262:self.P262, 263:self.P263, 
        264:self.P264, 265:self.P265, 266:self.P266, 267:self.P267, 268:self.P268, 269:self.P269, 
        270:self.P270, 271:self.P271, 272:self.P272, 273:self.P273, 274:self.P274, 275:self.P275, 276:self.P276, 277:self.P277, 278:self.P278, 279:self.P279, 280:self.P280, 281:self.P281, 
        282:self.P282, 283:self.P283, 284:self.P284, 285:self.P285, 286:self.P286, 287:self.P287, 288:self.P288, 2881:self.P2881, 289:self.P289, 290:self.P290, 
        291:self.P291, 292:self.P292, 293:self.P293, 294:self.P294, 295:self.P295, 296:self.P296, 297:self.P297, 298:self.P298, 300:self.P300, 3001:self.P3001, 301:self.P301, 
        302:self.P302, 303:self.P303, 304:self.P304, 305:self.P305, 306:self.P306, 309:self.P309, 3091:self.P3091, 310:self.P310, 311:self.P311, 312:self.P312, 313:self.P313, 314:self.P314, 315:self.P315,
        316:self.P316, 317:self.P317, 318:self.P318, 319:self.P319}

        self.endings = {145: 'Trial of Eren and Mikasa', 187: 'A Soldier\'s Duty', 200: 'An Ordinary Moment of Happiness', 203: 'Failure of the Reclamation Plan', 2061: 'Jean Kirstein of the Survey Corps', 
        213: 'A Narrow Victory', 215: 'Armin Arlert\'s Dream', 218: 'A Regular Soldier', 250: '104th Annihilated at HQ', 263: 'Junior High', 264: 'The Fall of Wall Rose', 
        287: 'Failure to Reclaim Trost District', 290: 'A Moment\'s Peace', 296: 'Eren Flees', 3001: 'Captain Levi\'s Recruit', 301: 'Mikasa\'s True Face', 304: 'Nameless Hero', 305: 'Eren Yeager\'s Hand', 
        3091: 'Sasha Blouse\'s Promise', 310: 'The Girl Who Hid Her True Self', 311: 'The Death of a Merchant', 312: 'No Regrets', 313: 'Jean of the Military Police', 315: 'Joining the Garrison'}

        # Variables
        self.cur_page = [0]
        self.choices = [[]]
        self.response2 = ['']
        self.state = state
        self.new_msg = None

    def page_flipper(self, option):
        self.all_pages[self.cur_page[0]](option)
        return self.all_pages[self.cur_page[0]]()

    def P1(self, *option):
        if option == ():
            response = 'A vast face appears from nowhere. Although it is human-shaped, it\'s also eerily \
skinless, its scarlet muscles standing exposed to the air. But you don\'t have even enough time to \
be distracted by its strangeness.\n\n\
A stunning wave of steam hits you. Your vision goes white; you feel yourself being blown away. Your \
mind feels as fogged as your vision. For a second, you don\'t know what\'s happening.\n\n\
You are thrown into the air. You\'re more than 50 meters above the ground. Above you, the blue sky \
is oddly peaceful. Below, you can see the reddish-brown roofs of the town. From here, they look like \
toys.\n\n\
❗Tip: Type **~stats** to bring up the battle report card.\n\n\
❗Tip: Type **~help** to see the list of available commands.\n\n\
Type 1⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 2

    def P2(self, *option):
        if option == ():
            response = 'You are 50 meters above the ground, but you won\'t be for long. What do you do?\n\n\
:one: Flail in the air, looking for something to grab on to\n\n\
:two: Use some gas to propel yourself farther into the air\n\n\
:three: Use vertical maneuvering, set an anchor, and grapple along the wall'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 3
        elif option[0] == 2:
            self.cur_page[0] = 4
        elif option[0] == 3:
            self.cur_page[0] = 5

    def P3(self, *option):
        if option == ():
            response = 'You find no handholds in the sky. There\'s a huge wall several meters away \
from you, but no matter how far you stretch out your arms you won\'t reach it. Helpless, you hit the \
ground and die.\n\n\
**You have died. To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P4(self, *option):
        if option == ():
            response = 'You let some gas out of the machine at your hip...but it doesn\'t change the \
speed of your fall. Someone more experienced might have been able to use the gas to effect a slight \
change in altitude, but it would not be enough to check the fall, or to fly. Someone more experienced... \
Someone more experienced in what?\n\n\
Before you can remember, you strike the ground, shattering your body.\n\n\
**You have died. To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P5(self, *option):
        if option == ():
            response = 'What is vertical maneuvering? What is an anchor?\n\n\
You may not remember, but your body does.\n\n\
Moving quickly in midair, you pull out the pistol-shaped control mechanism that had been in a holster \
at your side. You spin to face the wall, and pull the lever on the grip in your hand. Launchers on each side \
of you send out spear-tipped anchors. They bury themselves in the wall, trailing wires behind them. \
You stop falling and grapple against the wall. Pulling the trigger on the near side of your control \
device releases bursts of pressurized gas. A spool winds up the wires, and with its help, you plant \
your feet on the wall and begin to climb.\n\n\
You remember: you can control your position in midair, in a way not only impossible but unthinkable \
for a normal person. You lean against the thin wires, with the device supporting your weight. This \
skill is what you have to show for three years of blood, sweat, and tears. \n\n\
What do you do?\n\n\
:one: Carry on the fight\n\n\
:two: Try to recall the events in Trost leading up to this moment **(Plays the tutorial)**'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 96
        elif option[0] == 2:
            self.cur_page[0] = 7

    def P6(self, *option):
        if option == ():
            response = 'Would you like to play the tutorial?\n\n\
:one: Yes\n\n\
:two: No, let\'s get to the action!'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 7
        elif option[0] == 2:
            self.cur_page[0] = 96

    def P7(self, *option):
        if option == ():
            response = 'You remember. You are part of the 104th Training Corps, stationed at the Wall Rose \
South District training camp.\n\n\
There are camps to the east, west, south, and north, and you\'re at the one closest to the front line.\n\n\
After three years of brutal training, you and your classmates are on the cusp of graduating and receiving \
your official- or at least, you were.\n\n\
Why... Why now...?\n\n\
You think back to just a few hours earlier, when Trost was a peaceful city.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 8

    def P8(self, *option):
        if option == ():
            response = '**List of Comrades and Affinity**\n\n\
The Battle Report Sheet lists your brothers and sisters in arms - your classmates in the 104th Training Corps \
as well as other soldiers on the battlefield with you. It doubles as a casualty register. If you see one of \
these people die in battle, or if you receive word of their death, their status will be updated accordingly.\n\n\
You can also have a degree of **Affinity** with certain other characters. To start with, your **Affinity** with \
all characters is zero, but may change due to actions you take during the story.\n\n\
❗At any point in the game, you may type **~stats** to bring up the Battle Report Sheet.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 801

    def P801(self, *option):
        if option == ():
            response = '**Secrets Hidden Throughout the Game**\n\n\
During your journey, you might discover secret codewords which can be used in another scenario to achieve \
a different outcome. Taking stock of these codewords and paying close attention to the story is essential \
to discovering the secrets they lead to, which may give you a chance to change your situation - or your destiny.\n\n\
If you find a matching codeword somewhere, copy and paste the exact phrase as your response. If successful, \
the symbol :secret: will appear as a reaction. This means you have unlocked the secret option. Then simply \
type in the emoji :secret: to choose the secret option.\n\n\
Try typing \"**a matching codeword**\" now to try it out.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 802
        elif option[0] == 's':
            self.cur_page[0] = 8011

    def P8011(self, *option):
        if option == ():
            response = 'Great job, you have found a secret! How many can you find in the actual story?\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 802

    def P802(self, *option):
        if option == ():
            response = '**Different Endings**\n\n\
This game depicts the Battle of Trost, seen in Volumes 1-4 of the Attack on Titan manga.\n\n\
There are a number of possible endings.\n\n\
Depending on your choices, you may receive a worse ending than that in the manga: humanity may be defeated, or \
characters who survived in the original version may die.\n\n\
On the other hand, if you manage to survive the fight, you may get different endings based on your **Affinity** \
with various characters.\n\n\
There is even the possibility that, if you solve the puzzles and truly distinguish yourself, the story may \
develop or conclude differently from the original; you may even be able to save your friends from a brutal \
death.\n\n\
❗At any point in the game, you may type **~info** to see your rank and the list of endings you\'ve obtained.\n\n\
Everything depends on your choices.\n\n\
Choose so that you are left with no regrets.\n\n\
Are you ready?\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 9

    def P9(self, *option):
        if option == ():
            response = 'You are walking through the urban area known as Trost District.\n\n\
You are a member of the 104th Training Corps. Your unit is based in Trost District, and for three years you \
have been training at a camp outside the city.\n\n\
Trost is at the southernmost point of Wall rose, the front line of humanity\'s defense. Your unit boasts that \
of the eight training corps attached to the various districts, yours is the most elite.\n\n\
You remember the tragedy of five years ago - a century of peace shattered by the attack of the Colossal Titan, \
and the destruction of the first barrier, Wall Maria. Humanity was forced to flee deep into its territory, \
losing 20% of its population...\n\n\
You were just a child then. That attack was the reason you joined the Training Corps. The training was painful \
and brutal, but all your classmates were good people.\n\n\
There was the boy **Eren**, devoted to destroying every last Titan. The girl **Mikasa**, with her extraordinary \
physical abilities. **Armin**, a boy small in stature but great in intellect... There was the gentle, thoughtful \
**Marco**, while Reiner, reliable and brotherly, earned the trust of everyone in the \
unit. **Annie** was reticent and hard to get to know, but she excelled as a soldier. You\'d like to enter the \
same regiment as her.\n\n\
Silly Connie and ravenous **Sasha** were fun, too. **Krista** was always kind to everyone, and then there was \
the tall but timid Bertolt... You wonder what unit they all hope to join.\n\n\
You found the bully **Jean**, and the two lovebirds, **Hannah** and **Franz**, to be a bit aloof. Yet now that \
you\'re all going your separate ways, you can\'t help but feel a little sad...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 901

    def P901(self, *option):
        if option == ():
            response = 'You\'ve survived three grueling years of training together; yesterday was the graduation \
ceremony. Tomorrow you\'ll apply to the unit you hope to join, and finally be a real soldier.\n\n\
The units include the **Garrison**, which protects the people inside the wall; the **Military Police Brigade**, \
which guards the Interior and the king; and the elite **Survey Corps**, which ventures outside the Walls to do \
battle with the Titans...\n\n\
You think about which unit you\'ll join, and about which units your classmates are likely to enter. (The path that \
leads to the Military Police Brigade is narrow; only the top ten trainees in a class are admitted into the unit.) \
But for the moment, you and the others are wandering around Trost District.\n\n\
You have sundry duties to attend to, such as patrolling (that is, watching for enemy attacks) under the direction of \
the Garrison and cleaning your weapons, but you don\'t presently have any training exercises, and are meandering \
around Trost in relative freedom. Maybe they want to give you a chance to catch your breath before you enter regular \
duty. Taking advantage of the break, your classmates seem to have dispersed into town as well.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 10

    def P10(self, *option):
        if option == ():
            response = 'You look out at the town. The streets seem busier than they did when you first arrived here three \
years ago.\n\n\
Now, where to go...\n\n\
:zero: Riverbank\n\n\
:one: Back alley\n\n\
:two: Main street\n\n\
:three: Gate\n\n\
:four: Restaurant\n\n\
:five: Boulder\n\n\
:six: Headquarters\n\n\
:seven: Kids by the road side\n\n\
:eight: Inner gate\n\n\
:nine: Side street\n\n\
:keycap_ten: Tailor\n\n\
To ascend the wall, type :fast_forward:.'
            self.choices[0] = [0,1,2,3,4,5,6,7,8,9,10,11]
            return response
        elif option[0] == 0:
            self.cur_page[0] = 11
        elif option[0] == 1:
            self.cur_page[0] = 15
        elif option[0] == 2:
            self.cur_page[0] = 16
        elif option[0] == 3:
            self.cur_page[0] = 21
        elif option[0] == 4:
            self.cur_page[0] = 25
        elif option[0] == 5:
            self.cur_page[0] = 31
        elif option[0] == 6:
            self.cur_page[0] = 34
        elif option[0] == 7:
            self.cur_page[0] = 43
        elif option[0] == 8:
            self.cur_page[0] = 48
        elif option[0] == 9:
            self.cur_page[0] = 50
        elif option[0] == 10:
            self.cur_page[0] = 53
        elif option[0] == 11:
            self.cur_page[0] = 38

    def P11(self, *option):
        if option == ():
            response = 'While walking along the riverbank, you spot your fellow trainee, Armin.\n\n\
It looks like he\'s sitting and reading a book. He\'s smart, but you\'ve heard rumors he reads forbidden books.\n\n\
When you talk to him, Armin smiles. \"It\'s not a forbidden book. Even I\'m not crazy enough to walk around town carrying something \
like that. I\'m not a kid anymore.\"\n\n\
He shows you what he\'s reading. It\'s something technical. You recall that during training, anytime he wasn\'t in class learning tactics \
or techniques, he was studying intently. He\'s not just smart, he\'s a hard worker.\n\n\
\"What about you? Are you interested in books about...the outside world?\"\n\n\
You...\n\n\
:one: Are interested\n\n\
:two: Are not interested'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 23
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P12(self, *option):
        if option == ():
            response = 'Hannah and Franz are talking excitedly together.\n\n\
\"You\'d look beautiful no matter what you wore,\" says Franz.\n\n\
Hannah responds, \"I don\'t need a dress or a fancy wedding as long as I have you, Franz.\"\n\n\
What a conversation. Apparently they\'re already making plans for their wedding.\n\n\
Well, what can you expect from the two notorious lovebirds?\n\n\
To talk to someone else, type :one:.\n\n\
To pick another destination, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 53
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P13(self, *option):
        if option == ():
            response = 'You find yourself on a narrow side street well away from the broad main road.\n\n\
Your fellow trainees Reiner, Bertolt, and Annie appear to be talking about something.\n\n\
They were excellent trainees - all three of them made the top ten.\n\n\
You hear Annie say, \"See you later, then,\" before she walks away.\n\n\
:one: Follow Annie\n\n\
:two: Approach Reiner and Bertolt\n\n\
:three: Go farther down the lonely side street'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 32
        elif option[0] == 2:
            self.cur_page[0] = 49
        elif option[0] == 3:
            self.cur_page[0] = 15

    def P15(self, *option):
        if option == ():
            response = 'You are in a narrow, dim back alley near the riverbank. You spot a newspaper lying on the ground as you walk. \
It\'s the Berg Newspaper, published in Stohess District, in the eastern part of Wall Sina, far to the interior.\n\n\
You pick it up to take a look, and spot the following headline: \"*Survey Corps, Humanity\'s Hope, Launches 56th Expedition Beyond \
Wall.*\" And an article: \"*104th Training Corps to become full soldiers at long last. We have high hopes for these stalwart \
young defenders.*\"\n\n\
It\'s about you. You feel your chest puff out with pride.\n\n\
Suddenly, you hear an angry voice from beside you.\n\n\
\"Newspapers, pah! Fulla lies!\" It\'s a drunk man. \"Like their \'Plan to Take Back Wall Maria\' four years ago. Some plan! \
It was just a way to get rid of people they couldn\'t feed. Even kids know it - but will the papers write about it?\"\n\n\
He points to you and says: \"Trainee, huh? Wonder what the papers\'ll say about *you* if things go south for the men in charge.\"\n\n\
At that moment, another man approaches. He apologizes to you, and drags the drunk away.\n\n\
\"It\'s just the alcohol talking. Please, ignore him.\"\n\n\
Then he turns to the first man, but you can still hear him:\n\n\
\"You better watch it. You go around talking like that, the MPs are going to take you in...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 10

    def P16(self, *option):
        if option == ():
            response = 'You\'re on the city\'s bustling main street. Vendors\' stalls line both sides of the broad, stone-paved avenue, the \
place alive with locals walking around and doing their shopping. Carriages and carts rattle through from time to time.\n\n\
You see your fellow trainees, Eren, Franz, and Hannah. They seem to be having a friendly chat.\n\n\
\"It\'s pretty lively here for a front-line city.\"\n\n\
\"Things are different from five years ago.\"\n\n\
:one: Talk to Eren\n\n\
:two: Talk to Franz and Hannah\n\n\
:three: Eavesdrop on passers-by'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 41
        elif option[0] == 2:
            self.cur_page[0] = 26
        elif option[0] == 3:
            self.cur_page[0] = 36

    def P17(self, *option):
        if option == ():
            response = '\"Eren? He definitely stood out, but not in a good way. Like, he was too serious. He had decent combat sense, though.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 33

    def P18(self, *option):
        if option == ():
            response = 'You see Reiner not far away.\n\n\
\"Th-That would look great on her... She\'d be beautiful...\"\n\n\
You completely agree, but Reiner does seem a bit creepy right now.\n\n\
To talk to someone else, type :one:.\n\n\
To choose a new destination, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 53
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P19(self, *option):
        if option == ():
            response = 'Annie\'s expression shifts ever so slightly. Then she shrugs and says, \"Yeah, sure. I\'m gonna apply to the \
Military Police Brigade and head for the Interior. It\'ll be goodbye, boring frontier town.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 46

    def P20(self, *option):
        if option == ():
            response = 'Your fellow trainee, Mikasa Ackerman, is there.\n\n\
She stares silently at the dress, her black hair barely touching the old scarf she keeps wrapped around her neck.\n\n\
She says nothing, and you can\'t tell what she\'s thinking. As usual.\n\n\
You...\n\n\
:one: Say \"I\'ll bet it\'d look great on you too, Mikasa!\"\n\n\
:two: Say \"I\'ll bet you\'d surprise the heck out of Eren if you wore that!\"\n\n\
:three: Leave her alone and talk to someone else'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 51
        elif option[0] == 2:
            self.cur_page[0] = 35
        elif option[0] == 3:
            self.cur_page[0] = 53

    def P21(self, *option):
        if option == ():
            response = 'The gate mounted in the city\'s outer wall is so large it can be seen from anywhere in town.\n\n\
As suggested by the name \"Wall Rose,\" a huge crest of the goddess Rose is emblazoned on it.\n\n\
It is only when you approach the gate for yourself and gaze up at it that you realize just how big it is. \
Even cannons would barely scratch it, let alone a single human.\n\n\
The gate is at once the border of human territory and a barrier against the Titans that roam outside. There is \
a mechanism to raise and lower the gate, but it is hardly ever opened. These days, it is mainly used to accomodate \
the Survey Corps, who venture forth in efforts to learn about the world outside the wall.\n\n\
In fact, just today...mere hours earlier, the Survey Corps set out from this gate.\n\n\
If you reflect on that moment, type :one:.\n\n\
To choose a new destination, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 22
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P22(self, *option):
        if option == ():
            response = 'You think back to a few hours earlier.\n\n\
The townspeople had turned out to see the Survey Corps off on another of their expeditions. You were among those who \
stood and watched them go.\n\n\
The Survey Corps is composed of the most elite soldiers. Until five years ago, they were the only unit to have actual \
combat experience against the Titans. All of them were on horseback, followed by specially built military supply wagons.\n\n\
The number of soldiers and wagons seemed larger than usual this time. Perhaps they were planning an especially long \
expedition.\n\n\
They looked so trustworthy. Their leader, Erwin, had gathered brave men and women of long service.\n\n\
**Captain Levi** is particularly well known. Rumor has it he\'s a one-man army... That\'s probably an exaggeration, \
but nonetheless, he seems to deserve his nickname \"Humanity\'s Strongest Soldier.\"\n\n\
When you saw him, you were taken aback by how small he was. He didn\'t look very friendly, though nothing else about \
him jumped out at you. But it\'s surprising how often the truly strong are like that.\n\n\
The townspeople clamored. Many were cheering, but you also heard more than a few shouts of \"Why bother going \
outside the Wall?\" and \"If you\'re such great soldiers, stay here so you can protect us when we need it!\"\n\n\
That\'s the scene you remember.\n\n\
To climb the outer wall, type :one:.\n\n\
To choose a new destination, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 38
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P23(self, *option):
        if option == ():
            response = 'When he realizes you\'re interested, Armin begins to talk.\n\n\
\"According to this book I read when I was a kid...\"\n\n\
It was a book about the outside world, and Armin says it mentioned fiery water, a continent of ice, snowbound deserts... \
He says a strange word, one you barely know: *sea*.\n\n\
There\'s far more water in the \"sea\" than is in the canal. Probably enough to cover the entire area inside the walls. In \
fact, apparently the majority of the outside world is \"sea\", and the land rose up out of it. But even though the land \
covers less than half the world\'s surface, there is still vastly more of it than is contained within the walls.\n\n\
That tells you how big the \"sea\" must be - and it\'s salt water. So much salt the merchants could never squeeze it \
all out...\n\n\
You can hardly imagine it. It\'s like a myth, or a flight of fancy.\n\n\
You ask Armin if he really believes all that. He smiles sadly.\n\n\
\"In my mind...no,\" he says.\n\n\
Maybe he really doesn\'t, or maybe he doesn\'t quite trust you. Having an interest in the world outside is considered \
taboo among the populace. It isn\'t expressly forbidden for military trainees, but neither is it smiled upon.\n\n\
\"But...it is true that that book gave me my interest in the outside world,\" says Armin.\n\n\
He\'s choosing his words carefully, but he can\'t hide the light in his eyes.\n\n\
\"It might not be the dreamlike world from my book, but I\'m certain the outside world is huge...and I want to see it \
for myself.\"'
            if self.state.flags.armintutorial == 'No':
                response = response + '\n\n**Your Affinity with Armin has increased by 1!**'
                self.state.affinities.armin += 1
                self.state.flags.armintutorial = 'Yes'
            response = response + '\n\nType :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 24

    def P24(self, *option):
        if option == ():
            response = 'Two other trainees approach. It\'s Eren and Mikasa.\n\n\
\"Hey,\" Eren says to you happily. \"So you heard Armin\'s story too, huh? How about you join the Survey Corps with \
me, then? We\'ll exterminate the Titans and see what\'s outside!\"\n\n\
Armin smiles to see Eren this way.\n\n\
If you remember correctly, Eren used to live in Shiganshina District, the one that was attacked by the Titans.\n\n\
These three seem to share a special bond even for trainees: it isn\'t just that they\'re childhood friends, or what \
they\'ve survived together. Maybe it\'s their drive to see the outside world.\n\n\
Mikasa is looking at you with a stern expression.\n\n\
You ask her which unit she wants to join, but she tells you it\'s none of your business.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 10
            
    def P25(self, *option):
        if option == ():
            response = 'You find an eatery just off the main street, and it smells delicious.\n\n\
You see your fellow trainee Sasha staring hungrily just outside the shop.\n\n\
You think back to what you knew of her during training. She was always starving. She once stole a potato from the \
kitchen, an act the instructor made her pay dearly for.\n\n\
She looks as hungry as ever, right down to the thread of drool dangling from her mouth. Yuck...\n\n\
\"Hey,\" says an annoyed Connie as he goes by, \"you\'re scaring the customers away. They\'re gonna run you off.\"\n\n\
To talk to Sasha, type :one:.\n\n\
To choose another destination, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 52
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P26(self, *option):
        if option == ():
            response = 'Franz and Hannah are seriously in love with each other. Today they\'re walking along together, \
as usual.\n\n\
In training, they\'d been such an item that people started calling them \"the lovebirds.\"\n\n\
\"What, you mean like husband and wife?\" Franz would respond. \"No way! It\'s way too soon for that!\"\n\n\
And Hannah: \"Us, a nice couple? Eep!\"\n\n\
All right, they didn\'t say it. But their faces turned beet red. It was enough to embarass you.\n\n\
Today they\'re the same as always. You assume they\'ll apply to the same unit. Sometimes you found them grating in \
training, but the thought of not seeing their lovey-dovey faces again makes you a little sad.\n\n\
:one: Talk to someone else\n\n\
:two: Choose another destination'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 16
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P27(self, *option):
        if option == ():
            response = 'There\'s no sign of Annie Leonhart. She\'s probably not interested in a place like this.\n\n\
If you talk to someone else, type :one:.\n\n\
To choose another destination, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 53
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P28(self, *option):
        if option == ():
            response = 'As you prepare to leave, you notice some of your fellow trainees nearby.\n\n\
It\'s Eren, Armin, and Mikasa.\n\n\
You think you hear one of them say, \"Just like we used to be.\"\n\n\
They seem happy to be thinking of the past - but also somehow sad. You can\'t quite bring yourself to call out to them.\n\n\
You remember the three of them are all survivors of the Titan attack that destroyed Shiganshina District five years ago.\n\n\
They must have been so young. What hell did they witness...?\n\n\
Type :one: to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 10

    def P29(self, *option):
        if option == ():
            response = '\"The Military Police Brigade, obviously,\" Jean says, a little too loudly.\n\n\
Come to think of it, all three of them were among the top ten scorers in your class. If they want, they can join the MPs, \
the king\'s elite guard unit.\n\n\
\"Why someone would want to join the Survey Corps is beyond me,\" Jean goes on with a smirk. \"You guys know what I mean?\"\n\n\
Connie gives a click of his tongue. He seems a little miffed by Jean\'s attitude.\n\n\
Indeed, Jean was not very well liked in training, and his mouth was part of the reason. He seemed to particularly rub Eren \
the wrong way, and they often got into arguments and even fistfights.\n\n\
\"Hmm, yeah,\" Marco answers calmly. \"I\'m gonna go into the Military Police too. I\'ve always really admired them.\"\n\n\
The way he says it turns your stomach a little. Marco is a thoughtful boy whose gentle personality, the polar opposite of \
Jean\'s, won him a lot of friends in the unit. Maybe he just said what he said to be polite - since only the top ten \
trainees can get into the MPs.\n\n\
But you can\'t shake a sense of paradox: the better a soldier someone is, the more likely they are to get tucked away in \
the Military Police Brigade, far from battle.\n\n\
You think someone with Marco\'s character would make a great leader in combat...\n\n\
There are other trainees you know just across the way - if you approach them, type :one:.\n\n\
If you head away from the main street, type :two:.\n\n\
To choose another destination, type :three:.'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 16
        elif option[0] == 2:
            self.cur_page[0] = 13
        elif option[0] == 3:
            self.cur_page[0] = 10

    def P30(self, *option):
        if option == ():
            response = '\"...Hmph. Hand-to-hand combat isn\'t even part of our grade. As a soldier, you\'ll never need it.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 33

    def P31(self, *option):
        if option == ():
            response = 'The city is home to a boulder the size of a small mountain. There appears to be excavation work going on, \
but it is a very large rock; even if the excavation succeeds, it will be hard to move. You can hear people talking in the \
street as they go by.\n\n\
\"They say the army\'s digging that rock out so they can use it to block up a hole if the wall is ever damaged.\"\n\n\
\"Yeah? And if they do dig it up, how are they gonna move it? The army...pfft. What a bunch of worthless freeloaders.\"\n\n\
Type :one: to choose another destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 10

    def P32(self, *option):
        if option == ():
            response = 'Annie turns onto a deserted back street.\n\n\
She\'s certainly a beautiful girl, with a good sense of style and gorgeous blonde hair, but her sharp features and hawkish \
nose give her an intimidating air. She has a keen look in her eyes, and doesn\'t seem eager to let anyone get close to her.\n\n\
In training, she had been aloof and rarely showed emotion. She didn\'t seem to have any real friends. As you recall, she \
placed fourth in the class.\n\n\
When you call out to her, Annie stops and looks back.\n\n\
\"Oh, it\'s you,\" she says disinterestedly. \"What do you want?\"\n\n\
:one: \"Why do you want to join the MPs, Annie?\"\n\n\
:two: \"You have incredible fighting skills. Where did you learn them?\"\n\n\
:three: \"What do you think of Eren?\"'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 42
        elif option[0] == 2:
            self.cur_page[0] = 30
        elif option[0] == 3:
            self.cur_page[0] = 17
        elif option[0] == 's':
            self.cur_page[0] = 44

    def P33(self, *option):
        if option == ():
            response = '\"Is that all you wanted to ask? If you\'re done, I\'m gonna get out of here,\" Annie says.\n\n\
**From this point on, if you see the words \"a way to break this impasse\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\
If you ask another question, type :one:.\n\n\
To choose another destination, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 32
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P34(self, *option):
        if option == ():
            response = 'You come to the city\'s military headquarters building. It\'s noticeably taller than most of the town\'s \
other structures. Its architecture is distinct, too, as it\'s a sturdy building made of stone. It reminds you of a fortress.\n\n\
You count the windows and come up with seven floors, but floors one through four have high ceilings, making the headquarters \
even taller than you\'d expect. The first floor is big enough for entire wagons to go in and out. It contains storage for \
supplies, gas tanks for vertical maneuvering equipment, and replacement parts, among other things.\n\n\
It is both a supply base and the command center for the regiment that protects Trost District.\n\n\
A swarm of soldiers mills around it.\n\n\
\"You one of the trainees?\" an older soldier asks. The insignia on her chest shows the two-stemmed rose: she\'s a member \
of the Garrison.\n\n\
You salute, and she returns the gesture. She has thick eyebrows and a knowing look behind a pair of spectacles.\n\n\
Perhaps she knows you were just now taking in the building, because she looks up at it and says:\n\n\
\"The headquarters is built to last. It should hold even against a Titan attack. ...Although if it ever has to, everything \
may already be lost.\"\n\n\
Type :one: to choose another destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 10

    def P35(self, *option):
        if option == ():
            response = '\"...What?\" Mikasa\'s eyes go unusually wide and she looks at you. \"M-Maybe,\" she murmurs, a little \
embarassed.\n\n\
You\'re surprised to realize she has a soft side.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 39

    def P36(self, *option):
        if option == ():
            response = 'You can hear the townspeople talking.\n\n\
You hear some say: \"It was awful five years ago, but things are peaceful now. And we have the soldiers to protect us.\"\n\n\
But there are others:\n\n\
\"Sheesh. Just getting by is hard enough without those useless soldiers to feed.\"\n\n\
:one: Talk to someone else\n\n\
:two: Choose another destination'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 16
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P37(self, *option):
        if option == ():
            response = 'Annie narrows her eyes and goes silent for a second, but soon says:\n\n\
\"Yeah. It\'s a habit from our combat exercises. I guess I don\'t need it now that our final grades are out.\"\n\n\
That\'s right... On several occasions, they had you break up into squads and do a mock-combat exercise in which \
Trost was attacked by Titans.\n\n\
She wasn\'t just wandering the city streets at random. This was probably how she\'d learnt the lay of the land, \
the buildings... That\'s what got her into the top scorers.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 45

    def P38(self, *option):
        if option == ():
            response = 'A massive, 50-meter wall surrounds the city. Atop it you can see the fixed cannons and some soldiers \
on patrol. Here and there along the wall are elevators to carry people and material to the top.\n\n\
Now - what do you do?\n\n\
:one: Your watch shift is beginning. Ascend the wall\n\n\
:two: There\'s still someplace you want to visit in town'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 54
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P39(self, *option):
        if option == ():
            response = 'You see Jean not far away.\n\n\
\"Her black hair would be perfect with that white dress,\" he\'s muttering. \"Man, it was so long and beautiful...what a waste...\"\n\n\
Suddenly he glares at you.\n\n\
\"What\'re you looking at?\"\n\n\
To talk to someone else, type :one:.\n\n\
To choose a new destination, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 53
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P40(self, *option):
        if option == ():
            response = 'Your fellow trainee, Krista Lenz, is there.\n\n\
Krista is staring intently at the dress with her clear, blue eyes.\n\n\
Is she...thinking of someone? You can\'t help but notice that with her golden hair and blue eyes, Krista is strikingly beautiful. \
That dress was made for a girl like her.\n\n\
The freckled girl next to her says teasingly, \"Is that longing I see?\" The girl is another one of your classmates.\n\n\
She had a sharp tongue, but she\'d always gotten along with Krista. What was her name again?\n\n\
Krista answers hesitantly, \"I just... I was hoping she could have a happy wedding. I was thinking how I have to dedicate \
myself as a soldier to protecting people like this...\"\n\n\
\"Hmph. Spoken like a true overachiever...\" The freckled girl gives a defeated shrug. \"Hey, Krista, don\'t you think \
that dress would look good on you? You\'d probably look more like a princess than a bride, though...\"\n\n\
She laughs. The freckled girl\'s words are harsh, but there doesn\'t seem to be any malice behind them.\n\n\
Krista... Krista makes an inscrutable expression. Maybe she\'s embarassed?\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 18

    def P41(self, *option):
        if option == ():
            response = '\"Oh, hey,\" Eren says. \"Have you decided which unit you\'re joining? I\'m going into the Survey Corps, \
naturally - I\'m gonna wipe out every last Titan!\"\n\n\
He\'s really worked up about this. Come to think of it, he was always like that in training, too.\n\n\
\"Oh, yeah,\" he adds, \"don\'t forget you\'re on duty today. Come to the Outer Wall when it\'s time for your shift. Anyway, \
I\'m gonna hit the town and enjoy our last chance to relax. Careful you don\'t spend all your time playing around!\"\n\n\
:one: Talk to someone else\n\n\
:two: Choose a new destination'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 16
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P42(self, *option):
        if option == ():
            response = '\"... \'Cause it\'ll get me to the Interior.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 33

    def P43(self, *option):
        if option == ():
            response = 'Some children are playing on the flagstones.\n\n\
A few of them come over when they realize you\'re a trainee.\n\n\
One is an outgoing boy; another boy seems quieter. A girl is with them. They must be about ten years old.\n\n\
\"Hey, you\'re a soldier, aren\'t you?\" the energetic boy says, flushing.\n\n\
\"I saw the Survey Corps leaving through the gate this morning. They\'re so cool! When I grow up, I\'m gonna join \'em! \
I\'ll be just like Captain Levi!\"\n\n\
The girl comes closer, too. These kids seem to be obsessed with soldiers.\n\n\
You can\'t help feeling a bit pleased.\n\n\
\"You and your friends...\" the girl says. \"You\'ll beat the Titans for us, right?\"\n\n\
The quiet boy, probably a friend of the other two, speaks to you hesitantly:\n\n\
\"The Titans are scary...but I want to see what\'s outside the wall,\" he says. \"There\'s supposed to be way more \
space outside the Walls than inside them. If we had vehicles that could fly through the air like a bird, maybe \
we could go outside without running into the Titans...\"\n\n\
A flying vehicle? Kids get the strangest ideas in their heads. Something like that sure would make fighting and \
studying the titans easier, though.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 28

    def P44(self, *option):
        if option == ():
            response = 'You realize that while Annie seems disinterested at first glance, in reality she\'s carefully \
observing everything around her.\n\n\
She\'s not just taking in the sights. She\'s studying every building\'s location and height, trying to commit them \
to memory.\n\n\
What do you say to her?\n\n\
:one: \"Making sure you remember this place?\"\n\n\
:two: \"Thinking about what to do if there\'s a battle in Trost?\"'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 19
        elif option[0] == 2:
            self.cur_page[0] = 37

    def P45(self, *option):
        if option == ():
            response = '\"...I put a lot of effort into the combat exercises because they were worth a lot in our grades,\" \
she says with a shrug. Maybe she means Titans would never really attack Trost...or that it doesn\'t matter to her.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 46

    def P46(self, *option):
        if option == ():
            response = 'Even in training, Annie Leonhart had seemed aloof. It was almost as if she didn\'t trust the rest \
of you, not like your other classmates - especially Marco Bott.\n\n\
\"I\'m just making sure I take care of myself,\" she continues, as if reading your mind. \"When you\'re in combat, \
there are no guarantees your comrades will do what you\'d hope they would. They may not be bad people, but they\'re \
as likely to freeze in fear as they are to keep a cool head.\"\n\n\
She stares at you for a moment, then says:\n\n\
\"It looks like you\'re a pretty sharp observer yourself... Just be careful you don\'t rush to get yourself killed, \
trying to be a hero.\"\n\n\
**From this point on, if you see the words \"he/she has a goal in mind\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\
Type :one: to choose another destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 10

    def P48(self, *option):
        if option == ():
            response = 'North of the wall that surrounds the city, the wall that borders the rear of humanity\'s territory \
is known as the inner wall, or rear wall.\n\n\
Hence, the gate in the wall is known as the \"inner gate.\"\n\n\
The gate is emblazoned with a crest showing the profile of the goddess Rose, the symbol of the wall that bears her name.\n\n\
Beyond the inner gate is another urban area, and beyond that, fields and forests and villages. Follow the road north, and you \
will come to Ehrmich District at Wall Sina.\n\n\
The gate to the interior is a mirror of the gate to the outside: while the latter stays closed and is hardly ever opened, \
the former stays open and is rarely closed. Many come and go through it, including travelers and merchants, as well as \
those who commute to the farms near the city. When you and your regiment came to your training camp, it was this gate \
that you came through.\n\n\
Compared to the outer gate, which is patrolled by the Garrison, the inner gate is all but unguarded.\n\n\
This gate and wall would also serve as a last line of defense were Trost\'s outer wall ever to be compromised. The inner \
wall, like the outer one, bears fixed artillery emplacements. Though you hope humanity will never need to use them...\n\n\
If you head toward to outer gate, type :one:.\n\n\
To choose a new destination, type :two:'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 21
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P49(self, *option):
        if option == ():
            response = 'Reiner is well-built and gives the impression of a reliable older brother. Bertolt, in contrast, is \
taller, but comes across as timid. Although opposites, they\'re also friends, and you often see them together.\n\n\
At the moment, they\'re talking about something as they take in the town. Maybe it\'s for combat exercises. Not that \
they need to worry about those, now that you\'ve all graduated...\n\n\
When you call out, Bertolt seems oddly flustered.\n\n\
\"O-Oh,\" he starts, \"W-We\'re going to leave this place soon, and it\'s just a little...\"\n\n\
Reiner breaks in with his usual coolness: \"We were thinking about what would happen if Titans attacked.\"\n\n\
\"R-Reiner, what are you talking about?\" For some reason, Bertolt seems more and more upset, but Reiner, looking \
serious, goes on:\n\n\
\"Is it that strange? We\'re soldiers. We have to be ready for anything.\"\n\n\
He\'s right. Sometimes Reiner can seem a bit too serious, but he was one of the top graduates.\n\n\
If you go to look for Annie, type :one:.\n\n\
To choose a new destination, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 32
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P50(self, *option):
        if option == ():
            response = 'You\'re on a major road through town. You see a wide, flagstone-paved side street, crowded with carts and wagons. \
Along the street are places to unload cargo. Buildings, shops, and warehouses abound.\n\n\
You see your fellow trainees Jean and Marco, along with the shaven-pated Connie.\n\n\
The three of them appear to be discussing what unit they want to join.\n\n\
To talk to them, type :one:.\n\n\
To choose a new destination, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 29
        elif option[0] == 2:
            self.cur_page[0] = 10

    def P51(self, *option):
        if option == ():
            response = '\"...I doubt it. Besides, it would be hard to move in.\"\n\n\
Mikasa responds without a change of expression, in her usual detached tone. Then she touches the old scarf she\'s wearing and \
murmurs, \"It wouldn\'t suit me at all.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 39

    def P52(self, *option):
        if option == ():
            response = 'A man who looks like the owner comes out of the restaurant.\n\n\
\"You\'re trainees, aren\'t you? Our future protectors are welcome to a meal on me.\"\n\n\
He shows you to a table and brings out a steaming dish.\n\n\
\"Y-Y-You\'re the real hero!\" Sasha says with tears in her eyes, and falls upon the plate.\n\n\
\"No need to be shy, kids,\" he says - and you and Connie end up with bowls, too.\n\n\
It\'s sure better than the stuff they served at the training camp. It\'s a potato stew - nothing fancy, but it brings \
home how prosperous this town is, and how genuine your host.\n\n\
\"Umm,\" Sasha says, \"there wouldn\'t happen to be any meat around, would there?\"\n\n\
\"It\'s free food! Beggars can\'t be choosers!\" Connie says, giving her a bop on the head.\n\n\
But the shop owner just laughs, not bothered at all.\n\n\
\"Since our territory shrank five years ago, there have been strict limits on the number of livestock. Even in this \
city, meat\'s just for the richest merchants - or the highest-ranking soldiers.\"\n\n\
You, Sasha, and Connie thank the man profusely.\n\n\
Type :one: to choose another destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 10

    def P53(self, *option):
        if option == ():
            response = 'A tailor\'s shop faces the street. Here, women\'s dresses and gentlemen\'s suits are made to order.\n\n\
Places like this must be where the wealthy have their clothes made. The fact that it\'s here is proof of how well Trost \
is doing. Not that it has much to do with you. During training camp, you wore your military uniform all the time; \
the only civilian outfit you had was some old clothes you used as pajamas. Even once you\'re assigned to your new unit, \
you probably won\'t need to have new clothes made, even for your days off.\n\n\
Some of your fellow trainees are outside the shop, peering in.\n\n\
You take a look, too. You see a dresser and a mannequin torso, along with clothes and fabric on display.\n\n\
You also see a young woman in a pure white dress.\n\n\
An older woman, probably one of the employees, is smiling and pinning the dress.\n\n\
The young woman must be having her bridal gown fitted.\n\n\
She doesn\'t look poor, but neither does she seem especially rich - having this dress made is probably a once-in-a-lifetime \
event for her.\n\n\
Which of your friends do you notice?\n\n\
:one: Annie\n\n\
:two: Hannah\n\n\
:three: Mikasa\n\n\
:four: Krista'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 27
        elif option[0] == 2:
            self.cur_page[0] = 12
        elif option[0] == 3:
            self.cur_page[0] = 20
        elif option[0] == 4:
            self.cur_page[0] = 40

    def P54(self, *option):
        if option == ():
            response = 'You are on top of the outer wall of Trost District, 50 meters above the ground.\n\n\
This is the southernmost point of Wall Rose, directly above the gate.\n\n\
The top of the wall is about ten meters wide - that is to say, such is the wall\'s thickness.\n\n\
A rail runs along the wall, with the \"walltop fixed cannons\" mounted on it. They can be moved along the \
rail, and are fixed into place to be fired. Your unit\'s duties include patrol of the wall top and \
maintenance of these guns.\n\n\
You, along with Eren and Connie, are on duty now.\n\n\
\"I wanna join the Survey Corps,\" Connie says as he cleans a cannon. \"At least then I wouldn\'t \
be in the same unit as Jean!\"\n\n\
So he says, anyway, but you suspect Eren\'s influence. More than a few people have decided they want to join the Survey \
Corps because they were moved by Eren\'s passion.\n\n\
Some of Eren\'s squadmates - Thomas, Nac, and Mina - are working on nearby guns, and come to join the conversation.\n\n\
\"Say, everyone...\" Sasha says. \"I borrowed a little meat from the senior officers\' private stock. Let\'s all \
share it together.\" She pulls a hunk of ham out of her pack.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 5411

    def P5411(self, *option):
        if option == ():
            response = 'Your comrades offer various astonished remarks.\n\n\
\"That\'s dumb even for you!\"\n\n\
\"You wanna get tossed in the stocks?!\"\n\n\
You\'re just about to get your unit assignments. What is she thinking?\n\n\
Since the Titan attack five years ago, meat has become a previous commodity on account of humanity\'s diminished \
territory. She\'s committed a serious violation.\n\n\
\"It\'s fine,\" Sasha says easily, putting the meat away with a smile. \"Once we take our land back, we can raise \
more cows and sheep, too...\"\n\n\
All the others look startled.\n\n\
\"I get it,\" says Thomas. \"A little pre-celebration for the retaking of Wall Maria.\"\n\n\
Humanity will retake Wall Maria, which it lost to the Titans, and it is you newly-minted soldiers who will do it.\n\n\
The thought spreads among those of you gathered on the wall. Of what Sasha has done, but also why. Then again, \
maybe she was just hungry.\n\n\
Everyone pipes up once more.\n\n\
\"Well, then, I\'ll have some of that meat, too!\"\n\n\
\"Save some for me!\"\n\n\
Defeating the Titans, taking back Wall Maria... It sounds like a dream, but with these people by your side, you \
think maybe you can do it.\n\n\
No - you\'re *sure* you can.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 55

    def P55(self, *option):
        if option == ():
            response = 'From the heights of the outer wall, you can see the world outside Wall Rose.\n\n\
Near the wall is an abandoned city. There were people there until five years ago.\n\n\
No one lives there now, but it remains surprisingly well-kept; from a distance it could be mistaken for a normal \
town. Titans attack humans, not empty buildings.\n\n\
Far off in the distance, a great mountain range rises up to meet the sky. You know Wall Maria, ruined five years \
ago, must be out there as well, but even a wall 50 meters high fades into the horizon from here. Such is the \
scope of what humanity has lost.\n\n\
The sky vaults above your head and reaches out farther than you can see, clear and blue.\n\n\
You look out at the town that spreads out beneath that peaceful sky. It could almost be filled with people living normal lives.\n\n\
Just sky, sky, sky, and the mountains far away.\n\n\n\
Then, suddenly...\n\n\n\
With no warning, a giant face appears.\n\n\
It\'s a head taller than even the 50-meter wall - the Colossal Titan.\n\n\
With a start, you are brought back to the present.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 96

    def P56(self, *option):
        if option == ():
            response = 'You\'ve made it back to the top of the wall...but now you realize that the spot \
just beneath your feet has a huge gouge in it.\n\n\
It must be from where the Colossal Titan\'s arm struck the wall. You see the twisted remains of the \
cannon rail; of the guns themselves, there is no sign.\n\n\
Beyond the wall you can see the Colossal Titan, its exposed muscles obscured by clouds of scalding steam.\n\n\
You see Eren, facing this impossibly large opponent with his swords drawn.\n\n\
You...\n\n\
:one: Leap into the fray to help Eren\n\n\
:two: Can only watch\n\n\
:three: Seize the moment to help your injured friends'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 129
        elif option[0] == 2:
            self.cur_page[0] = 64
        elif option[0] == 3:
            self.cur_page[0] = 97

    def P57(self, *option):
        if option == ():
            response = 'You are assigned to the outer wall - the front line.\n\n\
Your orders are to join up with the front-line troops, aid them in executing any battle plans and get the lay of the land, then \
report back as needed.\n\n\
However, you are told, this is also the most dangerous area of operations. Only those who wish to go will be sent there.\n\n\
If you\'re having second thoughts, type :one:.\n\n\
If you find the courage to volunteer, type :two:.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 60
        elif option[0] == 2:
            self.cur_page[0] = 163

    def P58(self, *option):
        if option == ():
            response = 'As you watch dumbly, you see Eren rise, against every expectation. He flies crazily with the vertical \
maneuvering equipment, snatching Armin from the Titan\'s mouth. But it costs him his balance, and he winds up in the creature\'s \
jaws instead.\n\n\
You marvel that he has managed any of this with only one leg.\n\n\
\"You think I\'ll die here? Like this?\"\n\n\
He sounds so strong. ...But in the same instant, the Titan closes its mouth as if it has not heard him.\n\n\
Armin reaches out his hand. Just beyond his grasp, Eren\'s right arm, bitten off, falls uselessly to the ground.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 257

    def P59(self, *option):
        if option == ():
            response = 'The steam finally clears.\n\n\
Atop the ruined wall stands Eren.\n\n\
Did Eren kill it? For a second you think he may have, but Eren himself is staring vacantly into space.\n\n\
\"It\'s just like five years ago. It suddenly appears...and suddenly vanishes.\'\n\n\
There is much about Titans that is not well understood. Could such a Titan exist?\n\n\
At the moment, more pressing than the riddle of the Colossal Titan is the fact that the gate has been destroyed. A terrible hole \
gapes in it. The emergency materials will never be enough to cover it.\n\n\
What\'s more, all the fixed guns just above the gate have been smashed. It won\'t be long before Titans overrun the city.\n\n\
\"Trainees!\"\n\n\
Veteran soldiers from the Garrison rush up, landing nearby with their vertical maneuvering equipment.\n\n\
\"A plan has been put into effect with the appearance of the Colossal Titan. We\'re the vanguard squad. Leave the wall to us. You\'re \
to get back to headquarters, make your report, then follow whatever orders you\'re given.\"\n\n\
You and your friends salute, then head down into the city.\n\n\
Wheeled cannons have been pulled out onto the main street. They\'ve been lined up in front of the shattered gate to meet the \
inevitable Titan incursion.\n\n\
You head for the headquarters building deep in the city.\n\n\
The clanging of a bell reverberates throughout town, announcing the state of emergency.\n\n\
\"Please evacuate as we have drilled! Leave all personal belongings behind!\" The announcement can be heard far and wide.\n\n\
\"It\'ll be all right,\" somebody mutters. \"It\'s not like five years ago. We\'ve planned for the Colossal Titan, for a Titan \
attack. We\'ve got a strategy. We\'ve trained. This won\'t be like Shiganshina District five years ago...\"\n\n\
But you can hear the tremble in the soldier\'s voice.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 61

    def P60(self, *option):
        if option == ():
            response = 'Where have you been assigned in the defense of Trost district?\n\n\
:one: Forward group, with the vanguard\n\n\
:two: Middle guard, with Eren and Armin\n\n\
:three: Middle guard, with Jean, Krista and Sasha\n\n\
:four: Rear guard, with Mikasa'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 57
        elif option[0] == 2:
            self.cur_page[0] = 62
        elif option[0] == 3:
            self.cur_page[0] = 74
        elif option[0] == 4:
            self.cur_page[0] = 119

    def P61(self, *option):
        if option == ():
            response = 'You are at the Trost District headquarters.\n\n\
Headquarters personnel are standing at attention, receiving their orders, making their preparations, and then leaving.\n\n\
You and the other trainees are there too.\n\n\
\"Our strategy has been decided. We help the citizens evacuate safely out the back, meeting the Titan invasion from the front. \
Unfortunately, our most experienced troops, the Survey Corps, are currently on assignment outside the wall. The Garrison will \
have to execute the plan by themselves.\"\n\n\
A superior officer is giving orders.\n\n\
\"Trainees, you are to participate in the action with the Garrison. All of you succeeded in your graduation exercises. I expect \
you to succeed in this mission as well.\"\n\n\
You and your comrades salute just as you learnt in training.\n\n\
It\'s the salute of every soldier: you make a fist with your right hand and place it over your chest. It shows that your heart is \
dedicated to the cause.\n\n\
Throughout the headquarters, crowds of soldiers are hurriedly preparing to move out.\n\n\
All around, you can hear the fear as your classmates talk. Jean is especially upset. His face is pale.\n\n\
\"Damn,\" he mutters. \"Why did it have to be today? I would\'ve been in the Interior tomorrow!\"\n\n\
\"I will protect you,\" Franz says to Hannah. But his voice is shaking.\n\n\
**From this point on, if you see the words \"the scene seems somehow unreal\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 60

    def P62(self, *option):
        if option == ():
            response = 'You are assigned to Squad 34 with Eren and Armin, just as you were in the combat exercises.\n\n\
Eren calls out to the members of the squad with an incongruous smile.\n\n\
\"This is a good opportunity, don\'t you think? I mean, if we prove ourselves in this first battle before applying for the Survey \
Corps, watch how fast we get promoted up the ladder!\"\n\n\
Not to be outdone, your other comrades put in their two cents:\n\n\
\"You better believe we\'ll keep up our end of the fight! There\'s a lot of future Survey Corps members this time around!\"\n\n\
\"All right, let\'s just see who takes out the most Titans!\"\n\n\
Thomas, Mina, Nac, Mylius...everyone in the squad is itching to get to work. Only Armin seems too nervous to say anything...\n\n\
With Eren and the others by your side, you\'re sure you can win.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 115

    def P63(self, *option):
        if option == ():
            response = 'Your body is dark with cannon smoke and ash, and your ears ring from the explosions as the guns fire on.\n\n\
But the encroaching horde of Titans doesn\'t stop...\n\n\
Do you continue the barrage, or return to the rear to make a report?\n\n\
:one: Continue the barrage\n\n\
:two: Return to the rear to make a report'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 218
        elif option[0] == 2:
            self.cur_page[0] = 222

    def P64(self, *option):
        if option == ():
            response = 'You can\'t make yourself move. You\'ve heard about the Colossal Titan, but now, here, it hardly seems real. \
It is many times bigger than the Titan dummies you often faced off with in training. Steam that burns like fire rolls off its body. \
Facing it, Eren looks like a fly attacking a human. You can only marvel at his courage...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 152

    def P65(self, *option):
        if option == ():
            response = 'You take off running. You use your vertical maneuvering equipment to get onto a nearby building, from which you \
set your anchors in the outer wall and start up. The faint voices of dying soldiers drift up to you from below, but you block them \
out and make for the top alone.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 280

    def P66(self, *option):
        if option == ():
            response = '\"All right. It\'s a lot to handle...but I\'ll try.\"\n\n\
Marco gives everyone detailed instructions. Even the perennially ill-tempered Jean obediently follows his orders. It must be the \
warmth of Marco\'s personality.\n\n\
\"Just stay calm and do what we did in training. We\'ll take that Titan over there first.\" He pauses. \"I\'ll be the bait.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 219

    def P67(self, *option):
        if option == ():
            response = 'The retreat bell sounds at long last.\n\n\
\"A lot of people didn\'t make it... But I\'m so grateful we were able to help our friends,\" Krista murmurs, pain tingeing the \
smile on her face.\n\n\
You pass through the inner wall, into safety.\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 91

    def P68(self, *option):
        if option == ():
            response = 'The merchant shows no fear of Mikasa, but shouts boldly, \"Just try it! I\'m the boss of this town\'s \
merchant association! And I go way back with your employer! A single word from me can decide what happens to a grunt like you!\"\n\n\
\"And how would a dead man say a word?\"\n\n\
Mikasa has a strange look on her face. She isn\'t trying to intimidate the merchant; she\'s genuinely curious.\n\n\
\"B-Boss,\" says one of the man\'s subordinates, pale.\n\n\
The merchant finally caves, and orders his lackeys to pull the cart back and open the road.\n\n\
The assembled crowd gives a cheer.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 83

    def P69(self, *option):
        if option == ():
            response = 'As you advance into the city, you see destroyed buildings and the scattered corpses of soldiers.\n\n\
You see the Titans, too. There seems to have been an epic battle here on the front lines.\n\n\
You receive a report of your comrades who died in the line of duty, including Franz and Hannah.\n\n\
You see human shapes on the roofs of buildings all around the city center. They are your classmates from the Training Corps.\n\n\
This is strange... The retreat bell should have been audible from here, but no one has moved from the rooftops.\n\n\
Mikasa has noticed it, too. She lands on one of the rooftops.\n\n\
You see the faces of the Training Corps. Jean and Connie. All of them look utterly defeated.\n\n\
You spot Armin. You\'re sure he was part of Squad 34 with Eren and the others...\n\n\
He\'s sitting on the roof, his face bloodless.\n\n\
\"You\'re not hurt? Thank goodness you\'re all right,\" Mikasa says, walking up to him. \"Where\'s the rest of Squad 34?\"\n\n\
Type :one: to continue.'
            self.state.statuses.franz = 'Dead'
            self.state.statuses.hannah = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 70

    def P70(self, *option):
        if option == ():
            response = 'Armin can barely squeeze out an answer:\n\n\
\"Those five carried out their mission...and died bravely in battle...\"\n\n\
You think there must be a better way to tell an old friend about the death of someone to whom she was so close, but can\'t \
imagine what it might be.\n\n\
\"Eren... He went into that Titan\'s mouth, instead of me... To protect me...\" Armin says, half speaking, half crying.\n\n\
You...\n\n\
:one: Criticize Armin\n\n\
:two: Comfort Mikasa\n\n\
:three: Suggest a rescue attempt'
            self.state.statuses.eren = 'Dead'
            self.state.statuses.squad34 = 'Dead'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 76
        elif option[0] == 2:
            self.cur_page[0] = 177
        elif option[0] == 3:
            self.cur_page[0] = 234

    def P71(self, *option):
        if option == ():
            response = 'When you come to, you are lying on your side. Your body is shredded; half of it you can\'t even feel. Strangely, \
there is no pain.\n\n\
Krista is holding you and heaving with sobs.\n\n\
It looks like you managed to protect her.\n\n\
She\'s beautiful, angelic, and she\'s weeping for you.\n\n\
This sure is a better way to go than tumbling into some Titan\'s gullet...\n\n\
**You have died. Type `~reset` to start over.**'
            self.choices[0] = []
            return response

    def P72(self, *option):
        if option == ():
            response = 'You see soldiers firing the walltop guns.\n\n\
They\'re aiming for the Titans streaming through the hole in the gate, but the distance is impairing their accuracy. Few of their \
shots strike home.\n\n\
The soldiers\' mood is as dark as the smoke that billows from the cannons.\n\n\
\"Shit! We\'re not even gonna hold them up at this rate!\"\n\n\
\"The vanguard squad was our best hope...and they\'re gone...\"\n\n\
\"We might\'ve been able to resist if the Survey Corps was here. I can\'t believe an attack came the day they left!\"\n\n\
\"I wish we still had the guns on the outer wall. We could\'ve at least shot down at the Titans coming in.\"\n\n\
\"If you got time to whine, you got time to shoot! Load cannons!\"\n\n\
They can\'t stop the Titan invasion.\n\n\
On the ground below, the wheeled cannons are overrun; you hear the cries of men and women dying.\n\n\
You...\n\n\
:one: Help with the cannons\n\n\
:two: Try to get word to the Survey Corps\n\n\
:three: Descend to ground level'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 109
        elif option[0] == 2:
            self.cur_page[0] = 146
        elif option[0] == 3:
            self.cur_page[0] = 78

    def P73(self, *option):
        if option == ():
            response = 'You spot a trainee coming back from the front. It\'s Armin.\n\n\
\"Armin...are you alone? What happened to the rest of your squad?\"\n\n\
Armin, pale as the grave, falls to his knees. You realize Squad 34, including Eren, has been wiped out.\n\n\
Jean, his expression pained, mutters, \"That kid had a death wish... I told him this would happen!"\n\n\
Reports of soldiers killed in action are coming in from all over. There\'s more than you could have imagined. Trainees whose faces \
you knew are dying one after another. You hear Franz and Hannah\'s names among them.\n\n\
Jean, grinding his teeth, says only: \"Damn!\"\n\n\
Type :one: to continue.'
            self.state.statuses.eren = 'Dead'
            self.state.statuses.squad34 = 'Dead'
            self.state.statuses.franz = 'Dead'
            self.state.statuses.hannah = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 245

    def P74(self, *option):
        if option == ():
            response = 'You are assigned to the middle guard, as you were in combat exercises.\n\n\
You take in the members of your squad and the squads nearby.\n\n\
Jean, Krista, Sasha, Marco, Connie, and others, all familiar faces. You don\'t see Mikasa, Annie, Reiner, or the other top \
trainees. They must have been assigned to more important positions. You see Eren\'s Squad 34 head for the front, full of fight.\n\n\
You and your comrades here may not be the top of your class, but you\'ll have to get the job done.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 172

    def P75(self, *option):
        if option == ():
            response = 'You can barely bring yourself to do it - but you leave them behind. You have no choice.\n\n\
Krista moves to help them, but you hold her back yourself.\n\n\
Later, you link up with Jean and Connie, and a few others. It looks like they managed to survive, too.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 165

    def P76(self, *option):
        if option == ():
            response = 'You ask Armin why he ran away, alone.\n\n\
He has nothing to say, but only hangs his head in shame and quavers.\n\n\
Mikasa shoves you out of the way. \"I\'m glad you\'re alive,\" she says to Armin.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 177

    def P77(self, *option):
        if option == ():
            response = 'You and your comrades do an exemplary job of bringing down the Titans.\n\n\
When you stop to see whom you\'ve saved, you find they\'re also trainees.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 128

    def P78(self, *option):
        if option == ():
            response = 'If you refuse to hide, alone, and go to the ground to help your friends, type :one:\n\n\
If you think you can best help where you are, type :two:'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 123
        elif option[0] == 2:
            self.cur_page[0] = 72

    def P79(self, *option):
        if option == ():
            response = 'You decide to let Krista give the orders...what do you do?\n\n\
:one: Work to protect Krista\n\n\
:two: Avoid attacking, but try to provide relief\n\n\
:three: Hope she and her goody two-shoes act will get in trouble'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 99
        elif option[0] == 2:
            self.cur_page[0] = 148
        elif option[0] == 3:
            self.cur_page[0] = 168

    def P80(self, *option):
        if option == ():
            response = 'On your way to the rear, you run into Armin, standing in a torpor on a rooftop.\n\n\
\"What\'s wrong? Are you alone?\" one of your comrades asks. Armin tells you that the rest of his squad has been wiped out.\n\n\
The bile rises in your throat. That was Eren\'s squad.\n\n\
\"I\'m glad you survived, even if you\'re the only one,\" Krista says, trying to comfort him. But the twisting in his face \
suggests her words hurt him more than ever.\n\n\
He turns to your squad.\n\n\
\"Please,\" he says, \"take my report to headquarters. I\'m going back to the field.\" Without waiting for an answer, he \
launches off with his vertical maneuvering equipment.\n\n\
Your squad falls back toward the rear, bringing the broken Hannah with them.\n\n\
The retreat bell sounds at long last.\n\n\
You and the other soldiers in the rear pass through the inner wall, withdrawing into safety...\n\n\
Type :one: to continue.'
            self.state.statuses.eren = 'Dead'
            self.state.statuses.squad34 = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 91

    def P81(self, *option):
        if option == ():
            response = 'Mikasa seems to be worried about Eren, elsewhere on the battlefield.\n\n\
\"If I don\'t protect him...he\'ll get in trouble,\" she murmurs.\n\n\
True, Eren is all too ready to rush in headlong...\n\n\
What do you say to Mikasa?\n\n\
:one: \"If you\'re a real soldier, then obey orders and do your duty.\"\n\n\
:two: \"It\'s Eren! He\'ll be fine!\"\n\n\
:three: \"I\'ll create a diversion; you go find Eren!\"'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 169
        elif option[0] == 2:
            self.cur_page[0] = 103
        elif option[0] == 3:
            self.cur_page[0] = 211

    def P82(self, *option):
        if option == ():
            response = 'And so you act on the plan.\n\n\
Thankfully, it achieved its goals. But the sacrifice to do so was immense. Almost 80 percent of your comrades died.\n\n\
You and many of the others were decoys. You had nothing to do but flee. You were literally fodder. You saw friend after friend \
snatched from beside you and eaten by Titans. Titans in the 3-to-4-meter class don\'t swallow humans whole. They tear the living \
bodies apart and gnaw on bleeding flesh.\n\n\
You could do nothing. Nothing but run.\n\n\
That you are alive now is only a bit of luck. Good luck or bad, you can\'t tell.\n\n\
**If they were still alive, Armin, Franz, Hannah and Squad 34 are killed in this operation.**\n\n\
Type :one: to continue.'
            self.state.statuses.armin = 'Dead'
            self.state.statuses.franz = 'Dead'
            self.state.statuses.hannah = 'Dead'
            self.state.statuses.squad34 = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 284

    def P83(self, *option):
        if option == ():
            response = 'The evacuation resumes, and Mikasa returns to her position.\n\n\
You hurry to direct the evacuees, and help those who have been slow to flee. You\'re extremely concerned about another Titan attack, \
but thankfully, nothing serious follows. Thanks to Mikasa\'s actions, and the lives of many soldiers, the Titan invasion has been \
stopped.\n\n\
Finally, the evacuation is complete.\n\n\
\"Close the gate!\" With that order, the gate on the inner wall, and the route to the Interior, is sealed.\n\n\
You finally relax. A bell rings out. The soldiers in the city have been given the order to retreat.\n\n\
\"Give it some gas! All hands over the wall, retreat!\"\n\n\
The commander at your position gives the order, and you use your vertical maneuvering equipment to climb onto a rooftop. You find \
Mikasa there.\n\n\
\"The evacuation...is complete.\" She looks out at the city, her back to you. Then she says to the Garrison soldiers, \"I\'m going \
to go support the front line\'s withdrawal.\"\n\n\
You...\n\n\
:one: Follow Mikasa\n\n\
:two: Retreat past the inner wall'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 149
        elif option[0] == 2:
            self.cur_page[0] = 116

    def P84(self, *option):
        if option == ():
            response = 'The road through the inner gate, the path to safety, is roiling with bodies.\n\n\
It looks like the evacuation of the populace is taking longer than expected. The soldiers on the front line will do all they can \
to continue the fight until the evacuation is complete, but if they can\'t make it...\n\n\
There\'s a tremor from far away, a periodic rumble.\n\n\
Titan footsteps. And not far apart. It\'s running.\n\n\
\"It\'s a Titan!\"\n\n\
\"It\'s right over there!\"\n\n\
A Titan is running straight for you along the broad main street from the gate.\n\n\
The crowd is gripped with panic.\n\n\
A Titan of more than ten meters tall at a run can reach quite a pace. Soldiers pursue it with vertical maneuvering to defend, \
but no one can catch it.\n\n\
It must have come barreling past both the front and middle guards. It\'s an Abnormal.\n\n\
The Titan, a smile on its face, leans over and dashes for the assembled evacuees. Cries of despair run through the crowd.\n\n\
Then suddenly...\n\n\
You see a human form careen through the air behind the Titan. It\'s Mikasa, using her vertical maneuvering equipment.\n\n\
She slips through the air as if she really can fly, and soon catches up with the Titan.\n\n\
As she leaps, she sets an anchor in the running monster. Picking up speed, she reaches its neck and sinks her blades into its nape.\n\n\
With a crash, the Titan falls.\n\n\
Its head lands only steps from the crowd of evacuees. She was just in the nick of time.\n\n\
Still, you can only admire Mikasa\'s talent. You\'ve never seen anyone move like that.\n\n\
She always excelled during training, but how can she acquit herself like this in her very first battle with real Titans?\n\n\
Mikasa, for her part, jumps down to the ground with her usual bland expression, as if nothing special has happened.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 93

    def P85(self, *option):
        if option == ():
            response = 'Urban warfare against Titans is an ugly thing. It doesn\'t go like it did in training. Titans who fight back \
are far more terrifying than you had imagined.\n\n\
First one person, then another, falls to the monsters: other soldiers, classmates whose names you hardly know. With each one, Krista \
begins to weep afresh.\n\n\
She moves to face the Titans and protect your comrades, heedless of her own safety.\n\n\
You...\n\n\
:one: Risk your own life to protect her\n\n\
:two: Hold her back and tell her not to do anything rash'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 238
        elif option[0] == 2:
            self.cur_page[0] = 286

    def P86(self, *option):
        if option == ():
            response = 'With Eren in your arms, you use vertical maneuvering to head for the rear.\n\n\
You pause on a rooftop to bind the stump of his leg and stanch the bleeding. Eren groans, tears in his eyes. He must be in \
terrible pain, but you assume that isn\'t what makes him cry out.\n\n\
You pick him up again. You have no words to say to him. It\'s all you can do to work the maneuvering equipment with two people\'s \
weight.\n\n\
Type :one: to continue.'
            self.state.statuses.armin = 'Dead'
            self.state.flags.witheren = 'Yes'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 112

    def P87(self, *option):
        if option == ():
            response = 'You\'ve heard terrible news from a member of another squad: Headquarters has been surrounded by Titans, making \
it impossible to get any more gas for your vertical maneuvering equipment.\n\n\
The vertical maneuvering equipment allows a person to move at high speed using only a small machine; and to do so it requires \
pressurized gas, which it consumes at a high rate. Because of the hopeless battle you fought after the order to advance, your squad \
is nearly out of propellant. Even if you\'re careful to conserve it, you\'re not sure how long you can last...\n\n\
The rooftops around the headquarters building are populated with fellow soldiers who came here to be resupplied. Now they stand in \
shock. Things look bleak.\n\n\
Jean sits down on the roof and sighs. \"What a stupid life I had... If I\'d known it was going to end this way, I would\'ve just \
said something...\" You don\'t know what he\'s talking about, but he lapses into silence.\n\n\
Marco stands not far away. \"This is awful,\" he mutters. \"I was ready to die, but..I\'d hoped I would know what I was dying for...\"\n\n\
Reiner, Bertolt, and Annie are all close by. They\'re talking about how to handle the situation. But as skilled as they are, without \
gas even they are helpless...\n\n\
Everywhere you see your despairing brothers and sisters in arms. Sitting among them is Armin.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 124

    def P88(self, *option):
        if option == ():
            response = 'Heedless of your own safety, you launch yourself at the Titan.\n\n\
It spits out Thomas, whom it was about to eat; the lower half of his body is covered in Titan saliva, but he\'s alive.\n\n\
\"Everyone, stay calm and do what we learned in training!\" Eren says courageously.\n\n\
\"There\'s another one down below. Be careful!\"\n\n\
\"The small ones can be quick. Set your wires so you can strike and get away in one go.\"\n\n\
Everyone in Squad 34 takes a breath, then works together to bring down the Titans.\n\n\
\"We did it!\" Eren exclaims joyously.\n\n\n\
Everyone cheers. Your first victory in a real battle!\n\n\n\
But Armin says quietly, \"Real combat isn\'t like training at all. The sight and sound of a living Titan is something else. If \
any of us had made a single wrong move, we might all be dead now.\"\n\n\
Thomas groans; his leg has been hurt.\n\n\
Armin\'s right: you can\'t get too carried away.\n\n\
\"Let\'s take Thomas and fall back. We have to report that the frontline troops have been decimated, too.\"\n\n\
Squad 34, all its members alive, heads for the rear.\n\n\
Now you...\n\n\
:one: Join the middle group\'s defensive action and continue the fight\n\n\
:two: Take the wounded Thomas and withdraw through the inner gate'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 297
        elif option[0] == 2:
            self.cur_page[0] = 90

    def P89(self, *option):
        if option == ():
            response = 'You hear a bell ring out, clang, clang, clang, announcing that the populace has been evacuated. It\'s also the \
signal for the soldiers to retreat. Your duty today is finally over. You can fall back to safety...\n\n\
Then you notice a trainee, a young woman with black hair, coming your way.\n\n\
Armin calls out: \"Mikasa!\"\n\n\
In a single, fluid movement, Mikasa lands next to you.\n\n\
\"Hey, Mikasa!\" Eren says loudly. \"I wish you could\'ve seen my first battle! I\'ll bet you did pretty well yourself, but the \
Titan I took down was-\"\n\n\
Mikasa ignores what he\'s saying and catches him up in a hug.\n\n\
\"I\'m so glad you\'re alive.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 281

    def P90(self, *option):
        if option == ():
            response = 'You withdraw, taking the injured Thomas with you.\n\n\
You make for the headquarters building, but are informed that headquarters functions have been moved rearward, inside the inner gate. \
That\'s also the best place to get treatment for the wounded.\n\n\
You split off from the rest of Squad 34 and head for the inner gate.\n\n\
On the other side, the gate is more packed with evacuees and Garrison soldiers than you expected.\n\n\
Not all the squads have been as lucky as yours. You see badly-wounded soldiers, and hear reports of the battle not going in \
humanity\'s favor.\n\n\
You find a field hospital, but they tell you Thomas\'s injury is nothing, and to take him elsewhere. You\'re moved on from place \
after place. At last you find a first-aid center with some space. By the time you get Thomas settled there, a great deal of time \
has passed.\n\n\n\
Clang, clang, clang! You hear a bell ring out. The evacuation is finished, and the soldiers are being ordered to retreat.\n\n\
Are the others from Squad 34 still safe?\n\n\
From among the crowd, someone says to you, \"So you guys made it out, too?\" It\'s your fellow trainee, Krista. She\'s come here \
with a wounded squadmate of her own.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 252

    def P91(self, *option):
        if option == ():
            response = 'You, Krista, and the others withdraw beyond the inner wall.\n\n\
The far side of the wall is overflowing with evacuated soldiers and citizens.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 237

    def P92(self, *option):
        if option == ():
            response = 'You add your voice to Krista\'s.\n\n\
Perhaps moved by your pleas, the soldier nods and says, \"I can understand how you feel. I\"ll notify the defense squadron \
commander.\"\n\n\
Phew. You and Krista smile at each other.\n\n\
But...after the soldier leaves, the freckled girl gets a sour expression on her face and says, \"Not gonna happen. He won\'t \
notify a damn person. And even if he did, we\'d never get permission.\"\n\n\
This seems like a bit much even for someone who\'s known for her bad attitude. Krista looks disappointed, too.\n\n\
But she\'s right. No matter how long you wait, no help comes.\n\n\
You try to ask several more times, but you are turned away with only a harsh word.\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 144

    def P93(self, *option):
        if option == ():
            response = 'A greedy merchant has blocked the inner gate with a cart loaded down with goods.\n\n\
The gate is too small for the cart to pass through, but the merchant insists on trying to push it through anyway.\n\n\
So this is why the evacuation is taking so long.\n\n\
The merchant and some of his flunkies are trying to control the crowd.\n\n\
\"That cargo is worth more than all of you together could earn in a lifetime! Lend aid, and you\"ll be rewarded!\"\n\n\
What a self-serving thing to say when you\'ve blocked off the only escape route, putting people\'s lives at risk! This merchant \
is powerful enough that he\'s even got pull with the army; soldiers stand by helplessly.\n\n\
Then, Mikasa arrives.\n\n\
For an instant her eyes go wide, but she quickly returns to her usual flat expression.\n\n\
\"My comrades are dying as you speak,\" she says. \"They are dying holding off the Titans, to buy enough time for the evacuation.\"\n\n\
The merchant spits back, \"Of course they are! Give yourselves for the lives and the property of the populace - that\'s your duty as a \
soldier, isn\'t it?\"\n\n\
Mikasa takes a step closer to the merchant, sword in hand, expression unchanging.\n\n\
\"If you think it is so obvious that one person should die for another, then surely you\"ll understand...how the loss of your single, \
precious life may be forgiven in the interest of saving so many others.\"\n\n\
You...\n\n\
:one: Stand and watch\n\n\
:two: Take Mikasa\'s side. A guy like this deserves to die\n\n\
:three: Take the merchant\'s side\n\n\
:four: Jump in between Mikasa and the merchant and try to think of something'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 68
        elif option[0] == 2:
            self.cur_page[0] = 158
        elif option[0] == 3:
            self.cur_page[0] = 291
        elif option[0] == 4:
            self.cur_page[0] = 118

    def P94(self, *option):
        if option == ():
            response = 'You make a dash for the remaining cannon. A lone soldier is working it, his face covered in soot and sweat and fear. \n\n\
\"Thanks, trainee. Help me load \'er up!\"\n\n\
You load a cannonball into the gun, which is still so hot you fear you\'ll get burned.\n\n\
The soldier fires the cannon. There\'s an ear-splitting roar, and the cannonball rips into the leg of a Titan advancing toward you.\n\n\
The soldier whoops and throws up his arms. \"Take that, you damn monster!\"\n\n\
An instant later, though, a piece of debris kicked by another Titan comes flying through the air. You throw yourself to the ground.\n\n\
When you look back at the soldier, you see everything but his head.\n\n\
For the Titan, it had probably been like kicking a pebble. But humans are fragile things.\n\n\
You look forward again. The destroyed leg of the Titan in front of you is regenerating in a cloud of steam.\n\n\
**From this point on, if you see the words \"What a terrible state of affairs\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\
You...\n\n\
:one: Take over the cannon from the dead soldier\n\n\
:two: Ascend the wall\n\n\
:three: Run like hell'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 261
        elif option[0] == 2:
            self.cur_page[0] = 65
        elif option[0] == 3:
            self.cur_page[0] = 136

    def P95(self, *option):
        if option == ():
            response = 'Before you can say a word, the one-legged Eren speaks in a strained voice.\n\n\
\"Everyone\'s...dead... Even Armin... It...It should\'ve been me... Armin was the one...who told me about the outside world...if \
it weren\'t for him, I would\'ve...\"\n\n\
**From this point on, if you see the words \"protect their defenseless charge\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\n\
Mikasa\'s expression never changes, but she says, \"This is no time to be getting sentimental.\"\n\n\
She turns that same expressionless face to you. \"Are you the one who saved Eren?\"\n\n\
You nod, and she says simply, \"Please take care of him a little longer. I\'ll back you up.\"\n\n\
**Your Affinity with Mikasa has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 242

    def P96(self, *option):
        if option == ():
            response = 'You\'ve made your way back up the wall using vertical maneuvering. You collect \
your scattered wits and look around.\n\n\
It looks like everyone is all right. One trainee is unconscious, but Sasha is already setting her \
anchors and rescuing him.\n\n\
At that moment, a vast rumble threatens to turn heaven and earth upside-down, and the wall shakes \
violently.\n\n\
Chips fly up from directly below you - the gate has been pulverized!\n\n\
It\'s the Colossal Titan. The one that appeared suddenly in Shiganshina District and destroyed the \
wall there five years ago.\n\n\
You\'ve only heard stories - but now it seems to be happening again right in front of you!\n\n\
You hear your companions yelling - and screaming.\n\n\
You hear another explosion, this time from atop the wall, and see more fragments fly into the air \
in a cloud of smoke. Cannon barrels rocket into the sky like so much confetti.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 56

    def P97(self, *option):
        if option == ():
            response = 'Sasha immediately jumps down the wall to help your unconscious comrade. She\'s used one of the two guide wires \
of her vertical maneuvering equipment to stop his fall, and you doubt if a single wire can support the weight of two people. You rush \
down the wall to help. Samuel, the boy you\'ve rescued, is injured, but alive.\n\n\
**Your affinity with Sasha has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.sasha += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 104

    def P98(self, *option):
        if option == ():
            response = 'You and the others move to provide relief and extract your comrades still in the city.\n\n\
More and more Titans are wandering the streets.\n\n\
Injuries and casualties for both the rescued and the rescuers are hardly negligible...but still, you were able to save quite a \
few of your friends.\n\n\
You notice Eren among those you rescued. He thanks you:\n\n\
\"I\'m glad you came. Now we can strike back against those Titans!\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 213

    def P99(self, *option):
        if option == ():
            response = 'You have to protect something as pure as her.\n\n\
You agree with Krista, and plan to guard her with all your strength. You think people\'s morale will go up just by having her in \
charge. You tell her as much, as you say you\'re joining her command.\n\n\
\"B-But I would hate for you to get hurt,\" she says. That perfect smile again. You would gladly give your life for her.\n\n\
The freckled girl harumphs, but doesn\'t say anything.\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 85

    def P101(self, *option):
        if option == ():
            response = 'The ground forces are already nearly annihilated. The mobile guns deployed near the gate have been kicked \
apart by Titans.\n\n\
Occasionally a cannonball from the fixed emplacements on the wall flies over your head. The walltop guns were intended to fire \
outward - but with Titans running amok in the city, the only choice was to spin the guns around.\n\n\
You glance around, but see no other soldiers using vertical maneuvering nearby.\n\n\
Normally, the fixed guns use grapeshot to slow the Titans, after which elite soldiers finish them off with the help of vertical \
maneuvering equipment. Normally. That\'s what they taught you in training.\n\n\
But you gather all the soldiers involved in that strategy are gone.\n\n\
On the ground you see the corpse of a soldier, lying on its side, a sword in its hand.\n\n\
Now, what do you do?\n\n\
Other than the wall, there are few buildings in the immediate vicinity, making it hard for an inexperienced hand to fight the Titans.\n\n\
:one: Trust the gunners and focus on felling the Titans\n\n\
:two: Fight the Titans while dodging cannonballs\n\n\
:three: Give up and ascend the wall'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 155
        elif option[0] == 2:
            self.cur_page[0] = 120
        elif option[0] == 3:
            self.cur_page[0] = 280

    def P102(self, *option):
        if option == ():
            response = '\"We have to help the townspeople - and our friends!\" Krista says. \"B-But I don\'t want everyone here to be \
put in danger!\"\n\n\
Even here, on the battlefield, she sounds like an angel.\n\n\
The hard-eyed, freckled girl is there, of course. She snorts and says, \"Nice talk, but not practical. You always were an idealist, \
Krista.\"\n\n\
Maybe it would be better to :one: trust Jean with the command, or :two: Marco. If you decide to give Krista the command anyway, \
type :three:.'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 140
        elif option[0] == 2:
            self.cur_page[0] = 66
        elif option[0] == 3:
            self.cur_page[0] = 79

    def P103(self, *option):
        if option == ():
            response = '\"...You\'re right.\" Mikasa nods firmly. \"Eren promised me. Promised he wouldn\'t die.\"\n\n\
She seems to have regained her composure.\n\n\
**Your affinity with Mikasa has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 84

    def P104(self, *option):
        if option == ():
            response = 'Suddenly there\'s a roar like a volcanic eruption, and the area is filled with \
hot steam.\n\n\
Everything goes white; you can hardly see.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 59

    def P105(self, *option):
        if option == ():
            response = 'You help organize and direct the evacuation, but it seems to be going too slowly.\n\n\
Part of it is the suddenness of the Titan attack, but...it looks like there\'s a cart blocking the escape route. People are milling \
about near the road through the inner wall. It\'s chaos.\n\n\
From far off you hear a shout: \"It\'s an Abnormal!\"\n\n\
You see a Titan coming down the main street toward your position at a terrible speed.\n\n\
Veteran Garrison soldiers rush to respond, but the Titan is quicker than they are. It kicks at the ones in its path, or simply \
runs past those who are trying to intercept it with their vertical maneuvering equipment.\n\n\
The Titan dives into the crowd of evacuees.\n\n\
There\'s a sound of something breaking, and then a chorus of screams.\n\n\
You see people fly into the air.\n\n\
Rubble, debris, and human bodies tumble toward you -\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 145

    def P106(self, *option):
        if option == ():
            response = 'Two streets up, you see a Titan running at high speed. An Abnormal.\n\n\
\"The evacuees are that way!\"\n\n\
But Jean replies in a quavering voice, \"Don\'t go. The evacuation must be finished by now. And if it isn\'t, the elite soldiers \
are protecting the rear.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 267

    def P107(self, *option):
        if option == ():
            response = 'Before you can speak, Armin says in a strained voice, \"Those five carried out their mission...and died \
bravely in battle...\"\n\n\
You think there must be a better way to tell an old friend about the death of someone to whom she was so close, but you can\'t \
imagine what it might be.\n\n\
The other trainees, learning of this turn for the first time, cry out. But Mikasa is strangely calm. She says only, \"This is no \
time to be getting sentimental.\"\n\n\
You can\'t guess what she may be thinking.\n\n\
But she\'s right.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 117

    def P108(self, *option):
        if option == ():
            response = 'But...\n\n\
You see a signal flare rise up from the city.\n\n\
Red smoke. Something terrible has happened, or the plan has been aborted.\n\n\
What in the world is going on?\n\n\
At length, you observe a change in the behavior of the clustered Titans. Several of them begin walking toward the city, as if \
drawn by something.\n\n\
They\'re heading for the boulder...where Eren and the picked troops are staging their plan.\n\n\
You...\n\n\
:one: Take some of the gas tanks and head for Eren\'s position\n\n\
:two: Descend into the city and fight the departing Titans\n\n\
:three: See your duty through at your current position'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 205
        elif option[0] == 2:
            self.cur_page[0] = 212
        elif option[0] == 3:
            self.cur_page[0] = 187

    def P109(self, *option):
        if option == ():
            response = 'You join the soldiers firing the cannons. You shoot and shoot, knowing you won\'t stop the Titan invasion, \
knowing you can\'t help your fellow soldiers on the groud - with only the faith that it will be of some small use...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 63

    def P110(self, *option):
        if option == ():
            response = 'You stand by with Jean and the others.\n\n\
Rumors are running wild among your comrades: Eren turned into a Titan. He was eaten by a Titan. He was eaten by a Titan that \
then turned into him...\n\n\
You were told to stand by, but you can\'t shake the sense the Garrison soldiers all around are watching you. Does this have \
something to do with what happened to Eren?\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 258

    def P111(self, *option):
        if option == ():
            response = 'The plan...is a success.\n\n\
It was a close call. During the assault, only five of the seven Titans were killed.\n\n\
It\'s no one\'s fault - it was a risky plan to begin with. But it was Mikasa and Annie who brought down the last two.\n\n\
With no help from vertical maneuvering equipment, only their own strength, they\'d leapt three meters into the air to kill those \
Titans. Incredible.\n\n\
Thanks to the two women, the plan has miraculously come off.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 226

    def P112(self, *option):
        if option == ():
            response = 'Someone on the ground is shouting. It\'s Hannah.\n\n\
You settle to the ground.\n\n\
\"Franz isn\'t breathing. Help him!\"\n\n\
Weeping, she presses on his chest with all her strength, trying to bring him back to life.\n\n\
You take in the scene with a sense of unreality.\n\n\
The entire lower half of Franz\'s body is gone. He\'s obviously already dead.\n\n\
You...\n\n\
:one: Have no time for this. You leave the scene\n\n\
:two: Try to revive Franz\n\n\
:three: Drag Hannah away'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 221
        elif option[0] == 2:
            self.cur_page[0] = 154
        elif option[0] == 3:
            self.cur_page[0] = 181

    def P113(self, *option):
        if option == ():
            response = 'You make for the soldiers\' position once the Titans have left.\n\n\
Someone is on the ground, shouting. It\'s your classmate, Hannah.\n\n\
\"Help Franz!\" she cries as you land.\n\n\
Franz is just nearby...the top half of him is, anyway. And it\'s not moving.\n\n\
\"It\'s no use. He\'s long gone,\" the freckled girl says.\n\n\
Krista\'s face twists and she begins to cry.\n\n\
Hannah lets out one gasping sob after another, unwilling to give up on Franz - but you and the others push her off the body and \
drag her away. It\'s for her own safety. She can\'t be here, alone, in this state.\n\n\
Type :one: to continue.'
            self.state.statuses.franz = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 80

    def P114(self, *option):
        if option == ():
            response = 'It is a terrible plan, one likely to claim a great many lives. And yet - some may survive.\n\n\
Do you tell the others about the plan?\n\n\
:one: Think of another way\n\n\
:two: Do things this way'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 139
        elif option[0] == 2:
            self.cur_page[0] = 173

    def P115(self, *option):
        if option == ():
            response = 'Squad 34, move out!\"\n\n\
Eren gives the order, and the whole squad moves.\n\n\
Using your vertical maneuvering equipment, you jump from rooftop to rooftop. With each jump you reel your wires in, set a new \
anchor, then reel them in again, picking up speed each time. The wind whips around you, howling in your ears, as the reddish \
rooftops rush past.\n\n\
In between the buildings ahead, you see swaying humanoid silhouettes, a great many of them.\n\n\
It\'s the Titans. They\'re already past the middle guard!\n\n\
\"The Titans have come this far already?!\"\n\n\
\"What happened to the vanguard?\"\n\n\
The experienced Garrison soldiers up front were supposed to stop the Titans. That was the plan.\n\n\
And you were supposed to join the battle straight away.\n\n\
The battle has barely started, and it looks like the vanguard has already been shattered...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 217

    def P116(self, *option):
        if option == ():
            response = 'You know how Mikasa feels, and you have no intention of stopping her.\n\n\
You\'d probably just be a burden if you tried to go with her, though....\n\n\
You and the soldiers of the Garrison retreat past the wall.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 170

    def P117(self, *option):
        if option == ():
            response = 'Mikasa raises her sword above her head and proclaims, \"If we can clear out the Titans swarming the headquarters, \
we can get enough gas for everyone to make it over the wall.\"\n\n\
But the others aren\'t convinced: \"How will we take on that many Titans...?\"\n\n\
\"I can do it. Even if I have to do it myself. I am strong. And you...you\'re cowards. You mewling kittens and sit here and watch me.\"\n\n\
Her expression never changes as she speaks. She seems to be trying to goad the others to action, but she\'s not doing a very good job.\n\n\
\"If I fail, I\'ll die... But if I win, I\'ll live.\"\n\n\
Her words may be blunt, they they\'re true. Everyone there seems to realize it.\n\n\
\"And if we don\'t fight, we can\'t win.\"\n\n\
Without waiting for a response, she flies off in the direction of Headquarters.\n\n\
Jean mutters something, then rises to follow her.\n\n\
\"Hey! Were we taught to let one of our own fight alone?!\"\n\n\
The words seem to galvanize everyone. One after another they leap after Jean and Mikasa. You...\n\n\
:one: Follow Mikasa\n\n\
:two: Follow Jean'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 199
        elif option[0] == 2:
            self.cur_page[0] = 253

    def P118(self, *option):
        if option == ():
            response = 'You stand between them and offer your idea:\n\n\
Even the merchant can see the cart will never get through the tunnel. Why not have people carry the cargo through by hand, even \
just some of it? What can\'t be carried could be stashed in a spot unlikely to be attacked by Titans. Since Titans only attack humans, \
if the cargo were stored in a basement or other safe place, there would be a good chance of coming back to get it later...wouldn\'t \
there?\n\n\
\"Collect it later? If Trost District falls to the Titans, it would be lost to me!\" The merchant scrunches up his face, but after a \
moment he seems to start thinking like a businessman again, calculating. Finally, he nods. \"Fine. Far be it from the merchant Dimo \
Reeves to put his own property above the safety of the populace. I\'m sure you\'ll let everyone know what you\'ve seen here.\"\n\n\
He starts issuing orders to his cronies. \"Pull the cart back! Those with the Merchants\' Association, take as much cargo as you can \
carry!\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 1181

    def P1181(self, *option):
        if option == ():
            response = 'The townspeople cheer. With the road cleared, the evacuation resumes.\n\n\
There are taunting voices: \"So are you soldiers the pets of a few greedy businessmen?\" But mostly you hear words of gratitude.\n\n\
\"As a show of gratitude, I\'ll let you in on a little something,\" Dimo says. \"I left a delivery horse loaded with goods for the \
Garrison at the Merchants\' Association building. I knew as well as you do that the Titans don\'t attack non-human animals, and I \
gambled that it would survive. If it\'s still there, it\'s in a barn near the building. There\'s every chance the horse and all its \
supplies are gone, though - you\'re welcome to have a look yourself.\"\n\n\
He wears a cunning look and an incongruous smile. \"If the animal is there, I want you to report to the Garrison that Reeves the \
merchant provided them with supplies in their hour of need. I fully expect to collect a reward.\"\n\n\
Unlike the average pack horse, the horses that supply the Garrison are of exceptional pedigree and training. They do not quail even \
at the sight of a Titan, and have superb stamina. Back when you were being trained with the horses, you remember being told one of \
these animals was worth as much as a human life.\n\n\
You commit the location to memory and plan to make use of the animal if you have the chance and the need.\n\n\
**From this point on, if you see the words \"If you have/had a horse\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 83

    def P119(self, *option):
        if option == ():
            response = 'You are assigned to the rear group.\n\n\
This is supposed to be the last line of defense. If the Titans get past the front and middle guards, it will be your job to protect \
the evacuating citizens and make sure the Titans do not break through Wall Rose. Veteran soldiers of the Garrison are with you.\n\n\
You might have been picked for this assignment because of your superior ability - or it might just be they didn\'t think you could \
do any good up at the front. Either way, you\'d best help with the evacuation...\n\n\
You look up and see Mikasa. Looks like she\'s been assigned to the rear, as well. In the 104th Training Corps, she was the crème de \
la crème. It\'s only natural she would be stationed here. You\'re relieved to be near her.\n\n\
But...something\'s off. Her usual calm demeanor is gone; she seems skittish.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 81

    def P120(self, *option):
        if option == ():
            response = 'The cannonballs are even faster than you are with your vertical maneuvering equipment. Still, you try to fight \
while dodging the cannon fire - but the Titans aren\'t that stupid.\n\n\
As you struggle to maneuver, a massive hand grabs you out of the air.\n\n\
The Titan is struck by several cannonballs, taking off half its head, but it\'s already regenerating in a cloud of steam. Then it \
opens its huge mouth and swallows you whole.\n\n\
**You have died. Type `~reset` to start over.**'
            self.choices[0] = []
            return response

    def P121(self, *option):
        if option == ():
            response = 'Your comrades in Squad 34 bravely face down the seven-meter Titan that has appeared.\n\n\
They fire the wires of their vertical maneuvering equipment into the monster as they leap from the buildings and move to strike.\n\n\
\"We\'ve got to help Eren!\"\n\n\
But the Titan sweeps away the wires with its arm. Your friends miss their mark, or go flying into walls.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 132

    def P122(self, *option):
        if option == ():
            response = 'The female soldier with the glasses says to you:\n\n\
\"There\'s no point talking to you if you can\'t even make a calculation like that. It\'s not like the rest of us are watching \
our comrades die just for fun.\"\n\n\
And she leaves.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 144

    def P123(self, *option):
        if option == ():
            response = 'The ground level has become a hellscape.\n\n\
Titans pour in through the huge hole in front of you.\n\n\
You see the ruins of wheeled cannons and supply wagons. The mobile ground cannons never were as powerful as the fixed emplacements \
on the wall.\n\n\
Most likely, the ground crews were supposed to use the big guns to take out the Titans, supported by fire from the wall, while they \
used the materials in the wagons to plug the hole. You\'re sure they must have practiced it many times. But no battle plan survives \
contact with the Titans.\n\n\
Smoke and explosions whirl around you. Now and again, you can hear a faint voice among them. The neighing of horses. And the screams \
of people being eaten by Titans.\n\n\
You...\n\n\
:one: Make for the cannon and help with firing\n\n\
:two: Fight the Titans on horseback\n\n\
:three: Try to help the wounded'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 94
        elif option[0] == 2:
            self.cur_page[0] = 141
        elif option[0] == 3:
            self.cur_page[0] = 182

    def P124(self, *option):
        if option == ():
            response = 'You are standing on a building tall enough to see out over Trost District.\n\n\
The surviving members of the 104th Training Corps surround you.\n\n\
Many have gone limp with despair - with the scale of the destruction and the deaths of their friends, and more, with the knowledge \
that Headquarters had been surrounded and the supply of gas cut off.\n\n\
A bell rings: *clang*, *clang*, *clang*. That\'s the signal that the evacuation is complete. It\'s also the order for all soldiers to \
retreat. At last, you have fulfilled your duty. You can fall back to safety...\n\n\
You can\'t escape the irony that the retreat order should be issued now. Ascending the wall takes more gas than actual combat. \
With your remaining supply, you can\'t hope to withdraw.\n\n\
Then you notice a trainee with black hair coming toward you through the sky. It\'s Mikasa.\n\n\
She lands near you in a single, fluid movement.\n\n\
\"Where\'s the rest of Squad 34?\" she asks.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.eren == 'Alive' and self.state.statuses.armin == 'Dead':
                self.cur_page[0] = 95
            elif self.state.statuses.eren == 'Dead' and self.state.statuses.armin == 'Alive':
                self.cur_page[0] = 107
            elif self.state.statuses.eren == 'Dead' and self.state.statuses.armin == 'Dead':
                self.cur_page[0] = 244

    def P125(self, *option):
        if option == ():
            response = 'We can\'t let everyone endanger themselves! I\'ll be the decoy,\" Eren shouts, jumping up.\n\n\
He says he\'ll collect everyone\'s remaining gas, then go out and distract the Titans. As long as he\'s just running up to the roof, \
and not trying to fight, the modicum of gas should see him through.\n\n\
His plan is terrifyingly dangerous...but not without merit.\n\n\
\"I\'m going with you,\" Mikasa says, rising.\n\n\
Jean and several others raise their voices, inspired by the pair\'s determination.\n\n\
This decoy idea is a thin hope...but it\'s hope.\n\n\
If nothing else, the air in the room has changed. You have a plan.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 266

    def P126(self, *option):
        if option == ():
            response = 'A relief mission gets underway, organized by the veterans of the Garrison.\n\n\
You and the other trainees request to be part of the effort.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.eren == 'Alive':
                self.cur_page[0] = 98
            elif self.state.statuses.eren == 'Dead':
                self.cur_page[0] = 204

    def P128(self, *option):
        if option == ():
            response = 'The ones you rescued were Franz and Hannah.\n\n\
They hold each other jubilantly.\n\n\
\"You were so brave, Franz, shielding me like that...\"\n\n\
\"I just wanted to save you. That\'s all.\"\n\n\
You can\'t pry them apart. And you\'re pretty sure it was you and your friends who saved both of them...\n\n\
But then, they\'ve been lovebirds since training - and in the midst of a battle rife with cruelty, to see them warms your heart.\n\n\
\"Geez,\" someone mutters lightly, \"we should\'ve left you there.\"\n\n\
Type :one: to continue.'
            self.state.flags.memelevel += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 67
        elif option[0] == 's':
            self.cur_page[0] = 319

    def P129(self, *option):
        if option == ():
            response = 'You make a snap decision to support Eren. Your feet pound against the wall as you \
run in the opposite direction from him.\n\n\
The huge eyes roll in the huge face to leer down at you. If you can get the thing\'s attention, maybe \
that will help Eren.\n\n\
The Titan raises a massive, steam-clouded hand. You throw yourself from the top of the wall and run \
down the side. You fire your vertical maneuvering equipment\'s anchors into the side of the wall.\n\n\
**From this point on, if you see the words \"he/she looks around wildly for help\", copy and paste those words into the \
chat to reveal an additional option you may take.**\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 104

    def P130(self, *option):
        if option == ():
            response = 'Sasha agrees eagerly with your suggestion:\n\n\
\"Food! Great idea. Times like this, you need a good meal!\"\n\n\
You search the area and discover some provisions. Of course Headquarters would have emergency stores. You even find some meat, \
perhaps intended for the commanders. You and Sasha put it on plates and pass everyone a share.\n\n\
But not many find themselves able to eat. As they put the food in their mouths, some seem haunted by the memory of Titans \
eating their friends.\n\n\
You don\'t have much appetite, either. But you force yourself to eat, chew, swallow.\n\n\
It helps revitalize you, just a little. Your head starts to clear.\n\n\
You\'re not sure what the best plan is, but you know action is better than sitting still. You\'ve got some capable companions - \
they\'ll be able to figure something out.'
            if self.state.flags.sashaeaten == 'No':
                response = response + '\n\n**Your Affinity with Sasha has increased by 1!**'
                self.state.affinities.sasha += 1
                self.state.flags.sashaeaten = 'Yes'
            response = response + '\n\nType :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 139

    def P131(self, *option):
        if option == ():
            response = '\"Go back, damn you! Mikasa\'s still- \"\n\n\
Eren shouts and struggles violently in your arms.\n\n\
Selfish man. He has no idea how she feels.\n\n\
\"Stop! Stop it!\" His cries turn from anger to a howl of grief.\n\n\
\"Wasn\'t Armin enough? Not Mikasa, too- Curse me...!\"\n\n\
It hurts your heart - but you refuse to let it show on your face. You pick up speed with your vertical maneuvering equipment.\n\n\
At that instant, you\'re slammed by some impact, flung through the air.\n\n\
Is Eren struggling again? No, this was much too powerful...\n\n\
A Titan, then-?!\n\n\
You quickly right yourself, then roll along a rooftop, shedding speed.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 175

    def P132(self, *option):
        if option == ():
            response = 'A scene of surpassing horror unfolds before your eyes.\n\n\
A big-headed seven-meter Titan pulls one of your comrades close by the wires of his gear and grabs him.\n\n\
Nac and Mylius, unable to make use of their vertical maneuvering equipment, die screaming in the mouths of Titans.\n\n\
Mina, the girl who collided with the wall, is on the ground, motionless.\n\n\
Another Titan approaches. It has black hair and googly eyes. Just three or four meters tall, it stuffs Mina into its mouth \
head first. As Titans go, it\'s small. If her maneuvering gear were operational, she might well have been able to defeat it based \
on her training.\n\n\
Everyone had been so ready for battle just moments ago, and now...this. Who knew how different training was from real combat? \
This is a nightmare. It has to be.\n\n\
Type :one: to continue.'
            self.state.statuses.squad34 = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 133

    def P133(self, *option):
        if option == ():
            response = 'Eren is lying prone. One of his legs is gone. Is he even still alive?\n\n\
Armin appears to be in one piece, but he stares vacantly into space, eyes wide.\n\n\
Yet another Titan appears. Taller than the rooftops, with an old man\'s face and a long beard, its eyes are narrowed, its mouth \
half open. It plucks Armin off the rooftop and carries him toward its mouth...\n\n\
Are all of your friends going to die because of four Titans?\n\n\
You...\n\n\
:one: Look on helplessly\n\n\
:two: Face down the Titan and rescue Armin\n\n\
:three: Try to save Eren, at least, and withdraw'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 58
        elif option[0] == 2:
            self.cur_page[0] = 147
        elif option[0] == 3:
            self.cur_page[0] = 298

    def P134(self, *option):
        if option == ():
            response = 'A defensive regiment is formed with three elite soldiers of the Garrsion - Ian Dietrich, Mitabi Jarnach, \
and Rico Brzenska - each heading a squadron.\n\n\
You and Mikasa are assigned under them. It\'s dangerous work, but you were given it because you\'re close to Eren.\n\n\
The other soldiers have succeeded, at great cost, in drawing the Titans in the city into one spot.\n\n\
This operation hinges on you and your companions, and it\'s almost time to begin.\n\n\
Eren and his guard unit - that is, you - descend into the city with vertical maneuvering. The streets are empty of humans and Titans \
alike, and you move along as quickly as you can.\n\n\
You see your goal, the boulder. Eren catapults into the air and bites his own hand.\n\n\
An explosion sounds above you; smoke billows everywhere. A Titan appears before your eyes.\n\n\
You and the rest of the guard unit take up positions on the surrounding rooftops, and prepare to defend it.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 268

    def P135(self, *option):
        if option == ():
            response = 'You give your answer.\n\n\
\"The boulder? I see,\" Pixis says, and nods as in agreement.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 193

    def P136(self, *option):
        if option == ():
            response = 'Nearly insane with terror, you flee. You grip the controls of your vertical maneuvering equipment, but your \
hands are shaking so badly you have trouble using them.\n\n\
You trip on a torn-up piece of flagstone and fall. A giant hand surrounds you, lifting you into the air.\n\n\
You\'re still screaming in horror as the Titan bites down.\n\n\
**You have died. Type `~reset` to start over.**'
            self.choices[0] = []
            return response

    def P137(self, *option):
        if option == ():
            response = '\"...That\'s how things stand,\" Armin says. \"If all we need to do is clear out the three-to-four-meter ones \
from the houses, there might be another way.\"\n\n\
He might be mad with grief over Eren...or he might have had the same thought you did.\n\n\
\"It\'s not any safer. But if it works, we could save everybody.\"\n\n\
And he begins to explain.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 166

    def P138(self, *option):
        if option == ():
            response = 'Completely focused, you fly toward the Titan, delivering a cut to its face. You\'d had hopes of getting it \
to spit out Thomas. But in the next second, it turns toward you and bites down.\n\n\
The last thing you hear is a great gulp as it swallows you.\n\n\
**You have died. Type `~reset` to start over.**'
            self.choices[0] = []
            return response

    def P139(self, *option):
        if option == ():
            response = 'You\'re inside the headquarters building.\n\n\
All the surviving members of the 104th Training Corps are gathered here.\n\n\
At the moment, the building is surrounded by several Titans of approximately 15 meters each. The building is sturdy and they \
won\'t soon break it down, but so long as there are humans here, more Titans will come.\n\n\
Furthermore, everyone is effectively out of gas, and so unable to fight with vertical maneuvering.\n\n\
Gas supplies are on the first floor, but so is a group of relatively small, three-to-four-meter Titans. Reconnaissance suggested \
there were seven of them total. If you can\'t get rid of them, you\'ll have to go without gas.\n\n\
There has to be a way to break this impasse.\n\n\
\"The situation is hopeless anyway, so no idea is too outrageous to consider. Everyone, think of anything you can.\"\n\n\
What kind of plan do you propose?\n\n\
:one: Stay sequestered in here\n\n\
:two: Start with some food\n\n\
:three: Use one or more people as bait while another group grabs the gas canisters'
            self.choices[0] = [1,2,3]
            if self.state.statuses.armin == 'Alive':
                response = response + '\n\n\
:four: Follow Armin\'s plan\n\n\
:five: Confuse the Titans by sending Armin out in a dress'
                self.choices[0].extend([4,5])
            return response
        elif option[0] == 1:
            self.cur_page[0] = 156
        elif option[0] == 2:
            self.cur_page[0] = 130
        elif option[0] == 3:
            self.cur_page[0] = 114
        elif option[0] == 4:
            self.cur_page[0] = 275
        elif option[0] == 5:
            self.cur_page[0] = 151
        elif option[0] == 's':
            self.cur_page[0] = 317

    def P140(self, *option):
        if option == ():
            response = '\"Feh. Fine. You, come on.\"\n\n\
Jean maneuvers to the top of the highest building in the vicinity. He was one of the best at vertical maneuvering in training, and \
you can see the results on the battlefield.\n\n\
\"Keep an eye on the situation from here. Make sure you see any Titan movement.\"\n\n\
Jean surveys the area calmly, making no move to go himself.\n\n\
In the distance, you can see the Garrison soldiers fighting a pitched battle. Your companions are shouting that you have to help them, \
but Jean says stoically:\n\n\
\"Even the experienced soldiers are hard-pressed. What could a bunch of greenhorns do? Pay attention to the field. If a Titan comes \
for us, we run. If we can\'t run, then we fight. No need for us to die sooner than we have to.\"\n\n\
His words are cold, but he\'s right. Jean\'s voice quavers as he speaks - he doesn\'t like abandoning the others any more than you do.\n\n\
Still, you\'re surprised.\n\n\
You would\'ve expected Jean to be far more insufferable in a command role...\n\n\
**Your Affinity with Jean has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.jean += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 106

    def P141(self, *option):
        if option == ():
            response = 'You were trained to ride in boot camp, and you consider fighting from horseback.\n\n\
However, most of the horses that were here have run away, and the rest are neighing in terror.\n\n\
You...\n\n\
:one: Try to ride one of them anyway\n\n\
:two: Give up and help with the cannons\n\n\
:three: Ascend the wall'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 248
        elif option[0] == 2:
            self.cur_page[0] = 94
        elif option[0] == 3:
            self.cur_page[0] = 65

    def P142(self, *option):
        if option == ():
            response = 'You and your surviving comrades join the middle guard.\n\n\
The Titans are relentless, but you face them down. Even the scant experience you\'ve had in the battle so far is proving valuable.\n\n\
Your classmates are falling. Experienced soldiers are falling. And amidst it all, you\'re fighting for your life agaianst a massive Titan.\n\n\
You wonder how much time has passed...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 171

    def P143(self, *option):
        if option == ():
            response = 'The battle for Trost District is not looking good.\n\n\
The dead are piling up - the soldiers of the Garrison as well as your fellow trainees.\n\n\
This is, after all, your first encounter with actual Titans. Training and exercises are well and good, but an actual Titan is a \
far more terrible thing than you could have prepared for.\n\n\
You and the others zip around the battlefield, dodging Titans, stopping to help the fallen when you see them.\n\n\
In a way, it\'s worse than actual combat. Most of those you find are dead, their bodies torn, shattered.\n\n\
The ones who aren\'t, though, you can rarely save - they simply die moaning before your eyes.\n\n\
Krista struggles to save them.\n\n\
She offers them encouragement in her beautiful voice, holding their blood-soaked hands.\n\n\
You credit the sight of her for helping you retain some shred of sanity.\n\n\
Because so far, out of all those you\'ve encountered, you haven\'t managed to help a single one.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 198

    def P144(self, *option):
        if option == ():
            response = 'With no relief effort to be mounted, you can only wait.\n\n\
Krista continues to pray fervently for your friends\' safe return.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 186

    def P145(self, *option):
        if option == ():
            response = 'When you come to, you\'re lying on your side in a bed.\n\n\
By some miracle, you seem to have been saved. Maybe you were pulled from the rubble.\n\n\
\"You\'re awake, trainee?\"\n\n\
A stranger in a soldier\'s uniform sits beside you.\n\n\
You hurry to face him.\n\n\
What happened after...that? First things first...you need to know what happened to Mikasa. You ask the man.\n\n\
\"Mikasa Ackerman is safe. As is Eren Yeager, whom she rescued. I\'ve been told Trainee Eren was about to be eaten alive \
when she appeared.\"\n\n\
Thank God. Mikasa was able to do what she\'d set out to do...\n\n\
But the man continues matter-of-factly.\n\n\
He tells you the evacuation of Trost District failed, and the populace was decimated. Wall Rose was abandoned. Humanity\'s \
territory has been reduced to the all-too-confined boundaries of Wall Sina...\n\n\
You notice the crest of the man\'s uniform. He\'s with the Military Police Brigade.\n\n\
\"Trainees Eren and Mikasa will be court-martialed. We\'ll need you to testify,\" he says with disinterest, and then says nothing more.\n\n\
**You have obtained the \"Trial of Eren and Mikasa\" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P146(self, *option):
        if option == ():
            response = 'You ask if there\'s any way to get word to the Survey Corps outside the wall.\n\n\
\"No,\" a more experienced soldier says with a strained expression. Then he goes on:\n\n\
\"They purposely set up no way to get word to them. Once the Survey Corps is outside the wall, their commanders don\'t want any interference.\n\n\
\"It\'s a political problem. There\'s a very vocal faction that wants to do away with surveys of the world outside the wall. If it were \
too easy to call the Corps back for, say, a rescue mission, there are those who would use that capability to interfere with their activities.\n\n\
\"Damn those politicians. It\'s their fault that at a crucial time like this, we can\'t...\"\n\n\
What a terrible state of affairs. And you can\'t even blame the Titans; humans did this to themselves.\n\n\
But at the same time, you realize something. Just because there\'s no system, doesn\'t mean it\'s impossible.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 72
        elif option[0] == 's':
            self.cur_page[0] = 160

    def P147(self, *option):
        if option == ():
            response = 'You advance toward the Titan. Utterly focused, you shove Armin out of the way. But the Titan snatches you \
instead, tossing you into its massive jaws. You land on its huge tongue. Without a moment\'s mercy, the Titan closes its mouth.\n\n\
You managed to save your friend...but not yourself.\n\n\
**You have died. Type `~reset` to start over.**'
            self.choices[0] = []
            return response

    def P148(self, *option):
        if option == ():
            response = 'You suggest that rather than fighting the Titans directly, it might be better to give support where you can.\n\n\
There may be survivors among the units decimated by the Titans. If you avoid direct confrontation, you might be able to save some \
of them...\n\n\
\"That\'s a wonderful idea!\"\n\n\
Krista agrees with you eagerly, her eyes shining.\n\n\
\"Yeah, that\'s not half bad,\" says the freckled girl, there as always, with a crooked smile on her face. \"We stay safe, and we \
get the satisfaction of helping our comrades.\"\n\n\
She always has to add a little twist of the knife...\n\n\
You break off from Jean and the others, and start working.\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 143

    def P149(self, *option):
        if option == ():
            response = 'You understand how Mikasa feels. You\'re worried about your friends, too.\n\n\
With a burst of gas fro your vertical maneuvering equipment, you set off after her.\n\n\
There\'s always a risk you\'ll just be a burden, but you might also be able to help your friends.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 69

    def P150(self, *option):
        if option == ():
            response = '\"All right. Leave it to me. Just buy me a little time.\"\n\n\
Armin seems to have an idea. You\'ve decided to trust him.\n\n\
And then, to protect him and Eren, you throw yourself into battle with the Titans.\n\n\
**Your Affinity with Armin has increased by 2!**\n\n\
Type :one: to continue.'
            self.state.affinities.armin += 2
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 276

    def P151(self, *option):
        if option == ():
            response = '\"All right. If it\'ll help us, I\'ll...I\'ll give it a try.\"\n\n\
You pass Armin the woman\'s dress you happen to have found.\n\n\
In his new outfit, Armin looks strikingly like a beautiful young woman. He\'s almost as pretty as Krista.\n\n\
\"N-Now what do I do?\" Armin asks, and you give a start.\n\n\
Honestly, you hadn\'t thought that far.\n\n\
When you stop and think, you realize Titans will attack any human, and it probably won\'t make much difference whether or not \
they\'re wearing a soldier\'s uniform. You admit your mistake and apologize.\n\n\
\"Damn you!" Jean yells at you. \"Playing games at a time like this!\"\n\n\
But you see a lot of smiles.\n\n\
\"You\'ve got to be kidding me.\"\n\n\
One of the trainee girls is laughing so hard she\'s crying. \"How can a boy look that good in a dress? You\'re putting me to shame!\"\n\n\
\"Darn it! If we get out of this alive, I\'ll show you just how pretty I can be!\"\n\n\
Your friends, weighed down by despair just a moment ago, are bantering together.\n\n\
Even Armin is laughing.\n\n\
Your \"plan\" has helped lighten the mood - even if that wasn\'t what you intended.\n\n\
After a good laugh, Armin says with a relaxed look, \"You know, I think that helped me calm down. And I\'ve thought of a plan. Listen.\"\n\n\
Type :one: to continue.'
            if self.state.flags.armindressed == 'No':
                self.state.flags.memelevel += 1
                self.state.flags.armindressed = 'Yes'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 275

    def P152(self, *option):
        if option == ():
            response = 'You watch Eren as he flies at the Colossal Titan. Its body is like a wall, and he sinks his anchors into \
the Titan itself, using them to aid his vertical maneuvering. He didn\'t learn that in training. You can only marvel at his \
flying. He looks like a speck against the Colossal Titan, but precisely because he is so small, it\'s not easy for the Titan \
to react quickly to him. Eren lets his guide wires out, describing a wide arc. He\'s behind the Colossal Titan! Now all he has \
to do is strike its nape...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 104

    def P153(self, *option):
        if option == ():
            response = 'You shout for Eren to calm down.\n\n\
But in his frenzy, it\'s as if he doesn\'t hear you...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 180

    def P154(self, *option):
        if option == ():
            response = 'You start trying to revive Franz.\n\n\
It\'s obvious he\'s already gone. This is for Hannah\'s sake.\n\n\
You cradle his head to clear the airway, just like you learned in training. Then you press down on his chest.\n\n\
Franz\'s face is already growing cold, but his expression is somehow peaceful. Perhaps it\'s because he died saving the person \
he loved.\n\n\
\"It\'s all right.\"\n\n\
Hannah\'s voice comes from behind you.\n\n\
\"It\'s all right, I get it. Franz is... He\'s dead.\"\n\n\
She can barely squeeze the words out. You offer her what encouragement you can, then fire up your vertical maneuvering equipment \
and leave the scene.\n\n\
Type :one: to continue.'
            self.state.statuses.franz = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 142

    def P155(self, *option):
        if option == ():
            response = 'This is a wiser decision than trying to focus on two things at once.\n\n\
As soon as one barrage has cleared your head, you steel your resolve and throw yourself at the Titans.\n\n\
Luckily, no cannonballs come flying at you. From overhead, you hear something like a cheer. It seems the soldiers on the wall have \
noticed you.\n\n\
You focus on one Titan whose movement has been hampered by the barrage and maneuver behind it. You draw your blade in midair, throw \
your speed and weight into the nape of its neck, make the cut, and kill it.\n\n\
Just like in training. From the corner of your eye you see the Titan collapse in a cloud of steam.\n\n\
But you are snatched from the air by a giant hand.\n\n\
Other Titans swarm you, tear you limb from limb.\n\n\
You succeeded in striking a blow, yes, but there are just too many of them.\n\n\
**You have died. Type `~reset` to start over.**'
            self.choices[0] = []
            return response

    def P156(self, *option):
        if option == ():
            response = 'The headquarters building is solidly built, and stocked with provisions and water. Why not just stay there, \
you ask? As long as you avoid the little Titans, and the hands of the bigger ones that reach into the fissures in the building, \
you should have a better chance of surviving than if you do anything rash.\n\n\
Mikasa immediately opposes the idea: \"The Titans won\'t go that easy on us. If all you had to do to survive was hide...there would \
have been more survivors five years ago.\"\n\n\
Plenty of others join Mikasa in her objection.\n\n\
But it\'s said Titans slow down at night. If you can just hold out for a little while...\n\n\
\"You\'ve got a good point,\" Reiner says, nodding. \"The question is - can we make it that long?\"\n\n\
:one: Choose another plan\n\n\
:two: Stick with this one'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 139
        elif option[0] == 2:
            self.cur_page[0] = 264

    def P157(self, *option):
        if option == ():
            response = 'Things seem to have gone well for you...but you can\'t say the same of the other soldiers on the battlefield.\n\n\
Titans are streaming into the city proper - has the vanguard already been destroyed?\n\n\
As you move from building to building, you see everywhere the corpses of soldiers.\n\n\
You try not to think about it, to just follow Marco\'s instructions...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 73

    def P158(self, *option):
        if option == ():
            response = 'You take Mikasa\'s side. \"Just try it!\" the merchant says brashly - but Mikasa isn\'t one to make idle threats. \
She cuts him down where he stands, and he collapses to the ground.\n\n\
\"Pull the cart back,\" she orders, her expression unchanged.\n\n\
One of the Garrison soldiers present says in a trembling voice, \"Wh-What a tragic accident he died in. Everyone understand?\"\n\n\
Many around you are cowed into silence, but there is a smattering of cheers. \"That\'s what you get, you greedy pig!\" someone shouts.\n\n\
\"I\'m going back to my station,\" Mikasa says calmly, and leaves.\n\n\
**What transpired here may have repercussions in the future.**\n\n\
Type :one: to continue.'
            self.state.flags.flagD = 'Yes'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 83

    def P159(self, *option):
        if option == ():
            response = 'You think. If you combine Eren\'s \"Titan power\" with a certain object in Trost District, it should be \
possible...\n\n\
Add the height of Eren\'s Titan (in meters) to the difference between the heights of the Colossal Titan and Wall Rose. What do you get?\n\n\
:one: 25\n\n\
:two: 65\n\n\
:three: 75\n\n\
:four: 110'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 135
        elif option[0] == 2:
            self.cur_page[0] = 287
        elif option[0] == 3:
            self.cur_page[0] = 287
        elif option[0] == 4:
            self.cur_page[0] = 287

    def P160(self, *option):
        if option == ():
            response = 'You realize you might be able to aim the fixed gun directly upward and fire it.\n\n\
You bring your idea to the soldiers assigned to this area.\n\n\
\"We should have some blank training rounds. They don\'t have any killing power, but they leave a trail of colored smoke. If we fired \
them into the air, they could serve as crude signal flares.\"\n\n\
The commander seems intrigued by your idea.\n\n\
\"The gun\'s not built for that. The recoil might make it unusable. And even if it fired, there\'s no guarantee the bullet would get \
high enough into the air, or that the Survey Corps would notice if it did. We don\'t even know if they would understand what it meant \
if they saw it. ...But it\'s better than sitting here and letting the Titans have their way with us.\"\n\n\
And with that, he gives his permission.\n\n\
The cannon is fired into the air. The blank howls into the sky, trailing colored smoke. A cheer goes up from the soldiers on the wall.\n\n\
**The action you just took will be meaningful in the future.**\n\n\
**In subsequent playthroughs, if you see the words \"Survey Corps with its wealth of experience,\" copy and paste those words into \
the chat to reveal an additional option you may take.**\n\n\
Type :one: to continue.'
            self.state.flags.flagL = 'Yes'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 72

    def P161(self, *option):
        if option == ():
            response = 'As you watch him from behind, Levi stops, a disgusted look on his face. He seems to have gotten oil on his hands \
while walking through the impromptu camp. Frowning wordlessly, he reaches into his bag and pulls out a handkerchief, with which he \
wipes the grime away. The handkerchief is strikingly clean, and folded nearly.\n\n\
It seems the legendary captain is a bit of a neat freak...much to your surprise.\n\n\
Type :one: to continue.'
            self.state.flags.memelevel += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 162

    def P162(self, *option):
        if option == ():
            response = 'Apparently, the Survey Corps could tell something was wrong, and decided to come back - they even sent \
Captain Levi and several others ahead on horseback with lightened equipment to speed up their pace.\n\n\
Thankfully, this allowed them to reach you in time to help execute the plan.\n\n\
The soldiers from the Survey Corps are few in number, but their impact is great. And their presence gives the plan a much better \
chance of succeeding, as well.\n\n\
Captain Levi and the others join the defense of the Titan Eren.\n\n\
Now, decide once more which group you would like to join.\n\n\
:one: Help Levi defend Eren\n\n\
:two: Trust Levi, and join the rear guard that\'s drawing off the Titans\n\n\
:three: They may be excellent soldiers, but the big picture hasn\'t changed. You value your life and decide to run'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 210
        elif option[0] == 2:
            self.cur_page[0] = 225
        elif option[0] == 3:
            self.cur_page[0] = 290

    def P163(self, *option):
        if option == ():
            response = 'You are at the southernmost point of Trost District, near the outer wall.\n\n\
You hear occasional explosions and see dark smoke billowing up.\n\n\
The cannons are firing. But they don\'t mean much against the Titans, with their ability to regenerate lost body parts.\n\n\
You hear someone shouting in the distance, in between fusillades:\n\n\
\"The vanguard was supposed to strike the finishing blow against the Titans - but they\'ve been wiped out. And we can\'t \
stop them with the cannons alone!\"\n\n\
Near the gate you can already see wrecked guns and soldiers\' bodies.\n\n\
You...\n\n\
:one: Descend to ground level and join the cannon regiment\n\n\
:two: Engage the Titans and try to finish them off\n\n\
:three: Ascend the outer wall'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 123
        elif option[0] == 2:
            self.cur_page[0] = 101
        elif option[0] == 3:
            self.cur_page[0] = 280

    def P165(self, *option):
        if option == ():
            response = 'Jean, Connie, and the others are gathered on a rooftop.\n\n\
Among them, you see Armin, crouched and pale. Wasn\'t he a member of Squad 34? Eren\'s squad? A murmur runs through your gathered \
comrades. \n\n\
\"Hmph. Squad 34 is gone, except for its weakest member?\" the freckled girl spits out.\n\n\
\"What a thing to say!\" Krista exclaims, taking Armin\'s side.\n\n\
\"That\'s my Krista! After this mission is over, marry me!\" the freckled girl says sarcastically. It\'s the same attitude she\'s \
always had, but sharper than usual.\n\n\
Everyone on this battlefield seems to be struggling to hold onto themselves.\n\n\
You offer Armin your hand, but he simply stares at it, then suddenly stands. \"I\'m sorry I caused problems! I\'ll meet up with \
the rear guard!\"\n\n\
Then he heads for the rear, alone. He seemed calm - but was he really okay?\n\n\
Type :one: to continue.'
            self.state.statuses.eren = 'Dead'
            self.state.statuses.squad34 = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 195

    def P166(self, *option):
        if option == ():
            response = 'This is the plan.\n\n\
As things stand, the Titans that had been swarming the headquarters building are no longer a problem. The mysterious Titan outside \
has taken care of them all...or at least drawn them off.\n\n\
Taking advantage of that respite, a large number of you will board the lift to the first floor. Since Titans are drawn to crowds of \
people, that should lure them toward the center of the room. Thereupon, the people on the lift will shoot them with guns prepared \
beforehand. Naturally, the Titans will regenerate, but the goal is only to build them for an instant.\n\n\
Another contingent hiding among the rafters will simultaneously leap down and attack the Titans\' weak points.\n\n\
If everything goes well, all the Titans will die at once.\n\n\
But if even one person fails - if even one Titan is left alive - then, bereft of vertical maneuvering, you will all be killed.\n\n\
Everyone nods, agreeing to the plan despite the risks.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 1661

    def P1661(self, *option):
        if option == ():
            response = 'First you have to prepare the guns. In the storehouse, you find dusty rifles belonging to the Military Police Brigade. They\'re old \
weapons that would never have been any use against a Titan, but for this plan you\'ll need them. You were trained in the use of \
firearms. You assumed it was as useless as hand-to-hand combat. Who knew this was how that training would serve you?\n\n\
Everyone who can fit climbs onto the lift. They\'re the bait. The people with guns surround them along the edge of the lift. They \
will try to protect the bait from the encroaching Titans, and blind the monsters as well.\n\n\
Then there is the most crucial role, those who will finish off the Titans. For this you pick the most accomplished of your \
companions: Mikasa and Jean, Sasha and Connie. And of course Annie, Reiner, and Bertolt.\n\n\
This latter group secret themselves among the beams of the ceiling, ready to leap on the Titans the moment the guns fire. Without \
their vertical maneuvering equipment, they\'ll only have one chance, as they jump.\n\n\
All is ready. You get in position as well.\n\n\
Now...How many Titans are there on the first floor that you have to kill?\n\n\
Add this number to the number of your training class (i.e., you are the ___th Training Corps). What do you get?\n\n\
:one: 109\n\n\
:two: 110\n\n\
:three: 111\n\n\
:four: 112'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 250
        elif option[0] == 2:
            self.cur_page[0] = 250
        elif option[0] == 3:
            self.cur_page[0] = 111
        elif option[0] == 4:
            self.cur_page[0] = 250

    def P167(self, *option):
        if option == ():
            response = '**Your Affinity with Armin has increased by 1!**\n\n\
Armin explains his plan...\n\n\
Type :one: to continue.'
            self.state.affinities.armin += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.eren == 'Dead':
                self.cur_page[0] = 166
            elif self.state.statuses.eren == 'Alive':
                self.cur_page[0] = 173

    def P168(self, *option):
        if option == ():
            response = 'You entrust Krista with the command, but deep inside, you hope she\'ll get hurt.\n\n\
That\'s right. You\'ve never liked this goody two-shoes, not since training.\n\n\
The freckled girl is right. She\'s soft.\n\n\
You catch the freckled girl\'s eye, but she only frowns and glares at you.\n\n\
(If you go ahead with this course of action, type :one:. If you\'re having second thoughts, type :two: and choose again.)'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 185
        elif option[0] == 2:
            self.cur_page[0] = 79

    def P169(self, *option):
        if option == ():
            response = '\"I don\'t need you to tell me that,\" Mikasa says with a frosty look. \"Eren already said the same thing.\"\n\n\
Mikasa seems to have regained her composure.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 84

    def P170(self, *option):
        if option == ():
            response = 'The other side of the wall is overflowing with evacuated soldiers and citizens. Voices everywhere try to confirm \
the safety of family, friends, comrades.\n\n\
You look for other trainees from your class. You see Krista and the freckled girl who is forever at her side, and head toward them.\n\n\
\"Thank goodness you\'re all right!\"\n\n\
A smile spreads over Krista\'s face; she seems genuinely thrilled to see you.\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 178

    def P171(self, *option):
        if option == ():
            response = 'A member of another squad brings terrible news. The city\'s headquarters building has been mobbed by Titans, and \
you can no longer resupply your vertical maneuvering equipment with fresh gas.\n\n\
In order for such a small machine to propel a person at such high speeds, the vertical maneuvering equipment uses pressurized gas, \
and uses it at a tremendous rate. A battle as long as this one would normally require several resupplies. You had been confident that \
you would be able to get a fresh supply from headquarters. To think that the building had been overwhelmed...\n\n\
Even if you conserve your gas, you don\'t know how much longer it will last...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 124

    def P172(self, *option):
        if option == ():
            response = 'You all use vertical maneuvering to position yourselves on the rooftops.\n\n\
There, you join the middle guard, protecting the center of Trost District.\n\n\
You look to the south, where the vanguard stands. Between the buildings you can see the vast silhouettes of Titans. And they\'re \
coming closer. Maybe the vanguard alone couldn\'t fend off the Titans\' onslaught.\n\n\
All of you will soon have to fight.\n\n\
Now... Who do you choose as your leader?\n\n\n\
**Jean**: \"Huh? You want me to take command?\"\n\n\
**Marco**: \"It\'s a heavy responsibility, but I\'ll do my best.\"\n\n\
**Sasha**: \"I\'m so hungry...\"\n\n\
**Krista**: \"We have to help our comrades. But I don\'t want to put everyone at risk!\"\n\n\n\
:one: Jean\n\n\
:two: Marco\n\n\
:three: Sasha\n\n\
:four: Krista'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 140
        elif option[0] == 2:
            self.cur_page[0] = 66
        elif option[0] == 3:
            self.cur_page[0] = 256
        elif option[0] == 4:
            self.cur_page[0] = 102

    def P173(self, *option):
        if option == ():
            response = 'This is the plan.\n\n\
You\'ll take advantage of the Titans\' tendency to be attracted to large groups of people by using a group of your comrades as bait. \
A smaller group will then use that opening to grab the gas tanks. If even one of you can get gas, you could fight using vertical maneuvering. \
While that person is resisting, more might get gas and join the fight. Once all of you are resupplied, you can get out of here...\n\n\
Your companions listen to the idea with pale, downcast faces.\n\n\
The chance of success is not high, and whether it works or not, some people are bound to be sacrificed.\n\n\
You have no idea how many may die executing this plan...and you don\'t expect many volunteers to be the bait.\n\n\
\"Let\'s draw straws to decide who does what,\" somebody says.\n\n\
\"No,\" someone else says. \"We need every edge we can get. We have to put our best people on reclaiming the canisters.\"\n\n\
It\'s only logical - but a dark cloud has settled over your companions.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.eren == 'Alive':
                self.cur_page[0] = 125
            elif self.state.statuses.eren == 'Dead':
                self.cur_page[0] = 82

    def P174(self, *option):
        if option == ():
            response = 'A shockwave runs through the area, rocking everything around you.\n\n\
For a moment, you\'re not sure what happened.\n\n\
A second Titan, as big as the first, appears - and then slams its giant fist into the Titan that attacked Mikasa, sending it flying.\n\n\
The shockwave was the product of 15-meter Titans, the size of three-storey buildings, having a fist fight.\n\n\
The Titan who got hit falls to the ground with a resounding crash, trailing bits of flesh. The Titan who hit it gives an animal bellow, \
and continues to maul its fallen foe.\n\n\
It doesn\'t even look at you or Mikasa.\n\n\
A Titan that ignores humans? That fights other Titans? You\'ve never heard of such a thing.\n\n\
The scenery quakes, the air rattles.\n\n\
And you can\'t believe what you\'re seeing with your own eyes.\n\n\
Mikasa is looking up at the Titan, her eyes wide...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 239

    def P175(self, *option):
        if option == ():
            response = 'For a moment, you can\'t tell what\'s happened.\n\n\
A 15-meter Titan is there. On top of the half-ruined building.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 260

    def P176(self, *option):
        if option == ():
            response = 'You whisper the details of your plan into Mikasa\'s ear.\n\n\
You will distract the commander assigned to the two of you, giving her a chance to run for the vanguard.\n\n\
Mikasa hesitates, but you insist:\n\n\
\"A soldier like you can do the most good on the front line. If you can stop the Titans up there, this area will be safe.\"\n\n\
Your words seem to convince her. She gives you a word of thanks, and turns toward the front.\n\n\
You have a feeling you\'ve done a good thing.\n\n\
**Your affinity with Mikasa has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 105

    def P177(self, *option):
        if option == ():
            response = 'You talk and talk, trying to comfort Mikasa.\n\n\
But all your words seem to drift into the empty air.\n\n\
Armin is broken, weeping.\n\n\
Mikasa, who seems fearsomely alert, says to him, \"This is no time to be getting sentimental.\" Then she turns to you and adds, \
\"So...you can stop.\"\n\n\
**Your Affinity with Mikasa has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 117

    def P178(self, *option):
        if option == ():
            response = 'You and the others retreat to the safe zone beyond the inner wall.\n\n\
Krista and her friend the freckled girl are with you, but you don\'t see any other members of the 104th Training Corps.\n\n\
The battle with the Titans did tremendous damage; the Garrison is in an uproar. The one consolation is that all of the citizens \
were able to evacuate safely...\n\n\
You receive news of your friends\' deaths in battle. Franz and Hannah\'s names are among them. In your mind\'s eye, you picture \
the happy couple...\n\n\
Type :one: to continue.'
            self.state.statuses.franz = 'Dead'
            self.state.statuses.hannah = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 237

    def P179(self, *option):
        if option == ():
            response = '**Your Affinity with Mikasa has increased by 1!**\n\n\
You are completely focused on killing the Titan. You sink your blades into its massive shoulders.\n\n\
It\'s not enough. The Titan turns towards you. On its face is a thin smile.\n\n\
A giant hand reaches out for you. In midair, you are unable to dodge it, and it grabs you...\n\n\
Type :one: to continue.'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 174

    def P180(self, *option):
        if option == ():
            response = 'The Titan who swallowed Thomas turns as if nothing had happened and heads off in a new direction, smashing \
buildings as it goes.\n\n\
\"Wait, damn you!\" Eren says in a frenzy, and without a moment\'s thought he follows it with vertical maneuvering.\n\n\
No! you think, and at that moment a giant face appears beneath Eren, and bites at him.\n\n\
It\'s a Titan that had been hidden in the shadows of the building. Seven meters. The chasm of its mouth extends from ear to ear \
across its huge face.\n\n\
It tears off Eren\'s leg. He loses his balance; his body tumbles through the air, slamming into the roof of the next building.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 121

    def P181(self, *option):
        if option == ():
            response = 'You try to drag the wailing Hannah away.\n\n\
If only you and a wounded comrade are present with Hannah, you will have to abandon your wounded friend. (You are unable to carry \
both Hannah and the other person by yourself.)\n\n\
:one: Rescue Hannah\n\n\
:two: Leave Hannah behind'
            self.state.statuses.franz = 'Dead'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            if self.state.flags.witheren == 'Yes':
                self.state.statuses.eren = 'Dead'
            self.cur_page[0] = 142
        elif option[0] == 2:
            self.cur_page[0] = 221

    def P182(self, *option):
        if option == ():
            response = 'You look around, hoping to help the wounded. You have to get to whomever you can before the Titans show up... \
But all you can see are corpses. The soldiers who manned the cannons a moment ago now lie motionless beside the ruins of their guns.\n\n\
You call out at the top of your voice, but there\'s no answer.\n\n\
Nearby, you spot a soldier half buried under rubble.\n\n\
You desperately pull the debris away. You take his arm and tug.\n\n\
...He seems oddly light.\n\n\
That\'s when you realize everything below his waist is gone, crushed into a bloodly soup.\n\n\
Terror grips you.\n\n\
:one: Just run\n\n\
:two: Ascend the wall'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 136
        elif option[0] == 2:
            self.cur_page[0] = 65

    def P183(self, *option):
        if option == ():
            response = 'You received the order to advance because the vanguard has already been destroyed.\n\n\
The Titans are pouring in. The forward part of the middle guard tried to stop them, but they didn\'t last long. Now soldiers \
all over town are engaged in desperate battles with the Titans wandering the streets.\n\n\
\"Damn it all,\" Jean says archly.\n\n\
As your friends and the more experienced soldiers drop one after another, you continue the struggle as the Titans press in.\n\n\
You wonder how much time has passed...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 87

    def P184(self, *option):
        if option == ():
            response = 'With the gas left in your vertical maneuvering equipment, you and Mikasa are able to make it to the headquarters \
building. You owe this to the mysterious Titan, which fought off other Titans along the way as if to help you.\n\n\
You recognize several of the faces inside. Jean, Connie, Sasha, Marco...everyone seems to have made it here safely.\n\n\
\"Glad you made it.\"\n\n\
\"Yeah, but...what\'s that?\"\n\n\
\"A Titan...fighting Titans?\"\n\n\
Your friends\' attention is focused on the scene outside the window.\n\n\
\"A Titan that prefers to attack Titans...I believe it\'s an Abnormal,\" Mikasa says. \"It\'s thanks to him that we made it here.\"\n\n\
The two of you look at each other and nod. You\'ll keep to yourself the fact that you think the Titan is Eren. After all, even you \
can still hardly believe it.\n\n\
Some of your comrades ask whether Eren is alive, but you can only shake your head silently in answer.\n\n\
\"We might be able to use that Titan to get into Headquarters and get some gas,\" you tell everyone.\n\n\
\"Are you sure you understand that Titan?\" Reiner says with an uncharacteristic note of panic.\n\n\
You tell him that no, honestly, you don\'t.\n\n\
It\'s a very high-stakes gamble...\n\n\
\"Fine, let\'s gamble,\" Jean says. \"Sounds good to me. There\'s seven three- and four-meter Titans on the first floor, where \
the gas is. We were just talking about whether we should all just run in there together - even though it\'d probably get us killed.\"\n\n\
As you listen, you start to form a plan...\n\n\
**Your Affinity with Eren and Mikasa has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.statuses.eren = 'Dead'
            self.state.affinities.eren += 1
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 166

    def P185(self, *option):
        if option == ():
            response = 'In the ensuing battle, just as you expected, one after another of your comrades are slain by the Titans.\n\n\
It\'s the fault of your soft-headed commander, Krista.\n\n\
Each time someone dies she weeps afresh, but you can see them for the crocodile tears they are. Protect your other friends and keep \
everyone out of danger? As if it were ever that easy.\n\n\
At times, she faces a Titan to help one of your comrades, without regard for her own safety.\n\n\
You have no intention of letting that happen. Now that she\'s doomed the lot of you, she can\'t sacrifice herself just to make \
herself feel better.\n\n\
You plan to attack her when you\'re alone, just the two of you, hidden somewhere.\n\n\
That freckled girl is a problem. She\'s forever by Krista\'s side. But you wait for your moment, a moment when the freckled girl \
isn\'t there, and then you draw near to Krista.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 202

    def P186(self, *option):
        if option == ():
            response = 'There\'s good news. Members of the 104th Training Corps have returned safely.\n\n\
You\'re told they risked everything to retake Headquarters and were able to resupply themselves with gas.\n\n\
But your surviving comrades, it seems, are very few, and exhaustion is written all too clearly on their faces.\n\n\
You can\'t blame them - they\'ve been through hell.\n\n\
\"There\'s more to it than that,\" one of them, Jean, mutters, his face white. \"Eren... A Titan... No. We\'ve been ordered \
not to talk about it. But...a story this big, no way it\'ll stay quiet for long.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 110

    def P187(self, *option):
        if option == ():
            response = 'You do your duty where you are.\n\n\
A single soldier should not be moved by the fortunes of the battlefield.\n\n\
You\'ll do what you were told to do, where you were told to do it...\n\n\
Humanity\'s terrible fight will continue, long into the future...\n\n\
**You have obtained the \"A Soldier\'s Duty\" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P188(self, *option):
        if option == ():
            response = 'A short time later...\n\n\
You are now atop the wall, looking down on Trost.\n\n\
The city has been overrun by Titans. You see the shapes of them wandering among the buildings.\n\n\
Above it all hangs an incongruously blue sky.\n\n\
On top the wall, nearby, Eren is talking with a bald man, Commander Dot Pixis. In charge of the defense of the entire southern \
region, and famous lifelong perv.\n\n\
The commander himself appeared on the battlefield at the head of a regiment of reinforcements. He must have responded the moment \
a runner came to inform him of the Titan attack. Without his prompt action, it might have taken days longer for reinforcements to \
arrive.\n\n\
Commander Pixis intervened with the local guard captain at the last possible second and stopped him from attacking Eren.\n\n\
That meant he\'d saved you, as well.\n\n\
\"Earlier, you said - you think that with your \'Titan Power\' or whatever it is, it would be possible to retake Trost District,\" \
Commander Pixis says. \"Do you really believe that? Perhaps you could tell me what you had in mind.\"\n\n\
You...\n\n\
:one: Answer yourself'
            self.choices[0] = [1]
            if self.state.statuses.armin == 'Alive':
                self.choices[0].append(2)
                response = response + '\n\n\
:two: Leave it to Armin'
            return response
        elif option[0] == 1:
            self.cur_page[0] = 159
        elif option[0] == 2:
            self.cur_page[0] = 223

    def P189(self, *option):
        if option == ():
            response = 'This was Commander Pixis\'s plan.\n\n\
First, the majority of the soldiers, including his reinforcements, would gather on top of the wall. This was step one: to \
use the Titans\' attraction to the largest nearby group of humans to get them all in one place.\n\n\
Once that had been achieved, Eren in Titan form would pick up the boulder and use it to block the hole. A small number of \
elite members of the Garrison and other picked soldiers would act as his support.\n\n\
Naturally, it would be impossible to draw off every Titan, and there was no accounting for Abnormals, so the support group \
would be in significant danger.\n\n\
The group distracting the Titans would hardly be safe, either. It might be better than direct engagement, but some measure of \
losses was to be expected. In addition, some combat action might be required to keep the Titans at bay. If the Survey Corps \
with its wealth of experience were available, there might be another way, but this was the best thing he could think of under \
the circumstances.\n\n\
Now...which role do you take?\n\n\
:one: Protect the Titan Eren\n\n\
:two: Rear support distracting the Titans\n\n\
:three: It doesn\'t sound like leaving will be held against you - run'
            self.choices[0] = [1,2,3]
            if self.state.flags.flagL == 'Yes':
                self.choices[0].append('s')
            return response
        elif option[0] == 1:
            self.cur_page[0] = 134
        elif option[0] == 2:
            self.cur_page[0] = 225
        elif option[0] == 3:
            self.cur_page[0] = 290
        elif option[0] == 's':
            self.cur_page[0] = 209

    def P190(self, *option):
        if option == ():
            response = '\"I just don\'t want to die like a dog, that\'s all,\" Rico says, almost shouting.\n\n\
Perhaps it\'s her dudgeon that causes her to look at even you, who agreed with her, with hard eyes.\n\n\
She\'s probably no happier about this outcome than the rest of you.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 269

    def P191(self, *option):
        if option == ():
            response = 'You are fighting in the streets of Trost alongside other members of the 104th Training Corps.\n\n\
**Jean:** \"Try to coordinate with the others as much as possible. Attack the Titans if you think you\'ve got a real opportunity - but \
do it carefully.\"\n\n\
**Reiner:** \"The goal is to slow down as many Titans as we can. Let\'s split up. They won\'t target a small unit.\"\n\n\
**Sasha:** \"I\'m so hungry!\"\n\n\
Such are the words of your friends. Now, you...\n\n\
:one: Try to coordinate with the others as much as possible\n\n\
:two: Split up to take on the largest number of Titans\n\n\
:three: Are also very hungry'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 228
        elif option[0] == 2:
            self.cur_page[0] = 207
        elif option[0] == 3:
            self.cur_page[0] = 255

    def P192(self, *option):
        if option == ():
            response = 'The Garrison soldier raises his eyebrows at your words.\n\n\
\"How dare a mere trainee - !\" He moves to hit you.\n\n\
\"Stand down.\" A woman with glasses and an air of command stops him. \"Are we scared? You\'re welcome to see it that way. \
We don\'t want to die in vain, nor do we want to send others to do so.\"\n\n\
Whatever the case, you seem to have made the wrong move.\n\n\
You ask several more times after that, but your pleas fall on deaf ears.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 144

    def P193(self, *option):
        if option == ():
            response = '\"Trainee Eren. Can you block the hole?\"\n\n\
This time, Commander Pixis directs the question at Eren. \"Can you block the hole in the gate with your Titan power?\"\n\n\
You are confident what his answer will be. He responds with conviction, ready to gamble on his friend\'s plan.\n\n\
\"I can, and I will. No matter what!\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 197

    def P194(self, *option):
        if option == ():
            response = 'I\'ll...kill them...\" Eren mutters in his sleep. You hate to imagine what dreams he is having.\n\n\
Then, suddenly, he opens his eyes.\n\n\
\"Hey. Is everyone all right? How\'s the battle going? What about the Titans?\"\n\n\
In those words, you hear the Eren you know.\n\n\
But... The words he spoke in his sleep couldn\'t have been worse.\n\n\
\"Hey, he said he\'ll kill us!\"\n\n\
\"I knew he planned to slaughter us humans...\"\n\n\
The voices are those of the soldiers just nearby.\n\n\
You notice they are surrounding you with their weapons at the ready.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 208

    def P195(self, *option):
        if option == ():
            response = 'You part ways with Jean and the others again, and resume your search and rescue activities.\n\n\
Corpses are piling up all around the battlefield. You find the bodies of two fellow trainees... It\'s Franz and Hannah. \
Their bodies are close, almost cradling each other. They must have been together until the end.\n\n\
Once more, you wonder how much time has passed...\n\n\
At last, you hear the retreat bell sound. That means the populace has finished its evacuation.\n\n\
\"All that, and we weren\'t able to save anybody,\" Krista says in a voice heavy with grief.\n\n\
The surviving soldiers are withdrawing with evident relief.\n\n\
The two of you join them, passing beyond the wall and into safety.\n\n\
Type :one: to continue.'
            self.state.statuses.franz = 'Dead'
            self.state.statuses.hannah = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 91

    def P196(self, *option):
        if option == ():
            response = 'Several Titans are already headed for your position.\n\n\
The plan had been to seal the hole quickly, before any Titans arrived - but that plan is in ruins.\n\n\
\"The plan has failed,\" says Rico, a member of the guard unit, with profound regret. \"There\'s nothing we can do. We won\'t be \
able to extract him under the circumstances, either. Let\'s leave Eren here and exfil.\"\n\n\
Mikasa opposes this vigorously. She draws her blade; she appears ready to fight anyone who would abandon Eren.\n\n\
Then Ian, the commander of the guard unit, says:\n\n\
\"We\'ll deal with those encroaching Titans. We can\'t leave Eren here. We\'ve got to bring him to his senses, or get him out of \
that Titan body, somehow. We\'ve got to buy him some time.\"\n\n\
Rico and Mitabi object, naturally. There\'s no guarantee Eren will come to his senses, or that he won\'t go berserk again if he does.\n\n\
You...\n\n\
:one: Take Rico\'s side\n\n\
:two: Take Mikasa\'s side\n\n\
:three: Take Ian\'s side'
            self.choices[0] = [1,2,3]
            if self.state.flags.levihelp == 'Yes':
                response = response + '\n\n\
:four: Ask Levi for help'
                self.choices[0].append(4)
            return response
        elif option[0] == 1:
            self.cur_page[0] = 190
        elif option[0] == 2:
            self.cur_page[0] = 230
        elif option[0] == 3:
            self.cur_page[0] = 241
        elif option[0] == 4:
            self.cur_page[0] = 201

    def P197(self, *option):
        if option == ():
            response = 'From atop the wall, Commander Pixis addresses the assembled soldiers. He has a booming voice that all the \
soldiers can hear clearly, even though he is 50 meters above them.\n\n\
He tells them about the plan, which is to use Eren\'s Titan form\'s strength to plug the hole in the outer wall. And he tells them that \
the support of every soldier will be needed for this operation.\n\n\
A murmur of unease runs through the ranks.\n\n\
Can that hole be filled? It seems impossible. And the idea of a human who can transform into a Titan beggars the imagination.\n\n\
And for the sake of this unbelievable plan, they are to enter a city swarming with Titans, risking their lives?\n\n\
More than anyone else, the fear grips those who have had their first experience of real combat this day.\n\n\
\"You expect me to give up my life for some nonsense like that?! What do you take us for?! We\'re... We\'re not disposable blades!\" \
sobs Daz, another trainee.\n\n\
Several soldiers break from the ranks and begin to run.\n\n\
\"If we\'re all just going to die,\" someone says, \"I want to spend my last moments with my family!\"\n\n\
\"Desertion in the face of the enemy is a capital offense!\" bellows the guard captain, drawing his sword and standing in front of \
the fleeing soldiers. But they don\'t stop.\n\n\
Order seems to be collapsing. It looks like nothing can be done.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 1971

    def P1971(self, *option):
        if option == ():
            response = '\"Upon my order!\" Commander Pixis\'s voice rings out again. \"Anyone who leaves right now will go unpunished!\"\n\n\
The unexpected words stop even the would-be deserters in their tracks.\n\n\
\"If you have given in to your fear of the Titans, you will never be able to stand against them! Anyone who has succumbed to terror \
of the Titans should leave here! And...\" His voice hangs in the air. \"... all those who wish for their friends, their families, their \
loved ones to feel that same fear, they too should go!\"\n\n\
The square stands silent as the soldiers absorb the commander\'s words.\n\n\
Those who once sought to run now get back in line. Some seem resigned. Others struggle to control themselves.\n\n\
The commander\'s words were not intended to intimidate or to cajole, or to manipulate anyone. They are simply the truth. If the \
Titans are not stopped here, if this wall does not stand, there will be nothing to stop the Titans from feasting on the rest of \
humanity.\n\n\
Commander Pixis addresses the assembled crowd once more. \"We cannot die inside yet another wall! Given the choice, die here!\"\n\n\
It is not an order or a command. It is a leader\'s heartfelt request of you soldiers.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 189

    def P198(self, *option):
        if option == ():
            response = 'You work together with Krista. The streets of Trost are swarming with Titans, and they have killed more \
soldiers than you can count.\n\n\
From afar, people clustered around the Titans look like tiny bugs. Even now, the scene seems somehow unreal.\n\n\
In fact, at this moment, you can see human forms and two Titans far away.\n\n\
One of the Titans is lanky and long-haired, and wears a look of grief. The other is rotund and bald, with a neat beard around its \
mouth. From this distance, they almost look comical, and that makes them all the more unsettling.\n\n\
The two of them sweep away the little bugs surrounding them.\n\n\
You know that in reality, those bugs are people fighting desperately, trying to stay alive.\n\n\
You...\n\n\
:one: Know they are beyond help. Leave them to their fate\n\n\
:two: Go to rescue them after the Titans have left'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 75
        elif option[0] == 2:
            self.cur_page[0] = 113
        elif option[0] == 's':
            self.cur_page[0] = 77

    def P199(self, *option):
        if option == ():
            response = '**Your Affinity with Mikasa has increased by 1!**\n\n\
Mikasa leaps through the city with incredible agility. She strikes down every Titan in her path, slicing into the backs of \
their necks without slowing down.\n\n\
Some of your friends admire her; this is just what they expect from Mikasa. But all you can think is how reckless her actions \
look.\n\n\
Eren\'s death must have affected her deeply...\n\n\
Suddenly, Mikasa\'s body freezes in midair.\n\n\
She\'s out of gas.\n\n\
Normally, she would never have let herself run out of gas. You knew she wasn\'t thinking straight.\n\n\
Without the ability to send out or roll up her guide wires, movement is impossible. Mikasa slams into the side of a building.\n\n\
She bounces off the wall onto the ground. Thankfully, the awning of a street stall catches her, and she isn\'t critically injured.\n\n\
But she is lying on the pavement, motionless.\n\n\
And you see a Titan coming.\n\n\
You...\n\n\
:one: Attack the Titan to help Mikasa\n\n\
:two: Call out in a loud voice'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 179
        elif option[0] == 2:
            self.cur_page[0] = 235

    def P200(self, *option):
        if option == ():
            response = 'A lot happens after the battle.\n\n\
The members of the 104th Training Corps go their separate ways. The next time you all see each other is for Franz and Hannah\'s \
wedding.\n\n\
You\'re invited, too, and it\'s a chance to see familiar faces.\n\n\
Franz is in formal clothes, Hannah\'s wearing a wedding dress. They look as sweet as ever. You all cheer, but so far from looking \
embarrassed, they just seem more comfortable together than ever.\n\n\
You\'re thrilled to see all your classmates again. Eren and Jean manage to fight despite the celebratory mood, and Sasha is more \
interested in the buffet than the bride. No one has changed one bit. ...No, maybe they have, but together you\'re transported back \
to that time.\n\n\
Finally the ceremony begins. Hannah is radiant with joy in her simple white dress. Mikasa and Krista both study her closely. They \
must be picturing what they would look like in a dress like that.\n\n\
The jubilant bride and groom hold fast to each other amidst the approving shouts of their friends.\n\n\
This world is still harsh, still cruel. But surely you can afford yourselves a moment\'s joy like this.\n\n\
Hannah throws the bouquet into the air. The other girls reach out, each hoping to be the next bride. You don\'t see who catches it.\n\n\
**🎉 Congratulations! You\'ve obtained the \"An Ordinary Moment of Happiness\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P201(self, *option):
        if option == ():
            response = '\"You\'re asking me?\"\n\n\
Levi glares at you.\n\n\
\"If I had my way, I would beat the pulp out of someone so useless.\"\n\n\
Then he puts his face up close to yours and goes on:\n\n\
\"But I don\'t know anything about your precious Eren. Isn\'t that your business? We in the Survey Corps have been in actual \
combat, and I have never seen anything as ridiculous as a person who could turn into a Titan. But I suppose my experience \
doesn\'t serve me in this case. I guess I\'ll have to rely on you, even if you know barely more about it than I do. Can we trust \
him? Can we use him? ...I\'ll leave it to your judgment.\"\n\n\
With that, Levi makes to leap in the direction of the Titans.\n\n\
\"I was assigned to protect your little friend. My people and I will not let some mere Titan get close to you.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 269

    def P202(self, *option):
        if option == ():
            response = 'You are caught by a Titan that appeared from nowhere.\n\n\
You didn\'t sense anything nearby a moment ago-! An Abnormal?\n\n\
The Titan seems somehow feminine. It looks at you with eyes that convey emotion.\n\n\
If nothing else...it looks like Krista was able to escape.\n\n\
How ironic, that you should give your life to save her.\n\n\
The Titan squeezes.\n\n\
**You have died. Type `~reset` to start over.**'
            self.choices[0] = []
            return response

    def P203(self, *option):
        if option == ():
            response = 'You withdraw.\n\n\
You had no choice. What could you, a lone trainee, have done...?\n\n\
From behind you come the voices of the elite soldiers, doomed to die, and the moaning of the Titans that tear at Eren\'s \
motionless body.\n\n\n\
\"I see,\" Commander Pixis says gratefully as you speak. \"Thank you for your report. As the one who led the operation, I accept \
full responsibility.\"\n\n\
The plan claimed the lives of a vast number of soldiers, and it ended in failure.\n\n\
Behind you, Wall Rose is dyed the color of blood by the setting sun. How long will humanity be able to hold this wall...?\n\n\
**You have obtained the \"Failure of the Reclamation Plan\" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P204(self, *option):
        if option == ():
            response = 'You and the others head into town to rescue your surviving comrades.\n\n\
More and more Titans flood the city streets.\n\n\
The rescue party takes more than a few casualties itself...but you are able to save many of your friends.\n\n\
Other members of your training regiment thank you profusely when you bring them gas tanks.\n\n\
\"You saved our necks,\" says one of the people you help - Jean. \"We were about to storm the headquarters building when you guys \
showed up. Might\'ve cost us our lives.\"\n\n\
You see Mikasa among those who made it out safely. Nothing less from your top graduate.\n\n\
You look a little closer. Mikasa is holding a boy.\n\n\
It\'s Eren. You can\'t believe your own eyes. Eren was supposed to be dead... His vest and vertical maneuvering equipment are gone; \
he\'s wearing only his soldier\'s undershirt. He\'s unconscious - almost aas if asleep - but alive. And his arms and legs are in \
perfect shape. No injuries anywhere.\n\n\
Some of your friends are talking nearby.\n\n\
\"I still can\'t believe it. That Titan collapsed, and Eren came out of its corpse. Could it have...been Eren all along...?\"\n\n\
Whatever the case, you and the others withdraw beyong the inner wall, taking the unconscious Eren with you.\n\n\
Type :one: to continue.'
            self.state.statuses.eren = 'Alive'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 233

    def P205(self, *option):
        if option == ():
            response = 'Something unforeseen has happened, you\'re sure of it.\n\n\
You grab some of the gas canisters and head for the boulder.\n\n\
As you get closer, you can see a lone Titan slumped on the ground, leaning against the boulder.\n\n\
It looks like Eren in Titan form - but the top half of his head is missing, as are both his hands.\n\n\
You can pick out the silhouettes of soldiers on the rooftops nearby. You land near them.\n\n\
\"It\'s great that that kid can turn into a Titan and all, but then he went nuts and started attacking the people with him.\"\n\n\
The soldiers explain the situation to you with long looks.\n\n\
\"He ended up smashing his own head in, and... Well, you see. He\'s not going to be carrying any boulder anytime soon.\"\n\n\
It\'s worse than you imagined. The only upside is that the soldiers are grateful for the tanks of gas.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 231

    def P206(self, *option):
        if option == ():
            response = 'You apply to join the Survey Corps.\n\n\
More than a few of your classmates from the 104th Training Corps do the same.\n\n\
Many were surprised, though, when word went around that Jean Kirstein is among the applicants.\n\n\
His attitude had always been, \"Huh? No way, I\'m not like Eren. I don\'t have a death wish. And anyway, no one\'s gonna \
convince me to risk my life for anything.\"\n\n\
The turth is, when Commander Erwin addressed the trainees, not attempting to hide the facts - that the casualty rate among the \
Survey Corps had been 90% over the last five years, that half of all new recruits died on their first expedition outside the wall - \
many of the would-be applicants walked away.\n\n\
Jean, pale and gritting his teeth, had been one of those who stayed.\n\n\
\"Dammit. Why should I join the...the Survey Corps...\"\n\n\
He seemed to mock himself even in his resolution.\n\n\
You wondered what had driven him to it, but when you asked he only shouted and glared at you.\n\n\
Some time later...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 2061

    def P2061(self, *option):
        if option == ():
            response = 'You are lining up the horses during an expedition outside the wall - yes, the very expedition from \
which half of you will not return - when he suddenly tells you.\n\n\
\"Someone said to me once...that I had the makings of a commander. Even though honestly, I think he was the one who should\'ve \
been in charge.\"\n\n\
Then he looks at you like a thug with a nasty idea. Maybe he thinks he\'s smiling. You think maybe sometimes that face has worked \
against this man, Jean.\n\n\
\"You know why he said that? It\'s because I\'m weak. What a laugh, huh?\"\n\n\
Somehow, you think you have a sense of what Jean\'s mysterious mentor was trying to say.\n\n\
Jean is weak, but that means he understands what it is to be weak. As you, as many people, are. Not heroes. Just regular people.\n\n\
You think maybe you could follow this uncertain youth.\n\n\
But be that as it may, first the two of you must survive.\n\n\
You take your horse\'s reins in your hand, and join the rest of the Survey Corps.\n\n\
**🎉 Congratulations! You\'ve obtained the \"Jean Kirstein of the Survey Corps\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P207(self, *option):
        if option == ():
            response = 'You put some distance between yourself and your friends, and then you act.\n\n\
You\'re confident you can distract the Titans. But to actually kill one, alone, is difficult.\n\n\
You see Annie and Reiner, two of the top students in your trainee class, acting on their own. Maybe that\'s best for the truly \
skilled.\n\n\
Regardless, you forge ahead.\n\n\
You don\'t have to worry about killing them. You just have to get their attention; slowing them down is the real goal.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 294
        elif option[0] == 's':
            self.cur_page[0] = 318

    def P208(self, *option):
        if option == ():
            response = 'It doesn\'t look like things can get much worse. You were past the wall, supposedly safe at last, and now \
you\'re surrounded by your fellow soldiers.\n\n\
Members of the Garrison are lined up shoulder to shoulder, blades drawn. They watch you, ready to fight at any moment. The fixed \
guns are aimed at you from atop the wall. Those are supposed to be used against Titans.\n\n\
All this out of a surfeit of fear about Eren.\n\n\
No matter what you and your friends say, terror deafens the guard captain and his soldiers. But if you hadn\'t tried to talk to \
them, Eren might have been \"dealt with\" before he even woke up.\n\n\
\"Trainee Yeager!\" the guard captain shouts.\n\n\
The fact that the captain, responsible for all the soldiers in Trost District, immediately came out to deal with things personally \
shows just how dire he thinks the situation is.\n\n\
His voice is shaking; his words seem to catch in his throat.\n\n\
\"I\'ll ask you plainly. What are you? A man? Or a Titan?\"\n\n\
\"I... I don\'t understand the question!\" Eren answers. His voice is shaking, too.\n\n\
How could he? Even you don\'t understand what\'s happening.\n\n\
It\'s true Eren became a Titan. But is he, ultimately, a human like you - albeit one with the power to transform into a Titan - \
or is he now a Titan in human form?\n\n\
You...\n\n\
:one: Trust Eren!\n\n\
:two: Do not trust Eren'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 273
        elif option[0] == 2:
            self.cur_page[0] = 229

    def P209(self, *option):
        if option == ():
            response = 'A commotion breaks out in the camp as the soldiers are preparing.\n\n\
Word is that a Survey Corps squad has returned.\n\n\
With the gate in its current state, they climbed the wall to get back into the city.\n\n\
Several people come walking by wearing military uniforms, as well as capes designed for activities outside the wall.\n\n\
They carry themselves differently from the Garrison. With your newly-gained combat experience, you can tell. These are people who \
have survived not one fight, but many, against the Titans.\n\n\
They\'re coming toward you at a brisk pace.\n\n\
The man who appears to be their leader calls out to you:\n\n\
\"You. Where\'s the commander of the guard unit?\"\n\n\
The man is short, but his gaze is sharp, and he never seems to make an unnecessary movement. His very existence is somehow inspiring.\n\n\
You tell him where to find the command unit, and he spins on his heel and departs with his soldiers. You see the \"Wings of Freedom\" \
crest on his back - the symbol of the Survey Corps.\n\n\
A whisper runs through the camp: \"That\'s Captain Levi!\" Many sound deeply impressed.\n\n\
It wasn\'t possible to communicate with the Survey Corps once they left on their expedition; no one even knew where exactly they \
were. But they seem to have sensed that Trost was in trouble, and came back.\n\n\
Captain Levi is exceptional even among the elite troops of the Survey Corps. He\'s known as \"Humanity\'s Strongest Soldier\" \
and is said to be as strong as an entire brigade. You know rumor tends to exaggerate, but he sounds impressive nonetheless.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 161

    def P210(self, *option):
        if option == ():
            response = 'You work with Captain Levi and several other Survey Corps soldiers.\n\n\
**You now have the option of Captain Levi\'s help in some future battle scenarios.**\n\n\
Type :one: to continue.'
            self.state.flags.levihelp = 'Yes'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 134

    def P211(self, *option):
        if option == ():
            response = '\"...What?\" Mikasa\'s eyes widen at your words. \"No...I can\'t do that.\"\n\n\
What do you say?\n\n\
:one: \"You can do the most good in the front. Stop the Titans there and we\'ll be safe back there, too.\"\n\n\
:two: Encourage Mikasa. \"Eren will be fine. But if you\'re worried - then go to him.\"'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 176
        elif option[0] == 2:
            self.cur_page[0] = 103

    def P212(self, *option):
        if option == ():
            response = 'It looks like the plan has gone awry. You don\'t yet know what\'s happened.\n\n\
Has the plan failed completely? Or is there still a chance it could work?\n\n\
If there is, then you have to keep the Titans from reaching Eren and the others. That\'s all you can do now.\n\n\
You ask the commander at your position for permission to descend into the city and fight the Titans.\n\n\
\"Granted. Be careful, trainee.\"\n\n\
Some of your friends have the same idea. To your surprise, Jean is among them.\n\n\
You set your anchors in the wall in an explosion of guidewires, and head to the streets.\n\n\
**Your Affinity with Jean has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.jean += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 191

    def P213(self, *option):
        if option == ():
            response = 'A reinforcement unit soon arrives. At their head is Commander Dot Pixis, the man responsible for the whole \
southern territory, including Trost District. He received word of the Titan attack and acted immediately.\n\n\
Not long after, the elite men and women of the Survey Corps, who had been out on an expedition, return as well, and join the \
guard unit.\n\n\
This is how the end begins in the battle to defend Wall Rose.\n\n\
Many soldiers lost their lives, but the citizens were able to safely evacuate, and you were able to shore up the defenses.\n\n\
Compared to the tragedy in Shiganshina District five years ago, there is little to complain about today.\n\n\
Wall Rose is safe, but Trost has become a city infested by Titans.\n\n\
Everyone is constantly on high alert, because you don\'t know when the inner wall may be broken down.\n\n\
It\'s humanity\'s front line, the most dangerous place in the world, but also a prime spot for the Survey Corps to risk a little \
danger in order to observe the Titans and even collect samples.\n\n\
You, along with Eren and the others, apply to join the Survey Corps. Your survival in this battle has earned you some credit. \
Now, today, you prepare to enter Trost District once more on another dangerous mission...\n\n\
**🎉 Congratulations! You\'ve obtained the \"A Narrow Victory\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P214(self, *option):
        if option == ():
            response = 'Just before you must decide which unit to join...\n\n\
As the trainees all mull over the question together, you have a chance to talk to Annie Leonhart.\n\n\
\"I don\'t know. You should do what you want,\" she says diffidently.\n\n\
For her part, she\'s set on the Military Police Brigade: elite soldiers in the safety of the Interior. It\'s her right as one of \
the top scorers in the class. If it\'s what she wants, she\'ll probably get it.\n\n\
\"I just want to save myself,\" she says, her expression never changing.\n\n\
You think back to what you saw after the Battle of Trost: Annie apologizing endlessly to the corpse of her friend.\n\n\
Despite what she says, you think there\'s more than self-interest behind Annie\'s decision.\n\n\
She\'s strong-willed; you\'re sure she has a goal in mind.\n\n\
You\'re determined to choose your own path, like her. As long as the choice is in your power to make, you will.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 306
        elif option[0] == 's':
            self.cur_page[0] = 316

    def P215(self, *option):
        if option == ():
            response = 'You graduate from trainees into full soldiers, each of you going off to your different regiments.\n\n\
You claim your modest personal effects from the training camp and get ready to leave.\n\n\
Eren comes up to you as you\'re packing.\n\n\
\"This is a memento of Armin. I want you to have it.\"\n\n\
It\'s a single notebook, the pages packed with careful letters. It\'s his notes on tactics and strategy from your lectures during \
training...along with his personal observation. It\'s a testament to his intelligence and effort. If Armin had survived, you\'re \
sure he would have been invaluable to his unit, to humanity.\n\n\
He\'s also written about the \"outside world,\" information that nearly makes this notebook a forbidden object. A vast body of \
salt water called the \"sea,\" water made of fire, sandy snow fields... They sound like something out of a dream, but as you read \
them with Armin\'s observations, you can\'t help wondering if they might really exist.\n\n\
Holding the notebook, you reflect once more. You may never be like Armin. But you\'ll never forget the fact that he lived - a boy \
with an insatiable curiosity about the world outside the walls.\n\n\
Maybe one day, you\'ll be able to experience the world he so longed to see.\n\n\
**🎉 Congratulations! You\'ve obtained the \"Armin Arlert\'s Dream\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P216(self, *option):
        if option == ():
            response = 'That\'s right. A rescue operation would cost eight additional lives.\"\n\n\
Behind her glasses, the female soldier\'s eyes are as hard as ever, but you seem to have impressed her.\n\n\
\"Of course reality isn\'t as simple as our calculations. But it\'s highly likely that a rescue operation now would create more \
casualties than it would prevent. This battle has already claimed a huge number of lives, Headquarters has been overrun, and we \
can\'t count on fresh supplies. We have to put our remaining forces to best use in light of those facts.\n\n\
\"We\'d already considered the possibility of a rescue long before you trainees brought it up.\"\n\n\
She starts walking, and nods for you to follow.\n\n\
\"If you still think there\'s a case to be made, tell it to the captain.\"\n\n\
You approach the guard captain just as a veteran Garrison soldier is speaking to him.\n\n\
\"Trainee Mikasa\'s a unique asset, sir. A rescue operation would be worthwhile even if she were the only one it helped! \
We need her for this plan - we need her to shore up the defense of the wall!\"\n\n\
The guard captain doesn\'t exactly look comprehending, but he seems moved by the soldier\'s words. Looks like your timing is perfect. \
The bespectacled woman adds her own urging, and the guard captain nods slowly.\n\n\
A rescue operation it is.\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 126

    def P217(self, *option):
        if option == ():
            response = 'At that moment, you suddenly spot a tall Titan.\n\n\
\"An Abnormal!\"\n\n\
It dashes straight through the building you had hoped to land on.\n\n\
\"Split up!\"\n\n\
You frantically change direction in midair. For an instant, you see the sickening details of the Titan\'s form.\n\n\
It is thin, its body all muscles. Its arms are preternatually long. It has a square chin, and its eyes are somehow empty.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 265

    def P218(self, *option):
        if option == ():
            response = 'You and the other soldiers on the wall shoot and shoot until you\'ve lost all sense of time.\n\n\
The Titans can\'t reach the top of the wall, but by the same token you are isolated, unable to move.\n\n\
What\'s become of your allies? How is the battle going?\n\n\
As long as you have ammunition, you will keep at your work...\n\n\
Your fight ends here. Your companions are the ones who will determine ultimate victory or defeat. The End.\n\n\
**You have obtained the \"A Regular Soldier\" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P219(self, *option):
        if option == ():
            response = 'Everyone moves according to Marco\'s instructions.\n\n\
The plan is to lure the slower Titan to an open area, where Jean and three other capable people will jump on it from behind. \
The rest of you are to keep watch nearby for approaching Titans.\n\n\
Incredibly, the plan works and the Titan is defeated.\n\n\
You trainees have claimed your first victory in battle.\n\n\
It\'s thanks to Marco: it was his plan, and he was the one to lure out the Titan. You realize that even in training, Marco was \
less concerned about his own marks than about background roles like this.\n\n\
...At the same time, however, you can tell how dangerous this was. This isn\'t training, and Titans are living creatures. Marco \
might have just barely escaped being killed.\n\n\
**From this point on, if you see the words \"he/she seems somehow uneasy\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 157

    def P220(self, *option):
        if option == ():
            response = 'You face down the Titan, using all your skill in vertical maneuvering.\n\n\
But you\'re too late. The creature swallows Thomas as you look on.\n\n\
All you can think of is attacking the Titan - but your blade cuts only air. The Titan has turned around as though it hasn\'t even \
noticed you, and sets off, demolishing buildings as it goes.\n\n\
The missed swing throws you off balance, and you slam into a building, the pain knocking you unconscious.\n\n\
When you regain consciousness...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 132

    def P221(self, *option):
        if option == ():
            response = 'There\'s nothing you can do. You know this scene is being repeated endlessly, everywhere on the battlefield.\n\n\
You turn and leave.\n\n\
Type :one: to continue.'
            self.state.statuses.franz = 'Dead'
            self.state.statuses.hannah = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 142

    def P222(self, *option):
        if option == ():
            response = 'From the top of the wall at the very front lines, you return to the rear to make your report. Even as you go, \
your allies are keeping up a hopeless barrage from atop the wall with its ruined gate. Titans are flooding the city; you can see them \
wandering the streets. You run along the wall until you reach the part nearest the interior.\n\n\
The other side is packed with soldiers and evacuated citizens.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 178

    def P223(self, *option):
        if option == ():
            response = '\"Yes, sir. I did want to save him, of course, but it\'s also true that I have a plan,\" Armin responds. \"The \
boulder in the city...Eren will turn into a Titan and carry it for us.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 193

    def P224(self, *option):
        if option == ():
            response = 'The Garrison soldiers confronted with Krista\'s impassioned pleas seem to be only humoring her.\n\n\
\"I see. We\'ll handle it.\"\n\n\
With that, they turn and leave. You follow them. When Krista is out of earshot, you ask, \"Will you really send a rescue squad?\"\n\n\
\"Hm,\" says a bespectacled woman with the air of command. Then she looks at you and says, \"Say there are 20 soldiers left on the \
field, and if we leave them, 90 percent will die. Suppose a rescue operation could save half of them. We would need 40 soldiers for \
the operation, and only 60 percent of them would return alive. ...Try figuring out how many more soldiers would die as a result of \
the rescue effort.\"\n\n\
:one: 16\n\n\
:two: 8\n\n\
:three: 6\n\n\
:four: 0'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 122
        elif option[0] == 2:
            self.cur_page[0] = 216
        elif option[0] == 3:
            self.cur_page[0] = 122
        elif option[0] == 4:
            self.cur_page[0] = 122

    def P225(self, *option):
        if option == ():
            response = 'You are assigned as bait to distract the Titans, along with a great many other soldiers.\n\n\
At no small cost - twenty percent of the soldiers die in the effort, and even this is vastly better than if you were to engage the \
Titans directly - you succeed in drawing the Titans to one corner of the city.\n\n\
With this, the path through the city from the boulder to the gate is clear of Titans; the most crucial phase of the plan can now \
begin.\n\n\
Eren, along with his distressingly small squadron of select bodyguards, is going to infiltrate the city. Eren will transform into \
a Titan and use the boulder to block the hole.\n\n\
At any rate, that\'s what you, busy at your duty, are praying for.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 108

    def P226(self, *option):
        if option == ():
            response = 'In any case, the plan works. You manage to exterminate the Titans inside the headquarters building, meaning \
you can get more gas.\n\n\
You and the other survivors resupply your vertical maneuvering equipment. You\'ll once more be able to move freely through the air.\n\n\
Talking easily now, you and your friends make for the exit.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 236

    def P227(self, *option):
        if option == ():
            response = 'You set Eren down on the roof as quickly as you can, then use vertical maneuvering to drop to the ground.\n\n\
Mikasa\'s fall seems to have been broken by an awning; thankfully, she\'s not hurt.\n\n\
\"Why are you here?!\" She sounds at once shocked and angry.\n\n\
There is a rumbling. You suddenly register that a Titan, more than ten meters tall, is directly behind you.\n\n\
You rush toward Mikasa. She fights you, tries to push you away. Maybe she\'s telling you to save Eren, not her. ...Can you have \
one moment today when you\'re not holding a struggling comrade?\n\n\
Behind you, the rumbles are getting closer.\n\n\
With the modicum of gas you have left, can you even carry two people?\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 175

    def P228(self, *option):
        if option == ():
            response = 'You and the others leap into action.\n\n\
The hope is that together, you can bring the Titans down.\n\n\
And somehow, with one after another, you succeed.\n\n\
But then, too, one Titan after another seems to be converging on your position.\n\n\
Is this really helping Eren and the others...?\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 294

    def P229(self, *option):
        if option == ():
            response = 'You raise both hands and run toward the guard captain and his squadron, leaving Eren to his fate.\n\n\
The soldiers must believe you really are human, because they don\'t shoot you.\n\n\
After this, the guard captain coldly gives the order to fire.\n\n\
The walltop guns open up on Eren and the friends who believed in him.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 240

    def P230(self, *option):
        if option == ():
            response = 'Mikasa seems to be on the verge of cutting down the people around her. That can only make things worse.\n\n\
You tell her you know how important Eren is to her, but that she needs to calm down.\n\n\
Her cheeks turn a little red.\n\n\
\"Important... Yes. Eren is family, after all.\"\n\n\
It looks like you\'ve talked her down. You start talking to the commander, Ian.\n\n\
**Your Affinity with Mikasa has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 269

    def P231(self, *option):
        if option == ():
            response = 'The Titan Eren has collapsed.\n\n\
Instead of carrying the boulder, he tried to attack the friend who called out to him.\n\n\
Steam rises from the arms and face he himself ruined, but they show no sign of regenerating. It looks like he\'s alive...but he \
doesn\'t move, as if he has lost consciousness.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 196

    def P232(self, *option):
        if option == ():
            response = 'Eren, in his Titan form, has lost both hands and the top of his head; he sits motionless.\n\n\
The elite squad guarding him is engaged in a desperate battle with the oncoming Titans to protect their defenseless charge.\n\n\
They\'re excellent soldiers, but the Titans keep coming.\n\n\
At this rate, they\'ll never be able to hold them all off.\n\n\
What do you do?\n\n\
:one: Join the elite troops in their fight against the Titans\n\n\
:two: There\'s nothing to be done. Withdraw'
            self.choices[0] = [1,2]
            if self.state.statuses.armin == 'Alive':
                response = response + '\n\n\
:three: Rely on Armin'
                self.choices[0].append(3)
            return response
        elif option[0] == 1:
            self.cur_page[0] = 293
        elif option[0] == 2:
            self.cur_page[0] = 203
        elif option[0] == 3:
            self.cur_page[0] = 150
        elif option[0] == 's':
            self.cur_page[0] = 262

    def P233(self, *option):
        if option == ():
            response = 'You\'ve survived the battle in the hellish streets of Trost District, and now you withdraw.\n\n\
You and several of the other trainees fall back to the rear, to safety.\n\n\
At last you\'re in a safe place, full of Garrison soldiers. You...\n\n\
:one: Are with Eren\n\n\
:two: Are not with Eren'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 194
        elif option[0] == 2:
            self.cur_page[0] = 110

    def P234(self, *option):
        if option == ():
            response = '*Let\'s go get him*, you say to them.\n\n\
If he was swallowed whole by the Titan, it might still be possible to rescue him. And with Mikasa\'s skill...\n\n\
Armin\'s eyes widen at your words. You start to ask him what kind of Titan it was, what exactly happened, but Mikasa taps you \
on the shoulder.\n\n\
\"Forget it. If it were possible to save him, Armin would have done it.\"\n\n\
**Your Affinity with Mikasa and Armin has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.mikasa += 1
            self.state.affinities.armin += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 117

    def P235(self, *option):
        if option == ():
            response = 'You shout. Whether Mikasa hears you or not, you can\'t tell.\n\n\
But she rises and takes a blade in her hand. You doubt she can best the Titan, but she isn\'t going to give up, either. \
She\'s a strong woman.\n\n\
Even as you admire her, a Titan the size of a four-storey building is coming relentlessly closer.\n\n\
She sees it and takes her stance...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 174

    def P236(self, *option):
        if option == ():
            response = 'Outside, you see numerous Titan corpses.\n\n\
This is what happens when Titans fight each other. Even on a battlefield full of the enemy, this is the first time you\'ve seen \
so many fallen Titans in one place...\n\n\
Did that Titan take out all these others single-handedly?\n\n\
At the moment, the Titan has lost both its arms, but it sinks its teeth into two other Titans, kicks them, refuses to stop fighting. \
It seems to have regenerative abilities like other Titans, but it looks like its powers just can\'t keep up...\n\n\
\"If we could understand what that Titan is...\" somebody murmurs.\n\n\
You agree...but it doesn\'t look like you\'ll have the chance.\n\n\
The mysterious Titan topples the last of the nearby enemies, then sinks to its knees, exhausted.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 282

    def P237(self, *option):
        if option == ():
            response = 'You ask around the guard unit in hopes of getting news about other members of the 104th Training Corps.\n\n\
You learn that many of your classmates are dead, or missing in action, including Eren and his squad.\n\n\
You think of Eren and his companions, so full of spirit. Mikasa was so close to him. What will she think when she finds out?\n\n\
Type :one: to continue.'
            self.state.statuses.eren = 'Dead'
            self.state.statuses.squad34 = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 252

    def P238(self, *option):
        if option == ():
            response = 'Again and again you risk your life to protect her.\n\n\
There - a Titan is about to grab Krista with its giant hand!\n\n\
You leap over with vertical maneuvering. You dive between Krista and the Titan, slashing the great hand with your blade. You spin \
around, making to attack the Titan again...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 71

    def P239(self, *option):
        if option == ():
            response = 'Watching the Titan, you have an idea.\n\n\
If you could lure it toward Headquarters, maybe it would get rid of the Titans in that area...\n\n\
\"All right,\" Mikasa nods.\n\n\
You share what\'s left of your gas with Mikasa. It should be just enough for you to meet up with the others.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 139

    def P240(self, *option):
        if option == ():
            response = 'Out of the smoke of gunfire and explosions a Titan towers. In its hand, humans. Eren became a Titan once \
more to protect those who had faith in him.\n\n\
Soldiers all around cry out in terror and begin to flee.\n\n\
The Titan Eren looks down at you in pity as he rises, then sets off at a run with his friends still in his hand. No one with you is \
capable of stopping a 15-meter Titan.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 296

    def P241(self, *option):
        if option == ():
            response = '\"You\'re taking Ian\'s side?\" Rico says, fixing you with her intense glare.\n\n\
\"It isn\'t your fault the plan failed. Be rational,\" Mitabi says gently.\n\n\
As for Ian...he doesn\'t seem any happier with your support.\n\n\
Perhaps he trusts his own judgment - but knows all too well the terrible things it implies.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 269

    def P242(self, *option):
        if option == ():
            response = 'Mikasa makes for the headquarters building. It seems crazy, but then, it\'s better than waiting to be eaten \
by Titans after your gas inevitably runs out. ...No. You expect Eren will bleed out before that.\n\n\
Your comrades, moved to action, also start maneuvering toward headquarters.\n\n\
Some of them will probably make it.\n\n\
But you, carrying a wounded friend, and Mikasa, covering both of you, have a difficult fight. Despite her exceptional \
maneuvering abilities, Mikasa is hard-pressed.\n\n\
\"Dammit! Let me fight... No. I\'m useless. Just leave me here!\"\n\n\
Eren is making a racket on your back. You\'re sure he\'s serious. One Titan after another attacks you as you fly along awkwardly, \
but Mikasa wards them off with her incredible acrobatics.\n\n\
She flies brilliantly, trailing white mist from the expelled gas.\n\n\
But...\n\n\
Suddenly, the trail disappears. In midair, Mikasa goes stiff and gets thrown sideways.\n\n\
She\'s out of gas.\n\n\
That fantastic display must have burned through what little she had left. As she falls, Mikasa points toward the headquarters \
building.\n\n\
*Leave me*, she seems to say, *go*.\n\n\
You...\n\n\
:one: Go to rescue Mikasa\n\n\
:two: Resolve to rescue Eren, so her sacrifice won\'t be in vain'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 227
        elif option[0] == 2:
            self.cur_page[0] = 131

    def P243(self, *option):
        if option == ():
            response = 'Marco, having survived the brutal engagement thus far, is fighting on the same street as you are.\n\n\
\"Just a little longer. We have to fight...to save Eren.\"\n\n\
He smiles at you.\n\n\
It\'s just like you remember from training: his smile seems very warm, but his eyes are piercingly clear. Perhaps it\'s because \
of all the friends and soldiers who have died in front of them.\n\n\
\"If it\'s for a purpose, I\'m not afraid to die.\"\n\n\
He seems somehow uneasy... But now, you must fight.\n\n\
Fight for victory, or at least survival.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 314
        elif option[0] == 's':
            self.cur_page[0] = 247

    def P244(self, *option):
        if option == ():
            response = 'In a strained voice, you tell her the simple truth:\n\n\
You are the lone survivor of Squad 34.\n\n\
You feel like there must be something more to say...but no matter how you dress up the words, they won\'t bring your friends back.\n\n\
This is the first time some of the other trainees are learning the news. You hear moans and sounds of shock.\n\n\
But Mikasa herself responds with remarkable calm:\n\n\
\"...I see. All right.\"\n\n\
There is no trace of grief or distress in her eyes. And to your own surprise, you find that hard to bear.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 117

    def P245(self, *option):
        if option == ():
            response = 'You offer Armin your hand, but he simply stares at it, then suddenly stands.\n\n\
\"I\'m sorry I caused problems! I\'ll meet up with the rear guard!\"\n\n\
Then he heads for the rear, alone. He had seemed about to collapse a moment ago - is he really okay?\n\n\
Your ruminations are interrupted by Jean\'s voice.\n\n\
\"Hey. We\'ve got orders to advance.\"\n\n\
You have no choice. You and your comrades keep moving up.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 183

    def P246(self, *option):
        if option == ():
            response = 'Commander Dot Pixis, who has arrived with the reinforcements, quickly takes control of the situation.\n\n\
He is the one responsible for the defense of the entire southern region, which includes Trost District, and a famous lifelong \
perv. That he mustered reinforcements and arrived on the field at their head so quickly speaks to his genius.\n\n\
He is older, but full of life; though he has the air of command, he wears the same uniform and vertical maneuvering equipment \
as any other soldier.\n\n\
No one knew what happened to the Titan, rumors of which were on everyone\'s lips, but apparently the commander had asserted his \
authority, and vouched for the safety of Eren and his friends.\n\n\
The guard captain had been at the end of his rope, but with all the reinforcements he was able to reform his ranks.\n\n\
\"I heard there\'s a plan to strike back.\"\n\n\
\"Strike back? I know those reinforcements brought our numbers back up, but what are we going to do about those Titans?\"\n\n\
As unease and mistrust deepen among the soldiers, Commander Pixis informs them that he has a secret plan for a counterattack.\n\n\
\"The results of top-secret experiments in transforming humans into Titans.\"\n\n\
And then he introduces...Eren.\n\n\
\"What\'s going on here?\"\n\n\
The soldiers around you, not least your friends, are rocked by this.\n\n\
Maybe Eren did transform into a Titan - but you have a pretty good sense that this \"top-secret experiments\" stuff is just cover.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 197

    def P247(self, *option):
        if option == ():
            response = 'You decide to fight alongside Marco.\n\n\
His technique is superb, and he never hesitates to help your comrades - indeed, it seems basic to him. He distracts Titans, acts \
as bait.\n\n\
It is one of his best virtues, but to you, it also looks dangerous.\n\n\
You pause on a rooftop and bring it up with him.\n\n\
Marco shrugs slightly and says, \"I\'m just lucky.\"\n\n\
**From this point on, if you see the words \"Marco is lucky\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 314

    def P248(self, *option):
        if option == ():
            response = 'You approach one of the surviving horses and try to take it by the reins.\n\n\
But the animal fights you, the reins flapping around. It makes a terrible whinnying, eyes wide.\n\n\
This is something completely different from the calm, intelligent animals you rode during horsemanship training.\n\n\
You recall that the horses used by the Survey Corps to fight Titans are of peerless lineage and receive special training; \
they bond with just one human for their entire lives. The horses are themselves as expensive - and as valuable - as any weapon.\n\n\
Even people can hardly keep their composure under these circumstances; what more for an average horse?\n\n\
You drop the reins when a giant hand grabs you. In the instant you are being crushed to death, you see the horse flee. It needn\'t \
have. Titans only attack humans, anyway.\n\n\
**You have died. Type `~reset` to start over.**'
            self.choices[0] = []
            return response

    def P250(self, *option):
        if option == ():
            response = 'The plan fails.\n\n\
Maybe the timing of the lift was off. Maybe somebody fired at the wrong moment. Or maybe one of the Titans didn\'t go down...\n\n\
Any number of things might have gone wrong. The chances of success always were exceptionally small.\n\n\
It is no one\'s fault. And everyone pays the price equally. The Titans may be only three or four meters tall, but without vertical \
maneuvering the humans don\'t stand a chance. One after another of your friends are eaten by Titans.\n\n\
And then they come for you...\n\n\
**You have obtained the \"104th Training Corps Annihilated at Headquarters\" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P251(self, *option):
        if option == ():
            response = 'The Titan Eren rises with a great roar.\n\n\
Gushing steam, his ruined head and hands regenerate. And from the eyes in that newly-formed face shines the light of the real Eren. \
He hefts the nearby boulder with both arms, lifts it onto his shoulders, and begins to walk.\n\n\
The boulder looks heavier than he is, but he sets off for the gate. Steam rises from all over his body. For an instant, you are \
transfixed.\n\n\
The members of the selected squad, who have survived through desperate struggle, stop and stare at him, too.\n\n\
But...\n\n\
Under the weight of the stone, he walks powerfully, but slowly.\n\n\
At this rate the Titans in the streets will catch him, to say nothing of the ones flooding in from outside. And while he\'s \
holding that rock, he has no way to fight back...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 279

    def P252(self, *option):
        if option == ():
            response = 'You know many of your comrades have died. And of those that remain, many are still in danger.\n\n\
You learn that the city\'s headquarters was swarmed by Titans before anyone could withdraw, making it impossible \
to resupply with gas. Many of the middle guard soldiers are stranded in the city.\n\n\
At this rate they will all be destroyed, unable to escape from a city of Titans.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 270

    def P253(self, *option):
        if option == ():
            response = '**Your Affinity with Jean has increased by 1!**\n\n\
Maneuvering gracefully, Jean leads your companions into the city.\n\n\
But your gas reserves are scant, and the Titans are many.\n\n\
You see several of your friends grabbed by Titans. Or their gas runs out and their vertical maneuvering equipment stops working, \
throwing them to the ground. Several Titans close in on them. The despairing cries of your comrades echo through the streets.\n\n\
Jean has landed and is staring at one of your captured friends.\n\n\
You...\n\n\
:one: Help your friends!\n\n\
:two: Defer to Jean\'s judgment'
            self.state.affinities.jean += 1
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 271
        elif option[0] == 2:
            self.cur_page[0] = 283

    def P254(self, *option):
        if option == ():
            response = 'You use vertical maneuvering, fighting as hard as you can.\n\n\
You have to stop any Titans from getting through, so the elite squad\'s gambit won\'t be in vain.\n\n\
You rip through the air on a trail of gas. You slice with your sword, hearing the sound of the wind. Your perspective swings \
dizzyingly. The sky is sideways, then it\'s at your feet, the ground rushing to meet your head.\n\n\
Over that onrushing ground, you can see soldiers, surrounded by Titans, being eaten by them. Above the roar of the wind, screams \
reach your ears. You see both Ian and Mitabi about to be eaten. You just keep slicing. Soldiers die and despair. And just beyond, \
the Titan Eren walks.\n\n\
Type :one: to continue.'
            self.state.statuses.ian = 'Dead'
            self.state.statuses.mitabi = 'Dead'
            self.choices[0] = [1]
            if self.state.flags.levihelp == 'Yes':
                response = response + '\n\n\
:two: Seek help from Levi instead'
                self.choices[0].append(2)
            return response
        elif option[0] == 1:
            self.cur_page[0] = 302
        elif option[0] == 2:
            self.cur_page[0] = 259

    def P255(self, *option):
        if option == ():
            response = 'You realize you are a little hungry. After all, it\'s not like you\'ve had time to eat.\n\n\
But hunger is a sign you\'re still alive. Your anxiety eases slightly.\n\n\
If Sasha is alive and nearby, you think you\'ll tell her...\n\n\
Tell her that if you both survive this battle, you should get something delicious to eat together.\n\n\
And then...you return to the fight.\n\n\
**Your Affinity with Sasha has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.sasha += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 294

    def P256(self, *option):
        if option == ():
            response = '\"F-First, let\'s find some food!\" Sasha says. \"There must be provisions that got scattered around the city \
in the confusion. They\'ll help us later...\"\n\n\
Everyone is predictably exasperated at this idea.\n\n\
\"This is no time to be joking around!\" Jean yells.\n\n\
\"F-Food is definitely important.\" Krista alone tries to smooth things over.\n\n\
There is some logic to what Sasha is saying, but if this battle goes south, food isn\'t going to save you.\n\n\
**Your Affinity with Sasha has increased by 1!**\n\n\n\
Now, who do you choose as your leader?\n\n\
:one: Jean\n\n\
:two: Marco\n\n\
:three: Krista'
            self.state.affinities.sasha += 1
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 140
        elif option[0] == 2:
            self.cur_page[0] = 66
        elif option[0] == 3:
            self.cur_page[0] = 102

    def P257(self, *option):
        if option == ():
            response = 'You call out to Armin and head for the rear using vertical maneuvering. Armin is pale and silent, but seems to \
be following you.\n\n\
Type :one: to continue.'
            self.state.statuses.eren = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 112

    def P258(self, *option):
        if option == ():
            response = 'Suddenly, a fusillade rings out.\n\n\
It\'s practically right next to you. What in the world happened?\n\n\
Reiner jumps onto a nearby roof with his vertical maneuvering equipment without so much as asking the permission of your guards. \
Annie, Jean, and several others follow him.\n\n\
Including you.\n\n\n\
From the rooftop, you look toward the wall, and see an astonishing sight.\n\n\
The fixed guns are turned toward the inner wall. Not toward the Titans trapped in the city; they fired at this side of the wall. \
The side full of your allies.\n\n\
And then, through the smoke, you see what looks like a seated Titan.\n\n\
Its body is incomplete, just muscles and bones. And amidst the bones...Eren, who seems to have given birth to the thing.\n\n\
\"What...the hell...is going on?\" someone asks.\n\n\
Type :one: to continue.'
            self.state.statuses.eren = 'Alive'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 246

    def P259(self, *option):
        if option == ():
            response = 'At that moment, a group comes whizzing through the air.\n\n\
It\'s Captain Levi and his elite soldiers.\n\n\
Their capes flutter as they maneuver around, giving them the appearance of birds.\n\n\
They make sure that the sacrifices of the soldiers who landed on the ground are made good to the full.\n\n\
They assail one Titan after another. They slow down the monsters, save the soldiers on the ground, land precise blows on the \
Titans\' weak points. They massacre the creatures.\n\n\
A cheer goes up from the soldiers below.\n\n\
And through the sound, Eren walks.\n\n\
Type :one: to continue.'
            self.state.statuses.ian = 'Alive'
            self.state.statuses.mitabi = 'Alive'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 302

    def P260(self, *option):
        if option == ():
            response = 'The Titan appeared so suddenly, it seemed to come from the roof of a building.\n\n\
And it punched the Titan that was trying to attack Mikasa.\n\n\
You\'ve never seen two Titans fight before. The enemy Titan is thrown backward, smashing into the building.\n\n\
A Titan is attacking another Titan...as if to protect a human.\n\n\
The Titan looks at you. It looks like a raging monster, but its eyes have the glimmer of intelligence.\n\n\
You hear Mikasa\'s voice:\n\n\
\"Eren.\"\n\n\
You know instinctively that she\'s right. It makes no sense, but...that Titan is Eren.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 184

    def P261(self, *option):
        if option == ():
            response = 'Remembering your training, you work the gun as hard as you can.\n\n\
Normally it takes several people to load, aim, and fire, but you do it all by yourself - you, a trainee.\n\n\
With your fumbling hands, you do it.\n\n\
When you finish loading, the Titan is right in front of your eyes. You fire.\n\n\
There\'s an explosion - a direct hit on the Titan!\n\n\
Yes!\n\n\
But... The creature only stumbles a bit. Part of its chest was blown away, but it soon begins to heal in a cloud of white steam. \
Deafened by the explosion, you can\'t hear what\'s going on around you.\n\n\
A massive hand grabs you in what, to your ears, is silence. Silently it brings you to its gaping mouth.\n\n\
And then, not only sound, but light vanishes. You have been eaten by a Titan.\n\n\
**You have died. To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P262(self, *option):
        if option == ():
            response = 'You draw your blade and plunge it into the nape of the Titan\'s neck.\n\n\
You were watching when Eren became a Titan. If you strike here- careful not to injure the head of the real Eren inside...\n\n\
You succeed. As if in response to your action, the Titan gives a great thrash.\n\n\
You cling to the hilt of the blade to avoid being thrown off, and call to Eren: memories of training, his passion for killing \
Titans... Maybe even the dream of the world outside that you heard about from Armin.\n\n\
**Your Affinity with Eren has increased by 3!**\n\n\
Type :one: to continue.'
            self.state.affinities.eren += 3
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 251

    def P263(self, *option):
        if option == ():
            response = 'You wake up in a middle school classroom.\n\n\
You must have fallen asleep. You look around the classroom: Eren and Jean are fighting again. Armin is wrapped in a blanket, and \
the hearts are practically streaming off Franz and Hannah.\n\n\
\"What do you mean, peaceful?! Those Titan kids stole my lunch again!\" Eren shouts. It\'s true this is a pretty awful middle \
school - but you enjoy every day here. Everyone is happy and full of life. Don\'t forget, you\'ve got Wall Beautification Club \
after class...\n\n\
**👑 Congratulations! Through your intense dedication to the noble art of memeing, you\'ve earned the \
\"Attack on Titan: Junior High\" Secret Ending! 👑\n\n\
https://www.youtube.com/watch?v=yKq3N3Z8ueQ**'
            self.response2[0] = '\n\n\
**🏆 This is a truly remarkable achievement, give yourself a pat on the back! 🏆**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response


    def P264(self, *option):
        if option == ():
            response = 'You act on the plan to stay holed up in the building. More and more Titans show up nearby; you hear the \
disturbing sounds of them beating on the walls and ceiling, chewing on them. More than a few of your friends are grabbed by hands \
that come in wherever there\'s space.\n\n\
You wonder how much time has passed... Eventually, the light outside begins to fade.\n\n\
You can\'t see very well, and the Titans\' pounding prevents you from talking. You no longer even know if anyone else is left alive.\n\n\
But it will be night soon. That might be your salvation... So you struggle to go on.\n\n\
And then, suddenly, with one great noise, the building shakes violently.\n\n\
There\'s a sound like an explosion, and the headquarters, which had seemed so sturdy, begins to collapse.\n\n\
You clamber out of the building in a panic.\n\n\
When you look up, you see a massive Titan looming in the dusk.\n\n\
Fifteen meters. It looks immensely powerful, as though its entire body were covered in armor.\n\n\
Standing amidst the rubble and the bodies of your companions, all you can do is stare at it.\n\n\
The last thing you see is the Armored Titan rushing at the inner wall of Trost District to break it down.\n\n\
**You have obtained \"The Fall of Wall Rose\" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P265(self, *option):
        if option == ():
            response = 'You and the others land on the roof of a nearby building.\n\n\
\"Is everyone okay?!\"\n\n\
\"T-Thomas!\"\n\n\
You turn and see that one of your companions, Thomas, has been caught by a Titan. The lower half of his body is already in its \
mouth. Pale, he looks around wildly for help.\n\n\
\"Thomas!\" Eren shouts.\n\n\
You...\n\n\
:one: Rush to cut down the Titan and save Thomas\n\n\
:two: Recall your training and use vertical maneuvering to challenge the Titan\n\n\
:three: Tell Eren to calm down'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 138
        elif option[0] == 2:
            self.cur_page[0] = 220
        elif option[0] == 3:
            self.cur_page[0] = 153
        elif option[0] == 's':
            self.cur_page[0] = 88

    def P266(self, *option):
        if option == ():
            response = 'You wonder how Eren and the others are doing outside...\n\n\
As you wait, you hear rumbles and explosions.\n\n\
Then your companion who has been heading things up outside returns.\n\n\
\"Eren... He ran out of gas and wound up in the streets...\"\n\n\
So that\'s it. Brave Eren perished for the sake of his comrades...\n\n\
But then your companion\'s story takes an unexpected turn.\n\n\
\"And then... Damn. I still can\'t believe it. All I can do is tell you what I saw, but one minute Eren was there, and the next \
a Titan appeared. And for some reason, it started attacking the other Titans. It didn\'t even look at us humans. There\'s a huge \
Titan brawl going on outside right now...\"\n\n\
For an instant, a thought crosses your mind: Could it be that Eren turned into a Titan and is protecting you? But you brush it away. \
It\'s not possible. Eren is dead.\n\n\
Type :one: to continue.'
            self.state.statuses.eren == 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 137

    def P267(self, *option):
        if option == ():
            response = 'From that point on, Jean continues to run when a Titan approaches, fighting only when necessary.\n\n\
Even when he fights, it is only so he can get away; he doesn\'t kill any of the Titans.\n\n\
\"This when our friends and the more experienced soldiers are fighting...\" some of your companions say in disgust, but Jean shouts \
back:\n\n\
\"Shut up! Just distracting the Titans helps plenty. You\'re not gonna do any good if you\'re dead!\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 73

    def P268(self, *option):
        if option == ():
            response = 'But...\n\n\
Instead of picking up the boulder, the Titan Eren begins to attack the nearby soldiers!\n\n\
They take evasive maneuvers and come away unhurt, but Eren\'s Titan fist smashes into a building.\n\n\
Eren isn\'t unscathed by the attack; his fist begins to gush bodily fluid. It was a bizarre act.\n\n\
He seems to have forgotten about the boulder. He launches attack after attack at Mikasa as she calls to him desperately.\n\n\
He shows no sign of intelligence; he\'s attacking humans on instinct. As if he were a normal Titan...\n\n\
Perhaps he was never anything more than that.\n\n\
Eren continues to flail despite his ruined fist. He takes a swing at Mikasa, who has landed near his head to try to bring him back \
to himself, and he ends up destroying his own face.\n\n\
With a great noise, and taking half a building with him, he falls - and stops moving.\n\n\
\"Grr... The plan failed!\"\n\n\
Rico, a soldier of the Garrison and leader of the bodyguard detachment, makes a sour face and fires a signal flare.\n\n\
The flare means something desperate has happened, or the plan is being aborted. It trails red smoke into the air.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 231

    def P269(self, *option):
        if option == ():
            response = 'Rico\'s eyes are hard as she thrusts a question at Ian.\n\n\
\"Hundreds of people have already died for your precious human weapon... and you\'re saying we have to bring him back so we can go \
through it all over again?\"\n\n\
\"That\'s right... no matter how many die, we should keep trying! There\'s no replacement for him. Yes, the chances are abysmal. \
But this gamble is our only hope!\" Then Ian turns the question on Rico. \"Tell me... If we abandon him, how do you propose humanity \
beat the Titans?\"\n\n\
Rico has no answer.\n\n\
Ian is right. Right now humanity has nothing else - not even some other \"precious\" weapon. If you flee now, if you survive...you \
will only postpone your ultimate destruction.\n\n\
You, and everyone there, understand that.\n\n\
Ian doesn\'t seem pleased to have convinced you, though.\n\n\
\"This is all we humans can do. Die like insects for something with no promises and no certainties. That\'s our fight. Our final \
struggle.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 232

    def P270(self, *option):
        if option == ():
            response = 'You see Krista pleading with the Garrison soldiers.\n\n\
\"I\'m begging you. My friends are still out there. Please send someone to help them - no, send me!\"\n\n\
But the soldiers look at once troubled and unimpressed.\n\n\
You...\n\n\
:one: Join Krista in pleading with them\n\n\
:two: Taunt them. \"You afraid of a little rescue mission?\"\n\n\
:three: Think it\'s futile to beg'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 92
        elif option[0] == 2:
            self.cur_page[0] = 192
        elif option[0] == 3:
            self.cur_page[0] = 224

    def P271(self, *option):
        if option == ():
            response = 'You fly into the crowd of Titans.\n\n\
There are so many of them. Massive hands grab at you left and right. You feel your enemies taking bites out of you.\n\n\
You look up to see Jean and your other comrades growing smaller in the distance.\n\n\
Jean glances back, just for a second. He\'s far away now, but you think you see an apolegetic look in his eyes.\n\n\
Did your sacrifice save your friends...?\n\n\
**You have died. Type `~reset` to start over.**'
            self.choices[0] = []
            return response

    def P272(self, *option):
        if option == ():
            response = 'You, too, halt your vertical maneuvering and land on the ground.\n\n\
The members of the select squad smile weakly at you.\n\n\
Every face is marked with terror. With drawn looks and uncertain steps, they go about getting the Titans\' attention.\n\n\
No one dies bravely. They all go screaming, weeping, in agony; their deaths are brutal and ugly.\n\n\
But they are, undoubtedly, heroes.\n\n\
You join the parade of death.\n\n\
Beyond the awful cries of the perishing, Eren walks with the boulder on his shoulders.\n\n\
You look up at him. To protect that hope, you, too, will walk directly toward death.\n\n\
Finally, your body is grabbed by a huge hand.\n\n\
And just like the others, your fear breaks you; you scream at the top of your lungs...\n\n\
Your actions has saved one of the leaders of the elite squad. Who did you save?\n\n\
:one: Ian Dietrich\n\n\
:two: Mitabi Jarnach'
            self.choices[0] = [1,2]
            if self.state.flags.levihelp == 'Yes':
                response = response + '\n\n\
:three: Save both with Levi\'s help'
                self.choices[0].append(3)
            return response
        elif option[0] == 1:
            self.state.statuses.mitabi = 'Dead'
            self.cur_page[0] = 304
        elif option[0] == 2:
            self.state.statuses.ian = 'Dead'
            self.cur_page[0] = 304
        elif option[0] == 3:
            self.cur_page[0] = 277

    def P273(self, *option):
        if option == ():
            response = 'You trust Eren. You stand between him and the guard captain, shielding him.\n\n\
Next to you, MIkasa has drawn her blade, ready to fight if she has to.\n\n\
You think fast. You have to avoid a fight. Humans can\'t start killing each other.\n\n\
You wrack your brain for ideas.\n\n\
A voice pleads with the guard captain.\n\n\
It says Eren himself is a way to fight the Titans, that he can give hope to humanity. That with him on our side, it might even \
be possible to retake Trost District.\n\n\
Is that Armin\'s voice? Or are those words you yourself desperately shout?\n\n\
Either way, the soldiers around you don\'t seem to want to listen.\n\n\
The guard captain raises his hand mercilessly.\n\n\
He\'s about to give the order to fire the cannons at you...\n\n\
**Your Affinity with Eren and Mikasa has increased by 1!**\n\n\
Type :one: to continue.'
            self.state.affinities.eren += 1
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 188

    def P274(self, *option):
        if option == ():
            response = 'After that, Krista stops doing such rash things.\n\n\
You link up with Jean, Connie, and the others. It looks like they managed to survive, too.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 165

    def P275(self, *option):
        if option == ():
            response = 'Armin, wearing a grave expression, starts talking to everyone there.\n\n\
\"I\'ve got a plan. It\'s pretty dangerous, but if it works it could save us all. Will you hear me out?\"\n\n\
You...\n\n\
:one: Support Armin and listen to him\n\n\
:two: Don\'t listen'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 167
        elif option[0] == 2:
            self.cur_page[0] = 139

    def P276(self, *option):
        if option == ():
            response = 'You keep on fighting the Titans with your vertical maneuvering.\n\n\
There are moments when you catch sight of Armin. He is at the nape of the Titan Eren\'s neck and has buried a blade in it. The \
Titan\'s body gives a violent thrash in response. He\'s not trying to kill it. He has missed the vital point by inches. He just \
wants to wake Eren up. You catch glimpses of the scene. Armin shouting something at the top of his lungs. The word \"Eren!\" \
comes to you faintly in the breeze.\n\n\
Your attention is taken up by the Titan in front of you.\n\n\
You know Armin is fighting his own battle.\n\n\
Finally...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 251

    def P277(self, *option):
        if option == ():
            response = 'At that moment, human silhouettes fly through the air.\n\n\
It\'s Captain Levi and the elite troops of the Survey Corps.\n\n\
They slice apart Titan hands that have grabbed soldiers, Titan mouths that seek to eat them, rescuing the troops on the ground.\n\n\
You\'re near the ruined gate. There are no buildings here. Levi and his troops use the Titans themselves as anchor points from which \
to maneuver.\n\n\
This must be what they\'ve learned from all that time fighting Titans outside the wall, where buildings are few. They make you \
think of birds, flying freely through the vast space.\n\n\
The soldiers around you, who had given up all hope, let out tearful shouts of joy.\n\n\
With support from the air, the chances they might be rescued improve tremendously. At the very least, no one will die in vain.\n\n\
You go back to your duty.\n\n\
Your duty... To draw off the enemy Titans at the risk of your own life.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 312

    def P278(self, *option):
        if option == ():
            response = 'With so many of you pushing the cargo wagon together, it begins to move bit by bit. Or...it should have.\n\n\
You wonder how much time has passed.\n\n\
You fall into a reverie as you push, but are shaken from it by several large tremors.\n\n\
You look toward the town, and see a horde of Titans coming your way. There are many more monsters than there are soldiers to protect \
you.\n\n\
The warning bell rings out. Some of the soldiers on guard are shouting.\n\n\
\"Close the gate immediately!\"\n\n\
\"There\'s nothing we can do! We have to stop the evacuation!\"\n\n\
The crowd panics. They scramble over the cart, trying to make it through the gate as it closes, but the road becomes clogged with \
shoving people. \"Never mind!\" the merchant shouts, \"Forget the cargo!\" But he is sucked into the throng of people and you lose \
sight of him.\n\n\
And then the Titans come.\n\n\
They pick people out of the crowd around the gate, popping them into their mouths one after another.\n\n\
Shouts and cries rise up, mingling with the crunch of humans being chewed and eaten.\n\n\
What can people do now? Maybe Wall Rose will be destroyed... But you won\'t see it. A Titan\'s hand picks you up and drops you into \
its gaping mouth.\n\n\
**You have died. To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P279(self, *option):
        if option == ():
            response = 'The commander, Ian, shouts at you:\n\n\
\"You trainees, work with Eren. That\'s an order! Rico, your squad is to support them with vertical maneuvering!\"\n\n\
Then he turns to his own subordinates:\n\n\
\"Protect Eren with your lives!\"\n\n\
You see Mitabi\'s squad already on the ground. They\'ve stopped using vertical maneuvering and are simply walking along.\n\n\
They\'re distracting the Titans with their own bodies. When a Titan is hunting a human, it pays no attention to anything else.\n\n\
That will give Eren a chance to move to the objective. Such seems to be their plan.\n\n\
Ian and his squad follow them.\n\n\
You swallow heavily at the incredible scene.\n\n\
But this is all you have left. If you had a horse, things might be different, but now all that can be given for the success of the \
plan is human lives.\n\n\
You...\n\n\
:one: Support the troops with vertical maneuvering\n\n\
:two: Go to the ground yourself, and work with the picked squad'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 254
        elif option[0] == 2:
            self.cur_page[0] = 272
        elif option[0] == 's':
            self.cur_page[0] = 285

    def P280(self, *option):
        if option == ():
            response = 'The top of the wall, above the gate, looks almost as if it has been ground away by something. You see no sign of \
the fixed guns. The rail is gone, too, so there\'s no way to move new guns into place.\n\n\
Beyond this immediate area... You hear the fixed cannons on both the inner and outer walls firing intermittently.\n\n\
You make for where a few surviving guns remain atop the wall.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 72

    def P281(self, *option):
        if option == ():
            response = '\"This isn\'t the time to be letting our guard down,\" Jean says, for some reason in an even worse mood than \
usual. Then he explains the situation.\n\n\
He tells you how the headquarters in the city was swarmed by Titans, and how you can\'t resupply yourselves with gas and so can\'t \
cross over the wall and get out of here. You\'ll be left in a city full of wandering Titans, and when your gas runs out you won\'t \
even be able to maneuver anymore - only die.\n\n\
\"Things could be worse, though.\" Armin says. \"First, we survivors need to split our remaining gas between us, then we can think \
of a plan.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 173

    def P282(self, *option):
        if option == ():
            response = 'The smoking Titan corpse crumbles away.\n\n\
At the nape of the neck, you think you can make out a human form.\n\n\
...It\'s Eren.\n\n\
You thought Eren was dead. What is he doing in a Titan\'s neck?\n\n\
He has lost his jacket and his vertical maneuvering equipment; only the undershirt of his uniform remains. He\'s unconscious, \
but he\'s alive. What\'s more, his legs and arms are in perfect condition. He doesn\'t seem to be injured anywhere.\n\n\
\"Eren!\" Mikasa shouts, running toward him. She catches him in her arms.\n\n\
Normally calm and reserved, Mikasa sobs like a child, so loudly you can hear her from where you stand.\n\n\
\"What the hell\'s going on?\"\n\n\
Your companions seem every bit as confounded as you are.\n\n\
For now, you need to take the sleeping Eren and get out of here...\n\n\
Type :one: to continue.'
            self.state.statuses.eren = 'Alive'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 233

    def P283(self, *option):
        if option == ():
            response = 'Jean does nothing to help your companions, but only points ahead.\n\n\
\"Now\'s our chance. This way, follow me!\"\n\n\
In the blink of an eye, he made the decision to leave behind those who could not be saved, in order to save those who remained.\n\n\
He isn\'t simply running from fear. He refused to let their ultimate sacrifice go to waste.\n\n\
He seizes on a gap between Titans, and slips through it in the nick of time.\n\n\
A Titan\'s hand grabs Jean. He slips out of his boot and keeps pushing.\n\n\
The two of you think only of flying, using the last of your gas.\n\n\
The headquarters building is just ahead of you.\n\n\
You kick in a window on the second or third floor and dive in.\n\n\
As you land, you realize you\'re out of gas. You couldn\'t have cut it any closer.\n\n\
Jean\'s spontaneous decision...seems to have been the right one.\n\n\
But when you look at him, you see he doesn\'t have the calm, cold expression of a commander. In fact, exactly the opposite.\n\n\
\"How many of us made it...? Using the deaths of our comrades... How many died...on my signal?\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 139

    def P284(self, *option):
        if option == ():
            response = 'It\'s a terrible outcome... You don\'t even find the bodies of some of your friends.\n\n\
Somebody whispers:\n\n\
\"To think. this was the best we could hope for. If more Titans had come in from outside, casualties would\'ve been even worse.\"\n\n\
Quailing, you look out the window.\n\n\
A bizarre sight meets your eyes: Titans are fighting each other.\n\n\
A mysterious, 15-meter Titan with black hair gives a great bellow, and slams another Titan with his fist, biting with its teeth. \
The other Titans must see it as an enemy, because they are swarming it.\n\n\
\"We don\'t know where he came from, but the other Titans seem drawn to him. It\'s thanks to him we\'re alive.\"\n\n\
Now you know... Without that mysterious Titan, your losses would likely have been worse. Or perhaps the entire plan would have \
failed, and you would all have been annihilated.\n\n\
Could that Titan be an Abnormal? Even if it is, you\'ve never heard of a Titan like this, let alone one that arrives with such \
impeccable timing...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 226

    def P285(self, *option):
        if option == ():
            response = 'Then, you spot a flying column on horseback.\n\n\
The information you gave the commander seems to have helped; all the horses left in the city have been mustered.\n\n\
There are only a few of them, but they\'ve arrived at the best possible moment to ensure this precious strategy does not go to waste.\n\n\
They\'re specially trained, top-quality horses intended for the Survey Corps. They won\'t panic even in the face of the Titans. \
Bold animals a soldier can trust as much as his own feet.\n\n\
The mounted unit moves to support the brave soldiers on the ground, using their excellent horsemanship to lead the Titans on a chase.\n\n\
\"Change of plans!\" your commander, Ian, yells. \"Link up with the mounted troops. If you\'ve got gas left, use vertical maneuvering!\"\n\n\
Amidst the newly-energized soldiers, Eren lifts the great boulder onto his shoulders and begins to walk.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 302

    def P286(self, *option):
        if option == ():
            response = 'You pull Krista back and bring her to a safe location.\n\n\
\"Why did you stop me? O-Our friends...\"\n\n\
She struggles with you; she is weeping.\n\n\
Before you can say anything, the ever-present freckled girl breaks in.\n\n\
\"If we\'d left you alone, Krista, you would\'ve died. And if you hadn\'t, our friend right here would have.\"\n\n\
At her words, Krista falls silent.\n\n\
But you don\'t think what she says is quite true. Surely she herself would have saved Krista.\n\n\
That\'s what you think, anyway, but the freckled girl only snorts and adds:\n\n\
\"Get it? Next time, think before you act.\"\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 274

    def P287(self, *option):
        if option == ():
            response = '\"Is that so? I had my hopes, but I guess it was too good to be true.\"\n\n\
The commander gives a long sigh.\n\n\
And with that, the battle to defend Wall Rose comes to an end.\n\n\
With no way to reclaim the Titan-infested Trost District, the only thing to do now is stiffen the defenses on the far side of the \
inner gate.\n\n\
Commander Pixis seems personally sympathetic to you and your friends, but he cannot overlook something as dangerous as a boy who \
can turn into a Titan. Eren is sent under guard to await a court-martial.\n\n\
And no one knows how long the imperiled Wall Rose will hold...\n\n\
**You have obtained the \"Failure to Reclaim Trost District\" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P288(self, *option):
        if option == ():
            response = 'This is how the Battle of Trost ends.\n\n\
A victory for humanity - its first victory since the appearance of the Titans.\n\n\
You not only survived the brutal fight, but were able to contribute to that victory.\n\n\n\
But...the price of that triumph is staggeringly high.\n\n\
A huge number of soldiers died - including many of your fellow trainees from the 104th Training Corps.\n\n\
And those whose names could be added to the rolls of the dead were the lucky ones. Many more were eaten by Titans, or mangled \
beyond recognition. And that is to say nothing of all those who simply went missing in action.\n\n\
Two days pass.\n\n\
The Titans still wandering the streets of Trost District are finally dispatched by the ceaseless firing of the walltop gun \
emplacements and the tireless work of the Survey Corps\' elite troops.\n\n\
Along with the other surviving soldiers, you help the Sanitary Disposal Squad clean up the former battlefield and search for the \
missing. That is to say, you are tasked with discovering bodies that haven\'t yet been found and disposing of them. Decomposition \
has already begun, and you have to prevent a secondary disaster like an outbreak of disease.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 2881

    def P2881(self, *option):
        if option == ():
            response = 'You and the others gather countless bodies from throughout the city - bodies crushed, bodies maimed.\n\n\
You find a disturbing mass in which several people\'s bodies seem to have melted together.\n\n\
They are humans who were swallowed by a Titan.\n\n\
Titan biology is not yet well understood, but they do not seem to have other digestive or excretory functions. Humans a Titan \
eats are not even absorbed into its blood or flesh, but are simply spat back up this way, like vomit. They gorge themselves \
on humans not for sustenance, but only to kill. The dead are left a mound of flesh, without even their dignity.\n\n\
Even your friends, who survived that hellish battlefield, lose their composure at this. Some go blank in the eyes and begin \
muttering to themselves. Many cannot sleep in the barracks; many others wake screaming in the night.\n\n\
As you work, you spot Annie. Annie Leonhart, typically so calm and almost emotionless, stands in front of a friend\'s still body, \
murmuring.\n\n\
\"I\'m sorry... I\'m sorry...\"\n\n\
In the midst of all this, you run into Marco Bott.\n\n\
Marco is lucky.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 289
        elif option[0] == 's':
            self.cur_page[0] = 295

    def P289(self, *option):
        if option == ():
            response = 'Marco Bott is lucky: half his face is left, so you know the body is his.\n\n\
That means he can be officially listed among the deceased, rather than simply among the missing.\n\n\
The death of the cheerful, well-liked Marco is a shock to your entire unit.\n\n\
That night...\n\n\
Corpses, countless corpses, are piled up and cremated. Under the circumstances, it\'s impossible to hold a separate funeral for \
everyone who died. The ashes will all be buried together...\n\n\
\"Why him?\" Jean mutters, looking into the flames. Something about him has changed since the battle. Then, as if he\'s finally \
made up his mind, he says to all of you:\n\n\
\"Hey...you guys... Have you decided which branch of the military you\'re gonna apply to?\"\n\n\
His voice strained, he continues:\n\n\
\"I\'ve decided. I...I\'m...I\'m gonna join the Survey Corps.\"\n\n\
You should also decide which path you will take. Type :one:.\n\n\
If you decide to talk with Annie first, type :two:.'
            self.state.statuses.marco = 'Dead'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 306
        elif option[0] == 2:
            self.cur_page[0] = 214

    def P290(self, *option):
        if option == ():
            response = 'You flee the unit.\n\n\
Several others run, too, including your fellow trainee, Daz. True to his word, Commander Pixis lets you go.\n\n\
You go back to your home, to spend a brief, peaceful time. Daz ends up coming with you. He says shamefacedly that he can\'t go \
back to his hometown.\n\n\
You never hear what happened at the battle in Trost District. It\'s possible that humanity was victorious, but because of what \
happened with Eren, all information about the battle was deemed confidential...\n\n\n\
One clear day.\n\n\
With no warning whatsoever, you get word that Wall Rose has fallen.\n\n\
There\'s no time to run. The rumbling footsteps of Titans are too near...\n\n\
**You have obtained the \"A Moment\'s Peace\" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P291(self, *option):
        if option == ():
            response = 'You take the merchant\'s side and try to reason with Mikasa.\n\n\
You tell her you\'ll do something about it. Above all, a soldier, sworn to protect the people, must not go around killing civilians.\n\n\
Mikasa is silent for a moment... Then, with no change in her expression, she glares at you and says, \"I\'m going back to my station.\" \
She turns away from you and leave.\n\n\
The merchant pounds your back in elation.\n\n\
\"Well done! My gratitude will mean more for you than you could earn in a lifetime as a mere soldier!\"\n\n\
You start pushing the cart, and order the evacuees around you to help.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 278

    def P292(self, *option):
        if option == ():
            response = 'Just a moment more, and the plan will succeed.\n\n\
You and the others do everything in your power to stop the Titans in the city, to draw them off, slow them down, and otherwise \
keep every monster you can from reaching Eren.\n\n\
You keep on fighting with all your strength. So do your friends. Will you all make it through this battle in one piece?\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 243

    def P293(self, *option):
        if option == ():
            response = 'You fight alongside Mikasa and the elite troops against the encroaching Titans.\n\n\
You bring one down... But there are so many. And more seem to be coming every moment.\n\n\
You can keep fighting, but your defeat will be only a matter of time.\n\n\
Type :one: to go back and make a different choice.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 232

    def P294(self, *option):
        if option == ():
            response = 'A voice like a great howl sounds across the city from far off.\n\n\
\"Hey! Look at that,\" Jean calls to you from a high rooftop.\n\n\
Far away, you can see a massive human shape moving. It is obscured by buildings, but you can make out its head. No... That\'s not \
its head. It\'s a massive round object. A boulder, moving slowly through the streets.\n\n\
It\'s Eren.\n\n\
The Titan has picked up the huge rock and is moving toward the hole in the outer gate.\n\n\
You see, too, enemy Titans moving in his direction from all around the city, as if drawn to him.\n\n\
\"All right. Protect Eren!\" Jean shouts, and your friends take up the cry.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 292

    def P295(self, *option):
        if option == ():
            response = 'Marco Bott is lucky: he survived the awful battle.\n\n\
\"But...so many of our friends didn\'t. It wouldn\'t have been surprising if I had died, too...\"\n\n\
Marco speaks in a strained voice as he helps with the collection of the bodies.\n\n\
That night...\n\n\
Corpses, countless corpses, are piled up and cremated. Under the circumstances, it\'s impossible to hold a separate funeral for \
everyone who died. Marco stares vacantly into the flames.\n\n\
Jean comes up to him.\n\n\
\"Hey, Marco. Have you decided which branch of the military you\'re gonna apply to?\"\n\n\
When Marco answers, his eyes are strikingly clear.\n\n\
\"I\'m still thinking about it. I always had my heart set on the Military Police Brigade...but now I\'m not sure if it\'s right to \
join them.\"\n\n\
\"Haha. Well, I\'ve decided.\"\n\n\
Jean saw his share in this battle. The braggadocio and bravado he always used to put on are gone. So thoroughly gone, in fact, it\'s \
almost disconcerting. In a voice just the same - and completely different - from the one you know, he says:\n\n\
\"I\'ve decided. I\'m joining the Military Police.\"'
            if self.state.affinities.jean >= 2:
                response = response + '\n\n\
**You have sufficient Affinity with Jean!**\n\n\
If you wish to also apply to the Military Police Brigade, type :one:.\n\n\
Otherwise, type :two:.'
                self.choices[0] = [1,2]
            else:
                self.choices[0] = [1]
                response = response + '\n\n\
**You do not have enough Affinity with Jean to choose this option (2 needed).**\n\n\
Type :one: to continue.'
            return response
        elif option[0] == 1:
            if self.state.affinities.jean >= 2:
                self.cur_page[0] = 313
            else:
                self.cur_page[0] = 306
        elif option[0] == 2:
            self.cur_page[0] = 306

    def P296(self, *option):
        if option == ():
            response = 'After that...\n\n\
You don\'t know what happened to Eren and his friends.\n\n\
The Corps was in no condition to chase after him, once the inner gate of Wall Rose was smashed down.\n\n\
Humanity was forced to retreat to the last of its territory, behind the final barrier, Wall Sina.\n\n\
Thus...\n\n\
You now reside in Ehrmich District, at the southernmost point of Wall Sina.\n\n\
You and the rest of the surviving soldiers prepare for a final, hopeless defense.\n\n\
A thought flits through your mind:\n\n\
What if you had trusted Eren?\n\n\
**You have obtained the \"Eren Flees\" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P297(self, *option):
        if option == ():
            response = 'You and the surviving members of Squad 34 join the middle guard.\n\n\
The Titans are relentless, but you face them down. Even the scant experience you\'ve had in the battle so far is proving valuable.\n\n\
Experienced soldiers and other members of the squad are falling in droves. And amidst it all, you\'re fighting for your life against \
a massive Titan. You wonder how much time has passed...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 89

    def P298(self, *option):
        if option == ():
            response = 'You\'ve decided it\'s too late to help Armin. If you can at least save Eren...\n\n\
You jump to the roof where Eren lay and take him in your arms, then begin vertical maneuvering.\n\n\
You can hear Armin\'s screams behind you. In your arms, Eren is shouting.\n\n\
\"D-Damn you! We can\'t just leave Armin!\"\n\n\
You ignore him, trying to put space between the two of you and the horde of Titans.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 86

    def P300(self, *option):
        if option == ():
            response = 'You survive the battle and decide to join the Survey Corps.\n\n\
Now you are a member of the Survey Corps\' special unit commanded by Captain Levi - popularly known as Squad Levi.\n\n\
\"Hey, don\'t let it go to your head, new kid.\" One of the senior soldiers, Oluo, glares at you intimidatingly. \"I figure Captain \
Levi only picked you because your battle experience in Trost makes you unusual. I seriously doubt he saw any actual skill in you. \
Don\'t slow us down, now. Heh heh!\"\n\n\
So saying, he gives you an unsettling smile. Maybe he means it to look cool.\n\n\
\"Don\'t scare the rookies, Oluo,\" another of the established troops, Petra, breaks in with annoyance. She holds out her hand to \
you and smiles.\n\n\
\"You survived that awful battle, and that means you\'ve got real experience. I\'m sure the captain saw that, and that\'s why he \
picked you. Glad to have you with us.\"\n\n\
\"Right! Exactly! Your precious experience!\" Hange Zoë suddenly jumps into the conversation in a booming voice. \"Tell me \
everything about the new Titan you saw in Trost! Oooh! I wish I had been there! Now, you! You and I can talk the night through \
about Titans!\"\n\n\
Even for a member of the Survey Corps, this bespectacled individual has a great - perhaps *too* great - interest in Titan research. \
The researcher is a strange one even in a unit full of eccentrics. You\'ve already lost count of how many times Hange has made you \
talk about your experiences in Trost District.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 3001

    def P3001(self, *option):
        if option == ():
            response = '\"Hey, Hange. Don\'t waste my subordinates\' time.\"\n\n\
It\'s Captain Levi. He says to you:\n\n\
\"There\'s something I want you to do.\"\n\n\
You salute him anxiously. You would undergo any training and take on any task, no matter how difficult, if it meant remaining \
in the unit of the strongest man in the world.\n\n\
\"Good. I like that attitude.\" Levi hands you a broom and a rag. \"Clean the headquarters again. I won\'t let you slack off \
just because you\'re part of my unit now.\"\n\n\
So here you are, part of the special unit within a special unit, doing your duty to your utmost under your leader - your clean-freak \
leader.\n\n\
**🎉 Congratulations! You\'ve obtained the \"Captain Levi\'s Recruit\" Ending. 🎉**\n\n\
https://www.youtube.com/watch?v=chfmu7Jeyz0'   
            self.response2[0] = '\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P301(self, *option):
        if option == ():
            response = 'It has been three days since the end of the battle in Trost District.\n\n\
Mikasa is staying in lodgings near the military tribunal. Eren will be tried shortly, and those who are close to him are under \
house arrest and being interrogated. You suspect, though, that Mikasa would have been there whether or not she was legally \
confined. You know she wants to be as close to Eren as she can.\n\n\
\"Eren... He still hasn\'t opened his eyes.\"\n\n\
He\'s been asleep for two days straight, and apparently still hasn\'t woken on this, the third day.\n\n\
\"What will we do if he... If he stays like this...?\"\n\n\
Mikasa has the anxious face of a young child. She is stroking the old scarf she always wears like a prayer. You always knew her as \
a woman of steel, who hardly knew how to hesitate. You\'ve never seen her this way before.\n\n\
You tell her it\'ll be all right. Who could leave a girl as beautiful as her waiting? And in your heart of hearts, you do believe it.\n\n\
Mikasa gives you the faintest of smiles. You\'ve never seen an expression quite like that on her face before, either.\n\n\
You wonder if you might get to know her better now. Perhaps one day she\'ll tell you about Eren, and about that old scarf wrapped \
around her neck.\n\n\
**🎉 Congratulations! You\'ve obtained the \"Mikasa\'s True Face\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P302(self, *option):
        if option == ():
            response = 'Eren walks, a giant lumbering amongst the deaths of countless soldiers.\n\n\
He\'s nearly to the gate.\n\n\
\"GOOO!\" you hear someone shout - or is that your own voice?\n\n\
Eren raises the great stone overhead, then flings it at the hole in the wall.\n\n\
The crash of it shakes the whole city.\n\n\
It is the sound of victory.\n\n\
A signal flare arcs into the air. Yellow smoke: The plan has succeeded.\n\n\
You, all of you, have triumphed.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 303

    def P303(self, *option):
        if option == ():
            response = 'What happens next, you remember only as in a dream.\n\n\
After the hole was blocked with the boulder, the Titan Eren, as if knowing his duty was finished, slumped to the ground and ceased to \
move. His body, with its extremely high temperature, steamed mightily.\n\n\
As the Titans remaining in the city converged on him, you tried to save Eren by cutting his human body out of that steaming \
Titan form...\n\n\
You were saved by soldiers who arrived on a rescue mission in the nick of time.\n\n\
It was the Survey Corps, which had returned from its exploration of the outside world and climbed over the wall to get back into \
the city.\n\n\
You were at their backs as they fought to protect you, so you had a clear view of the crest emblazoned on the Survey Corps\' \
capes. The crest is called the \"Wings of Freedom,\" and you will never forget it.\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 288

    def P304(self, *option):
        if option == ():
            response = 'This is how you fall, one more of this battle\'s innumerable nameless dead.\n\n\
\"The plan was a success,\" someone says. \"Today, humanity claimed its first victory against the Titans.\"\n\n\
\"Thank God...Everyone... Everyone\'s death meant something.\"\n\n\
Rico Brzenska is weeping. The elite soldier of the Garrison who once glared at you with those implacable eyes - now she cries like \
a little girl.\n\n\
And some of those tears are for you. You wonder how many.\n\n\
That\'s not so bad.\n\n\
**🎉 Congratulations! You\'ve obtained the \"Nameless Hero\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P305(self, *option):
        if option == ():
            response = '\"It\'s all thanks to you!\"\n\n\
The next time you see Eren Yeager, he sticks out his hand to you.\n\n\
The aftermath of the battle was almost as eventful as the battle itself. So many things have happened around you and to you. Eren \
must not be the hot-blooded, single-minded boy he was in training any longer.\n\n\
But he is still Eren.\n\n\
\"I wanted to thank you again, too,\" says Armin hesitantly, standing next to Eren. \"Because of what you did...I\'m alive now and \
can be with Eren. Thanks to you.\"\n\n\
Then he smiles. He and Eren have been friends for a long time. You think you and he could be friends for a long time to come.\n\n\
Another of Eren\'s old friends is there - Mikasa. But she only looks at you silently, with cold eyes. You\'d like to be friends \
with her, too, but...\n\n\
\"Now,\" Eren says to you forcefully, \"join us in stopping the Titans. And in exploring the world outside the wall!\"\n\n\
What he\'s saying seems impossible; an extravagant dream. But when he says it, you think it might just come true.\n\n\
You take Eren\'s outstretched hand with all the strength you can muster.\n\n\
**🎉 Congratulations! You\'ve obtained the \"Eren Yeager\'s Hand\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P306(self, *option):
        if option == ():
            response = 'You\'ve survived the battle. But what does your future hold?'
            if self.state.flags.flagD == 'Yes':
                response = response + '\n\n\
**Flag D has been checked.**\n\n\
Type :one: to continue.'
                self.choices[0] = [1]
            else:
                self.choices[0] = [1]
                #Affinities check
                if (self.state.affinities.eren + self.state.affinities.armin) >= 5:
                    response = response + '\n\n\
**You have sufficient combined Affinity with Eren and Armin!**'
                    self.choices[0].append(2)
                else:
                    response = response + '\n\n\
**You do not have enough combined Affinity with Eren and Armin (5 needed).**'

                if self.state.affinities.mikasa >= 4:
                    response = response + '\n\n\
**You have sufficient Affinity with Mikasa!**'
                    self.choices[0].append(3)
                else:
                    response = response + '\n\n\
**You do not have enough Affinity with Mikasa (4 needed).**'

                if self.state.affinities.jean >= 3:
                    response = response + '\n\n\
**You have sufficient Affinity with Jean!**'
                    self.choices[0].append(4)
                else:
                    response = response + '\n\n\
**You do not have enough Affinity with Jean (3 needed).**'

                if self.state.affinities.krista >= 3:
                    response = response + '\n\n\
**You have sufficient Affinity with Krista!**'
                    self.choices[0].append(5)
                else:
                    response = response + '\n\n\
**You do not have enough Affinity with Krista (3 needed).**'

                if self.state.affinities.sasha >= 3:
                    response = response + '\n\n\
**You have sufficient Affinity with Sasha!**'
                    self.state.flags.memelevel += 1
                    self.choices[0].append(6)
                else:
                    response = response + '\n\n\
**You do not have enough Affinity with Sasha (3 needed).**'

                if (self.state.statuses.franz == 'Alive') and (self.state.statuses.hannah == 'Alive'):
                    response = response + '\n\n\
**Both Franz and Hannah have survived until the end of the battle!**'
                    self.choices[0].append(7)

                if self.state.flags.levihelp == 'Yes':
                    response = response + '\n\n\
**You have fought with Levi!**'
                    self.choices[0].append(8)
                
                if self.state.flags.memelevel >= 3:
                    response = response + '\n\n\
*For some reason, you begin to feel a sense of dissonance...as if the world around you is not what it seems. You think back to \
the events that transpired up until this point. Even in this crazy world, there seemed to have been some things that were out of \
place, things that don\'t quite make sense.*\n\n\
*Are you beginning to lose your sanity from the traumatic battle? Or...is there something more to this world you live in-?*'
                    self.choices[0].append(9)
                
                #Options
                response = response + '\n\n\n\
Now, which path do you take?\n\n\
:one: Join the Garrison'
                if (self.state.affinities.eren + self.state.affinities.armin) >= 5:
                    response = response + '\n\n\
:two: Go with Eren and Armin'

                if self.state.affinities.mikasa >= 4:
                    response = response + '\n\n\
:three: Go with Mikasa'

                if self.state.affinities.jean >= 3:
                    response = response + '\n\n\
:four: Go with Jean'

                if self.state.affinities.krista >= 3:
                    response = response + '\n\n\
:five: Go with Krista'

                if self.state.affinities.sasha >= 3:
                    response = response + '\n\n\
:six: Go with Sasha'

                if (self.state.statuses.franz == 'Alive') and (self.state.statuses.hannah == 'Alive'):
                    response = response + '\n\n\
:seven: Go with Franz and Hannah'

                if self.state.flags.levihelp == 'Yes':
                    response = response + '\n\n\
:eight: Go with Levi'

                if self.state.flags.memelevel >= 3:
                    response = response + '\n\n\
:nine: Pinch yourself'
            return response

        elif option[0] == 1:
            if self.state.flags.flagD == 'Yes':
                self.cur_page[0] = 311
            else:
                self.cur_page[0] = 315
        elif option[0] == 2:
            if self.state.statuses.armin == 'Alive':
                self.cur_page[0] = 305
            elif self.state.statuses.armin == 'Dead':
                self.cur_page[0] = 215
        elif option[0] == 3:
            self.cur_page[0] = 301
        elif option[0] == 4:
            self.cur_page[0] = 206
        elif option[0] == 5:
            self.cur_page[0] = 310
        elif option[0] == 6:
            self.cur_page[0] = 309
        elif option[0] == 7:
            self.cur_page[0] = 200
        elif option[0] == 8:
            self.cur_page[0] = 300
        elif option[0] == 9:
            self.cur_page[0] = 263

    def P309(self, *option):
        if option == ():
            response = 'After the battle, you and Sasha are walking through the streets of Trost.\n\n\
The evacuated populace is crammed into temporary shelters on the far side of the inner wall. It will be some time before the town \
looks anything like it used to. There is a painful time of rebuilding to come.\n\n\
But everyone is alive. All those people - you soldiers put your lives on the line and saved them.\n\n\
\"Hey, you two! Thank you!\"\n\n\
A little girl calls out to you and Sasha. You swell with pride.\n\n\
But Sasha is looking at the girl with a greedy glint in her eyes. She seems to be looking at the bread ration in the girl\'s hand.\n\n\
\"Umm, you\'re welcome. To thank me, maybe you could give me some of that-\"\n\n\
You rush to drag Sasha away. Imagine, asking for food from a little evacuee girl.\n\n\
\"Aww. We\'re heroes, remember? We saved this town. And they\'re just gonna let us starve?\"\n\n\
You lead Sasha up onto the wall as she complains. You take out the field ration you\'ve been saving for just such an occasion.\n\n\
\"Oh, wow! Are you an angel? Or even a god?\"\n\n\
With that, she wolfs down your precious food. You\'d hoped she might leave half for you, but in moments most of it is gone...\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 3091

    def P3091(self, *option):
        if option == ():
            response = 'Sasha seems to feel a twinge of guilt when she\'s done eating, because she looks at you apologetically.\n\n\
\"Er. Um...\"\n\n\
She\'s wracking her brain for something to say. Eventually, this is what she comes up with:\n\n\
\"Oh, yeah! My home is a village in the woods, so I\'m a pretty good hunter. There\'s not as much to hunt now on account of the Titans, \
but if we ever get a chance, I\'ll share some of the meat from my catch with you.\"\n\n\
It seems to be her way of showing gratitude. But then, \"some\" also seems just like her. She plans to eat most of it herself...\n\n\
But this is the first time you\'ve heard her talk about this. You hope you can visit her village someday.\n\n\
You look out over Trost District.\n\n\
For a moment, it\'s peaceful.\n\n\
You\'re sure one day you\'ll cherish simple conversations like this.\n\n\
**🎉 Congratulations! You\'ve obtained the \"Sasha Blouse\'s Promise\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P310(self, *option):
        if option == ():
            response = 'You survive the battle, but death was so near the entire time. Things look different now.\n\n\
For example, the girl, Krista Lenz.\n\n\
She\'s petite and pretty, with a kind heart. Those things make her popular, and in training she was sort of the unit\'s mascot.\n\n\
Now...it\'s different. She\'s still lovely, and still acts the part of a compassionate girl, but you can\'t help thinking it\'s not \
the real her. In fact, you noticed how her impulse to kindness caused her to ignore danger on the battlefield.\n\n\
\"Hey, you. What are you staring at my Krista for?\"\n\n\
It\'s the freckled girl. She gives you a poke and a glare.\n\n\
During training, you wondered why such an ill-tempered girl would have been so close to someone like Krista... But maybe she caught \
on to who Krista was long before you did.\n\n\
If you could learn more about who the girl really is, maybe you could be better friends with her, too.\n\n\
\"Hmm.\" The freckled girl stares openly at you. Then, as if by intuition, she says, \"Whatever happens after this, trust her.\"\n\n\
This girl might just be better than she looks, too.\n\n\
Hrm. What was her name again?\n\n\
\"It\'s Ymir. You could at least remember a person\'s name,\" she says, but then shrugs.\n\n\
You would eventually find out who she truly was. But not for a very long time.\n\n\
**🎉 Congratulations! You\'ve obtained the \"The Girl Who Hid Her True Self\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P311(self, *option):
        if option == ():
            response = 'A short while later, you find yourself in a dilemma.\n\n\
So many things have happened since then. You\'ve joined the Survey Corps. You\'ve even become a member of the so-called \"Squad Levi,\" \
serving directly under the famous captain - along with several of your other friends and fellow survivors.\n\n\
If that were all, you would be quite proud of yourself.\n\n\
But instead, you are being hounded by the First Interior Squad of the Military Police Brigade. They are chasing you down with vertical \
maneuvering equipment designed for use against humans, bent on wiping all of you out. The papers are publishing nonsense claiming \
the Survey Corps rebelled against the king and killed innocent people.\n\n\
You were all caught in a trap. You are bereft of friends among both the military and the populace.\n\n\
How did this happen? With no way of resupplying and scant information, you are unable to mount an effective response. If only you \
had an ally - so much as a merchant who would cooperate with you... Where did you go wrong?\n\n\
But to your worries, Captain Levi says quietly:\n\n\
\"Even I don\'t know when I\'ve made the right choice and when the wrong in my life so far. The most any of us can do is try to act \
in a way that leaves us without regrets.\"\n\n\
You nod. The First Interior Squad forces encircling you begin to move. You prepare to fight this hopeless battle with your comrades \
at your side...\n\n\
**You have obtained \"The Death of a Merchant\" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P312(self, *option):
        if option == ():
            response = 'You lie on the ground, covered in blood. You can\'t feel your legs - they were bitten off by a Titan.\n\n\
You\'re going to die.\n\n\
At least this is better than being devoured or swallowed alive by a Titan...you think.\n\n\
How did the battle turn out, anyway?\n\n\
The next thing you know, you\'re in someone\'s arms. Short in stature, with piercing eyes - it\'s Captain Levi.\n\n\
His hands and uniform are drenched with your blood. But he doesn\'t flinch, doesn\'t even seem to mind, despite the fact that \
he\'s supposed to be a bit of a clean freak. \"The plan worked,\" he tells you, with as much brevity and dispassion as ever. \
\"You did your duty with honor.\"\n\n\
Most people probably have no idea that he would take the time to hold a nameless soldier, talk to them. He must have cared for \
many dying boys and girls in his time.\n\n\
\"You\'ve done more than enough...and you\'ll do more. The resolve you leave behind will give me strength. I swear to you...I will \
eradicate the Titans!!\"\n\n\
As you breathe your last, you smile.\n\n\
Does the Captain see it?\n\n\
**🎉 Congratulations! You\'ve obtained the \"No Regrets\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P313(self, *option):
        if option == ():
            response = 'Jean Kirstein learned a great deal from the battle. But in the end, he applied to the Military Police Brigade. \
Complete with the same bad attitude he had in training.\n\n\
You went into the Military Police, too. In principle, only the top ten graduates of any class are eligible to join the MPs, but \
because many of the top scorers in your class didn\'t apply to the unit, you were allowed in based on your actions in the Battle \
of Trost.\n\n\
You are assigned to the Military Police unit in Stohess District of Wall Sina - in the interior.\n\n\
This is where you see firsthand the corruption of the Military Police Brigade. They are supposed to be the elite of the elite, \
protecting the interior and the royal capital, but you see them drinking before noon, foisting not only random chores but their \
actual duties on you new recruits.\n\n\
Jean mixed quite well with this way of life outwardly, but inside he was stewing.\n\n\
His anger was directed not at the disgraceful conduct of his superior officers or the organization as a whole, but at your fellow \
recruit, Marlo.\n\n\
Marlo Freudenberg is a serious boy with a strong sense of right and wrong, convinced that he is going to reform the Military Police. \
Jean does not find this amusing, and finally confronts him.\n\n\
\"You, straighten out the MPs? Dammit, there are idiots like you even here?!\"\n\n\
Right now he\'s got Marlo by the collar again. Marlo, being Marlo, won\'t back down a step.\n\n\
\"Ha ha ha! Glad to see you two getting along!\"\n\n\
Another new recruit, a girl named Hitch, is laughing uproariously.\n\n\
**🎉 Congratulations! You\'ve obtained the \"Jean of the Military Police\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P314(self, *option):
        if option == ():
            response = 'You wonder how much time passed in the fighting.\n\n\
You dart about, swinging your blade for all you\'re worth. What\'s become of the other soldiers, of your friends, you have no idea.\n\n\n\
There\'s a rumble from far off. That\'s the direction of the gate.\n\n\
As you maneuver through the sky, the air you fly through is the same air that brings you word.\n\n\
You catch a glimpse of the sky, where your eye is drawn to a yellow line.\n\n\
A signal flare. Yellow smoke - the sign that a plan has succeeded.\n\n\n\
\"They did it!\" someone shouts.\n\n\
People have climbed up onto the nearby rooftops. They cheer, or shout that you should go help Eren; others head for the gate themselves.\n\n\
The plan worked.\n\n\
The city is still overrun with Titans. At this moment, soldiers are still being overpowered by the monsters, killed and eaten. \
The tragedy of this battle is still playing out.\n\n\
But you are triumphant.\n\n\
Type :one: to continue.'
            self.state.statuses.ian = 'Dead'
            self.state.statuses.mitabi = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 288

    def P315(self, *option):
        if option == ():
            response = 'You decide to join the Garrison. Among other things, this battle taught you how important it is to protect the \
people inside the walls. That experience also gets you assigned to the Trost District unit.\n\n\
And so...\n\n\
Today, you\'re once more assigned to the top of the city\'s wall.\n\n\
\"Hey, rookie. How ya doin\'?\" One of the more experienced soldiers, Mr. Hannes, calls out to you. \"Well, don\'t go crazy. Relax \
a little.\"\n\n\
Then he laughs. He\'s an easygoing guy.\n\n\
\"I\'ll thank you not to encourage laziness in my troops.\"\n\n\
That\'s your commanding officer, Squad Leader Rico. She glares at him.\n\n\
Mr. Hannes smiles indulgently. She gives him a thin smile in return. You were all in different places, but all of you came through \
that battle and saved this town.\n\n\
Mr. Hannes looks down at the gate, still blocked by the boulder, and murmurs fondly, \"I wonder if Eren\'s doing all right.\"\n\n\
**🎉 Congratulations! You\'ve obtained the \"Joining the Garrison\" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P316(self, *option):
        if option == ():
            response = 'Congratulations! You have successfully navigated Annie\'s labyrinth of secrets. However, even though you\'ve found out much about her during \
the Battle of Trost, you have the feeling that they are not the only secrets Annie is hiding.\n\n\
Perhaps, in the future, with the knowledge you have gained, you might be able to uncover her deepest secrets-?\n\n\
**You have obtained the Stohess Key! 🔑**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    # def P316(self, *option):
    #     if option == ():
    #         response = '3 years have passed since the battle of Trost.\n\n\
    # So much has changed since then. Technology has advanced tremendously, and humanity\'s future looks brighter than ever.\n\n\
    # You wonder what has happened to Annie in this period of time, as you have not heard from her since your encounters in the battle of Trost.\n\n\
    # Today, on your day off, you are walking along the streets of Stohess District.\n\n\
    # You happen to overhear some passers-by chatting excitedly of a concert being held by a famous singer right here in Stohess. You don\'t \
    # follow this pop culture that has sprung up recently, but for lack of things to do, you decide to check it out anyway.\n\n\
    # Even though you arrived early, the concert hall was already packed. Getting in was a challenge, but you eventually made it.\n\n\
    # The curtains part to massive cheers, screams and applause from the audience.\n\n\
    # With a screen in front of them, you can only make out the silhouette of the lead singer. However, it seems oddly familiar somehow, \
    # as if you have seen them somewhere before.\n\n\
    # It was only when the screen is dropped that you realize why. To your utter amazement, you see *Annie Leonhart* in a stylish new outfit, who proceeded to dazzle \
    # the crowd with dance moves like you\'ve never seen before.\n\n\
    # You realize that this was the goal she had in mind all along, the purpose that kept her going in life.\n\n\
    # Astonishment gives way to joy, as you join the crowd in clapping along with the music and calling her name.\n\n\
    # **👑 Congratulations! Through sheer perseverance and determination, you have successfully navigated Annie\'s labyrinth of secrets, earning you the \
    # \"Queen of Pop\" Secret Ending! 👑\n\n\
    # https://www.youtube.com/watch?v=IB8bMTn9mCk**'
    #         response2[0] = '\n\n\
    # **🎩 Now you can call yourself a real Smooth Criminal! 🎩**\n\n\
    # **To play again, type `~reset`.**'
    #         self.choices[0] = []
    #         return response

    def P317(self, *option):
        if option == ():
            response = 'You notice Annie standing at the back of the room by herself, away from the rest of your comrades.\n\n\
To your astonishment, she\'s wearing the same expressionless look on her face she always had during training. Normally, this \
wouldn\'t surprise you, but under these circumstances, shouldn\'t she be a little concerned, at least-?\n\n\
Curious, you decide to approach her.\n\n\
"The situation is grim, I don\'t deny that, but what\'s the use in panicking about it?", Annie says to you.\n\n\
"Look over there." Annie points to the rest of your comrades. "The others are already formulating a plan to get us out of here. \
When the time comes to take action, we must be ready to perform at our best. One slip-up can get us all killed."\n\n\
"And in any case, even if I were to die in this place, I want to die knowing that I\'ve did my very best to fulfill my duty."\n\n\
She is right. To maximize your chances of survival, you cannot afford to make any mistakes. \n\n\
Talking to Annie gives you renewed confidence. However, you can\'t shake the feeling that her courage comes from elsewhere...\
perhaps she knows something that you don\'t?\n\n\
Nevertheless, you are impressed with how she has managed to keep a clear and cool head under such dire circumstances. This combined \
with her keen observational abilities was likely what propelled her to the top 10 of your graduating class in the first place.\n\n\
**From this point on, if you see the words \"the top students in your trainee class\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 139

    def P318(self, *option):
        if option == ():
            response = 'In the midst of the never-ending battle, you happen to spot Annie sitting alone on a rooftop. From afar, she seems to be shivering.\n\n\
As you maneuver closer to check if she\'s alright, you realize that she wasn\'t actually \
shivering at all, but sobbing uncontrollably, her chest heaving with each sob. Between her sobs, she doesn\'t hear you land behind her.\n\n\
You are taken aback. You\'ve never seen Annie like this before.\n\n\
"I\'m sorry... I\'m so sorry..." you hear Annie mutter to herself.\n\n\
You see an extra set of maneuvering gear laying beside her. This must have belonged to the soldier whose death she had recently witnessed.\n\n\
You can\'t bring yourself to step forward and comfort her. After such a traumatic experience, she probably wants to be left alone right now.\n\n\
**From this point on, if you see the words \"in the midst of a battle rife with cruelty\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 294

    def P319(self, *option):
        if option == ():
            response = 'Watching Franz and Hannah in the distance, you didn\'t notice someone coming up beside you until they spoke. It was Annie.\n\n\
"Look at them, oblivious to the harsh reality of the world they live in. It does make all of this seem less pointless."\n\n\
You look at her quizzically. What was she trying to say?\n\n\
"Spending your entire life within this confined space. The Titan invasion. The reminder that your fate is completely at their mercy."\n\n\
She turns to look at you. "Have you ever wondered if there could be a point to all of this, something to justify all this death and destruction?"\n\n\
You find yourself unable to respond. Up till now, you have only been concerned about being a good soldier and doing your duty.\n\n\
But you understood what she meant. If humanity\'s extinction is inevitable, then what\'s the point of holding on to your dreams, holding on to life-?\n\n\
"That\'s what I thought in the past, anyway." Annie continued, as if picking up on your train of thought.\n\n\
"I had spent some time in the Interior before joining the military. While there, I met a man who showed me why that isn\'t the case. \
I still remember his words to me."\n\n\
*\'Every last person I\'ve seen was the same way.\'*\n\n\
*\'Whether it was booze, women, or even God.\'*\n\n\
*\'Family, the King, dreams, children, power.\'*\n\n\
*\'They couldn\'t keep going... unless they were drunk on something.\'*\n\n\
"I now understand what he meant. Life does not come with any meaning attached to it... everyone must find their own purpose in this world we live in. \
That\'s what keeps us all going in life despite the odds."\n\n\
She pauses, then says quietly, almost to herself,\n\n\
"And I am no exception."\n\n\
Annie tilts her head towards you. "So what keeps *you* going?"\n\n\
Without waiting for a reply, she takes off, leaving you to your thoughts.\n\n\
**From this point on, if you see the words \"a keen look in his/her eyes\", copy and paste those words into the chat to reveal an \
additional option you may take.**\n\n\
Type :one: to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 67

    