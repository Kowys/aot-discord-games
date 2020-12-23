import discord

class Book():
    def __init__(self, state):
        # Constants
        self.intro_msg = 'Welcome to the Attack on Titan adventure game!\n\n\
This is Book 2.\n\n\
**If you\'re ready, type `~start` to begin.**'

        self.reset_msg = discord.Embed(title = 'Game Reset!', description = 'Type **`~start`** to start a new game.\nType **`~intro`** for more information about the game.', colour=0xE5D2BB)

        self.EC = {'0️⃣':0, '1️⃣':1, '2️⃣':2, '3️⃣':3, '4️⃣':4, '5️⃣':5, '6️⃣':6, '7️⃣':7, '8️⃣':8, '9️⃣':9, '🔟':10, '⏩':11, '㊙️':'s'}
        self.EC2 = {0:'0️⃣', 1:'1️⃣', 2:'2️⃣', 3:'3️⃣', 4:'4️⃣', 5:'5️⃣', 6:'6️⃣', 7:'7️⃣', 8:'8️⃣', 9:'9️⃣', 10:'🔟', 11:'⏩', 's':'㊙️'}

        self.secrets = {
            'take a close look': 44,
            'take their conversation at face value': 92,
            'become exceptional soldiers': 9601,
            'she knows how to fight': 222}

        self.annie_secrets = {}

        self.all_pages = {1:self.P1, 1001:self.P1001, 2:self.P2, 3:self.P3, 4:self.P4, 5:self.P5, 6:self.P6, 8:self.P8, 9:self.P9, 11:self.P11, 12:self.P12, 
        13:self.P13, 15:self.P15, 16:self.P16, 18:self.P18, 19:self.P19, 21:self.P21, 22:self.P22,
        23:self.P23, 24:self.P24, 25:self.P25, 26:self.P26, 27:self.P27, 28:self.P28, 29:self.P29, 30:self.P30, 31:self.P31, 32:self.P32, 
        33:self.P33, 34:self.P34, 35:self.P35, 36:self.P36, 37:self.P37, 38:self.P38, 39:self.P39, 40:self.P40, 41:self.P41, 
        42:self.P42, 43:self.P43, 44:self.P44, 45:self.P45, 46:self.P46, 47:self.P47, 48:self.P48, 49:self.P49, 50:self.P50, 51:self.P51, 52:self.P52, 
        53:self.P53, 54:self.P54, 55:self.P55, 56:self.P56, 57:self.P57, 58:self.P58, 59:self.P59, 60:self.P60, 61:self.P61, 62:self.P62,
        63:self.P63, 64:self.P64, 65:self.P65, 66:self.P66, 67:self.P67, 68:self.P68, 69:self.P69, 70:self.P70, 71:self.P71, 72:self.P72, 73:self.P73, 74:self.P74, 75:self.P75, 76:self.P76, 77:self.P77, 
        78:self.P78, 79:self.P79, 80:self.P80, 81:self.P81, 82:self.P82, 83:self.P83, 84:self.P84, 85:self.P85, 
        86:self.P86, 87:self.P87, 88:self.P88, 8801:self.P8801, 89:self.P89, 90:self.P90, 92:self.P92, 93:self.P93, 94:self.P94, 95:self.P95, 96:self.P96, 9601:self.P9601, 97:self.P97, 
        98:self.P98, 9801:self.P9801, 99:self.P99, 9901:self.P9901, 100:self.P100, 101:self.P101, 102:self.P102, 103:self.P103, 104:self.P104, 
        105:self.P105, 106:self.P106, 107:self.P107, 108:self.P108, 109:self.P109, 
        110:self.P110, 111:self.P111, 112:self.P112, 113:self.P113, 114:self.P114, 115:self.P115, 117:self.P117, 118:self.P118, 119:self.P119, 120:self.P120, 121:self.P121, 
        122:self.P122, 123:self.P123, 124:self.P124, 125:self.P125, 126:self.P126, 127:self.P127, 128:self.P128, 129:self.P129, 130:self.P130, 131:self.P131,
        132:self.P132, 133:self.P133, 134:self.P134, 135:self.P135, 136:self.P136, 137:self.P137, 138:self.P138, 139:self.P139,
        140:self.P140, 141:self.P141, 142:self.P142, 143:self.P143, 144:self.P144, 146:self.P146, 147:self.P147, 148:self.P148, 149:self.P149, 
        150:self.P150, 151:self.P151, 152:self.P152, 153:self.P153, 154:self.P154, 155:self.P155, 1551:self.P1551, 156:self.P156, 157:self.P157, 158:self.P158, 159:self.P159, 160:self.P160, 
        161:self.P161, 162:self.P162, 163:self.P163, 164:self.P164, 165:self.P165, 166:self.P166, 167:self.P167, 168:self.P168, 169:self.P169, 170:self.P170, 
        171:self.P171, 172:self.P172, 173:self.P173, 174:self.P174, 
        175:self.P175, 176:self.P176, 177:self.P177, 1771:self.P1771, 179:self.P179, 181:self.P181, 182:self.P182, 
        183:self.P183, 184:self.P184, 185:self.P185, 186:self.P186, 187:self.P187, 188:self.P188, 189:self.P189, 190:self.P190, 
        191:self.P191, 192:self.P192, 193:self.P193, 194:self.P194, 195:self.P195, 196:self.P196, 197:self.P197, 198:self.P198, 199:self.P199,
        200:self.P200, 201:self.P201, 202:self.P202, 203:self.P203, 204:self.P204, 205:self.P205, 206:self.P206, 207:self.P207, 208:self.P208, 209:self.P209, 210:self.P210, 211:self.P211, 
        212:self.P212, 213:self.P213, 214:self.P214, 215:self.P215,
        216:self.P216, 217:self.P217, 218:self.P218, 219:self.P219, 220:self.P220, 221:self.P221, 222:self.P222, 223:self.P223, 224:self.P224, 225:self.P225, 
        226:self.P226, 227:self.P227, 228:self.P228, 229:self.P229, 230:self.P230, 231:self.P231, 232:self.P232, 
        233:self.P233, 234:self.P234, 235:self.P235, 236:self.P236, 237:self.P237, 238:self.P238, 239:self.P239, 240:self.P240, 241:self.P241, 242:self.P242, 243:self.P243, 244:self.P244, 245:self.P245,
        246:self.P246, 247:self.P247, 248:self.P248, 249:self.P249, 2491:self.P2491, 250:self.P250, 251:self.P251, 
        252:self.P252, 253:self.P253, 254:self.P254, 255:self.P255, 256:self.P256, 257:self.P257, 258:self.P258, 259:self.P259, 260:self.P260, 261:self.P261, 
        262:self.P262, 263:self.P263, 264:self.P264, 265:self.P265, 266:self.P266,
        267:self.P267, 268:self.P268, 269:self.P269, 270:self.P270, 271:self.P271, 272:self.P272, 273:self.P273, 274:self.P274, 275:self.P275, 276:self.P276, 278:self.P278, 279:self.P279, 
        280:self.P280, 281:self.P281, 282:self.P282, 283:self.P283, 284:self.P284, 285:self.P285, 286:self.P286, 287:self.P287, 288:self.P288, 289:self.P289, 291:self.P291, 292:self.P292,
        293:self.P293, 294:self.P294, 295:self.P295, 296:self.P296, 297:self.P297, 298:self.P298, 299:self.P299, 300:self.P300,
        301:self.P301, 302:self.P302, 3021:self.P3021, 3022:self.P3022, 3023:self.P3023, 3024:self.P3024, 303:self.P303, 304:self.P304, 305:self.P305, 306:self.P306, 307:self.P307, 308:self.P308, 
        309:self.P309, 310:self.P310, 311:self.P311,
        312:self.P312, 313:self.P313, 314:self.P314, 315:self.P315, 316:self.P316, 317:self.P317, 318:self.P318, 319:self.P319, 320:self.P320, 
        321:self.P321, 322:self.P322, 3221:self.P3221, 323:self.P323, 324:self.P324, 325:self.P325, 326:self.P326, 
        327:self.P327, 328:self.P328, 329:self.P329, 330:self.P330, 331:self.P331, 332:self.P332, 3321:self.P3321, 333:self.P333, 334:self.P334, 3341:self.P3341, 335:self.P335, 336:self.P336}

        self.endings = {146: 'A Cruel World', 161: 'Destruction of the Survey Corps', 209: 'Traitor’s Friend', 216: 'A Soldier in the Trost District Garrison', 
        304: 'A Sliver of Hope', 314: 'Beyond the Walls', 325: 'Eren Yeager’s Choice', 326: 'Jean Kirstein’s Vow', 328: 'Flight of the Female Titan', 329: 'The True Face of Sasha Blouse',
        330: 'The Girl Who Hid Herself', 331: 'A World Beautiful and Cruel', 3321: 'Hange Zoë’s Truth', 333: 'Armin Arlert’s Dream', 3341: 'Captain Levi’s Scars', 336: 'A Soldier of the Survey Corps'}

        # Variables
        self.cur_page = [1]
        self.choices = [[]]
        self.response2 = ['']
        self.state = state
        self.new_msg = None

    def page_flipper(self, option):
        self.all_pages[self.cur_page[0]](option)
        return self.all_pages[self.cur_page[0]]()

    def P1(self, *option):
        if option == ():
            response = 'The Titans pour into the city, one after another. The creatures are easy to spot because they loom over even the tallest buildings.\n\n\
This is Trost District. The town was supposed to be safe behind its walls - but suddenly the Colossal Titan appeared and destroyed the town gate, letting in this flood of man-eating monsters.\n\n\
You are a member of the 104th Training Corps. You’ve spent the last three years learning to fight, and today was to be the day you were inducted as a full member of the armed forces. \
You couldn’t have imagined that this was how your day of celebration would turn out. You and your fellow trainees have been thrown into the battle.\n\n\
Your enemies are numerous and massive. Your friends, including the more experienced soldiers, are killed one after another, devoured by Titans. \
You are wracked with exhaustion; you can hardly move. You’re almost out of gas for your Vertical Maneuvering Equipment, as well.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 1001

    def P1001(self, *option):
        if option == ():
            response = 'That’s when the black-haired boy appears. You know his uniform; he’s one of the other trainees. \
You feel a rush of relief - until his body begins to grow in size, and he becomes a Titan himself!\n\n\
What do you do?\n\n\
1️⃣ More Titans? You run away as fast as you can\n\n\
2️⃣ A human who can turn into a Titan? You’re going to bring him down!\n\n\
3️⃣ Work with this transforming Titan to fight nearby enemies'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 2
        elif option[0] == 2:
            self.cur_page[0] = 3
        elif option[0] == 3:
            self.cur_page[0] = 4
    
    def P2(self, *option):
        if option == ():
            response = 'On the battlefield, when you let fear take control of you and rob you of rational judgement, the only possible outcome is death.\n\n\
You fail in your attempt to run- a giant hand grabs you, and you are eaten by a Titan.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 5

    def P3(self, *option):
        if option == ():
            response = 'You launch yourself at the titan, using vertical maneuvering to help you move. You can sense a humanlike intelligence in this Titan’s eyes.\n\n\
You remember your comrade, Eren, and hesitate. The Titan roars. From anger, or sorrow? But then he begins to ramage, as if he’s just another monster. \
Is it because you didn’t trust him? Or is this what was inside him all along?\n\n\
His face looms in your vision, and his mouth is wide open.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 5

    def P4(self, *option):
        if option == ():
            response = 'You remind yourself- you remember that this creature was one of your comrades. You’re sure he’s different from the Titans who attack and eat humans.\n\n\
The Titan looks down at you, intelligence and emotion in his eyes. He’ll be a stalwart ally. With him on your side, you can beat the other Titans!\n\n\
Before you know it, the scene before you has changed. The black-haired titan is walking around, carrying a boulder almost as big as he is. Your comrades are sacrificing themselves to protect him. \
People you know, people you cared about, are among the dead. And yet, the Titan must be protected. He is humanity’s very hope for survival…\n\n\
Soldiers drop like flies. The black-haired Titan steps over their corpses, moving forward.\n\n\
You, too, join in the fight to defend him…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 5

    def P5(self, *option):
        if option == ():
            response = 'You open your eyes. It was all a dream. You’re soaked with sweat.\n\n\
It all starts to come back. You’re in the Garrison, and all the things you just dreamed about are over.\n\n\
The Battle of Trost was some days ago. It was a brutal fight with the Titans, and many soldiers died, including no small number of your brothers and sisters in arms from the 104th Training Corps.\n\n\
After the battle, you were assigned to help with corpse retrieval duty in the city. You remember all too well the horrifying state many of your friends were in. \
Ever since then, you’ve had nightmares almost every night. And it’s not just you. They seem to afflict a large number of your comrades.\n\n\
The dream you just had… may not have been something you actually experienced. Actual memories are so easily confused with things you’ve only heard about.\n\n\
You know it’s a fact that Eren Yeager, who was in the same class as you, turned into a Titan, and you know that was the key to humanity’s victory.\n\n\
You know it’s true, but it’s not an easy story to believe. Deep in your heart, you’re afraid of Eren, and maybe that’s what led to your dream…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 6

    def P6(self, *option):
        if option == ():
            response = 'You remember. You are the part of the 104th Training Corps, stationed at the Wall Rose South District training camp.\n\n\
This posting at the southernmost border of human territory is what got you involved in the Battle of Trost a few days ago. \
Humanity snatched victory from the jaws of the Titans, but not before a great many soldiers had sacrificed themselves. The fact that you survived may be nothing more than luck…\n\n\
You ponder your dream. Is Eren not really a friend? No. You don’t want to start thinking like that. But suppose there were other humans who could turn into Titans… \
Are there any guarantees that they would be allies, too?\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 8

    def P8(self, *option):
        if option == ():
            response = 'You think back on the vicious Battle of Trost.\n\n\
The fight was hideously one sided, with Titans pressing in all around. Even the more experienced soldiers were dropping like flies with the guard unit in tatters. \
The one silver lining was that with their sacrifice, the soldiers bought time for the people to safely evacuate.\n\n\
In the midst of this chaos, a boy from the 104th Training Corps, Eren Yeager, transformed into a Titan. It allowed him to save his friends from danger, but even Eren didn’t seem to know how he had done it. \
When Commander Pixis arrived with reinforcements, he came up with a bold plan to use the Titan Eren as a “living weapon” to retake Trost District. \
The operation cost many lives, but ultimately succeeded. Eren, in his Titan form, used a massive boulder to plug the hole in the town gate.\n\n\
This was humanity’s first victory against the Titans.\n\n\
Eren, however, was not hailed as a hero. \
The other soldiers regarded him as something weird and dangerous; he was put to a court-martial, where some even suggested that he should be executed and his body dissected for science.\n\n\
Thanks to the quick thinking and intervention of the Survey Corps, including its commander, Erwin, Eren was spared execution and was instead released into the custody of the Survey Corps. Or so you’ve heard…\n\n\
Now, where are you after the Battle of Trost?\n\n\
1️⃣ With Eren in “Squad Levi” of the Survey Corps\n\n\
2️⃣ With your friends at the army headquarters in Trost District'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 12
        elif option[0] == 2:
            self.cur_page[0] = 18

    def P9(self, *option):
        if option == ():
            response = '“Eren…” one of your comrades says. “He was about to kill Mikasa, wasn’t he?”\n\n\
There are rumors about the incident: they say that when Eren transformed into a Titan, he lost his sanity and began going berserk.\n\n\
Armin doesn’t deny it. “It’s true, he was. But in the end, he found his human heart again. Eren led us to victory.” Armin should know. He was there. \
“Not to mention, he never actually killed any of his allies. There’s a big difference between the potential to kill and actually killing. If he had accidentally caused any casualties, \
I’ll bet Commander Erwin and the others wouldn’t have been able to cover for him at the tribunal.”\n\n\
Everyone nods. This makes sense to them.\n\n\
You feel a rush of admiration. Armin is a smart young man. Yet at the same time, you can’t help feeling like his story had a certain detachment. \
If Eren had “accidentally caused any casualties,” what would Armin be saying now?\n\n\
The boy glances at somebody. You follow his gaze and see Annie. She’s trying to look disinterested, but you think she was quite engaged in Armin’s story. \n\n\
**From this point on, if you see the words "take their conversation at face value", copy and paste those words into the chat to reveal an additional option you may take.**\n\n\
Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 18

    def P11(self, *option):
        if option == ():
            response = 'You’re at the Old Survey Corps headquarters, where you’ve come with Squad Leader Hange. You’ve received special permission to enter, partly on the basis of being a classmate of Eren’s.\n\n\
The former Survey Corps baser is a dilapidated building located well away from the city center or any of the villages. Levi and the others members of his squad operating here are cautious, \
but regard you with a certain friendliness. Maybe they’re interested in you because you have real experience fighting Titans, even though you’re just a trainee.\n\n\
This building has been out of use for a long time. Yet despite its age, the interior is sparkling. Apparently the first thing Captain Levi did was order a thorough cleaning. \
Maybe part of being a top-level soldier is doing a good job at even the most mundane tasks.\n\n\
Now, where do you go?\n\n\
1️⃣ Talk to Captain Levi\n\n\
2️⃣ Talk to Eren\n\n\
3️⃣ Talk to Hange\n\n\
4️⃣ Go to the old well\n\n\
5️⃣ Talk to Squad Levi\n\n\
6️⃣ Look around the headquarters\n\n\
7️⃣ Go to Trost’s Army HQ with Hange\n\n\
⏩ Wait for the Day You Enter the Ranks'
            self.choices[0] = [1,2,3,4,5,6,7,11]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 58
        elif option[0] == 2:
            self.cur_page[0] = 22
        elif option[0] == 3:
            self.cur_page[0] = 73
        elif option[0] == 4:
            self.cur_page[0] = 45
        elif option[0] == 5:
            self.cur_page[0] = 31
        elif option[0] == 6:
            self.cur_page[0] = 64
        elif option[0] == 7:
            self.cur_page[0] = 18
        elif option[0] == 11:
            self.cur_page[0] = 13

    def P12(self, *option):
        if option == ():
            response = 'Your actions in the Battle of Trost got the attention of Captain Levi and the other members of the Survey Corps, and, combined with the fact that you were a classmate of Eren’s, \
you’re granted special dispensation to work with Squad Levi. You aren’t a full member of the Survey Corps- consider it an apprenticeship.\n\n\
The two of you got to the former Survey Corps headquarters, a dilapidated structure located well away from the city center or any of the villages.\n\n\
Supposedly, it’s a safe place for Eren to lie low for a while. Whether it’s meant to be safe for Eren, or for those around him, is hard to tell…\n\n\
Your duties begin with cleaning this long-unused building. The sight of the more experienced members of the Survey Corps, elite soldiers all, \
putting on the aprons and bandannas and doing housekeeping is very strange.\n\n\
Captain Levi, often called the strongest soldier in human history, has turned his undivided attention to cleaning up this building. \
You can tell top-leveled soldiers are different from other people even when they’re doing the most mundane tasks.\n\n\
Now, where do you go?\n\n\
1️⃣ Talk to Captain Levi\n\n\
2️⃣ Talk to Eren\n\n\
3️⃣ Talk to Hange\n\n\
4️⃣ Go to the old well\n\n\
5️⃣ Talk to Squad Levi\n\n\
6️⃣ Look around the headquarters\n\n\
7️⃣ Go to Trost’s Army HQ with Hange\n\n\
⏩ Wait for the Day You Enter the Ranks'
            self.choices[0] = [1,2,3,4,5,6,7,11]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 58
        elif option[0] == 2:
            self.cur_page[0] = 22
        elif option[0] == 3:
            self.cur_page[0] = 73
        elif option[0] == 4:
            self.cur_page[0] = 45
        elif option[0] == 5:
            self.cur_page[0] = 31
        elif option[0] == 6:
            self.cur_page[0] = 64
        elif option[0] == 7:
            self.cur_page[0] = 18
        elif option[0] == 11:
            self.cur_page[0] = 13

    def P13(self, *option):
        if option == ():
            response = 'You can simply wait here, helping Captain Levi and the others squad members, until the day you become a full soldier. If you do, type 1️⃣. \
Careful: you won’t be able to return here.\n\n\
If there’s anything else you still want to do, type 2️⃣.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 56
        elif option[0] == 2:
            self.cur_page[0] = 11

    def P15(self, *option):
        if option == ():
            response = '“Yeah.” Your words evoke a small smile from Armin. “You’re right. Why would I doubt my comrades? Maybe the fatigue is getting to me.”\n\n\
**Your Affinity with Armin has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.armin += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 95

    def P16(self, *option):
        if option == ():
            response = '“Wh-What makes you bring her up?” Bertolt seems unusually edgy.\n\n\
Reiner, however, looks thoughtful. He seems to be choosing his words carefully. “Hm. Annie Leonhart? We’re not very close, but I’m confident she’s a good soldier. \
I remember she threw me in combat training once like I was light as a feather.”\n\n\
Maybe it’s that memory that makes his shoulders slump. Reiner is no slouch himself in hand-to-hand combat, so Annie must be quite a fighter. \
Bertolt adds, almost as though apologizing for her, “She’s… Sh-She’s not a bad person. She keeps her comrades at arm’s length, but I think she just isn’t very social…” \n\n\
If you ask them what unit they’re going to join, type 1️⃣.\n\n\
If you go somewhere else, type 2️⃣.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 54
        elif option[0] == 2:
            self.cur_page[0] = 18

    def P18(self, *option):
        if option == ():
            response = 'You are at the army headquarters in the heart of Trost District.\n\n\
After the Titan Eren succeeded in blocking the ruined gate with the huge boulder, \
the fixed guns on top of Trost’s walls along with the efforts of the Survey Corps succeeded in mopping up the remaining Titans in the city.\n\n\
You may be free from the immediate threat of the Titans, but the city remains in shambles, and the citizens can’t yet resume their normal lives.\n\n\
The army headquarters miraculously survived the battle unscathed and has been turned into an impromptu base. \
The survivors of your 104th Training Corps are here, too, helping out with whatever the army needed done. But it’s really just a way of passing the time…\n\n\
Now, who do you want to see?\n\n\
1️⃣ Armin\n\n\
2️⃣ Jean\n\n\
3️⃣ Annie\n\n\
4️⃣ Bertolt and Reiner\n\n\
5️⃣ The captured Titans, Sonny and Bean\n\n\
6️⃣ Mikasa\n\n\
7️⃣ Krista\n\n\
8️⃣ Sasha and Connie\n\n\
9️⃣ Mike\n\n\
🔟 Follow Hange to the Old Survey Corps Headquarters\n\n\
⏩ Wait to Become a Full Soldier'
            self.choices[0] = [1,2,3,4,5,6,7,8,9,10,11]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 78
        elif option[0] == 2:
            self.cur_page[0] = 53
        elif option[0] == 3:
            self.cur_page[0] = 28
        elif option[0] == 4:
            self.cur_page[0] = 38
        elif option[0] == 5:
            self.cur_page[0] = 33
        elif option[0] == 6:
            self.cur_page[0] = 68
        elif option[0] == 7:
            self.cur_page[0] = 85
        elif option[0] == 8:
            self.cur_page[0] = 25
        elif option[0] == 9:
            self.cur_page[0] = 62
        elif option[0] == 10:
            self.cur_page[0] = 11
        elif option[0] == 11:
            self.cur_page[0] = 19

    def P19(self, *option):
        if option == ():
            response = 'You can simply wait here with the other numbers of the 104th Training Corps until the day you become a full soldier. If you do, type 1️⃣. \
Careful: you won’t be able to return here.\n\n\
If there’s anything else you still want to do, type 2️⃣.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 56
        elif option[0] == 2:
            self.cur_page[0] = 18

    def P21(self, *option):
        if option == ():
            response = 'You remove your familiar trainee’s uniform and don the “Dual Rose” of a Garrison soldier. \
In light of your experiences in this area, you’re assigned to the unit defending Trost District.\n\n\
There’s a great deal to do, from the maintenance of the walltop guns to the repair of the damaged city. The work is hard, but there’s no danger of Titans attacking this place; the days go by in peace.\n\n\
Before you know it, it’s been a month. The army officially announced that the Survey Corps will be making an expedition outside the walls.\n\n\
Trost District was once an important base for these forays, but with its gate rendered useless, it can no longer fill that role.\n\n\
The Survey Corps will be using the eastern district of Karanes as their launching point this time. You wonder if those among your comrades who joined the Survey Corps will be all right.\n\n\
You’ve been assigned to guard duty atop the walls. You cast your gaze out toward what’s beyond them. Of course, from this distance, \
you can’t see so much as the faintest shadow of the Survey Corps far, far to the east.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 216

    def P22(self, *option):
        if option == ():
            response = 'You meet with your classmate, Eren Yeager. Another soldier is monitoring your conversation, as a guard, and you’ve been warned not to ask about anything inappropriate.\n\n\
You take a good look at Eren, but he still looks like a normal young man to you. Can he really turn into a Titan…?\n\n\
“Oh, it’s you,” Eren says. “How’s everyone doing?”\n\n\
He seems to be asking after your other classmates. You tell him what you can, given the gaze of the soldier standing nearby. When you inform him that several people he knows are safe, \
Eren seems very relieved. He isn’t exactly under house arrest here, let alone tied up in a jail cell somewhere, but neither does he seem to have true freedom of movement.\n\n\
“I sleep in the basement room. I think the idea is that if I accidentally turn into a Titan in my sleep, it’ll be too confined for me to do anything.” He laughs uneasily. \
Eren doesn’t seem to have suffered any external injuries, but he appears subdued. No doubt there’s a lot on his mind.\n\n\
Finally he says, “I know how this looks, but I’ve become a real member of the Survey Corps.” He pauses, then says, “You know, I wonder what everyone else is going to do about their future. \
After what happened, I wouldn’t blame anyone for not wanting to join the Survey Corps anymore.”\n\n\
Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 11

    def P23(self, *option):
        if option == ():
            response = '“I picked this team myself,” Levi says. “They’ve fought Titans outside the walls. They’ve survived hellish conditions, time and again.”\n\n\
Levi is a man of few words, but you can tell how much he’s trusted.\n\n\
If you ask him something else, type 1️⃣.\n\n\
Otherwise, type 2️⃣ to choose a new destination. The captain is a busy man.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 58
        elif option[0] == 2:
            self.cur_page[0] = 11

    def P24(self, *option):
        if option == ():
            response = '“In the well, we did experiments on Eren’s ability to turn into a Titan,” he says. “But no matter how many times he bit his own hand, he couldn’t do it. \
But look… We took him out of the well and were having a break, drinking some tea, and all of a sudden his arm- just his arm- turned into a Titan arm. \
When we asked him about afterward, it didn’t sound like he did it on purpose. According to Squad Leader Hange, he was trying to pick up a spoon or something…”\n\n\
Gunther scratches his own cheek uncomfortably.\n\n\
“We were pretty panicked, so yeah… We didn’t ask nicely. Weapons out.” He pauses, then says, “We did wrong. He bit that hand til it flowed with blood. It must’ve hurt.”\n\n\
You notice something on Gunther’s palm as he speaks to you: a scar, the imprint of teeth. It must’ve been their way of apologizing to Eren.\n\n\
Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 11

    def P25(self, *option):
        if option == ():
            response = 'Your classmates Sasha and Connie are standing and talking together. They’re discussing the units they want to join, a decision you’ll all have to make soon. \
Both of them were at the top of your class, so they could choose the Military Police Brigade if they want to.\n\n\
“I’m definitely thinking about the MPs,” Connie says. “I was planning to join the Survey Corps like Eren. But when we had to fight the Titans for real, I was just… I was so scared. \
And the Military Police Brigade is supposed to be the elite of the elite. If I could get in there, it would make my mom proud.”\n\n\
“You’re right,” Sasha says. “The Military Police are a good choice. I hear they get good food, too. They don’t have to live on potatoes. They get meat and everything…”\n\n\
As enthusiastic as both of them sound, their expressions are dark. They seem to be wondering if the MPs are really the right choice.\n\n\
Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 18

    def P26(self, *option):
        if option == ():
            response = '“I wouldn’t lose to the likes of him,” Mikasa mutters.\n\n\
There’s no question that her fighting abilities are superb. She might even be the equal of Captain Levi…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 69

    def P27(self, *option):
        if option == ():
            response = '“Hmph. I liked the look in his eyes when he declared that he was going to destroy all the Titans.” Levi stares into space for a second.\n\n\
“He might make a good soldier, but he does have a Titan within him. If he can’t control it, then I will bury him. That’s all there is to it.”\n\n\
If you ask him something else, type 1️⃣.\n\n\
Otherwise, type 2️⃣ to choose a new destination. The captain is a busy man.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 58
        elif option[0] == 2:
            self.cur_page[0] = 11

    def P28(self, *option):
        if option == ():
            response = 'You spot Annie Leonhart and call out to her. With her golden hair and sense of style, there’s no question Annie is attractive, \
but her aquiline nose and sharp features make her intimidating as well. She has a hard look in her eyes and doesn’t seem to want to get close to people.\n\n\
Even in training, she was taciturn and never very expressive. Neither did she seem especially close to anyone else in the unit. When you call her name, she turns towards you with a look of annoyance.\n\n\
“Oh, it’s you,” she says disinterestedly. “You want something?”\n\n\
1️⃣ Ask what unit she plans to join\n\n\
2️⃣ Ask her to teach you martial arts'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 55
        elif option[0] == 2:
            self.cur_page[0] = 43

    def P29(self, *option):
        if option == ():
            response = 'Hange’s explanation is long and technical, and most of it goes over your head. The following points, however, sink in.\n\n\
“Titans eventually stop moving when they’re totally cut off from sunlight. How long it takes varies from Titan to Titan.\n\n\
“The Survey Corps has never before succeeded in actually capturing a Titan like this and subjecting it to observation and experiments. \
If we can keep gathering data, it could give us a huge advantage in our struggle against the Titans.”\n\n\
You gather that this is the first time anyone has managed to demonstrate the truth of the point about sunlight. You have to admit, you’re impressed. \
If the Survey Corps can continue to study their two captives, there’s a lot they can learn about the formerly inscrutable Titans. You might start to find out who your enemies really are, \
and that thought gives you hope.\n\n\
“Anyways, I’ve got to get back to my experiments!”\n\n\
Hange is finally done talking.\n\n'
            if self.state.flags.hange_explanation == False:
                response += '**Your Affinity with Hange has increased by 1!**\n\n'
                self.state.affinities.hange += 1
                self.state.flags.hange_explanation = True
            response += 'Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.flags.from_squad_levi == True:
                self.cur_page[0] = 11
                self.state.flags.from_squad_levi = False
            else:
                self.cur_page[0] = 18

    def P30(self, *option):
        if option == ():
            response = 'Mikasa is lost for words. She stares at you, her eyes wide.\n\n\
Finally, she says, “I know that. But I should have done better. The failure was mine.” \n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 69

    def P31(self, *option):
        if option == ():
            response = 'The Survey Corps Special Operations Squad, informally known as Squad Levi, has four members. They are all specially chosen, \
distinguished soldiers even within the elite ranks of the Survey Corps.\n\n\
You salute; they return the gesture and introduce themselves. You find them surprisingly friendly.\n\n\
Petra, the only woman in the squad, is the first to speak to you. “You’re from the 104th Training Corps, aren’t you? Eren’s classmate.”\n\n\
“Eren’s group…?” Eld and Gunther, two men, mutter together. They don’t seem to like this news.\n\n\
“Feh. So you’re friends with that prissy little brat? Just mind you, don’t get in the way, rookie,” the final member, Oluo, says threateningly. You…\n\n\
1️⃣ Ask about Levi, Eren, and Hange.\n\n\
2️⃣ Take umbrage at Oluo’s tone'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 87
        elif option[0] == 2:
            self.cur_page[0] = 32

    def P32(self, *option):
        if option == ():
            response = '“So you want to know why I said that?” Oluo scoffs. “I don’t think a greenhorn like you would get it.” Maybe he thinks he sounds cynical. \
“I’m not a nice enough guy to just spill the beans for you, either. Have a think and figure it out for yourself.”\n\n\
Petra breaks in. “Stop that Oluo. You’re not doing yourself any favors. You never used to talk like that. If you think you sound like Captain Levi, you don’t at all. \
Remember that time we were on horseback and you were blathering away dramatically and bit your tongue?”\n\n\
This exchange clarifies things for you. These people greatly respect Levi, and are very focused on him. Still… maybe Oluo’s a little strange.\n\n\
“Heh heh! Petra,” he says. “You’re practically hen-pecking me. I know we’re in the same squad, but I’m not ready to make you my wife just yet!”\n\n\
“I wish you’d bitten your tongue off and died from blood loss…”\n\n\
You wonder: is that the kind of joke only two comrades who have lived through battle together can share? Or is she serious? Maybe you’ll learn the answer when you get a little more experience.\n\n\
If you talk about something else, type 1️⃣.\n\n\
If you’ve had enough, type 2️⃣ to choose a new destination.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 87
        elif option[0] == 2:
            self.cur_page[0] = 11

    def P33(self, *option):
        if option == ():
            response = 'In a corner of the headquarters’ central courtyard are two Titans. The Survey Corps managed to capture them during the cleanup of Trost District. \
The four-meter Titan has been named Sonny, while they’re calling the seven-meter one Bean.\n\n\
You gape. Countless iron nails and thick metal bands have been used to bind them, and some of their elite Survey Corps members are guarding them. \
But still, it’s not pleasant seeing a living Titan before your eyes.\n\n\
A voice comes from behind you.\n\n\
“Heh heh heh! Cute, aren’t they?”\n\n\
The person who speaks to you is wearing glasses, their long hair casually tied back. It’s Hange Zoe, a squad leader with the Survey Corps. \
Known as one of the top Titan researchers, Hange is responsible for conducting experiments on these captives.\n\n\
“Nooow then, I wonder what kind of tests we should do today?”\n\n\
Hange’s face is flushed with what might be happiness. The question doesn’t appear to be rhetorical.\n\n\
What do you say?\n\n\
1️⃣ “We should see if we can communicate with the Titans\n\n\
2️⃣ “We should chop those things up.”\n\n\
3️⃣ “Tell me about Titans”'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 34
        elif option[0] == 2:
            self.cur_page[0] = 52
        elif option[0] == 3:
            self.cur_page[0] = 81

    def P34(self, *option):
        if option == ():
            response = '“Ahh! That’s a fantastic idea!” Hange exclaims, spreading both arms wide. “If Titans can understand human language, we might be able to learn about them!”\n\n\
“I thought you already tried that yesterday- and the day before,” says the aide next to Hange. “Didn’t you conclude that it was impossible to talk to the Titans, or even make ourselves understood.”\n\n\
“Ah, but Moblit, today could be the day! Let’s try a different way of communicating.”\n\n\
With that, Hange approaches the four-meter Titan, Sonny, and waves. Sonny doesn’t seem interested. His eyes evince not a shred of intelligence. But he does open his mouth and say, “Ahhhh.”\n\n\
“Hm? What’s that? You want to say something, Sonny?” Hange comes even closer.\n\n\
Suddenly, Sonny clamps his giant mouth shut! His massive teeth make an audible gnashing sound. Hange is only just able to jump back, exclaiming, “Ha ha ha! Did you see that? Sonny responded to my words!”\n\n\
“He was trying to eat you, Squad Leader!” Moblit objects, dragging Hange back. “If you keep this up, you really are going to die one of these days!”\n\n\
It looks like this is how these experiments always go… \n\n\
If you want to spend more time with Hange, type 1️⃣ and make a different suggestion.\n\n\
If you’re tired of playing along, type 2️⃣ to choose a new destination.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 33
        elif option[0] == 2:
            self.cur_page[0] = 18

    def P35(self, *option):
        if option == ():
            response = 'Annie’s eyes soften when you say this.\n\n\
“Yeah. My father is a worrier. I think it would be better to work on my fighting skills than to use something like this. This wouldn’t do any good against a Titan, anyway.”\n\n\
Annie thanks you again. You give her the ring and leave.\n\n\
**You obtain Key Number R, the secret of the ring. Write down or remember the number 40.**\n\n\
Type 1️⃣ to choose a new destination.'
            self.state.flags.keyR = 'Yes'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 18

    def P36(self, *option):
        if option == ():
            response = 'You pay close attention to Annie’s feet, read her movements. She kicks fast and high- but you dodge.\n\n\
“Well, well.” Annie’s eyes widen the slightest bit, the hint of a smile passing over her face. “Not bad. Looks like I’d better get serious.” A furious flurry of kicks follows.\n\n\
In the end, Annie works you over; her last strike sends you flying.\n\n\
Her fighting skills are incredible. You never had a chance of winning.\n\n\
“You put up a halfway decent fight. Feel free to ask for another lesson sometime.”\n\n\
Annie smiles a little, and walks away in good spirits.\n\n'
            if self.state.flags.annie_training == False:
                response += '**Your Affinity with Annie has increased by 1!**\n\n'
                self.state.affinities.annie += 1
                self.state.flags.annie_training = True
            response += 'Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 37

    def P37(self, *option):
        if option == ():
            response = 'Annie has been gone for a few minutes before you manage to haul yourself up.\n\n\
Suddenly you notice something on the ground: a silver-colored metal ring.\n\n\
Did Annie drop this during the fight? You pick it up.\n\n\
The ring looks very plain and simple, maybe a little large for a woman to wear. It looks less like a piece of jewelry and more like maybe it’s supposed to protect the finger.\n\n\
As you fiddle with the ring, you must brush a particular spot by accident, because there’s a click and a tiny blade extends. What a nasty little trap. You carefully fold the blade back in.\n\n\
Now… What do you do with the ring?\n\n\
1️⃣ Take the underhanded thing back to headquarters\n\n\
2️⃣ Give it back to Annie\n\n\
3️⃣ Leave it and choose a new destination'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 40
        elif option[0] == 2:
            self.cur_page[0] = 89
        elif option[0] == 3:
            self.cur_page[0] = 18

    def P38(self, *option):
        if option == ():
            response = 'Reiner is well-built and looks like a dependable older brother. In contrast, Bertolt is taller but doesn’t look as strong. \
The vibes they give off are also polar opposites, but they must get along well because they’re often together.\n\n\
You can talk to them. If you ask about which unit they want to join, type 1️⃣.\n\n\
If you ask what they think about Annie, type 2️⃣.\n\n\
If you’d rather go somewhere else, type 3️⃣.'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 54
        elif option[0] == 2:
            self.cur_page[0] = 16
        elif option[0] == 3:
            self.cur_page[0] = 18

    def P39(self, *option):
        if option == ():
            response = 'You think back to what happened here.\n\n\
This was several days ago now. Hange came to the old Survey Corps headquarters and began conducting experiments on Eren. The dried-up old well seemed to get Hange’s attention.\n\n\
If Eren were to transform while inside it, it would be the perfect size to contain his Titan body and he couldn’t move. On the off chance he lost himself and went berserk, \
it would be possible to observe and even experiment on him. That, at least, was the logic by which Eren was lowered into the well.\n\n\
During the Battle of Trost, Eren transformed when he felt physical pain. So he kept biting his hand down in that well, until it was covered in blood… but he still didn’t transform into a Titan.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 67

    def P40(self, *option):
        if option == ():
            response = 'You’re just about to head off… when someone attacks you from behind. You’re knocked unconscious.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 51

    def P41(self, *option):
        if option == ():
            response = '“Hey, hey. I’m a modest young lady, remember? What do you think you’re doing?”\n\n\
Annie dodges you, moving quickly. In the same motion, she grabs your hand and bends it backward.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 71

    def P42(self, *option):
        if option == ():
            response = '“Ahh! My dear trainee! So you’re interested in the Titans, too?” Hange’s face splits into a grin. “And why not? You have a classmate who can turn into one, after all. \
You know, I’m hoping to get Eren’s cooperation in some new experiments on Sonny and Bean. I’m just waiting for permission. Oh- Sonny and Bean are the names of the Titans the Survey Corps captured. \
They’re at Trost District army headquarters right now…” Hange’s furiously paced speech suddenly comes to a stop.\n\n\
“Ha ha! I see I’ve started monologuing. Sorry about that.” The smile widens. “I should have started by explaining about our pet Titans and the experiments we’ve done so far. \
Let’s not just stand here and talk. Let’s find somewhere nice to sit down…”\n\n\
It looks like you’re going to be hearing about Titans for the foreseeable future…\n\n\
Type 1️⃣ to continue.'
            self.state.flags.from_squad_levi = True
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 29

    def P43(self, *option):
        if option == ():
            response = '“Huh…? Annie’s expression changes. Her usual impassive face betrays just the hint of a happy smile. Or is that the cruel grin of someone who’s found their next victim…?\n\n\
If you’re going to back out, now’s your chance. Type 1️⃣ to make a different choice.\n\n\
If, with no thought for your own safety, you forge ahead with the martial arts lesson… type 2️⃣.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 18
        elif option[0] == 2:
            self.cur_page[0] = 44

    def P44(self, *option):
        if option == ():
            response = 'You and Annie head for the martial arts practice ground in the courtyard.\n\n\
“I think it’s best to learn from experience,” Annie says. “Come at me however you like.” Then she assumes a fighting stance.\n\n\
Her defense is perfect; you see no way through her guard. Take a close look at her and decide what to do.\n\n\
You…\n\n\
1️⃣ Fire off your best punch!\n\n\
2️⃣ Grab her in a hug to keep her from moving!\n\n\
3️⃣ Attack quickly, watching out for her kick!'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 86
        elif option[0] == 2:
            self.cur_page[0] = 41
        elif option[0] == 3:
            self.cur_page[0] = 50
        elif option[0] == 's':
            self.cur_page[0] = 36

    def P45(self, *option):
        if option == ():
            response = 'You come to an old well. The water has been long since dried up.\n\n'
            if self.state.flags.seen_well == False:
                response += 'If you were with Eren after the Battle of Trost, type 1️⃣.\n\n\
Otherwise, type 2️⃣.'
                self.choices[0] = [1,2]
            else:
                response += 'Type 1️⃣ to continue.'
                self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.flags.seen_well == False:
                self.cur_page[0] = 39
                self.state.flags.seen_well = True
            else:
                self.cur_page[0] = 70
        elif option[0] == 2:
            self.cur_page[0] = 49

    def P46(self, *option):
        if option == ():
            response = 'Her look gets even sharper. “And just what do you mean by that?” she asks.\n\n\
1️⃣ “What if there was some situation where you had to hurt yourself for some reason?”\n\n\
2️⃣ “I heard some of our comrades shot themselves during the Battle of Trost.”'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 79
        elif option[0] == 2:
            self.cur_page[0] = 75

    def P47(self, *option):
        if option == ():
            response = 'You hurry to help Eren. His hand detaches from the massive arm with a popping sound.\n\n\
“Th-Thanks,” he says. The gigantic arm lies on the ground, blowing out steam until it was all but dissolved.\n\n\
Hange dashes up to the two of you, exclaiming, “No! I wanted to study that!”\n\n'
            if self.state.flags.eren_hand == False:
                response += '**Your Affinity with Eren has increased by 1!**\n\n'
                self.state.affinities.eren += 1
                self.state.flags.eren_hand = True
            response += 'Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 80

    def P48(self, *option):
        if option == ():
            response = 'Armin isn’t biting. “No,” he says, “maybe I misunderstood what I was seeing.”\n\n\
If you keep the secret to yourself, type 1️⃣.\n\n\
If you decide to ignore Armin and go after Annie yourself, type 2️⃣.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 77
        elif option[0] == 2:
            self.cur_page[0] = 90

    def P49(self, *option):
        if option == ():
            response = 'Gunther, a member of Squad Levi, passes by, muttering, “The experiments we did here were terrible.”\n\n\
If you ask him what he’s talking about, type 1️⃣.\n\n\
If you aren’t interested, or already know, type 2️⃣ to choose a new destination.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 24
        elif option[0] == 2:
            self.cur_page[0] = 11

    def P50(self, *option):
        if option == ():
            response = 'You think you’re being careful, but Annie’s kick is astoundingly fast. Her leg lifts higher than you expect.\n\n\
“Hah! Too slow!” Her foot connects to your temple.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 71

    def P51(self, *option):
        if option == ():
            response = 'Not long after, the murder of Sonny and Bean occurs. You are among the corpses that result.\n\n\
They ultimately decide that you killed the Titans out of personal hatred, but that the two fought back and you couldn’t escape being killed yourself.\n\n\
**You have died. To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P52(self, *option):
        if option == ():
            response = '“Ooh! I like that!” Hange hefts a steel spear that appears intended for use in experiments.\n\n\
“Didn’t you try that the other day?” Hange’s aide says.\n\n\
“The key to a successful experiment is repetition, Moblit! How do Titans respond when injured? Do they feel pain? How quickly can they heal? There are so many things to study!”\n\n\
With that, the squad leader approaches Bean, the 7-meter Titan and begins jabbing at him with the spear.\n\n\
“Waaah!” Bean’s wail is uncanny.\n\n\
“Waaaah!” For some reason, Hange begins wailing too.\n\n\
“Why are you making that noise, Squad Leader?” Moblit shouts. “And you’re too close- it’s dangerous!”\n\n\
Hange looks back. “How can you not cry back at him? Bean is enduring such pain!” Perhaps it’s an excess of emotion that has brought the tears to the squad leader’s eyes. \
“How can you call yourself a researcher if you don’t understand the Titans’ feelings? Please, Bean, endure! It hurts me too!” Hange exclaims, resuming spearing the Titan.\n\n\
You see the steam of the Titan healing its wounds, and the two wailing voices mingle together…\n\n\
If you want to continue to entertain Hange, type 1️⃣ and make another suggestion.\n\n\
If you’re tired of this, type 2️⃣ to choose a new destination.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 33
        elif option[0] == 2:
            self.cur_page[0] = 18

    def P53(self, *option):
        if option == ():
            response = 'Jean Kirstein, a young man who was one of your classmates, is standing and talking with several of the other trainees.\n\n\
Jean got excellent marks, but his bad attitude during training caused others to resent him. Rumor had it that he was going to pick a cushy life with the Military Police Brigade, \
as is his right as one of the top scorers.\n\n\
But something seems to have changed about him since the Battle of Trost. He’s started saying that he’s decided to join the Survey Corps. \
He first mentioned it while on cleanup duty after the battle- while bringing in the corpses of his friends and comrades.\n\n\
It seems like the normal reaction to a firsthand experience of just how terrifying the Titans are would be to want to join the MPs even more. \
That seems to be what Jean and the soldiers around him are discussing.\n\n\
“Heh! Just ‘cause I want to join the Survey Corps doesn’t mean I’m like that suicidal bastard all of a sudden.” Jean all but spits the words out. That, at least, hasn’t changed.\n\n\
“‘That suicidal bastard’- you mean Eren?” one of your classmates asks. It’s a nickname Jean gave Eren when you were all training together. \
Eren, eager to join the Survey Corps and exterminate the Titans, was often at loggerheads with Jean. Jean would always taunt Eren with this nickname, \
and it found a certain currency among members of the 104th Training Corps.\n\n\
And now Jean is planning to join the Survey Corps himself. Life is truly strange.\n\n\
Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 18

    def P54(self, *option):
        if option == ():
            response = '“I’m going to join the Survey Corps,” Reiner says. “I know it’ll be dangerous, but I want to go back to my hometown; no matter what. I would do anything.”\n\n\
You’re impressed, but this is also what you expected from him. Reiner would no doubt help boost the Survey Corps’ morale.\n\n\
In contrast, Bertolt is ambivalent; he seems to want to avoid the entire subject. “I’ve just been… going with the flow. I really respect the rest of you. \
You’ve got all these ideals that you’re working towards.”\n\n\
If you ask what they think of Annie, type 1️⃣.\n\n\
If you want to go somewhere else, type 2️⃣.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 16
        elif option[0] == 2:
            self.cur_page[0] = 18

    def P55(self, *option):
        if option == ():
            response = '“I’m set on joining the Military Brigade,” she says. You know that she was ranked fourth among your classmates; the top 10 have the option of joining the MPs. \
“But so what?” she goes on. “Were you going to change your plans based on what I do or something?” Her expression never alters; her eyes are cold.\n\n\
If you ask her to teach you martial arts, type 1️⃣.\n\n\
If you want to go somewhere else, type 2️⃣.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 43
        elif option[0] == 2:
            self.cur_page[0] = 18

    def P56(self, *option):
        if option == ():
            response = 'One morning, an urgent dispatch arrives at the old Survey Corps headquarters.\n\n\
“What?!” Hange exclaims upon hearing the message. “Sonny and Bean-?!” The squad leader rushes off to Trost army headquarters.\n\n\
It looks like something big is going on. Captain Levi and the members of the special operations squad hurry around. \
They decide to take Eren with them (you suspect they can’t afford to leave someone behind to guard him). You end up going with them as well.\n\n\
You all ride to army headquarters as fast as you can. When you arrive, the place is in an uproar. You learn that the two captured Titans have been killed.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 82

    def P57(self, *option):
        if option == ():
            response = 'One morning, you find the army headquarters in an uproar. The two captured Titans were killed in the night.\n\n\
After a while, Squad Leader Hange arrives, riding as fast as possible. The squad leader was responsible for experimenting on the Titans, but had been somewhere else last night. Bad timing.\n\n\
“No… And today I was going to get Eren’s help to do some new experiments...”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 82

    def P58(self, *option):
        if option == ():
            response = 'Captain Levi is there. You salute.\n\n\
You’ve heard a lot of rumors- that he’s the strongest soldier humanity has, that he’s a one-man brigade. From up close like this, though, you find him surprisingly small, with a few distinguishing features. \
Yet just standing there, he exudes a sense of intimidation. There’s no question this is an experienced soldier.\n\n\
He’s staring right at you. You can’t tell if you’ve done something to earn a glare, or if he just always looks this severe.\n\n\
“One of Eren’s classmates, are you? Did you want something from me?”\n\n\
You…\n\n\
1️⃣ Ask about Squad Leader Hange Zoe\n\n\
2️⃣ Ask about the Special Operations Squad, aka Squad Levi\n\n\
3️⃣ Ask about Eren'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 59
        elif option[0] == 2:
            self.cur_page[0] = 23
        elif option[0] == 3:
            self.cur_page[0] = 27

    def P59(self, *option):
        if option == ():
            response = '“Ah. That Abnormal,” he says.\n\n\
A human Abnormal…? You suppose he just means Hange is strange.\n\n\
“If the squad leader asks for your help, then help. Even if it ends up being troublesome.”\n\n\
If you ask him something else, type 1️⃣.\n\n\
Otherwise, type 2️⃣ to choose a new destination. The captain is a busy man.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 58
        elif option[0] == 2:
            self.cur_page[0] = 11

    def P60(self, *option):
        if option == ():
            response = 'You stand beside Captain Levi, helping him protect Eren.\n\n\
The members of Squad Levi call out to you:\n\n\
“What are you doing, trainee? Get away from there!”\n\n\
“Captain Levi, you have to move, quickly!”\n\n\
You hear them, but you don’t move.\n\n\
In the meantime, Eren withdraws his own arm from the Titan arm. As the massive appendage begins to waste away, the armed soldiers at last begin to relax. Only Hange is upset, crying, “No! My Titan arm!”\n\n\
After it’s all over, Captain Levi says, “I told you to remain calm. This trainee seems to have a cooler head than anyone else here.”\n\n'
            if self.state.flags.levi_hand == False:
                response += '**Your Affinity with Levi has increased by 1!**\n\n'
                self.state.affinities.levi += 1
                self.state.flags.levi_hand = True
            response += 'Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 80

    def P61(self, *option):
        if option == ():
            response = 'That night, an idea comes to you in a rush. You suddenly remember the discussion of whether Eren needed to bite his hand to transform into a Titan. \
But if some kind of pain is the key, then there’s a better way than biting himself…\n\n\
You realize there’s someone with you, there in the darkness, but a second later you take a sharp blow to the head and lose consciousness.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 51

    def P62(self, *option):
        if option == ():
            response = 'A bearded Survey Corps soldier is there. It’s Squad Leader Mike Zacharias, rumored to be the strongest man in the unit after Captain Levi himself.\n\n\
Suddenly, he brings his face very close to your body and begins sniffing you. Then he snorts- but with a smile- and leaves without saying anything.\n\n\
What was that all about? You’ve heard tell that the brutality of the work in the Survey Corps means only the crazies end up here. Maybe he’s one of them…\n\n\
Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 18

    def P63(self, *option):
        if option == ():
            response = 'You take Eren’s other hand and ask him to calm down.\n\n\
“Hey, that’s dangerous!” the soldiers are yelling. “Get away from him, trainee!” But you, instead, call out to Eren.\n\n\
Maybe it’s the presence of a familiar classmate, the fact that he finally has an ally, but Eren starts to grow calmer. Once the soldiers realize he’s not going to do any harm, they relax, too.\n\n\
“Good work! Eren, don’t move! Let me see your arm!” Only Hange seems downright excited by this turn of events, and spends the next hour studying and experimenting on the arm until it finally vanishes.\n\n'
            if self.state.flags.hange_hand == False:
                response += '**Your Affinity with Hange has increased by 1!**\n\n'
                self.state.affinities.hange += 1
                self.state.flags.hange_hand = True
            response += 'Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 80

    def P64(self, *option):
        if option == ():
            response = 'You discover some old graffiti on the wall of the building. It’s faded in places, but from what you can make out, it says:\n\n\
*Levi’s the best		Survey Corps is the worst		-lan & Isa-*\n\n\
Maybe it was left by some member of the Survey Corps long ago. It looks like Levi was a valued comrade even then.\n\n\
(There’s no special meaning to this graffiti, but the fact that you found it shows your gift for careful observation, which could lead to you discovering other information in the future. That could be useful.)\n\n\
**From this point on, if you see the words "take a close look", copy and paste those words into the chat to reveal an additional option you may take.**\n\n\
Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 11

    def P65(self, *option):
        if option == ():
            response = 'When you say this, it starts a buzz among your comrades.\n\n\
“When you put it that way- so would I!”\n\n\
“I remember Annie and Mikasa being paired up once during training. It was a sight to see!”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 69

    def P66(self, *option):
        if option == ():
            response = '“The same reason as Eren? What, do you think we have matching rings or something?”\n\n\
Annie shrugs. She doesn’t smile. You’ve never seen Eren with a ring. So why did you think they were related?\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 61

    def P67(self, *option):
        if option == ():
            response = 'That isn’t the only strange thing to happen that day.\n\n\
The experiment is called off, and Eren joins Captain Levi and the others at an outdoor table for a break. Without warning,, there’s a rumbling noise and a cloud of steam. \
Suddenly Eren, who was seated innocently at the table, has a Titan’s arm!\n\n\
The four members of Squad Levi have their weapons drawn almost instantly and begin flinging questions at Eren.\n\n\
“Why did you transform into a Titan without permission? Answer me!”\n\n\
“Move that arm an inch- just an inch- and I’ll cut your damn head off!”\n\n\
Eren himself isn’t sanguine about the situation; he groans in distress.\n\n\
“Shut up and leave me alone for a minute!” he exclaims, but this only agitates the people around him. He begins trying to pull his own arm out of the Titan arm.\n\n\
Squad Leader Hange is excited: “Let me examine that arm!”\n\n\
And in the midst of all this confusion…\n\n\
“Calm down, all of you.” Captain Levi alone sounds control of himself. He inserts himself between Eren and his squad.\n\n\
With everything going on, what choice do you make?\n\n\
1️⃣ Help Eren pull his arm out\n\n\
2️⃣ Try to calm Eren down and get him to stop moving\n\n\
3️⃣ Join Levi in trying to stop the Special Operations Squad'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 47
        elif option[0] == 2:
            self.cur_page[0] = 63
        elif option[0] == 3:
            self.cur_page[0] = 60

    def P68(self, *option):
        if option == ():
            response = 'Mikasa is discussing something with several of her classmates and comrades.\n\n\
“...That shorty is full of himself. One of these days, I’ll take him down a peg…” Mikasa mutters, her face terrifying.\n\n\
This sets the others chattering. “Shorty? Does she mean Levi…?”\n\n\
“That’s some way to talk about the guy they call humanity’s strongest soldier. Mikasa’s something else. Looks like she’s pretty ticked…”\n\n\
Mikasa looks at you, her eyes dangerous.\n\n\
“What do you think?”\n\n\
How do you answer?\n\n\
1️⃣ “You mean what happened at the military tribunal? It was necessary.”\n\n\
2️⃣ “You’d only put yourself in danger pulling something like that. I wish you wouldn’t.”\n\n\
3️⃣ “You versus humanity’s strongest soldier? Now that I’d like to see.”'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 30
        elif option[0] == 2:
            self.cur_page[0] = 26
        elif option[0] == 3:
            self.cur_page[0] = 65

    def P69(self, *option):
        if option == ():
            response = 'The source of Mikasa’s anger is the military tribunal that happened several days ago- Eren’s interrogation. Your friends here have told you what happened.\n\n\
There was hostility toward Eren from the start, but when someone testified that after turning into a Titan during the Battle of Trost, Eren had attacked Mikasa, \
the hostility intensified, becoming a concern that he was a danger to the human race. Mikasa tried to stand up for Eren, but it only led some people to speculate that she herself was a spy for the Titans.\n\n\
You find this ridiculous. Why would Eren attack Mikasa if she were a Titan spy? The mood in the room was so tense that even such basic lapses of logic were being ignored, \
which was not going to benefit Eren in the least.\n\n\
The Military Police Brigade was among the first to suggest that Eren should be executed and an autopsy performed. Eren being Eren, he yelled something like, \
“Just shut your mouths and invest everything in me!” Which, of course, didn’t help matters any.\n\n\
It was then (you’re told) that Captain Levi began kicking Eren mercilessly. Even those who had been calling for execution found a modicum of pity in their hearts at the scene, and so the wrath abated.\n\n\
Commander Erwin took the opportunity to suggest that Eren be given custody of the Survey Corps, and his suggestion was accepted.\n\n\
No one is sure whether Levi’s burst of violence was an act arranged with Eren ahead of time, or a decision he made on the spot. \
Mikasa looks likely to hold a grudge about it forever- but it was thanks to that brutality that Eren is still alive.\n\n\
Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 18

    def P70(self, *option):
        if option == ():
            response = 'You think back to what happened here. Could this place hold the secret key to Eren’s transformations into a Titan?\n\n\
Forget it. You’re no specialist; your thinking about it won’t do any good. What’s more important is that right now, Eren is able to transform of his own volition.\n\n\
Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 11

    def P71(self, *option):
        if option == ():
            response = 'Annie proceeds to land a flurry of kicks on you, finishing with a sweep that takes your legs out from under you and sends you sprawling on the ground.\n\n\
Her fighting technique is astonishing. You had no hope of winning.\n\n\
“Looks like you’re not going to challenge me anything soon. Points for effort, though,” Annie says with the slightest hint of a smile. “Feel free to ask for another lesson sometime.”\n\n'
            if self.state.flags.annie_training == False:
                response += '**Your Affinity with Annie has increased by 1!**\n\n'
                self.state.affinities.annie += 1
                self.state.flags.annie_training = True
            response += 'If you challenge Annie again, type 1️⃣.\n\n\
If you’ve had enough, type 2️⃣ to choose a new destination.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 44
        elif option[0] == 2:
            self.cur_page[0] = 18

    def P72(self, *option):
        if option == ():
            response = 'That night, you go missing. Later, your body is found somewhere well outside Trost District, still wearing your Vertical Maneuvering Equipment.\n\n\
The powers that be decide you were the one who murdered Sonny and Bean. Fearing discovery when the investigations began, you fled, \
but you made a mistake while trying to use your Vertical Maneuvering Equipment at night, and died as a result.\n\n\
The Military Police Brigade issues its report to this effect, and the case is closed.\n\n\
**You have died. To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P73(self, *option):
        if option == ():
            response = 'Squad Leader Hange Zoe is visiting the old Survey Corps headquarters.\n\n\
Hange is not a member of the Special Operations Squad, but is the premier Titan specialist in the unit. \
The squad leader seems to be making frequent trips between Trost District army headquarters and this place in order to observe and study Eren.\n\n\
“Oh! You’re one of Eren’s fellow trainees!” Hange exclaims upon seeing you, looking happy. Is this how the squad leader always acts…? \
“After all you’ve been through…. Have you developed an interest in the Titans, too? Anything you want to ask.”\n\n\
You…\n\n\
1️⃣ Have something to ask\n\n\
2️⃣ Hold back (Choose a new destination)'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 42
        elif option[0] == 2:
            self.cur_page[0] = 11

    def P74(self, *option):
        if option == ():
            response = 'Your equipment is examined, but it shows no sign of having been used, and you are cleared of suspicion. As are Armin, Connie, and Annie.\n\n\
Still, something nags at you.\n\n\
You’re released after the conclusion of the investigation. That’s when Armin comes up to you.\n\n\
“You noticed it too, didn’t you? The Vertical Maneuvering Equipment Annie presented during the investigation… That wasn’t her own gear. \
That belonged to Marco, who died at Trost.” He goes on: “I’m not sure I can believe it myself, but…”\n\n\
You…\n\n\
1️⃣ Go after Annie!\n\n\
2️⃣ Think Armin must be mistaken\n\n\
3️⃣ Keep this revelation secret'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 48
        elif option[0] == 2:
            self.cur_page[0] = 15
        elif option[0] == 3:
            self.cur_page[0] = 77

    def P75(self, *option):
        if option == ():
            response = 'You talk. You tell her how when the army headquarters building was surrounded by Titans and escape seemed impossible, some of your comrades shot themselves to death. \
They figured it was better than being eaten…\n\n\
“Yeah,” Annie says, “it’s a sad story. And I’m just like them. I sure as hell don’t want to be eaten by some Titan. If there’s ever a time when I have no other choice, I’ll use this. Truth is, I’m a coward.”\n\n\
For some reason, she looks almost relieved. You accept it and leave.\n\n\
**You obtain Key Number R, the secret of the ring. Write down or remember the number 40.**\n\n\
Type 1️⃣ to choose a new destination.'
            self.state.flags.keyR = 'Yes'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 18

    def P76(self, *option):
        if option == ():
            response = 'You take Annie at her word. But that night, something occurs to you. When did Annie get so philosophical? \
For that matter, when did she get her hands on Marco’s Vertical Maneuvering Equipment? If she found it on the battlefield, she should’ve given it back to the unit. \
It would be very strange if she had secretly kept it, anticipating everything that had just happened…\n\n\
You realize there’s someone behind you in the darkness, but at the same instant, you take a sharp blow to the head and lose consciousness.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 72

    def P77(self, *option):
        if option == ():
            response = '“I think that’s a good idea,” Armin nods. “I might just be imagining things… In fact, I hope I am.”\n\n\
You take what you know and store it away in your heart.\n\n\
**Your Affinity with Armin has increased by 1!**\n\n\
**You obtain Key Number A. It represents the secret you share with Armin. Write down the number 77, or commit it to memory.**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.armin += 1
            self.state.flags.keyA = 'Yes'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 95

    def P78(self, *option):
        if option == ():
            response = 'Armin is discussing with several of your classmates and comrades. He appears to be talking about the time Eren turned into a Titan. \
The subject is of great interest, and his audience is rapt. Annie is there, too. She listens without evident interest.\n\n\
If you listen, too, type 1️⃣.\n\n\
Otherwise, type 2️⃣ to choose a new destination.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 9
        elif option[0] == 2:
            self.cur_page[0] = 18

    def P79(self, *option):
        if option == ():
            response = 'The gleam in Annie’s eye grows more and more dangerous.\n\n\
“What are you talking about? I’m not that type. And when I want to liven things up, I use my fists. This is just… Well, sometimes it’s helpful to have a blade around.”\n\n\
This makes sense to you. You give her the ring and leave.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 61

    def P80(self, *option):
        if option == ():
            response = 'Ultimately, the reason for this incident remains mysterious, even to Eren himself.\n\n\
Hange, after inspection of the bones left behind by the Titan arm, hypothesizes that when he attempted to pick up the spoon, Eren unconsciously turned just a part of himself into a Titan. \
In other words, pain isn’t the only factor; he may be able to transform when he has some sort of goal.\n\n\
Once they understand what happened, the members of Squad Levi apologize to Eren. You hear that they each bite their own hands hard enough to leave a scar. \
The soldiers weren’t wrong; they were simply loyal to their duty. Eren is quite apologetic himself.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 70

    def P81(self, *option):
        if option == ():
            response = '“Ahh! My dear trainee! So you’re interested in Titans, too?” Hange’s face splits into a grin. “It’s true; this isn’t the first time we’ve succeeded in capturing Titans. \
According to the Survey Corps’ records, the first Titans to be taken alive were-” Hange is off and running. You immediately regret saying anything, but you can’t stop the squad leader-cum-professor now.\n\n\
Hange talks to you passionately for the better part of half an hour.\n\n\
“-and so, this is the first time we’ve had a chance to observe and experiment on Titans in such a controlled environment. Two of them, no less! Do you understand how fantastic this is?”\n\n\
You nod. Just as you think the lecture is almost over, Hange’s voice rises again.\n\n\
“On to the main point, then. Thanks to our delightful friends Sonny and Bean, we’ve managed to learn-”\n\n\
So all that talk was just preamble.\n\n\
You spend a very long time learning about Titans.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 29

    def P82(self, *option):
        if option == ():
            response = 'All that’s left of the 2 Titans is their erstwhile restraints. Those, and something that looks like bones, along with a mark on the ground. \
Like other Titans, the corpses wasted away immediately after death. The vestiges that remain suggest the Titans died rather than fled.\n\n\
“Sonny! Bean!” Hange is calling their names and weeping piteously. You would think the squad leader had lost a pair of beloved children.\n\n\
The area is crawling with soldiers.\n\n\
“Is it true they were killed?”\n\n\
“Yeah. This wasn’t a natural death. The guard said he heard the sound of Vertical Maneuvering Equipment, but the killer was already gone when he got there.”\n\n\
“Vertical Maneuvering Equipment? So the culprit was with the army?”\n\n\
“Who else would know how to kill a Titan?”\n\n\
“Good point. I’ll bet this guy had at least a couple of accomplices, too.”\n\n\
“Oh yeah? What makes you say that?”\n\n\
“You said the killers were already gone when the guard got there, right? No way 1 person could off 2 Titans that fast.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 83

    def P83(self, *option):
        if option == ():
            response = 'The scene of the crime is packed with people. Suddenly, you notice Captain Levi and Eren are there, too. Eren takes in his surroundings with a look of shock.\n\n\
Someone approaches. It’s Commander Erwin Smith, the man with ultimate responsibility for the Survey Corps. Is what’s going on here so important that the commander himself has come to see it?\n\n\
You overhear what Erwin says as he walks up to Eren: “What can you see? Who do you think our enemy is?”\n\n\
You…\n\n\
1️⃣ Think about what his words might mean\n\n\
2️⃣ Don’t understand what he’s saying, or decide it has nothing to do with you'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 88
        elif option[0] == 2:
            self.cur_page[0] = 93

    def P84(self, *option):
        if option == ():
            response = 'Your equipment is investigated, but (naturally) it shows no sign of having been used, and you are cleared of doubt.\n\n\
The Vertical Maneuvering Equipment of your other comrades, Armin, Annie, and Connie, is similarly clean. Apparently the killer isn’t among you.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 95

    def P85(self, *option):
        if option == ():
            response = 'There’s Krista. She’s with Ymir, the freckled girl who’s often by her side. Krista is a sweet young woman who shows kindness to everyone, making her very popular. \
Ymir, on the other hand, is sharp-tongued and ruthless. The two of them couldn’t be more different, yet they’ve been close since basic. They’re talking about something. \
It sounds like they’re discussing their futures, which they’ll have to decide soon.\n\n\
“I… I think I’ll join the Survey Corps,” Krista says. “To help everyone.” She’s one of the top scorers in your class and could join the Military Police Brigade, \
but maybe her experiences in Trost have changed her mind.\n\n\
“You sure? You’re shaking awful hard as you say that,” Ymir says with a shrug. “If you’re doing it for others’ sake, then don’t.”\n\n\
Ymir can be rather rough, but she seems concerned about Krista. She notices you watching them. “What are you looking at?” she asks.\n\n\
Type 1️⃣ to choose a new destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 18

    def P86(self, *option):
        if option == ():
            response = 'Annie dodges quickly, then throws you.\n\n\
“When you just try to fire off your strongest punch, your movements get broader. You leave yourself open.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 71

    def P87(self, *option):
        if option == ():
            response = '“Captain Levi is amazing,” Petra says. “He’s personally selected us- it’s an honor.”\n\n\
The other three nod. You can tell how much they trust and respect Captain Levi. He impresses even these experienced soldiers.\n\n\
“I’m going to give everything I’ve got to completing this mission,” Gunther says.\n\n\
“Me, too,” adds Eld.\n\n\
The “mission” in question is protecting Eren. But when you say as much, the others act strangely uneasy.\n\n\
“R-Right,” says Petra. “We’re going to look after your friend, of course we are.”\n\n\
“Yeah,” says Eld. “I mean… Eren’s got it rough, too.”\n\n\
From the way they’re talking, you realize that yes, they are protecting Eren, but at the same time, they’re keeping watch on him so that they can respond if and when necessary. \
You see that each of the four soldiers has bite marks on their hand. There’s a lot going on with Eren.\n\n\
Finally, the talk turns to Squad Leader Hange Zoe. Everyone seems to share a tacit understanding about this person.\n\n\
“The squad leader is very… passionate about Titan research.”\n\n\
“Just… try to avoid telling Hange that you want to learn about Titans or anything. Trust us.”\n\n\
Such is their advice to you.\n\n\
If, now that you think about it, you’re bothered by the way Oluo spoke to you, type 1️⃣.\n\n\
If you don’t mind, type 2️⃣ to choose a new destination.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 32
        elif option[0] == 2:
            self.cur_page[0] = 11

    def P88(self, *option):
        if option == ():
            response = 'You take in the scene and think over what you’ve heard.\n\n\
The two Titans have been killed; that much is obvious. Whether or not there were two or more killers isn’t certain.\n\n\
The murder of both Titans in such a short period of time suggests the possibility, but it could also be the worst of a single, extraordinarily talented individual.\n\n\
The fact that both Titans were killed probably means something. For example, maybe someone wanted to stop the Survey Corps from experimenting any further… \
If it was done out of sympathy, they could’ve just killed one of them and then beat feet.\n\n\
**Look at the previous 3 passages, including this one. How many times is the word "Titan" or "Titans" mentioned?**\n\n\
1️⃣ 5\n\n\
2️⃣ 6\n\n\
3️⃣ 7\n\n\
4️⃣ 8'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 93
        elif option[0] == 2:
            self.cur_page[0] = 93
        elif option[0] == 3:
            self.cur_page[0] = 93
        elif option[0] == 4:
            self.cur_page[0] = 8801

    def P8801(self, *option):
        if option == ():
            response = '“It looks like you’ve worked something out.”\n\n\
The voice startles you. Commander Erwin is talking to you.\n\n\
You hurriedly tell him what you’ve been thinking. Maybe it will help somehow.\n\n\
“Hmm,” the commander says, an odd expression on his face. It doesn’t seem like you’ve given him the answer he was looking for. \
But he says, “So you considered what was going on here and figured the numbers had significance. Not a bad thought. I hope you’ll remember this lesson. What’s your name?”\n\n\
You tell him, and he nods.\n\n\
“I’ll remember it.”\n\n\
You might not have given him the answer he expected, but you’ve proven yourself worthy of a spot in his memory.\n\n\
Suddenly, you realize Captain Levi is looking at you. He’s as expressionless as ever, but he seems to have heard everything. \
(You seem to have gotten Levi’s attention as well.)\n\n\
**Your Affinity with Levi has increased by 1!**\n\n\
**From this point on, if you see the words "become exceptional soldiers", copy and paste those words into the chat to reveal an additional option you may take.**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.levi += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 94

    def P89(self, *option):
        if option == ():
            response = 'You take the ring back to Annie. “Thanks,” she says, but there’s a hard edge to the look she gives you. She accepts the ring and glances at you. \
She seems to have figured out that you know its little secret.\n\n\
“Why do you think I carry this?”\n\n\
What do you say?\n\n\
1️⃣ “For protection?”\n\n\
2️⃣ “To use it on yourself?”\n\n\
3️⃣ “For the same reason Eren does?”'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 35
        elif option[0] == 2:
            self.cur_page[0] = 46
        elif option[0] == 3:
            self.cur_page[0] = 66

    def P90(self, *option):
        if option == ():
            response = 'You follow Annie to a deserted corner.\n\n\
She looks down and says softly, “I wanted to take revenge for my comrades. Marco was killed by the Titans, so I used his Vertical Maneuvering Equipment to get back at them. \
Any chance you could keep it to yourself? I’ll turn myself in to headquarters when the time is right.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 76

    def P92(self, *option):
        if option == ():
            response = 'It is decided that all military personnel in the building will submit their Vertical Maneuvering Equipment to be inspected for signs of use. \
You trainees are among those gathered in the main hall. You set your equipment on a table, and one by one the units are inspected. \
As you stand at attention waiting for your turns, some of your comrades begin to whisper to each other.\n\n\
“Who knew they’d punish you for killing a Titan.”\n\n\
“No way there’s a criminal among us… I’m totally wiped from cleaning up the battlefield all day…”\n\n\
You just stand there, listening. Armin, Connie, and Annie are all standing nearby. They, too, are conversing quietly. \
Connie seems to be worried about which unit he should join, and he’s talking to Armin and Annie about it. \
Come to think of it, both Connie and Annie scored well enough that they could join the Military Police Brigade.\n\n\
“Maybe I should join the Survey Corps,” he mutters, but immediately says, “Hey, Annie… You think the Military Police Brigade would be better?”\n\n\
“If somebody told you to die, would you?” Annie says bluntly. “Then you should do what you want to do.”\n\n\
“Annie, you’re actually pretty nice,” says Armin. “It seems like you don’t want us to join the Survey Corps… and I bet you have a reason for joining the Military Police.” \
He keeps his eyes fixed on the table as he speaks.\n\n\
“I just… want to save myself,” Annie mutters.\n\n\
Can you take their conversation at face value? Or is there some deeper meaning…?\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 84
        elif option[0] == 's':
            self.cur_page[0] = 74

    def P93(self, *option):
        if option == ():
            response = '“Come again?” Eren looks perplexed. It seems he didn’t understand what Commander Erwin said. It makes no sense to you, either. Captain Levi is standing nearby- did he understand?\n\n\
“Sorry,” Erwin says after a moment. “I didn’t mean to ask such a strange question.”\n\n\
Then he disappears into the crowd.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 94

    def P94(self, *option):
        if option == ():
            response = 'You’re curious about what Commander Erwin meant, but you don’t have time to think about it because Trost District army headquarters is soon in an uproar.\n\n\
The culprit is believed to be a soldier, so everyone who has been in or out of headquarters recently is a suspect. That includes the 104th Training Corps- and you. \
It doesn’t matter if you were somewhere else that night. You might have lent some equipment to one of the conspirators.\n\n\
Eren, who has been under lock and key and without his equipment in another location entirely, is the only one who doesn’t seem to be under suspicion…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 92

    def P95(self, *option):
        if option == ():
            response = 'The inspection ends. It seems no one’s Vertical Maneuvering Equipment shows signs of having been used.\n\n\
Some say, “I knew it had to be an outside job. No way any of us is a criminal.” But there are others who whisper that the killer must have had some clever way of deceiving the inspectors.\n\n\
Days pass, and the criminal isn’t found. You and the others finish your assigned duty of cleaning up from the Battle of Trost. \
The Survey Corps, which had borrowed this facility in order to experiment on the Titans, gives it back to its rightful owners, the Trost Guard Unit of the Garrison, and withdraws. \
With their “subjects” murdered, there’s no more reason for them to be here.\n\n\
As for you and the other members of the 104th Training Corps, you continue working your way through the red tape required to become full soldiers. \
The day when you decide what path you’ll take- which was supposed to be the very day that became the Battle of Trost- finally arrives.\n\n\
You hear that Commander Erwin of the Survey Corps, which is currently sharing the headquarters building with you, will be giving a speech to solicit new members. \
At the commander’s request, all members of the 104th Training Corps are required to attend, but which path you take remains your free choice.\n\n\
More than a few of your comrades want to join the Survey Corps, and plenty more saw the unit in action during the Battle of Trost. Nobody objects to hearing what Commander Erwin has to say.\n\n\
You line up in front of the stage with the rest of your classmates and listen.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 96

    def P96(self, *option):
        if option == ():
            response = '“I’m Commander Erwin Smith of the Survey Corps. You’re standing in the spot where my unit received its commission from the king.”\n\n\
This is all the preamble he offers; he moves immediately into his main subject.\n\n\
“In the recent Titan attack, everyone here experienced what the average excursion outside is like. As a result, I’m sure you’ve come to know your own limits, and the terror of the Titans. However.” \
His voice rises. “Despite all the people we lost in that attack, humanity was able to seize a victory such as we have never known. And Eren Yeager holds the key.”\n\n\
Erwin goes on to talk about Eren’s achievements, and to suggest that he may be able to make clear the true nature of the Titans. \
He also tells you that the secret of the Titans is hidden in the basement of Eren’s birth home.\n\n\
“If we can retake Wall Maria and just get to that basement, we may be able to escape from these 100 years of domination by the Titans.”\n\n\
This starts everyone chattering. You’ve never heard anything like this before.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 9601

    def P9601(self, *option):
        if option == ():
            response = '“But,” Commander Erwin goes on, “it will be necessary to retake Wall Maria for this to work. With the gates of Trost District no longer usable, \
we’ll need to find an alternate route. Over the past 4 fruitless years, casualties in the Survey Corps have been very high, with 9 out of 10 dead. \
Converservatively, to send a major unit to Wall Maria would require 5 times that long.”\n\n\
Everyone starts talking again.\n\n\
“The Survey Corps is perennially short on personnel. We need new members. I won’t try to hide it: if you join our unit, you will be asked to participate in our expedition beyond the walls 1 month from now. \
5 in 10 new recruits die on their first expedition. Those who survive, however, become exceptional soldiers with a high survival rate.”\n\n\
Finally, the commander says, “That’s all I have to say. Most of those who join the Survey Corps will die. If, knowing that, you still want to be part of our unit, then please remain here.”\n\n\
Which unit do you join?\n\n\
1️⃣ The Survey Corps\n\n\
2️⃣ The Garrison\n\n\
3️⃣ The Military Police Brigade'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 97
        elif option[0] == 2:
            self.cur_page[0] = 140
        elif option[0] == 3:
            self.cur_page[0] = 163
        elif option[0] == 's':
            self.cur_page[0] = 144

    def P97(self, *option):
        if option == ():
            response = 'After everything Commander Erwin had said, most of the unit leaves. Many of them had already decided to join some other branch of service. You see Annie among them. \
She must have settled on the Military Police Brigade.\n\n\
You’re sure there were more people than this who wanted to join the Survey Corps… But the commander’s vivid and upsetting speech seems to have scared them off. \
Then again, there are those who have chosen to remain, speech or no speech. Some are trying not to let their teeth chatter, while others appear to be crying. You are among those who stay.\n\n\
Commander Erwin looks down from his platform at the few who remain.\n\n\
“If you were told to die, could you do it?” he asks you.\n\n\
“I don’t wanna die!” somebody wails.\n\n\
“I see…” The commander nods, apparently satisfied. “I like the look of each of you. I welcome you as new members of the Survey Corps!”\n\n\
He salutes you, placing his right hand on his chest- symbolizing how soldiers offer up their very hearts. You all salute him in return,\n\n\
“You have withstood your fear well… You’re all brave soldiers.”\n\n\
Including yourself, 21 people remain to become members of the Survey Corps. You’re provided with new uniforms. You remove your familiar trainee outfit and replace it with one bearing the Wings of Freedom.”\n\n\
You and your comrades are now members of the Survey Corps.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 98

    def P98(self, *option):
        if option == ():
            response = 'And so, after a month of training…\n\n\
The day finally comes for the Survey Corps to make its next expedition beyond the walls, with its newly minted members from the 104th Training Corps in tow.\n\n\
Karanes District is to be your staging area. It’s furthest to the east, one of the cities established at the four cardinal compass points along Wall Rose.\n\n\
The place looks a lot like Trost District. A huge gate, topped by fixed gun emplacements, separates what’s behind the wall from what’s beyond it. \
The guns occasionally fire in the direction fire in the direction of whatever is out there. They’re clearing away Titans in the area around the gate so the expedition can leave.\n\n\
Those of you comprising the expedition are already lined up at the gate, all of you waiting on horseback, the cannon fire ringing overhead.\n\n\
You’ve never been on an expedition outside the walls before, but this seems like an awfully large group.\n\n\
You remember Commander Erwin explaining earlier: “One of our objectives on this mission is to get all of our new recruits, Eren Yeager included, some real-life experience. \
For that reason, we plan a relatively brief expedition this time. Additional goals include some exploratory scouting and a delivery to our resource dump. \
This will further the Survey Corps’ long-standing mission to secure a route into Wall Maria.”\n\n\
You take another look at the group participating in this expedition. You still think it looks like a lot of people for a short trip. The baggage train alone is considerable. \
No doubt much of it is intended for the resource dump.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 9801

    def P9801(self, *option):
        if option == ():
            response = 'Although the commander didn’t mention it, you suspect part of this expedition is about making sure Eren has some success in battle. \
If Eren, the human soldier who can transform into a Titan, were able to achieve great things outside the walls, it would prove that he carried the hope of humanity- \
and that would silence the Military Police Brigade and his other critics.\n\n\
But for now, it’s the cannons that go quiet. A voice comes from beyond the wall, the signal that everything is ready.\n\n\
“Open the gate!” \n\n\
With a tremendous creaking and shuddering, the gate of Karanes District slowly begins to open.\n\n\
“It’s almost time! We’re going to take another step forward for humanity!” The Survey Corps leaders shout to you. “Show us the fruits of your training!”\n\n\
You and all your fellow participants in this expedition have been waiting in formation on horseback just inside the gate. Now you raise a great noise.\n\n\
“The 57th expedition beyond the walls shall now begin! All troops, move out!”\n\n\
The moment the gate opens wide enough to permit passage, the entire unit surges forth as one.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 99

    def P99(self, *option):
        if option == ():
            response = 'Outside the gate, you find the old city spread out before you. Humans used to live here- until five years ago, when the Titans destroyed Wall Maria.\n\n\
Now it’s a ghost town beset by wandering Titans. The expeditionary force moves through it in a pack. There’s a great clatter of hooves as dozens of horses ride through the empty streets.\n\n\
Suddenly, a Titan appears from the shadow of a building.\n\n\
“Left-front! Ten-meter approaching!”\n\n\
The preemptive cannon barrages never clear away all the Titans, and anyway, where humans gather, so will Titans.\n\n\
Soldiers with Vertical Maneuvering Equipment respond. They came down into the city ahead of the rest of you to help keep the expedition safe and support you as extra muscle. \
Instantaneously, a life-and-death struggle between humans and Titans break out in the city.\n\n\
Voices fly back and forth.\n\n\
“Protect the column with your lives!”\n\n\
“Stay calm! Let the support unit do its job- keep marching!”\n\n\
With people and horses and baggage carts packed so close together, a wayward strike from a Titan could be disastrous. Getting through the city as fast as possible is your first test.\n\n\
You draw on everything that was pounded into you over a month of training.\n\n\
“Forward!”\n\n\
“Keep going!”\n\n\
You run as hard as you can- and then you’re out of the city. Ahead of you lies wasteland.\n\n\
Someone shouts an order: “Form up in long-distance enemy-scouting formation!”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 9901

    def P9901(self, *option):
        if option == ():
            response = 'The expeditionary unit, which had been marching in single file, breaks up into predetermined squads and spreads out across the vast area.\n\n\
Long-distance enemy-scouting formation is an arrangement supposedly promulgated by Commander Erwin, and it takes up a great deal of space. \
The various squadrons, marching at specified intervals, communicate via colored smoke signal and messengers on horseback, in order to quickly alert the rest of the formation if they encounter a Titan.\n\n\
Whatever an enemy appears, a swift response is possible, allowing the unit as a whole to evade danger. The adoption of this formation precipitated a dramatic jump in the survival rate among the Survey Corps.\n\n\
You new recruits spent the last month in intensive training in order to be a part of this.\n\n\
“Listen up, recruit,” one of the more experienced soldiers once told you. “The Survey Corps is in the business of figuring out how not to fight Titans.”\n\n\
You once believed that the Survey Corps were elite soldiers who went toe-to-toe with the Titans- but it turns out to be the opposite. \
The most important thing on an expedition beyond the walls are your duties to secure a route and do reconnaissance, and then to avoid contact with Titans, \
doing the minimum amount of combat necessary to protect your comrades if you do encounter one. The experienced members of the ranks drill this into you.\n\n\
You learn that the reason the casualty rate in this unit is so high is that sometimes the Titans are simply too big. \
Those who survive to become experts at fighting the Titans do so precisely because of this commitment to the minimum of combat- and nothing more.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 100

    def P100(self, *option):
        if option == ():
            response = 'Where were you stationed within the formation?\n\n\
1️⃣ Center Front [Commander Erwin, Hange]\n\n\
2️⃣ Left Wing Center Column [Sasha, Mikasa, Connie]\n\n\
3️⃣ Right Wing Front [Armin, Ness and Siss]\n\n\
4️⃣ Right Wing Rear [Jean, Reiner]\n\n\
5️⃣ Center Rear [Eren, Levi, Squad Levi]\n\n\
6️⃣ Tail [Krista, Ymir, Bertolt]'
            self.choices[0] = [1,2,3,4,5,6]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 101
        elif option[0] == 2:
            self.cur_page[0] = 122
        elif option[0] == 3:
            self.cur_page[0] = 202
        elif option[0] == 4:
            self.cur_page[0] = 149
        elif option[0] == 5:
            self.cur_page[0] = 105
        elif option[0] == 6:
            self.cur_page[0] = 233

    def P101(self, *option):
        if option == ():
            response = 'You show up at the center front, but there’s no way you belong here. As you might have noticed when you looked at the strategic plan, \
not a single one of your fellow rookies is stationed here. Even among the members of the Survey Corps, only the longest-standing- and longest-lived- are present.\n\n\
Type 1️⃣ to choose a different destination.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 100

    def P102(self, *option):
        if option == ():
            response = 'Running becomes your entire world. Finally, you burst through the trees and into an open area.\n\n\
You look around. You see Jean, on horseback. There are no more Titans nearby. You and the others approach the horse.\n\n\
“Did you see how the old guard looked back there?” Jean asks. “I don’t think even the Survey Corps has ever seen a group of Titans like that before.”\n\n\
You nod. You may be outside the walls, but an attack by such a large number of Titans at once seems unusual.\n\n\
“Heeeey! Are you okay?” a friend calls, riding up. It’s Reiner. Looks like he’s all right. “My squad was attacked by a horde of Titans, too,” he says. “We had to scatter to get away.”\n\n\
It looks like the right wing is in more than a little trouble right now. And you thought this formation was supposed to be exceptionally safe…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 107

    def P103(self, *option):
        if option == ():
            response = 'One of the more experienced soldiers volunteers to carry out instructions. You approach Sasha hesitantly. She looks like she’s going to die.\n\n\
“I’m so hungry…”\n\n\
You…\n\n\
1️⃣ Feel silly for worrying, and leave her alone\n\n\
2️⃣ Give her something to eat'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 137
        elif option[0] == 2:
            self.cur_page[0] = 294

    def P104(self, *option):
        if option == ():
            response = 'A little while later… You hear another strange voice, this time from within the forest. It’s like a scream mixed with an animal cry. \
You’ve never heard anything like it. Is it the voice of a Titan? Krista trembles, terrified.\n\n\
Suddenly, the Titans lose all interest in you; as one, they make for the woods.\n\n\
“What in the world…?” Krista’s teeth are chattering. She looks like she might fall out of the tree. Despite her obvious fear, though, she tries to put on a brave front, saying, \
“Something terrible must have happened there. We have to go help them.”\n\n\
You…\n\n\
1️⃣ Hold Krista close, to protect her\n\n\
2️⃣ Say that you’ll go into the woods yourself'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 272
        elif option[0] == 2:
            self.cur_page[0] = 136

    def P105(self, *option):
        if option == ():
            response = 'You are assigned to the same unit as Eren. Captain Levi and the Special Operations Squad are protecting him. \
This unit is in the center and towards the rear of the formation- by far the most protected spot.\n\n\
Eren’s presence here is a surprise to you. He’s an important person, and his location hasn’t been divulged to the entire expedition.\n\n\
You ride up alongside Eren and Captain Levi. For a time, things are startlingly peaceful. The danger you all faced before assuming this formation seems like a distant memory.\n\n\
Levi and the others are silent. The only sound is the clopping of horses’ hooves.\n\n\
Once in a while, a smoke signal goes up in the distance, or messengers come and go, but on the whole everything is so calm that you would never imagine you were in the Titan-infested lands outside the walls.\n\n\
Then again, maybe it’s precisely because this is the safest part of the formation…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 259

    def P106(self, *option):
        if option == ():
            response = '“If you’re worried about Eren… I’m sure he’ll be fine,” you say.\n\n\
“I know,” Mikasa says, her voice still calm. Her expression doesn’t change.\n\n\
**Your Affinity with Mikasa has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 274

    def P107(self, *option):
        if option == ():
            response = '“Hey, there’s a horse,” Reiner says.\n\n\
The animal is carrying Survey Corps equipment, but it has no rider. Reiner runs up close and grabs the reins. \
“It must have thrown off whoever was riding it,” he says. “They might still be nearby- and alive.”\n\n\
You work your way around the area, looking closely. Some distance away, you spot someone sitting on the ground.\n\n\
It’s Armin.\n\n\
“You okay? Can you stand up, Armin?” Reiner asks, leading the horse over.\n\n\
Happily, Armin appears to be unharmed. He gets back on his horse.\n\n\
You’ve all linked back up. You ride side by side, talking. Armin seems to be alone. What happened to the rest of his unit?\n\n\
“I’m… I’m the only survivor,” he says with a shake of his head. “Ness and all our other senior hands were killed… by that.”\n\n\
You look. Up ahead, you see the back of a Titan who is running along. It has a slim, feminine body… A female Titan.\n\n\
**The Kill Count has increased by 1.**\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.dieter = 'Dead'
            self.state.statuses.lukesiss = 'Dead'
            self.state.flags.killcount += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 148

    def P108(self, *option):
        if option == ():
            response = 'Bertolt and Ymir are assigned to the same place as you.\n\n\
Bertolt seems fidgety, as always. “Bertolt,” Ymir is saying, “you don’t happen to know where my Krista is, do you?”\n\n\
You continue trying to draw off the Titans. Maybe they have some capacity to learn, because they slowly begin to climb the trees.\n\n\
Bertolt had been worried, but it doesn’t look like his abilities with the Vertical Maneuvering Equipment have rusted at all. Ymir, for her part, dodges the Titans flawlessly, looking almost bored.\n\n\
You yourself somehow manage to avoid the Titans- and the mission continues.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 215

    def P109(self, *option):
        if option == ():
            response = 'You charge at the Female Titan’s head. You see her eye open wide in anger.\n\n\
That’s impossible. She couldn’t have healed yet-\n\n\
But even as you think this, you find yourself caught by the Titan’s gaping mouth, and you are devoured. Your last thought before consciousness leaves you is:\n\n\
*I hope my sacrifice contributes to our victory…*\n\n\
**You have died. To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P110(self, *option):
        if option == ():
            response = 'Thanks to the exceptional reconnaissance system this formation represents, you’re able to advance while avoiding any Titans. Once in a while you see a smoke signal go up. \
Your own squad leader sends up a signal in response, and sometimes you all change direction.\n\n\
Suddenly, you see a Titan approaching at a terrific speed. Ten-meter class; an Abnormal.\n\n\
“We’ve got no choice but to engage the Abnormal!” Squad Leader Ness exclaims. “Siss, you take the nape! I’ll keep it pinned!”\n\n\
Working together, Siss and Squad Leader Ness bring their horses up on either side of the Titan. The creature is running strangely, pitched slightly backward. It’s a little more oval-shaped than a human.\n\n\
Squad Leader Ness sets his anchors in the Titan from horseback, then goes into a leap, cutting into its leg. As the Titan loses its balance and starts to fall forward, Siss jumps onto its back, \
cutting into the nape of its neck to destroy it.\n\n\
It’s a perfect tandem attack. Using Vertical Maneuvering Equipment out here on the flat plains, with no buildings to assist, is supposed to be difficult, and yet- well, \
that’s two experienced Titan fighters for you.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 121

    def P111(self, *option):
        if option == ():
            response = 'Suddenly, a Titan appears from the shadow of the abandoned building.\n\n\
“Oh no, there’s one now!” Sasha cries.\n\n\
The Titan must be ten meters tall. It comes at you on all fours, crawling at a stunning speed. The movement is like some sort of insect. Sasha screams and starts fleeing.\n\n\
“The scouts must have missed this enemy!” one of the experienced soldiers yells. “This is not good. Draw it this way!”\n\n\
You…\n\n\
1️⃣ Rush to help Sasha!\n\n\
2️⃣ Help the other soldiers'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 147
        elif option[0] == 2:
            self.cur_page[0] = 301

    def P112(self, *option):
        if option == ():
            response = 'Both of them look back at you.\n\n\
“And just how is that?!” they yell in unison, staring daggers at you.\n\n\
...They’re even more alike than you thought.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 184

    def P113(self, *option):
        if option == ():
            response = 'You try to explain, but it’s hard to have a complicated conversation while flying with vertical maneuvering. \
Not to mention, you find it difficult to explain in simple terms the unbelievable things you just witnessed. \n\n\
“Failed? Under those circumstances? But how?”\n\n\
“What do you mean, a horde of Titans showed up?”\n\n\
Nobody quite seems to accept what you’re saying.\n\n\
You’re slow, but thankful, to notice the figure coming toward you. It’s wearing a Survey Corps cape. The hood is pulled up, so you can’t see its face, but it has to be…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 176

    def P114(self, *option):
        if option == ():
            response = '“Oh, him? I’m sure they’ve got him in the safest place they can find around here. He’s Mr. Titan after all, oh so important.” Ymir says. There’s a bitter edge to her voice.\n\n\
“You don’t have to talk like that,” Krista says. “I think it must be terrible for Eren, carrying that burden.”\n\n\
“He has a strong will of his own,” Bertolt says. “Someone like me just gets ignored by everyone.” He looks at the ground.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 194

    def P115(self, *option):
        if option == ():
            response = 'You send up a smoke signal and wait for a nearby unit to send help.\n\n\
At last, you see someone approaching with extra horses. It’s Krista, a girl from your training squadron. “Are you okay? I found some lost horses… And then I saw your smoke signal.”\n\n\
You’re saved, thanks to Krista. Squad Leader Ness, along with Siss, both cheer.\n\n\
“We’re saved!”\n\n\
“This girl is like a goddess!”\n\n\
Krista has brought Ness’s horse, along with the others that fled. You’re all on horseback again.\n\n\
All around you, you see smoke signaling the presence of Titans go up.\n\n\
“We’re going to go reinforce the units that are being attacked,” Ness and Siss say to you and Armin. “You new kids, head for the center of the formation and tell them about the Female Titan.”\n\n\
“I’m going back to my assigned unit,” Krista says. “Ymir will be worried.” Then she leaves.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 227

    def P117(self, *option):
        if option == ():
            response = 'You head off for the neighboring squadron with your message and inform the squad leader about the events with the crawling Titan.\n\n\
“Understood. Link up with my squadron; we’ll work together!” he says.\n\n\
Mikasa and Connie are in this unit.\n\n\
“How’s it going with your squad?” Connie calls out. You tell them briefly about what happened.\n\n\
Then, you…\n\n\
1️⃣ Ask them about Sasha\n\n\
2️⃣ Ask them about Eren'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 225
        elif option[0] == 2:
            self.cur_page[0] = 212

    def P118(self, *option):
        if option == ():
            response = 'Jean is there, cheering. Armin and Reiner are with him.\n\n\
“You saved our necks,” Jean says. “Armin’s horse got done in. We were just talking about which of us would have to stay behind.”\n\n\
“Thank goodness we made it,” Krista says, tears in her eyes.\n\n\
You, too, are glad to see her rewarded this way.\n\n\
Jean, Armin, and Reiner look at Krista as though beholding a goddess.\n\n\
You wouldn’t mind reminding them that you helped in this rescue, too… But, well, she really is divine.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 157

    def P119(self, *option):
        if option == ():
            response = 'You jump at her as well, attempting to restrain her.\n\n'
            if self.state.flags.keyR == 'Yes':
                response += 'You have Key Number R! What was the number corresponding to this key?\n\n\
1️⃣ 40\n\n\
2️⃣ 77\n\n\
3️⃣ 100\n\n\
4️⃣ 251'
                self.choices[0] = [1,2,3,4]
            else:
                response += 'Type 1️⃣ to continue.'
                self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.flags.keyR == 'Yes':
                self.cur_page[0] = 159
            else:
                self.cur_page[0] = 142
        elif option[0] == 2:
            self.cur_page[0] = 142
        elif option[0] == 3:
            self.cur_page[0] = 142
        elif option[0] == 4:
            self.cur_page[0] = 142

    def P120(self, *option):
        if option == ():
            response = 'You’re the only hope!\n\n\
Determined, you slice at the Female Titan. You don’t have to be victorious. You just have to buy some time.\n\n\
Even while trying to climb the wall, the Female Titan is a powerful opponent. She lashes out with one hand, attacking despite her unstable position. \
You try to strike at her eye; she opens her mouth and attempts to eat you.\n\n\
You respond with vertical maneuvering, but she grabs your wire and slams you against the wall.\n\n\
You feel your consciousness growing faint. But just at that moment, you spot other soldiers launching themselves at the Female Titan. Your comrades haven’t wasted the precious time you gained them.\n\n\
Under the assault of several soldiers using vertical maneuvering, the Female Titan finally falls.\n\n'
            self.choices[0] = [1]
            response += 'Your actions were admirable. Choose a character to increase your Affinity with:\n\n\
1️⃣ Eren\n\n'
            if self.state.statuses.mikasa == 'Alive':
                self.choices[0].append(2)
                response += '2️⃣ Mikasa\n\n'
            if self.state.statuses.armin == 'Alive':
                self.choices[0].append(3)
                response += '3️⃣ Armin\n\n'
            response += '4️⃣ Jean\n\n\
5️⃣ Krista\n\n\
6️⃣ Sasha\n\n\
7️⃣ Hange\n\n\
8️⃣ Levi'
            self.choices[0].extend([4,5,6,7,8])
            return response
        elif option[0] == 1:
            self.state.affinities.eren += 1
            self.cur_page[0] = 322
        elif option[0] == 2:
            self.state.affinities.mikasa += 1
            self.cur_page[0] = 322
        elif option[0] == 3:
            self.state.affinities.armin += 1
            self.cur_page[0] = 322
        elif option[0] == 4:
            self.state.affinities.jean += 1
            self.cur_page[0] = 322
        elif option[0] == 5:
            self.state.affinities.krista += 1
            self.cur_page[0] = 322
        elif option[0] == 6:
            self.state.affinities.sasha += 1
            self.cur_page[0] = 322
        elif option[0] == 7:
            self.state.affinities.hange += 1
            self.cur_page[0] = 322
        elif option[0] == 8:
            self.state.affinities.levi += 1
            self.cur_page[0] = 322

    def P121(self, *option):
        if option == ():
            response = 'Another new Titan appears in the distance. You can hear its footsteps pounding as it dashes toward you. Another Abnormal? The Titan bends forward as it runs, its form excellent. \
It looks like it’s over ten meters.\n\n\
“Another one?” Ness says. “Siss, here we go again.” Then he turns to you and Armin. “You rookies, go on ahead. Send up a smoke signal.”\n\n\
You don’t like the way this feels. The Titan running at you isn’t ovoid, but very much humanoid. That in itself is strange for a Titan. Its body looks like that of a slim young woman.\n\n\
You…\n\n\
1️⃣ Do as Ness tells you\n\n\
2️⃣ Will fight the Titan, too!\n\n\
3️⃣ Urge Ness not to fight'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 252
        elif option[0] == 2:
            self.cur_page[0] = 315
        elif option[0] == 3:
            self.cur_page[0] = 200

    def P122(self, *option):
        if option == ():
            response = 'You are assigned to the same unit as Sasha. According to the strategic map, Mikasa and Connie are around here, too.\n\n\
Mikasa received excellent marks in training. During the Battle of Trost, she comported herself in a way well beyond that of a mere trainee.\n\n\
Sasha also had strong grades. Her constant hunger is the most noticeable thing about her, but she also seems to have an almost animalistic intuition; she might not be surprisingly capable in battle. \
You recall that in just the last month of training, she’s become quite proficient at horseback riding.\n\n\
**Your Affinity with Sasha has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.sasha += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 235

    def P123(self, *option):
        if option == ():
            response = 'Bertolt grows paler and paler.\n\n\
Out of concern, you decide to stay here. Krista and Ymir go to bring support.\n\n\
As Ymir leaves, she says to you, “Keep a close eye on Bertolt there. And you, Bertolt, don’t do anything funny. Think about just letting this one go.”\n\n\
Then they ride away.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 204

    def P124(self, *option):
        if option == ():
            response = 'Deep in the forest, the command squadron and the baggage train come to a halt.\n\n\
Another squadron that went on ahead is already there; they’ve made preparations of some kind.\n\n\
One of the wagons, which was supposedly carrying supplies, is lying on its side. It turns out it was carrying neither food nor resources. \
It was piled with barrels- and those barrels are fixed to the wagon. Now on its side, they look like an assembly of small cannons. Maybe this wagon was actually built for an eventuality like this. \
You’ve never seen such a thing before.\n\n\
“This weapon serves to bind a specific target,” Hange mutters beside you. “I can’t say more than that. Explanations come later.”\n\n\
All you can do is look, but every indication is that this equipment and the activity surrounding it have been under preparation for some time.\n\n\
Commander Erwin has overseen all of this; he’s been readying a secret plan.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 220

    def P125(self, *option):
        if option == ():
            response = 'You all get out of the woods, somehow managing to secure horses and join up with the main unit.\n\n\
When you get out of the Titan Forest, you find Commander Erwin along with the rest of the main unit and all of your friends.\n\n\
Eren is covered in some viscous liquid and is unconscious, but safe.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 130

    def P126(self, *option):
        if option == ():
            response = 'Cautiously, you approach the Female Titan on horseback.\n\n\
Suddenly, however, the Titan spins on her heel and starts running at a tremendous speed. She closes in on Armin, then kicks his horse and sends it flying!\n\n\
In the same motion she kneels down, bringing her face close to where Armin lies in the dirt.\n\n\
“Armin!” From the back of his own horse, Jean fires his anchors at the Titan, transitioning immediately into vertical maneuvering. In a superb display, he gets close to the Titan’s back. \
He should be able to finish it off- at least, he could if it were a normal Titan.\n\n\
The Female Titan covers the nape of her neck with her hand. She knows her own weak point.\n\n\
She’ll grab the wire and smash Jean to pieces!\n\n\
At that moment, someone starts shouting. “Jean! Take revenge!” It’s Armin, who has stood up. “Take revenge for that suicidal bastard! She stomped him to death!”\n\n\
You don’t understand what he’s talking about. Has Armin gone insane?\n\n\
The Female Titan, however, stopped moving immediately. Almost as if she were reacting to Armin’s words…\n\n\
Jean takes the opening to drop to the ground. Then, another human form comes flying from the Titan’s foot. It’s Reiner!\n\n\
He tries to take advantage of the Titan’s distraction to attack the nape- but the Titan glares at him and grabs him out of the air. Reiner is clasped in the huge hand… \
There’s a puffing sound and a crimson liquid goes flying everywhere.\n\n\
“What?!” Jean bellows. “Reinerrrr!”\n\n\
But then, something comes spinning out of the Titan’s hand. It’s Reiner. He has drawn his swords and cut off the Titan’s fingers; he jumps down and lands on the ground. The red liquid was the Titan’s blood.\n\n\
You swallow. Reiner is an incredible soldier.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 191

    def P127(self, *option):
        if option == ():
            response = 'The Female Titan crouches down, reaching into the underground tunnel; she stands up again and stamps on the ground. She seems to be attacking Eren and the others.\n\n\
**The Kill Count has increased by 3.**\n\n\
They’ll be in trouble at this rate.\n\n\
Type 1️⃣ to continue.'
            self.state.flags.killcount += 3
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.petra == 'Alive':
                self.cur_page[0] = 169
            elif self.state.statuses.dieter == 'Alive' and self.state.statuses.gunther == 'Alive':
                self.cur_page[0] = 169
            else:
                self.cur_page[0] = 308

    def P128(self, *option):
        if option == ():
            response = '“We should tell a nearby squad about this abandoned village, and the Titan,” the squad leader says. “Any volunteers to take a message?”\n\n\
The communication is to be carried out to the squad where Mikasa and Connie are. Sasha is pale, perhaps on account of the battle with the Titans.\n\n\
You…\n\n\
1️⃣ Stay close; you’re worried about Sasha\n\n\
2️⃣ Take the message to where Mikasa is'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 103
        elif option[0] == 2:
            self.cur_page[0] = 117

    def P129(self, *option):
        if option == ():
            response = 'You’ve been riding for a while when you encounter Jean and Reiner, sharing a horse.\n\n\
“Thank goodness!” Reiner says. “This horse wasn’t going to put up with two riders much longer.”\n\n\
They tell you how they encountered a new type of Titan, and fought it together with Armin. Where is Armin?\n\n\
“He’s…” Jean trails off, his eyes downcast. “Damn it. If only this extra horse could have come sooner… I never thought he was good for much, but… he did himself proud. \
He told us he would stay behind. Told us to report to Commander Erwin instead.”\n\n\
You’re shocked. But what is this important information that Armin left as his last will and testament? Jean is about to tell you, but Reiner cuts him off.\n\n\
“This is crucial stuff. We’d better not talk about it to just anybody. We should hurry to find the commander. Armin would have wanted that.”\n\n\
“Yeah… You’re right, Reiner.”\n\n\
The two of them take the horse from you and ride off.\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.armin = 'Dead'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 161

    def P130(self, *option):
        if option == ():
            response = 'The formation is reformed on the western edge of the woods, but at a significantly smaller scale than when you set out. Losses have been serious. \
What percentage of the expedition’s soldiers is still alive? Most of the baggage train was destroyed in the Titan Forest. \
You don’t know whether the point of this expedition beyond the walls was really to bolster a supply dump, as you were told, or if there was something else going on- \
but you understand that it has all come to nothing.\n\n\
Those who are too badly hurt to move are loaded onto the handful of remaining baggage carts. The unconscious Eren is among them.\n\n\
Even Captain Levi is wounded, his foot injured fighting the Female Titan as he tried to save Eren. He looks okay riding his horse, but you’ve heard he won’t be able to use vertical maneuvering for a while…\n\n\
“This is a general retreat,” Commander Erwin says. “Everyone, back to Karanes District!”\n\n\
The commander’s expression doesn’t change as he forcefully issues the order. But how must he feel in his heart? Massive losses, empty hands, and Eren wasn’t even able to achieve his Titan form.\n\n\
This time, you lost.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 247

    def P131(self, *option):
        if option == ():
            response = 'Levi listens to him, absolutely silent. He seems to be staring at nothing; his expression never flinches.\n\n\
You can’t stand it anymore, and find somewhere else to be.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 248

    def P132(self, *option):
        if option == ():
            response = 'The first thing you have to do is calm down and tend to Armin’s wounds. His Vertical Maneuvering Equipment is, thankfully, undamaged.\n\n\
The danger of the Female Titan seems to have passed, but you have another problem: you don’t have enough horses.\n\n\
Armin’s mount is no good, and Jean’s horse has run away. Jean has been whistling for his horse for some time now, but there’s no sign of the animal.\n\n\
Your own horse is injured, and won’t be able to support two people.\n\n\
Reiner’s horse might be able to take two riders… but that would mean leaving one person behind.\n\n\
Who do you think should have to stay behind?\n\n\
1️⃣ Reiner\n\n\
2️⃣ Jean\n\n\
3️⃣ Armin\n\n\
4️⃣ You yourself\n\n\
5️⃣ Try to somehow get all four of you on horseback'
            self.choices[0] = [1,2,3,4,5]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 267
        elif option[0] == 2:
            self.cur_page[0] = 239
        elif option[0] == 3:
            self.cur_page[0] = 260
        elif option[0] == 4:
            self.cur_page[0] = 287
        elif option[0] == 5:
            self.cur_page[0] = 183

    def P133(self, *option):
        if option == ():
            response = 'You ride on. Your position at the very back affords you a modicum of peace.\n\n\
Sometimes you see a smoke signal in the distance, and the formation changes direction. This goes on and on.\n\n\
Are those soldiers up ahead, the men and women under those smoke signals, encountering danger? You hear Krista murmur, “I hope all our friends are all right…”\n\n\
What do you talk about with the people around you?\n\n\
1️⃣ Bring up Armin\n\n\
2️⃣ Bring up Eren\n\n\
3️⃣ Bring up Annie, who’s now with the Military Police Brigade'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 255
        elif option[0] == 2:
            self.cur_page[0] = 114
        elif option[0] == 3:
            self.cur_page[0] = 166

    def P134(self, *option):
        if option == ():
            response = 'The soldiers around you all wear dark expressions. The fatigue accounts for some of this, but mostly you suspect it’s because the plan has failed. \n\n\
Hange is there, too. “There goes my big chance… Damn it!” the researcher groans.\n\n\
Commander Erwin looks unperturbed as he dispenses orders to the squad leaders. Even Captain Levi has his orders- to make sure extra gas and spare blades are available. \
The unit is preparing to fight tooth and nail, and Levi’s strength will be important.\n\n\
If you accompany Levi, type 1️⃣.\n\n\
If you stay with the commander and Hange, type 2️⃣.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 173
        elif option[0] == 2:
            self.cur_page[0] = 302

    def P135(self, *option):
        if option == ():
            response = '“We’re moving forward!” Eren shouts.\n\n\
A palpable relief passes through the members of Squad Levi. Nobody feels lost now. They ride ahead at full tilt.\n\n\
From behind come the screams of soldiers, rising up and then being cut off.\n\n'
            if self.state.flags.killcount > 0:
                response += '**The Kill Count has increased by 2.**\n\n'
                self.state.flags.killcount += 2
            response += 'You glance to the side and see distress written on Eren’s face. He’s made his choice, but it was a difficult one.\n\n\
You advance as the soldiers trying to slow down the Female Titan sacrifice themselves behind you, yet slowly but surely, the Female Titan makes up ground. Then she’s within arm’s reach.\n\n\
A massive hand reaches out. It’s about to grab Eren…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 221

    def P136(self, *option):
        if option == ():
            response = 'No sooner have you said this than another voice breaks in.\n\n\
“Hey, Krista, are you all right?”\n\n\
It’s Ymir, a girl Krista is friends with. She seems to have come from somewhere else. Her ability to intuit where Krista is must be a sort of instinct.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 182

    def P137(self, *option):
        if option == ():
            response = 'For a while, things are peaceful. But then…\n\n\
A messenger arrives and tells you that something strange has happened to the right wing, over on the other side of the formation. Some kind of enemy attack. \
You further learn that the right wing has taken a devastating blow. Even the experienced soldiers are taken aback.\n\n\
This is the opposite of what Sasha predicted. It seems she was wrong after all…\n\n\
**The Kill Count has increased by 5.**\n\n\
You start to worry about your friends on the right flank.\n\n\
A smoke signal goes up from the front. The entire formation is being ordered to make a major change in direction, perhaps to deal with the new situation. Your squad wheels around as well.\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.dieter = 'Dead'
            self.state.statuses.lukesiss = 'Dead'
            self.state.flags.killcount += 5
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 150

    def P138(self, *option):
        if option == ():
            response = 'You throw yourself off the wall, hoping to distract the Female Titan.\n\n\
You don’t know if it works, but at least it doesn’t seem to hurt.\n\n\
Mikasa sets her anchors in the wall and goes flying again, chopping off more of the Titan’s fingers. No longer able to support herself, the Female Titan comes crashing down.\n\n\
**Your Affinity with Eren has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.eren += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 322

    def P139(self, *option):
        if option == ():
            response = 'Who should appear but Krista?\n\n\
“Jump on, everyone! Quick!”\n\n\
She has two horses with her- a fresh spare, and Jean’s missing mount. She must have found the frightened animal and come looking for you. \
You remember that even in training, Krista was on good terms with the horses. All of you mount up, thanking Krista as you do so.\n\n\
“Thank goodness,” she says. “I’m just… I’m just so glad that the worst hadn’t happened to you.” There are tears in her eyes as she smiles. She seems to be speaking from the heart.\n\n\
You all feel your chests tighten to see her expression. Jean and Armin look as though they’re beholding a goddess. Reiner, for his part, is obviously red-faced. \
You never expected to see that from someone as reserved as him.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.flags.stay_behind == True:
                self.cur_page[0] = 143
            else:
                self.cur_page[0] = 296

    def P140(self, *option):
        if option == ():
            response = 'You decide to join the Garrison.\n\n\
It’s not that you were unmoved by Commander Erwin’s speech, but the Battle of Trost showed you how important it is to protect the people inside the walls.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 21

    def P141(self, *option):
        if option == ():
            response = 'The whole formation makes a major change in direction. A forest of huge trees loom ahead of you. \
The “Titan Forest” is a localized group of massive trees that grow outside one wall and inside another. They can reach more than 80 meters in height, higher than the walls that protect humanity’s territory.\n\n\
As you get closer, the size of them becomes overwhelming; you start to get dizzy staring up at the branches.\n\n\
“We’re going into this forest,” says Captain Levi, who has received orders from the messenger.\n\n\
It seems a fresh directive has been issued to help deal with the current situation.\n\n\
This tall forest was within Wall Maria until five years ago, and had been treated like a nature reserve. Wide flagstone walking paths and carriage trails stretch into the woods. \
They aren’t in the best repair anymore, but they’ll be no trouble for the horses and baggage train.\n\n\
Without slowing your pace, you ride into the darkness under the vast thicket.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 152

    def P142(self, *option):
        if option == ():
            response = 'You notice that on the pointer finger of Annie’s flailing right hand is a large silver ring.\n\n\
There’s a click, and a little blade extends from it. The ring has some trick to it. You hurriedly reach for it- but Annie is an instant quicker; she gouges her own finger. \
Bright red blood flows from the wound.\n\n\
Pain: the stimulus required to initiate the transformation into a Titan.\n\n\
Even as you recall this fact, there’s a blinding light. Your body is blown backwards by the explosion that claims your life.\n\n\
**You have died. To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P143(self, *option):
        if option == ():
            response = '“You… You really saved us,” Jean mutters. “We were just tryin’ to decide who… who would have to stay behind. \
And this loon here volunteered,” he says, indicating you. “It was a tough spot.”\n\n\
“What?” Krista says. Her eyes go wide.\n\n\
You feel a fresh wave of relief. You’re glad it ended with nothing more than a tease from Jean. All thanks to Krista.\n\n\
Suddenly, you realize Krista is coming up to you. She whispers: “What we talked about earlier... If I had been in your place, I think I would’ve said the same thing.”\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 296

    def P144(self, *option):
        if option == ():
            response = '“So you noticed too, huh?” Armin says to you. “The commander even talked about the key to Eren’s basement. He wanted someone here to hear that. \
Plus, the way he focused on how bad the Survey Corps’ casualty rate is- he wanted to scare us more than he really needed to.”\n\n\
So was the idea that there was a Titan spy among them, and suspicion would fall on anyone who was willing to volunteer for the Survey Corps despite the horrible things the commander had said? \
That’s your guess. And that puts everyone under suspicion. Wait- does such a thing as a Titan spy even exist?\n\n\
“I don’t know about any of that,” Armin says, smiling grimly at your questions. “This is all just my speculation.\n\n\
“And it’s possible the spy is someone who deliberately didn’t join the Survey Corps. Smart people are able to load one speech with several meanings. \
Maybe Commander Erwin deliberately emphasized the worst parts of reality so that only the most determined would join up.”\n\n\
Armin seems to be giving you his honest opinion.\n\n\
But then he says, “Then again, maybe I’m the Titan spy, and I’m feeding you misinformation.”\n\n\
He gives you a strained smile. You can’t tell if he’s joking.\n\n\
**You obtain Key Number Y. Key Number Y represents the question “What can you see?” Write down or remember the number 100.**\n\n\
Type 1️⃣ to go back and choose another path.'
            self.state.flags.keyY = 'Yes'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 9601

    def P146(self, *option):
        if option == ():
            response = 'In the scant few moments before the end of your life, you hear a screaming that reverberates in your ears. Your shaking vision shows you Eren turning into a Titan.\n\n\
Perhaps your death was what gave him the impetus he needed. You pray for your friends’ victory even as your life slips away.\n\n\
Will Eren Yeager remember your name among all the many comrades he’s lost?\n\n\
(Thanks to your actions, Mikasa Ackerman and Armin Arlert survive)\n\n\
**You have obtained the "A Cruel World" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P147(self, *option):
        if option == ():
            response = 'You ride off to save Sasha! You’ve never seen such strange movements from a Titan before. What should you do…?\n\n\
“Yaaaaaahhh!” Sasha cries.\n\n\
You pick up the scream yourself, and end up fleeing in panic from the Titan.\n\n\
“Yaaaaaahhh!”\n\n\
As the two of you scramble to get away, a senior soldier shows up and rescues you…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 203

    def P148(self, *option):
        if option == ():
            response = 'You’re riding along with Armin, Jean, and Reiner. Ahead of you is the Female Titan, moving at a run. You’re tailing her, trying to keep a safe distance.\n\n\
On horseback, the three of you talk, exchanging information. Armin tells you the Female Titan appears to possess intelligence. Jean and Reiner report that a pack of Titans attacked the right wing.\n\n\
Could these two things be connected?\n\n\
As you talk, something strange comes to light. Eren’s position within the formation was marked in a different place on each of your strategic maps.\n\n\
“So are they trying to hide things from their allies, too?” Reiner asks, frowning. “Where’s Eren, then?”\n\n\
“I assume he’s in the safest spot in the formation, probably around the rear-center,” Armin says. Reiner seems to accept this.\n\n\
“Hey!” Jean calls. “We don’t have time for guessing games! If that Titan’s as dangerous as all that… we’ve gotta do something!”\n\n\
He’s right. If you don’t act soon, the whole formation could be in danger. But a complex idea like “there’s a special Titan that possesses intelligence” is too much to communicate by smoke signal.\n\n\
“At this distance… I think we should be able to slow it down, buy some time,” Jean says. But then, his voice shaking, he adds, “I wish.” He tries to sound like he’s joking, but he’s serious.\n\n\
The Female Titan certainly does look strong, and seems to be intelligent… The four of you together could end up crushed like insects. But maybe it would be worth it in order to protect your allies.\n\n\
You’re surprised. Back in training, Jean always seemed so self-centered, like he didn’t care about anyone else…\n\n\
“I just… don’t want ‘em to be disappointed in me,” he mutters. Then he shouts:\n\n\
“This is what we have to do right here, right now! So help me out!”\n\n\
You…\n\n\
1️⃣ Help Jean challenge the Female Titan!\n\n\
2️⃣ No, it would be better to fall back and let the others know what’s going on.'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 223
        elif option[0] == 2:
            self.cur_page[0] = 280

    def P149(self, *option):
        if option == ():
            response = 'You are assigned to the same squad as Jean. According to the strategic map, Reiner is in one of the nearby squadrons. This is a great relief to you. \
Jean and Reiner both got high marks in training.\n\n\
Reiner comes across as a physically fit older brother; ever since your time as trainees he’s seemed dependable. Jean is exceptionally talented when it comes to vertical maneuvering. \
He had a contemptuous streak back in training, but it seems to have vanished since the battle in Trost.\n\n\
**Your Affinity with Jean has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.jean += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 187

    def P150(self, *option):
        if option == ():
            response = 'The whole formation makes a major change in direction; you head into the Titan Forest. This is a localized group of massive trees that grow outside one wall and inside another. \
They can reach more than 80 meters in height, higher than the walls that protect humanity’s territory.\n\n\
As you get closer, the size of them becomes overwhelming; staring up at them makes you dizzy. New orders arrive by smoke signal and messenger. You’re to dismount outside the forest and climb the trees, \
then make sure the Titans don’t get into the woods.\n\n\
It isn’t just your squadron; the entire expedition appears to be splitting up to guard the perimeter of the forest.\n\n\
You can’t shake the sense that these orders are impossible to carry out… but soldiers who have been here longer than you are following them. \
This is your first expedition outside the walls; how are you to decide if your orders are impossible or perfectly reasonable? You decide to obey them.\n\n\
You climb off your horse, tying the reins to a tree root. Titans don’t attack non-human animals, so as long as there aren’t any accidents, the horses should be safe.\n\n\
Following the example of the other soldiers, you ascend one of the trees using vertical maneuvering. These plants are taller than the walls; about halfway up one, you’ll already be above most Titans.\n\n\
At last, the Titans arrive. They flock to the trees where the soldiers are.\n\n\
There’s no need to fight them. Your only job is to keep them from getting into the woods; distracting them is good enough. \
You might have to fight the occasional Abnormal that ignores you and tries to go into the trees, but otherwise you have little to worry about.\n\n\
Still, you can’t help wondering what’s going on inside this forest…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 151

    def P151(self, *option):
        if option == ():
            response = 'You’re on guard duty outside the Titan Forest, making sure the Titans don’t get in.\n\n\
Now… who’s around you?\n\n\
(You can choose the person or people you were stationed with immediately prior to this, or you can pick a different comrade. \
If you do, you are considered to have been assigned to a new position along with these new orders)\n\n\
1️⃣ Armin and Jean\n\n\
2️⃣ Bertolt and Ymir\n\n\
3️⃣ Sasha and Mikasa\n\n\
4️⃣ Krista'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 256
        elif option[0] == 2:
            self.cur_page[0] = 108
        elif option[0] == 3:
            self.cur_page[0] = 172
        elif option[0] == 4:
            self.cur_page[0] = 217

    def P152(self, *option):
        if option == ():
            response = 'The road runs directly through the center of the Titan Forest. The woods, home as they are to trees reaching eighty meters in height, are vast and dark. You move through on horseback. \
The only sound is the clopping of hooves, and even that is quickly swallowed up by the forest.\n\n\
You have a bad feeling about this.\n\n\
What change in strategy brought you here? The trees block your vision and make it impossible to say what direction a Titan may attack from. \
Eren must be thinking along similar lines, because he shouts the same question to Captain Levi.\n\n\
The captain’s response is blunt: “Don’t ask about the obvious.”\n\n\
It’s true; the more experienced soldiers- the members of Squad Levi- don’t voice any complaints. They simply trust the order they’ve been given and silently carry them out.\n\n\
A sound like a whirlwind comes from behind you.\n\n\
“Everyone, draw your swords,” Levi says. “It’ll appear in an instant.”\n\n\
The sound of ringing steel fills your hearing. What is “it,” you wonder, even as you draw your sword.\n\n\
A moment later, “it” is there.\n\n\
It’s running down the path through the forest at an incredible speed. A Titan, about ten meters tall. Its movements are efficient, and it has the slim build of a woman.\n\n\
It’s a female Titan.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.flags.killcount == 0:
                self.cur_page[0] = 160
            else:
                self.cur_page[0] = 170

    def P153(self, *option):
        if option == ():
            response = ''
            if self.state.flags.mikasa_help == True:
                response += '**Your Affinity with Mikasa has increased by 1!**\n\n'
                self.state.affinities.mikasa += 1
            response += 'She catches up to the Female Titan quickly. Mikasa draws her sword, lashes out violently again and again. Cuts and scratches appear on the Titan, but none of the wounds are fatal. \
The Titan appears to have the ability to toughen her skin. Nor does she stop running, even as she covers her own weak point.\n\n\
Mikasa’s attacks are berserk, without any of her usual clear-headedness. It’s only good fortune that keeps her from being killed by a counterattack.\n\n\
It looks like the Female Titan is feeling the fatigue of battle, too. She’s pouring all her remaining energy into the flight from the field.\n\n\
“Just wait for me, Eren!” Mikasa strikes again. Her form is impeccable.\n\n\
The Titan finally stops moving for a second, striking at Mikasa with a sweeping motion of her arm.\n\n\
Mikasa just manages to dodge. The tree behind her is struck by the Titan’s blow, giving a great crack.\n\n\
Suddenly, a new figure appears. It grabs the off-balance Mikasa from the sky.\n\n\
“We need to retreat for the time being.” It’s Captain Levi. He must have been following the Titan as well. “We have nothing to gain by fighting now. Let’s get some distance.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 174

    def P154(self, *option):
        if option == ():
            response = 'Finally, you hear a Titan’s footsteps nearby. You and Levi move toward the sound.\n\n\
The Female Titan’s back comes into view, as does a soldier using vertical maneuvering around her. It’s Mikasa. She must have been following the Titan as well.\n\n\
Mikasa flits around the Female Titan, striking out again and again. How many attacks must she have made before the two of you showed up? The Titan is covered in steaming injuries, but none of them are fatal.\n\n\
Mikasa’s attacks are berserk, without any of her usual clear-headedness. The Titan spins, sweeping at Mikasa with her arm.\n\n\
Oh no! You think, but Mikasa just manages to dodge. The Titan’s arm strikes the tree behind Mikasa; there’s a great crack and splinters come flying at you.\n\n\
Captain Levi increases his speed. He grabs Mikasa out of the air even as she prepares to attack again.\n\n\
“We have nothing to gain here. We need to retreat for the time being,” he says. “Let’s get some distance.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 174

    def P155(self, *option):
        if option == ():
            response = 'The Female Titan runs along, sweeping aside soldiers as she goes, closing in behind you.\n\n\
The members of Squad Levi start to shout as they watch:\n\n\
“Captain, give us orders! We can take down that Titan!”\n\n\
“Let us use vertical maneuvering!”\n\n\
You agree with them. Captain Levi’s hand-picked troops ought to be able to beat that Titan. And anyway, if you all just keep running, it’s only a matter of time before you get caught.\n\n\
But Captain Levi says, “All of you. Have you forgotten the orders your squad received?” He looks straight at Eren as he speaks. “They’re to protect this brat. With your lives. We keep riding.”\n\n\
At that, the squad members’ attitude changes. “Understood, sir!”\n\n\
Behind you, one soldier after another flings themselves at the Female Titan in an attempt to protect you and Squad Levi. The Female Titan continues to swat them down with precise, unsparing movements.\n\n'
            if self.state.flags.killcount > 0:
                response += '**The Kill Count has increased by 2.**\n\n'
                self.state.flags.killcount += 2
            response += 'Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 1551

    def P1551(self, *option):
        if option == ():
            response = 'Eren seems unable to accept it: not the deaths of his comrades, not the fact that Squad Levi is leaving their friends behind in order to keep him safe.\n\n\
You see him raise his hand to his mouth. He means to transform into a Titan.\n\n\
There’s no question that if he turns into a Titan here, he could fight back against the monster pursuing you. At that very instant, soldier after soldier is being killed.\n\n\
“Eren, what are you doing?!” Petra cries.\n\n\
Levi speaks. “Eren.” His voice is soft, yet it carries unmistakably even over the sounds of clattering hooves and raging wind. \
“You aren’t wrong. The unit’s decision is based on experience- but you don’t have to rely on that. You have a choice: trust yourself… or trust me and the members of the Survey Corps.”\n\n\
He goes on, almost in a whisper: “I don’t know the right answer. You can choose to put faith in your own strength, or to believe that your comrades are worthy of trust… \
Either way, no one knows what will happen. The most you can do...is choose whatever you will regret the least.”\n\n\
Eren appears to be thinking about this.\n\n\
What do you say?\n\n\
1️⃣ “Captain Levi is right!”\n\n\
2️⃣ “Transform, Eren!”\n\n\
3️⃣ “I’ll trust whatever decision you make, Eren!”'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 281
        elif option[0] == 2:
            self.cur_page[0] = 213
        elif option[0] == 3:
            self.cur_page[0] = 253

    def P156(self, *option):
        if option == ():
            response = '“They got Gunther!” A shock runs through the members of Squad Levi.\n\n\
“Eren, don’t stop- just keep moving forward!”\n\n\
“Head for our allies as fast as you can!”\n\n\
The next instant, a beam of light shines in the forest; there’s a roar, and suddenly a Titan appears.\n\n\
It’s the Female Titan.\n\n\
What’s going on? Is there another one? No… If this person has the same abilities as Eren, they themselves must have escaped in the fracas earlier, then transformed into a Titan again.\n\n\
“Crap! I can’t believe this!” Eren shouts. “This time, I’m going to finish her!”\n\n\
He seems to intend to turn into a Titan himself and fight. But then the remaining three members of Squad Levi stop him:\n\n\
“No, don’t! Your powers are too risky!”\n\n\
“Leave this to us!”\n\n\
It’s Petra who cries, “Please- trust us!”\n\n\
What do you do?\n\n\
1️⃣ Try to encourage Eren by yelling at him to become a Titan\n\n\
2️⃣ Trust Squad Levi and run away with Eren\n\n\
3️⃣ Forget about Eren and fight alongside Squad Levi'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 270
        elif option[0] == 2:
            self.cur_page[0] = 291
        elif option[0] == 3:
            self.cur_page[0] = 164

    def P157(self, *option):
        if option == ():
            response = 'Jean, Armin, and Reiner tell you how they encountered and did battle with the Female Titan. The fact that you’re all on horseback makes it hard to get details, though.\n\n\
The entire unit seems to be in chaos. A smoke signal goes up and the formation changes direction.\n\n\
“We’re heading toward… the Titan Forest,” Armin says in surprise.\n\n\
It’s true; you can see huge trees piercing the sky ahead of you.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 150

    def P158(self, *option):
        if option == ():
            response = 'You stay where you are and call to Eren. You dearly hope the sight of his comrades fighting to the death will help him resolve himself…\n\n\
Mikasa and Armin both move to their respective positions. They wave, signaling each other. They’re probably just about to move.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.petra == 'Alive':
                self.cur_page[0] = 288
            elif self.state.statuses.dieter == 'Alive' and self.state.statuses.gunther == 'Alive':
                self.cur_page[0] = 288
            else:
                self.cur_page[0] = 295

    def P159(self, *option):
        if option == ():
            response = 'You notice a large silver ring on Annie’s right pointer finger.\n\n\
You recognize that ring. And you remember a unique feature it had…\n\n\
Now you realize what the ring was really for. If Annie is the Female Titan, then pain would provide the stimulus to start the transformation.\n\n\
A small blade pops out from the ring. But you’re too fast; you block it. Pain shoots through you as it pierces your hand- but Annie’s plot is foiled.\n\n\
Annie Leonhart is arrested.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.flags.killcount > 0:
                self.cur_page[0] = 242
            else:
                self.cur_page[0] = 304

    def P160(self, *option):
        if option == ():
            response = 'The Female Titan gives chase, running after you.\n\n\
The soldiers accompanying Squad Levi, along with those who had been chased into the forest, fling themselves at her with vertical maneuvering, but they are unable to stop her. \
She anticipates their maneuvering, but they are unable to stop her. She anticipates their movements, sweeps away their wires to limit their mobility, and dodges with her body to evade their sword attacks. \
Unlike a normal Titan, she seems to possess intelligence.\n\n\
She doesn’t even try to grab and eat any humans.\n\n\
Strangely, although some of the soldiers appear to be wounded when she stops them cold, none of them, as far as you can tell, are killed.\n\n\
No… Your opponent is a Titan. It’s probably just coincidence.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 155

    def P161(self, *option):
        if option == ():
            response = 'After that, you try to return to your unit, but it doesn’t go well. You receive a strange order to head for the Titan Forest. \
All you can think is that your commanders have become deeply confused.\n\n\
At length, you encounter some defeated soldiers.\n\n\
“The center of the formation was destroyed. We don’t even know if Commander Erwin and Captain Levi are still alive.”\n\n\
“It’s not just that ‘Female Titan’- the Armored Titan showed up, too!”\n\n\
With your commanders gone, you are divided and conquered. Not only is the expedition beyond the walls a failure, but the Survey Corps itself has been destroyed.\n\n\
You start running in the direction of Wall Rose. How many of your comrades are even still alive…?\n\n\
**You have obtained the "Destruction of the Survey Corps" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P162(self, *option):
        if option == ():
            response = 'The Female Titan catches up with you almost instantly. One of her huge feet comes at you from above.\n\n\
You somehow manage to dodge being struck directly, but you tumble off your horse and land on the ground. The same thing seems to have happened to Armin.\n\n\
You briefly black out from the pain. Somehow, though, you force yourself to sit up- and find the Titan staring down at you.\n\n\
Her eyes somehow seem almost intelligent… and cold.\n\n\
You prepare yourself for death. And yet the Titan turns around and heads off. Why?\n\n\
“She’s not… going to kill us?” Armin says from beside you, his voice quaking. “Do you think she… recognized us just now?”\n\n\
Suddenly someone calls out. “Heeey! Armin!”\n\n\
It’s Jean and Reiner, both on horseback. You take a look around, and discover that your and Armin’s horses are both safe as well. \
The four of you link up, the urge your horses on as you chase down the Female Titan. As you ride, you give Jean and Reiner the short version of everything you’ve been through until now.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 148

    def P163(self, *option):
        if option == ():
            response = 'Unfortunately, you can’t choose the Military Police Brigade. That’s a privilege reserved for only the top ten scorers in each class.\n\n\
Type 1️⃣ to go back and choose again.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 9601

    def P164(self, *option):
        if option == ():
            response = 'You face down the Female Titan with the remaining members of Squad Levi- Oluo, Petra, and Eld.\n\n\
“Hey, rookie!” Oluo spits. “Just make sure you don’t slow us down!” \n\n\
Well, you knew that already. You don’t expect to be able to match the effectiveness of these three hardened soldiers in combat. But you believe you can do something.\n\n\
The three of them form a single group as they attack the Female Titan. She bats them away with a nimble motion.\n\n\
You’re sure Eld, who was at the vanguard of the attack, is done for- but even as the thought crosses your mind, he dodges the Female Titan with a tremendous display of maneuvering. \
Oluo and Petra launch themselves at the Titan’s face from just behind him. Spinning like wheels, they each slice at one of the Titan’s eyes, blinding her!\n\n\
An incredible combined offense. You can only marvel.\n\n\
Eld’s attack was just a feint; it was a bid to steal her vision all along. The three of them haven’t signaled to each other ahead of time, they all just knew what to do. \
So this is what it means to be an experienced member of the Survey Corps.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 222

    def P165(self, *option):
        if option == ():
            response = '“We’ve got to get away from Eren’s location!” you shout to the others, and then you point your horse towards the center of the formation- the very place where Eren is.\n\n\
Armin must have caught on to what you’re thinking, because he raises his own voice and says, “Good idea! Let’s get as far away from Eren as possible!”\n\n\
Squad Leader Ness and the others look confused for a second, but then maybe they get it, too, because they start riding in the same direction.\n\n\
The Female Titan sees all of you, but she turns her back on you and begins running the opposite way.\n\n\
“No, wait! Not that way!” Armin calls. The Titan keeps going.\n\n\
“Hey! What do you think you’re doing?” Ness demands, once the Titan is gone.\n\n\
Armin tries to placate the squad leader. “We were trying to trick that Titan. If she’s really intelligent, we thought she might try going the other direction.”\n\n\
“Clever. So you think she understands human language?”\n\n\
“I can’t be sure, but…”\n\n\
Squad Leader Ness and the others understand and accept what you’ve done. It may or may not be your decision to make, but it seems to have worked.\n\n\
“Reiner and the others are right in that Titan’s path,” Armin murmurs. “I hope they’ll be okay.”\n\n\
Nearby, smoke signals go up indicating contact with Titans.\n\n\
“We’re going to go back up the squads that have run into Titans,” Ness and Siss say to you and Armin. \
“You kids, head for the center of the formation and tell them about that Female Titan. Don’t stay together.”\n\n\
The two of you nod, then turn and ride for the middle, both of you taking different routes.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 227

    def P166(self, *option):
        if option == ():
            response = '“Yeah. I bet she’s living a nice, cushy life with the MPs right about now,” Ymir says sarcastically, then she snorts. “Krista should’ve done the same thing.”\n\n\
“That’s not a very nice way of putting that,” Krista says.\n\n\
Bertolt’s expression changes. Maybe the subject of Annie bothers him.\n\n\
Krista seems to notice and says, “If we survive, I’m sure we’ll meet again someday.”\n\n\
Bertolt nods at that. Yet, looking at his face, you can’t help thinking that isn’t quite what’s on his mind. You can just hear him murmuring:\n\n\
“That’s right. No matter what, we have to survive… So we can all go back to our home, together…”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 194

    def P167(self, *option):
        if option == ():
            response = 'When the smoke clears, the Female Titan is towering there in an unnatural pose. Something like arrowheads are lodged all over her body, connected to countless wires.\n\n\
They look like the anchors used for vertical maneuvering, but much bigger. The wires are thicker, too. The Female Titan, ensconced in these thick metal wires, can’t move an inch. \
The smoke from the shooting still wreaths the carts lying on both sides of the road.\n\n\
This isn’t some slapdash solution improvised in the heat of the moment- this is the specialized weapon obviously designed specifically to tie down Titans. It was ready in advance; \
it seems that luring this Titan and then capturing her was the plan all along.\n\n\
Did Commander Erwin really foresee all of this? The Female Titan’s attack? The retreat into the Titan Forest? The fact that if Eren and the others ran down this road, \
the Titan would follow them straight into the trap?\n\n\
The soldiers all cheer. This unit acted with Commander Erwin to have this trap ready.\n\n\
“We did it! Did you see that?!”\n\n\
“You get a load, Eren? That’s the Survey Corps at work!”\n\n\
Squad Levi, the unit that had been working with Eren, cheers too. Judging by the shocked expression on his face, though, no one told Eren about the weapon or the plan. \
It’s precisely that secrecy that has garnered this extraordinary prize: a living Titan.\n\n\
Captain Levi dismounts his horse, then uses his Vertical Maneuvering Equipment to get up into one of the tall trees. Standing where he can look down on the Female Titan, \
he appears to be talking with Commander Erwin.\n\n\
The commander gives orders. Hange and Levi jump into action against the Titan. The soldiers who led the Titan here are ordered to keep watch on the immediate area; \
they too ascend into the trees with their Vertical Maneuvering Equipment and head to their respective stations. Squad Levi, Eren, and the others set to their work as well.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 186

    def P168(self, *option):
        if option == ():
            response = '“I’ll stay behind,” Armin says. He’s sweating, but he looks determined.\n\n\
“Hey, wait just a flippin’ second, Armin,” says Jean, sounding desperate, but Armin goes on: “In exchange, there’s something I need you to report. To Commander Erwin alone, if possible…”\n\n\
Reiner listens to this, looking as worried as Jean.\n\n\
Suddenly, though, Jean shouts and points into the distance.\n\n\
“You’re gonna tell ‘im yourself, Armin. Somebody’s coming this way- and they’ve got a horse!”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 139

    def P169(self, *option):
        if option == ():
            response = 'You watch and wait for a time, but there’s no movement underground. If Eren turns into a Titan you might be able to fight back… What’s he doing?\n\n\
You…\n\n\
1️⃣ Challenge the Female Titan yourself\n\n\
2️⃣ Watch, wait, and pray'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 218
        elif option[0] == 2:
            self.cur_page[0] = 318

    def P170(self, *option):
        if option == ():
            response = 'The Female Titan comes running after you.\n\n\
The soldiers who had been working with Squad Levi, along with those who had run into the forest, fling themselves after one another with their Vertical Maneuvering Equipment, but they are unable to stop her.\n\n\
She seems to anticipate what they’re going to do, grabbing their maneuvering wires to throw them off course and slamming them into trees or the ground. \
Other times, she simply swats them out of the air or grabs and crushes them. The soldiers’ blood and limbs go flying through the sky.\n\n\
Unlike a normal Titan, she doesn’t bring any of her victims to her mouth and try to eat them. But she does kill one person after another with precise movements. \
This Titan seems to be intelligent- but a cruel intelligence it is.\n\n\
**The Kill Count has increased by 2.**\n\n\
Type 1️⃣ to continue.'
            self.state.flags.killcount += 2
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 155

    def P171(self, *option):
        if option == ():
            response = 'Bertolt, sounding oddly panicked, says, “No way. How could we drag Annie into this?”\n\n\
“I’m for it,” Reiner says. “Annie is very capable. It would be all right. And she knows how to turn something down if it’s hopeless.”\n\n\
Armin, too, looks at you; he says, “I was thinking about Annie, myself. There’s no telling whether she’d join us or not. All we can do is ask.”\n\n\
**Your Affinity with Armin has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.armin += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 251

    def P172(self, *option):
        if option == ():
            response = 'You are assigned to the same location as Sasha and Mikasa.\n\n\
“The long-distance enemy-scouting formation isn’t working anymore,” Mikasa says coldly. Sasha, for her part, seems pretty panicked. You hope she’ll be all right…\n\n\
For a time, you continue your attempts to keep the Titans at bay. Maybe the Titans do have some ability to learn, because they slowly start climbing the trees. \
Mikasa calmly dodges them, occasionally engaging. Sasha groans pathetically, “I’m sooooo hungry…”\n\n\
You…\n\n\
1️⃣ Encourage Mikasa\n\n\
2️⃣ Give Sasha something to eat'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 106
        elif option[0] == 2:
            self.cur_page[0] = 276

    def P173(self, *option):
        if option == ():
            response = 'You’re in a dim forest of gigantic trees. You advance alongside Captain Levi. Once in a while he heads to the upper branches of one of the trees, as though looking for something, \
before deciding where to go next. And then, as if he senses something, the two of you change direction.\n\n\
You use vertical maneuvering to move forward- and emerge into a clearing devoid of trees.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 241

    def P174(self, *option):
        if option == ():
            response = 'Levi told you to get some distance. You, he, and Mikasa tail the Female Titan, keeping back a ways.\n\n\
“Maybe she’s getting tired, too. She doesn’t seem to be moving that fast,” Levi says. There’s a beat, then he asks calmly, “Is Eren dead?”\n\n\
Mikasa lays out her thoughts. She saw the Titan swallow Eren. If the Titan had meant to kill him, she could have simply crushed him. Deliberately putting him in her mouth and escaping seems to be her plan.\n\n\
“So she may have been planning to eat him all along,” Levi says. “That would mean he’s in her stomach right about now.”\n\n\
Mikasa replies forcefully, “He’s alive! Anyway, if you had done your job protecting him, we wouldn’t be in this situation.”\n\n\
As you fly along with your Vertical Maneuvering Equipment, Mikasa seems ready to slice Levi in half.\n\n\
What do you say?\n\n\
1️⃣ “I’m sure this isn’t easy for Captain Levi, either.”\n\n\
2️⃣ “Mikasa’s right. You made the wrong call, Captain.”\n\n\
3️⃣ “You two aren’t so different.”'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 306
        elif option[0] == 2:
            self.cur_page[0] = 195
        elif option[0] == 3:
            self.cur_page[0] = 112

    def P175(self, *option):
        if option == ():
            response = '“We’ve got to get away from Eren’s location!” you shout to the others, and then you point your horse toward the outer edge of the formation.\n\n\
Squad Leader Ness and the others seem to see what you have in mind, because Ness says, “You’re right. We risk getting cut off… but we have to protect our friends!” \
They set their horses running in the same direction as you. You hope to lead the Titan away from the center of the formation.\n\n\
As it happens, however, for some reason the Female Titan fails to follow you. She turns her back on you and begins running the opposite way- directly into the center of the formation, where Eren is.\n\n\
What’s going on here? Is she intelligent enough to have seen through your plan?\n\n\
“Hey! Not that way, this way!” Ness and Siss wheel their horses around and go after the Titan. You and Armin follow them.\n\n\
Suddenly the Titan lashes out with her foot, kicking at the animals. First Ness, then Siss, then Armin, and finally you- with no time to dodge, you fall off your horse and tumble onto the ground.\n\n\
You connect with the earth at high speed. Agony assaults your body.\n\n\
When you finally roll to a stop, you fight the pain back long enough to stand up. The Titan is well away from you now. Squad Leader Ness, along with Siss, is getting to his feet with a groan. \
Armin is moaning; he appears to be injured.\n\n\
“We’re all alive, huh?” Ness says.\n\n\
“Damn good luck. Never known a Titan to pull its punches before… or its kicks.”\n\n\
“But she’s headed for the center…” Armin grunts.\n\n\
“We have to worry about us first. Without horses, we’re sitting ducks for the next Titan that comes along!”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 115

    def P176(self, *option):
        if option == ():
            response = 'You’re only just registering what’s happening when the figure rushes at Gunther, slicing him with a sword as they pass by!\n\n\
Gunther, taken totally by surprise, has no chance to dodge. He loses his balance and slams into a tree root.\n\n'
            if self.state.flags.killcount == 0:
                response += 'Gunther is flung through the air. His arm is bent at an unnatural angle and he’s groaning. He’s alive, but he’s out of combat.\n\n'
            else:
                response += 'A wire drags Gunther into the air, where he’s shaken like a ragdoll. Blood comes flying out of him. His neck breaks, his head hanging at an unnatural angle.\n\n\
**The Kill Count has increased by 1.**\n\n'
                self.state.statuses.gunther = 'Dead'
                self.state.flags.killcount += 1
            response += 'Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 156

    def P177(self, *option):
        if option == ():
            response = 'You think back… Back to the day before this meeting. Before the Military Police Brigade showed up.\n\n\
You were part of a secret conference within the Survey Corps. Commander Erwin and Captain Levi were there, as were Eren, Armin, and Mikasa.\n\n\
“We believe we know who the Female Titan is,” the Commander said. “Our target is part of the Military Police Brigade in Stohess District. We have a plan to catch them. \
Zero hour is the day after tomorrow. That’s also the day we and Eren are to go to the capital.”\n\n\
Depending on how blame is assigned for this recent incident, the Survey Corps might be dissolved; at best, its future activities would be severely curtailed. It isn’t clear what would become of Eren, either.\n\n\
“We’ve developed a plan that will make everything that’s going on nice and obvious. We’re staking everything on this. There will be no more opportunities.”\n\n\
The commander explains: Eren, being transported under guard, will leave the city and make contact with the target. They will pretend he was planning to escape. \
The target is after Eren, so he’s going to be the bait. Survey Corps troops will have infiltrated Stohess District and will participate in the capture operation.\n\n\
“It’s Armin who figured out who our target is. He also proposed this strategy, which we adopted,” the commander says.\n\n\
You’re impressed with Armin’s powers of observation. But when you glance over at him, he doesn’t look very pleased.\n\n\
Commander Erwin continues: “The target’s name is Annie Leonhart.”\n\n\
You can hear Eren draw a sharp breath. “What?” he says, astonished. “That’s not possible. What are you playing at, Armin?!”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 1771

    def P1771(self, *option):
        if option == ():
            response = 'Calmly, Armin lays out the proof: Marco’s Vertical Maneuvering Equipment. The Female Titan’s reaction to the name “that suicidal bastard,” \
which was known only to the members of the 104th Training Corps.\n\n\
Eren sounds ready to argue to the bitter end, but as you look in his eyes, you see the realization overcoming him. How could it not? He knows Annie well, and he fought the Female Titan himself…\n\n\
“Even within the Survey Corps, only a few trusted people know about this plan. It’s absolutely confidential,” Commander Erwin says by way of conclusion.\n\n\
The top-secret plan to exfiltrate Eren from under the noses of his guards has been put into motion, largely utilizing members of the 104th Training Corps. \
At the same time, however, preparations are being made for the real objective- Annie’s capture. A secret plan covering for an even more secret one.\n\n\
“All of you, make sure you keep this strictly to yourselves,” the commander reminds you. “You can’t reveal our true objective to anyone, not even your friends from the 104th.”\n\n\
You nod along with the others. It hurts you to have to deceive your friends, but under the circumstances you have no idea who might be a Titan spy.\n\n\
The last thing Armin says to you before you go is, “When we leave this room, I”m going to act like I don’t know anything about the plan, either. Play along, okay?”\n\n\
(Don’t forget what happened here… but play along with Armin.)\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 250

    def P179(self, *option):
        if option == ():
            response = 'You all form up your squadron and advance on horseback. The formation seems to have spread out significantly; you can’t see any of the other squads anywhere. \
From time to time, a red signal goes up in the far distance, the sign that someone has encountered a Titan. Your own squad leader sends up a red smoke signal to communicate that fact to any nearby squadrons.\n\n\
The squad leader says to you, “The formation’s frontlines are full of experienced trackers. You newcomers are a little farther back, where it’s comparatively safe.”\n\n\
Still, Sasha looks nervous. “But what if some Titans hide out so the trackers miss them?”\n\n\
You’re passing by what appears to have been a village once. You see abandoned houses among the trees.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 111

    def P181(self, *option):
        if option == ():
            response = 'You hear a sound from the forest, some kind of explosion. A cannon, or perhaps a bomb…?\n\n\
“Sounds like they’re doing something in the woods,” Jean says.\n\n\
“Yeah,” Armin says.\n\n\
Both of them seem to have an idea what it is. Then they begin to talk.\n\n\
Veering off into the woods was not a spur-of-the-moment decision, they think, but part of something Commander Erwin had planned all along. \
The plan was all to help capture the Female Titan...and it was kept in utmost secrecy. Most likely, there’s a Titan spy in the ranks.\n\n\
That would explain a lot, including the fact that no one seems to be telling you anything about anything.\n\n\
“I’m still not thrilled,” Jean says. “They could’ve let us in on it a little bit. Maybe fewer soldiers would have had to die.”\n\n\
Armin, however, replies, “I think the commander made the right decision. Otherwise who knows where information might have leaked out and compromised the entire plan?”\n\n\
You…\n\n\
1️⃣ Agree with Jean\n\n\
2️⃣ Agree with Armin'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 198
        elif option[0] == 2:
            self.cur_page[0] = 219

    def P182(self, *option):
        if option == ():
            response = '“You were gonna go into the woods alone?” Ymir asks, sounding exasperated, when Krista tells her as much. “Shaking like that? You’d be better off running. \
This isn’t the time to be waiting for a retreat order.”\n\n\
She turns and says to you, “The same goes for you. You go into the woods, the only things that can happen are you either become collateral damage, or you get in the way.”\n\n\
You…\n\n\
1️⃣ Leave Krista with Ymir and head into the woods\n\n\
2️⃣ Take Ymir’s advice and run'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 327
        elif option[0] == 2:
            self.cur_page[0] = 268

    def P183(self, *option):
        if option == ():
            response = 'Jean actually looks relieved at your suggestion.\n\n\
“Gotta say, after the four of us survived for this long, I didn’t want to have to look someone in the eye and tell them to die.”\n\n\
But Armin shakes his head. “No… ‘Leave no one behind’ isn’t practical. Most likely, it would just get all four of us killed.” There’s a beat. “I’ll stay behind.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 168

    def P184(self, *option):
        if option == ():
            response = '“We need to restrict ourselves to one objective,” Levi says quietly. “We’re going to give up trying to stop the female. \
We gamble everything on the hope that Eren is still alive, and try to rescue him before she leaves the forest.”\n\n\
Mikasa, who looked so angry a moment ago, nods in acknowledgement.\n\n\
“I’ll wear her down. You distract her,” Levi says to Mikasa.\n\n\
Then the two superhuman soldiers head for the Female Titan with a burst of gas.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 243

    def P185(self, *option):
        if option == ():
            response = 'The battle in Stohess District may be over, but there’s no time to rest. You receive shocking news: a horde of Titans has appeared inside Wall Rose.\n\n\
That’s the area where your friends from the 104th Training Corps are stationed. Ironically, they’re there because they were under guard, except for those who accompanied you to Stohess. \
The Survey Corps forms a relief unit.\n\n\
You join the brigade. You’re going to fight the Titans to rescue your classmates and friends.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.flags.krista_ending == True:
                self.cur_page[0] = 330
            elif self.state.flags.sasha_ending == True:
                self.cur_page[0] = 329
    
    def P186(self, *option):
        if option == ():
            response = 'The capture mechanisms totally succeeds in immobilizing the Female Titan, but she has assumed a pose in which both hands protect the nape of her neck. \
She must have done that the instant the cannon fired. She’s proven to be one tough foe.\n\n\
The Survey Corps evidently intends to cut into the Titan’s body and remove whatever is inside. They must think there’s a human in there, just like with Eren. \
And if she is like Eren, then the human is resting at the nape of her neck. Perhaps that’s why the Female Titan is protecting her nape so aggressively.\n\n\
This means a very difficult job for the Survey Corps.\n\n\
The most capable soldiers in the unit, Levi and Mike, both set to work with their swords, but they don’t manage to cut off the arm guarding the neck. \
It looks like the Female Titan has the ability to harden that area.\n\n\
The enemy may be immobilized, but you don’t have unlimited time. You’re outside the walls now. And where humans have gathered, Titans will come…\n\n\
Commander Erwin issues an order. He wants to use the gunpowder from the capture mechanisms to blow off the hand at the wrist. It’s not a subtle solution, \
but it might finally allow you to get at whoever is inside the Female Titan.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 286

    def P187(self, *option):
        if option == ():
            response = 'For a time, you don’t encounter any Titans.\n\n\
A copse of trees rises up nearby. The only sound is the clopping of your horses’ hooves.\n\n\
But suddenly, you hear an earthshaking noise approaching.\n\n\
“Titans!” your squad leader shouts.\n\n\
It’s Titans, all right- a terrifying number of them. You can just make them out in between the trees. They’re of the 10-meter class, \
and you estimate there are more than ten of them! How many more, you don’t know.\n\n\
Your unit dissolves into chaos.\n\n\
“I know we’re outside the walls, but how can there be so many at once?!”\n\n\
“This has never happened before!”\n\n\
The group is totally crippled. You can’t find a moment in which to send up a smoke signal to alert everyone else to the situation.\n\n\
“You rookies, go!” the squad leader shouts. “Link up with the other units and tell them what’s going on!”\n\n\
You do as you’re told, whipping your horse on desperately.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 102

    def P188(self, *option):
        if option == ():
            response = 'The path through the forest stretches on. The woods, full of trees 80 meters and taller, is dim and eerie. \
All you can hear are the sound of your own horse’s hooves and the clattering of the wagons. And even those sounds seem to be sucked up by the dark foliage.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 124

    def P189(self, *option):
        if option == ():
            response = 'Even your squad leaders, experienced soldiers, remark on how this is unprecedented for an expedition beyond the walls, how it warrants waiting for instructions from the commander.\n\n\
“Let me go help them!” Krista begs, but the squad leaders’ judgement prevails over an imploring rookie.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 299

    def P190(self, *option):
        if option == ():
            response = 'Mikasa’s face shows no hesitation. You realize she’s been prepared for this for a long time now. She glances at you. \
You wonder if perhaps you’ve done something inappropriate, but then Mikasa says, “Thank you.”\n\n\
You’ve come to the bottom of the new hole. You wave at Armin across the way, signaling to him.\n\n\
**Your Affinity with Mikasa has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.petra == 'Alive':
                self.cur_page[0] = 224
            elif self.state.statuses.dieter == 'Alive' and self.state.statuses.gunther == 'Alive':
                self.cur_page[0] = 224
            else:
                self.cur_page[0] = 295

    def P191(self, *option):
        if option == ():
            response = 'Reiner runs past Armin, grabbing him as he goes by.\n\n\
“That’s got to be enough time, right?! Let’s get the hell out of here!”\n\n\
His shouting seems to bring Jean back to himself, for he sets off running as well. You follow them.\n\n\
The Female Titan looks intently at her brutalized hand… then suddenly leaves. Most Titans tend to attack humans, but this one seems to leave you alone if you get far enough away.\n\n\
“Lookit that. Big girl’s just a big baby. She’s running scared!”\n\n\
Reiner looks relieved, but Armin, for some reason, appears shocked. The source of his astonishment seems to be the direction the Female Titan has gone.\n\n\
“She’s… She’s heading for the center-rear,” he says.\n\n\
You seem to recall the center-rear is the heart of the formation, and Eren’s location. If that Titan attacks them, there’s going to be real trouble. \
Yet you can’t help thinking that there may be something else behind Armin’s amazed expression.\n\n\
You think back on some words that didn’t make sense to you at the time. Could they somehow be connected?\n\n\
**From this point on, if you see the words "she knows how to fight", copy and paste those words into the chat to reveal an additional option you may take.**\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 132

    def P192(self, *option):
        if option == ():
            response = 'You all find horses and jump on, riding through the woods.\n\n\
When you emerge from the Titan Forest, Commander Erwin is there, along with your friends.\n\n\
Eren’s injuries are startlingly bad; he’s unconscious, but it looks like he’s alive.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 130

    def P193(self, *option):
        if option == ():
            response = 'Eren raises a cry, a mournful howl.\n\n\
He turns, maneuvering directly at the Female Titan.\n\n\
A bright light shines in the dark forest, and there’s a sound like thunder.\n\n\
You see Eren above the tops of the trees: he’s a Titan now, and he throws himself at his adversary.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 231

    def P194(self, *option):
        if option == ():
            response = 'Things continue peacefully for a while- but then something, evidently, changes. Orders come in one after another. \
Word is that up at the front of the formation, the right wing has suffered a devastating blow, and the formation is in disarray.\n\n\
The more experienced soldiers, having heard the report, break into nervous chatter:\n\n\
“What the hell?! How could the long-distance enemy-scouting formation crumble so quickly?!”\n\n\
“An Abnormal…? They say something they called ‘the Female Titan’ appeared, bringing a horde of other Titans with her…”\n\n\
Female? Even in the Battle of Trost, you didn’t see any Titans with female body characteristics. Could this be some new type of Abnormal?\n\n\
All the soldiers around you appear equally shaken. Bertolt is visibly pale.\n\n\
“I’m not involved in this killing for fun…!” You hear him murmur.\n\n\
**The Kill Count has increased by 5.**\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.dieter = 'Dead'
            self.state.statuses.lukesiss = 'Dead'
            self.state.flags.killcount += 5
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 211

    def P195(self, *option):
        if option == ():
            response = 'When she hears you say this, Mikasa closes her mouth. Levi glares at you. Then he shifts his gaze forward again.\n\n\
“My duty is to protect that little brat.”\n\n\
**Your Affinity with Mikasa has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 184

    def P196(self, *option):
        if option == ():
            response = 'Even three elite soldiers can barely contain the Female Titan; she’s that powerful an opponent. She very nearly caught Eren, who was slammed into a tree root and now appears injured.\n\n\
Squad Levi doesn’t have much gas left.\n\n\
But that’s when Captain Levi appears!\n\n\
“Good work,” he says. “Let me handle the rest.”\n\n\
He throws himself at the Titan, alone. The Female Titan reaches out her hand, but Levi shifts in midair, dodging her. He really looks like he’s flying. \
He spins furiously, attacking. He looks like a bladed wheel.\n\n\
Even the Titan’s ability to harden her skin seems unable to keep up with this action. He slices a tendon in her foot, landing cuts all over and robbing her of the ability to move.\n\n\
He twists again in midair, and says to you, “Retreat. We have to get Eren and the other wounded out of here before she recovers.”\n\n\
He sounds preternaturally calm. Perhaps it’s his superhuman fighting skills and his long experience that allow him to seem so detached. Plus, his orders to protect Eren are important.\n\n\
“Hrrgh… Damn it,” Eren groans. “Captain Levi, you could have brought her down if you didn’t have me holding you back…”\n\n\
The members of Squad Levi don’t seem much happier about it than Eren, but they keep it to themselves and follow orders.\n\n\
You all retreat, carrying off the wounded. The Female Titan pursues you no more.\n\n\
You go to where the horses are, mount up and hurry to where your allies wait.\n\n\
As you ride, Captain Levi asks about the situation.\n\n\
You hear Petra concluding her report about you: “That rookie saved all our lives.”\n\n\
Levi stares in your direction for a moment, then says, “Hmph.”\n\n\
**Your Affinity with Levi has increased by 3!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.levi += 3
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 192

    def P197(self, *option):
        if option == ():
            response = 'The formation makes a major change in direction; the command unit heads for the Titan Forest.\n\n\
This is a localized group of massive trees that grow outside one wall and inside another. They can reach more than 80 meters in height, higher than the walls that protect humanity’s territory. \
As you get closer, the size of them becomes overwhelming; staring up at them makes you dizzy.\n\n\
“It looks like the wagons can manage in here,” Commander Erwin says as you enter.\n\n\
This tall forest was within Wall Maria until five years ago, and had been treated like a nature reserve. Wide flagstone walking paths and carriage trails stretch into the woods. \
They aren’t in the best repair anymore, but they look usable.\n\n\
“Take a message to the rear. Tell them only the unit assigned to protect the wagons in the center column is to enter the forest.”\n\n\
Commander Erwin issues these orders calmly, almost as if he knew ahead of time that he would be giving them.\n\n\
The other units are told to position themselves around the periphery of the forest and intercept any incoming Titans.\n\n\
Wouldn’t that completely defeat the purpose of the long-distance enemy-scouting formation? It would represent a major change in the strategy. Or perhaps the commander foresaw all of this happening…?\n\n\
You keep up your horses’ pace, heading deeper in to the dark wood full of vast trees.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 188

    def P198(self, *option):
        if option == ():
            response = 'You agree with Jean. With someone else on his side, he seems a little less nervous.\n\n\
“Maybe you’re even right, Armin,” he says, “but I still can’t let it go. We’re talking about guys dying here.”\n\n\
**Your Affinity with Jean has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.jean += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 240

    def P199(self, *option):
        if option == ():
            response = '“Eren!” someone cries.\n\n\
It’s Mikasa, who has arrived via vertical maneuvering. She must have come here when she heard the sound of Titans fighting.\n\n\
“Wait…” Her voice wavers with pain. The hint of vulnerability vanishes as quickly as it came, though. With a steely expression, she goes after the Female Titan.\n\n\
You…\n\n\
1️⃣ Are sure there must be some allies in the direction Mikasa went. You retreat.\n\n\
2️⃣ Chase after Mikasa and help her'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 263
        elif option[0] == 2:
            self.state.flags.mikasa_help = True
            self.cur_page[0] = 153

    def P200(self, *option):
        if option == ():
            response = 'You realize that this Titan is different from normal. You shout to Ness and the others not to engage her.\n\n\
“What’re you talking about, rookie?!”\n\n\
Ness and Siss seem to be of the opinion that a greenhorn on their first expedition beyond the walls wouldn’t know a Titan from a hole in the ground, but then Armin throws his weight in with you.\n\n\
“I don’t mean to be presumptuous, but I agree! That Female Titan is… She’s intelligent. Just like Eren!”\n\n\
Squad Leader Ness and Siss look at each other as they ride along. Armin seems to have convinced them to rethink things. He’s a newcomer just like you, \
but he was with Eren at the Battle of Trost when the boy turned into a Titan. That seems to earn him a little bit of notice from the leaders.\n\n\
And anyway, both these men are experienced members of the Survey Corps. They must realize that this Titan feels different. \
She’s chasing you, but not trying to eat you- almost like she’s tailing you, just to see what you do.\n\n\
“So what now?” Squad Leader Ness says. “If she’s intelligent, all the more reason we can’t leave her alone. We need to deal with her ourselves, to keep the entire formation safe!”\n\n\
You say…\n\n\
1️⃣ “Let’s lead her away from the center, Eren’s there!” and head for the outer edge of the formation\n\n\
2️⃣ “Let’s lead her away from Eren’s location!” and head for the center of the formation'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 175
        elif option[0] == 2:
            self.cur_page[0] = 165

    def P201(self, *option):
        if option == ():
            response = 'You use vertical maneuvering to head for where Eren and Squad Levi are waiting. \
They, along with everyone else, are weaving through the tall trees with their Vertical Maneuvering Equipment.\n\n\
“Yeah. Sounds like we’ve been ordered to retreat,” Eren and the others say cheerfully. “Did you figure out who the Female Titan is?”\n\n\
Now you realize: only the order to retreat as such can be communicated by smoke signal. They think they’re falling back because the plan succeeded. \
They were far enough away that they have no idea what really happened.\n\n\
They’re in high spirits, even bantering a bit.\n\n\
Another smoke signal can be seen, not far away.\n\n\
“Hey, there’s the signal. It’s gotta be Captain Levi,” Gunther says. “Let’s link up with him!”\n\n\
You…\n\n\
1️⃣ Go with them to link up with Captain Levi\n\n\
2️⃣ Tell them what happened with the Female Titan'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 257
        elif option[0] == 2:
            self.cur_page[0] = 113

    def P202(self, *option):
        if option == ():
            response = 'You are assigned to the squadron under Dieter Ness. Another experienced soldier there, Luke Siss, is someone who was a help to you even in training. Armin is in the same squad as well.\n\n\
You have two battle-tested senior hands, plus Armin’s intelligence. It takes a load off your mind. You feel lucky to have been assigned here.\n\n\
**Your Affinity with Armin has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.armin += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 110

    def P203(self, *option):
        if option == ():
            response = 'The crawling Titan destroys the abandoned building, then stops moving.\n\n\
You’re impressed: the experienced soldiers didn’t even use their Vertical Maneuvering Equipment. Nor do they bother to strike a killing blow.\n\n\
“Most Titans slow down in a big way after running as fast as they can,” one of them explains. “He won’t come after us again, and we sent up a smoke signal up, so the guys behind us will know to avoid him.”\n\n\
That makes sense. So this is how the long-range enemy-scouting formation is supposed to work.\n\n\
“This is how we deal with Normals. But if we meet an Abnormal, we’ll probably have to fight it to the death.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 128

    def P204(self, *option):
        if option == ():
            response = 'After Krista leaves, the bad news just keeps rolling in. You see smoke signals going up all around. You feel an overwhelming sensation of chaos.\n\n\
Bertolt grows paler and paler. You think back on what Ymir said and try to cheer him up as the two of you ride along. Luckily, he doesn’t seem inclined to do “anything funny.”\n\n\
At last, new orders, via smoke signal relay. The formation is making a major change in direction.\n\n\
The squad leader is talking to the other soldiers. “This way is… the Titan Forest.”\n\n\
“Are you sure these are the right orders?”\n\n\
“Yeah, no doubt. I’ve got them by messenger as well.”\n\n\
The squad leader gives the command. You all change direction, and slowly but surely the forest comes into view.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 150

    def P205(self, *option):
        if option == ():
            response = 'There are no other soldiers atop the walls. In this situation, you’re the only one who can do anything about the Female Titan.\n\n\
You…\n\n\
1️⃣ Let her go, and don’t do anything dangerous\n\n\
2️⃣ Prepare to fight the Female Titan to the death\n\n\
3️⃣ Betray humanity, and help the Female Titan escape'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 328
        elif option[0] == 2:
            self.cur_page[0] = 120
        elif option[0] == 3:
            if self.state.affinities.annie >= 2:
                self.cur_page[0] = 314
            else:
                self.cur_page[0] = 209

    def P206(self, *option):
        if option == ():
            response = 'An uncanny cry comes from deep in the woods. It sounds like a wild animal, but not one you’ve heard. \
Could it be the bellow of a Titan? Ymir and Bertolt both look wide-eyed with amazement.\n\n\
Suddenly the Titans ignore you and start heading into the forest. It happens so abruptly. All you can do is watch in astonishment.\n\n\
“All right, I’m going.” Ymir’s voice brings you back to reality.\n\n\
“Huh?” Bertolt asks. “But our orders were…”\n\n\
“Look at what’s happening. They’re going to tell us to retreat sooner or later, and if they don’t, things are only going to get worse. Anyway, I’m going to find Krista.”\n\n\
Bertolt seems worried about what’s happening in the forest, but finally he says, almost as if to himself, “It’s all right… I’m sure they’ll be fine… They don’t need me there…”\n\n\
You…\n\n\
1️⃣ Head into the forest\n\n\
2️⃣ Get out of here'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 271
        elif option[0] == 2:
            self.cur_page[0] = 268

    def P207(self, *option):
        if option == ():
            response = 'No sooner do you dive down the stairs and around a corner than there’s a shock you can feel all the way underground. \
You turn and see someone who was blown into the air by the impact; they’re a bloody lump of flesh now, stuck to the wall. If it weren’t for Mikasa’s quick thinking, you probably would be, too.\n\n\
“Is anyone injured?” Mikasa asks, then she shouts: “If you can stand, then run!”\n\n\
All of you set off as fast as you can into the dim underground tunnel. A massive hand comes after you. Annie in Titan Form- the very Female Titan herself- is reaching into the tunnel. \
You evade her, just in time. The hand scrabbles at the walls.\n\n\
“She saw through my lie all along… She knew we were waiting for her underground. There must be another way…” Armin says self-reproachfully in between gasps of breath.\n\n\
“We can berate ourselves later,” Mikasa says, calm, cold. “The question is, what do we do now?”\n\n\
“Right,” Armin says. “I think we should join up with the other squads waiting underground and move to plan B…”\n\n\
He sounds calm again. It looks like he anticipated this possibility, and prepared a backup plan.\n\n\
From down the tunnel comes a voice: “Heeey! What was that noise? Did plan A fail?” It must be the soldiers in the other underground squads.\n\n\
Armin calls back, indicating what to do next.\n\n\
**The Kill Count has increased by 3.**\n\n\
Type 1️⃣ to continue.'
            self.state.flags.killcount += 3
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 269

    def P208(self, *option):
        if option == ():
            response = 'You bellow a warning to the members of Squad Levi. They hear you and, on the cusp of attacking, bolt away from the Titan instead. \
Even Eld, practically in the middle of swinging his sword, jukes away.\n\n\
At that instant, the Female Titan opens one eye wide.\n\n\
This was outside of any calculation. If Eld had continued his move, she probably would have counterattacked.\n\n\
The Female Titan is fast. Her arms hang uselessly by her sides, but she moves nimbly on her feet, lashing out with powerful kicks. The soldiers just manage to avoid the blows.\n\n\
“Thanks. You saved us,” Petra says as she regains her balance and flies up next to you. “There are always individual differences in how fast they heal, so we weren’t guaranteed a full minute. \
But we never expected her to prioritize regenerating just one eye so that she could get it back in less than half that time.”\n\n\
You certainly didn’t know anything about that either- but for once, your instinctive caution as a new soldier may have served you well. \
Squad Levi, with their extensive Titan-fighting experience, might have assumed just a bit too much.\n\n\
The Female Titan wastes no time. Seeing that she isn’t going to take down any of these soldiers, she sets off running after Eren, ignoring you entirely. Her arms are both steaming, already starting to heal.\n\n\
“Protect Eren!” Eld shouts.\n\n\
“We aren’t going to be able to kill her- but we have to harry her, buy time!” Oluo puts in.\n\n\
The Female Titan is clever; she has more than a few tricks up her proverbial sleeve. The squad knows now that they have to be careful.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 196

    def P209(self, *option):
        if option == ():
            response = 'Having climbed to the top of the wall, the Female Titan- Annie- stares at you with her giant eyes. Her gaze is cold, her expression flat.\n\n\
She reaches toward you with one massive hand. Is she going to crush you, or take you with her…?\n\n\
Before her hand reaches you, though, she stops, then jumps over the other side of the wall. She starts running, never looking back.\n\n\
The attempt to capture the Female Titan has failed- Annie has escaped.\n\n\
You are thrown in prison on suspicion of being a Titan sympathizer. There’s an investigation, during which you undergo a very unpleasant interrogation.\n\n\
A rumor you hear in the brig holds that Annie is gone without a trace. The army has yet to discover her location.\n\n\
Maybe she’s hiding somewhere even now, still practicing her kicks, her face as expressionless as ever.\n\n\
**You have obtained the "Traitor’s Friend" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P210(self, *option):
        if option == ():
            response = 'Armin is shaking and pale, but he manages to keep running. He looks at you and laughs unconvincingly. \
“Ha ha… That’s a help. If we split up again and you go a third direction, maybe we can distract Annie just the tiniest bit.”\n\n\
You’ve come to the bottom of the underground stairs. You wave at Mikasa across the way, signaling her.\n\n\
**Your Affinity with Armin has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.armin += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.petra == 'Alive':
                self.cur_page[0] = 224
            elif self.state.statuses.dieter == 'Alive' and self.state.statuses.gunther == 'Alive':
                self.cur_page[0] = 224
            else:
                self.cur_page[0] = 295

    def P211(self, *option):
        if option == ():
            response = 'The squad leader and the experienced soldiers are saying: “We don’t know the situation. Let’s send out some reinforcements and see how things develop.”\n\n\
“Send me to reinforce them!” Krista says loudly.\n\n\
You…\n\n\
1️⃣ Ask to go with Krista to reinforce\n\n\
2️⃣ Stay here, as you’re worried about Bertolt\n\n\
3️⃣ Sense danger, and are desperate to stop Krista at any cost'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 228
        elif option[0] == 2:
            self.cur_page[0] = 123
        elif option[0] == 3:
            self.cur_page[0] = 189

    def P212(self, *option):
        if option == ():
            response = '“I’m not smart enough to understand all of this, but… It looks like he’s got it rough,” Connie says.\n\n\
“He spent the whole time in training talking about how he was gonna exterminate the Titans or whatever- and then it turns out he’s one of ‘em!” Says Jean. “I don’t know what to think about that.”\n\n\
Mikasa, on the other hand, adopts a serious tone. “They must have Eren in the safest possible place. As long as this long-distance enemy-detection formation does its job, he’ll be fine.”\n\n\
As she rides along, the old scarf she wears billows out behind her. “And if it doesn’t do its job… I’ll go save him.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 137

    def P213(self, *option):
        if option == ():
            response = 'You shout to Eren. In his Titan form, he’s capable of helping so many people. \
Most of the soldiers here probably don’t know about the intense fighting at the Battle of Trost. But you- you know.\n\n\
For the members of the 104th Training Corps, Eren is like a place of refuge. So you shout, in the faith that he can turn this situation around.\n\n\
Eren appears to hear you, because he nods.\n\n\
**Your Affinity with Eren has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.eren += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 226

    def P214(self, *option):
        if option == ():
            response = 'Suddenly, one of the Titan’s eyes opens wide. Eld, who was supposed to strike at the final blow, is caught in her mouth. She bites down.\n\n\
“She focused on just one eye so she could heal quicker?” Petra exclaims in astonishment. “Is that even possible?!” \
She manages to change direction at the last possible moment, but now she’s hopelessly off balance.\n\n\
The Female Titan doesn’t let the opportunity slip. With her arms hanging uselessly at her sides, she lashes out with a kick, catching Petra with her shin. \
The woman is slammed against a giant tree trunk- and crushed.\n\n\
Oluo is the only one left, but he’s able to get behind the Titan. He launches himself at her defenseless back, bent on taking revenge for his comrades.\n\n\
But his blade snaps.\n\n\
As he looks at his broken sword blankly, the Female Titan whips a kick backward through the air.\n\n\
It has been the work of a moment: the situation is turned on its head, the three soldiers brutally murdered.\n\n\
The Female Titan had more than one trick she’d been hiding. The ability to regenerate just a single eye. Making a show of covering her nape with her hands, \
even though she secretly possessed the ability to strengthen her own weak point.\n\n\
She’s not just huge and agile. She was a better fighter than her opponents…\n\n\
**The Kill Count has increased by 3.**\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.petra = 'Dead'
            self.state.statuses.oluo = 'Dead'
            self.state.statuses.eld = 'Dead'
            self.state.flags.killcount += 3
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 193

    def P215(self, *option):
        if option == ():
            response = 'You hear some kind of explosion from deep within the woods. Could that be cannons firing?\n\n\
“What a noise,” Ymir says. Bertolt seems oddly bothered by the sound; maybe it frightens him.\n\n\
You feel a rush of anxiety yourself, and wonder what’s going on.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 206

    def P216(self, *option):
        if option == ():
            response = 'At long last, news reaches you in the Trost District Guard Unit- and it isn’t good.\n\n\
The 57th expedition beyond the walls ended in disaster, sustaining heavy losses. You don’t know the details, but it sounded like Eren, so far from using his Titan powers to help the mission succeed, \
was defeated, resulting in many losses.\n\n\
The Survey Corps finds itself in an untenable position; Commander Erwin and the other leading members of the unit are summoned to the capital, where Eren is to be handed over into custody.\n\n\
Mr. Hannes, an experienced soldier and your superior, tries to talk the leader of the guard unit into letting him testify at Eren’s trial, but it is a thin hope. \
It’s not even certain that a proper tribunal will be held.\n\n\
You worry about what will happen to Eren and your friends, but as a prole in the Garrison, there’s nothing you can do…\n\n\
**You have obtained the "A Soldier in the Trost District Garrison" Ending.**\n\n\
**To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P217(self, *option):
        if option == ():
            response = 'Krista is assigned to the same location as you. She ties up her horse carefully, and checks on the other animals. The horses seem to like her.\n\n\
Having ascended into the branches of a huge tree with vertical maneuvering, her voice shakes with fear as she says quietly, “I wonder if the others are all… okay…”\n\n\
It’s just like her to put her concern for everyone else ahead of herself; what a thoughtful girl she is.\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 320

    def P218(self, *option):
        if option == ():
            response = 'You leap into battle, despite having no real plan. If you can just help your comrades underground mount a counterattack…\n\n\
But against the intelligent, calculating Titan, you have no chance. She grabs your wire in one hand and slams you against a building.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 146

    def P219(self, *option):
        if option == ():
            response = 'You agree with Armin. He gives you a weak smile.\n\n\
“But,” he says, “I do understand… how terrible it is.”\n\n\
**Your Affinity with Armin has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.armin += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 240

    def P220(self, *option):
        if option == ():
            response = 'You hide on either side of the road and wait.\n\n\
From the direction of the forest entrance you hear several horses on the run, along with the booming footsteps of a Titan.\n\n\
It’s Squad Levi. Eren is there, too. And the Female Titan is right behind them. Eren is in danger!\n\n\
Wait, no. They were using him to draw her out.\n\n'
            if self.state.flags.killcount > 0:
                response += 'You realize a great many sacrificed themselves to buy you this moment.\n\n\
**The Kill Count has increased by 6.**\n\n'
                self.state.flags.killcount += 6
            response += 'At that instant, Commander Erwin gives the order.\n\n\
“Fire!”\n\n\
There are flashes of light, roars; the smoke of explosions goes up. From the overturned carts shoot countless huge arrowheads.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 167

    def P221(self, *option):
        if option == ():
            response = 'At that moment, you hear a voice from the woods.\n\n\
“Fire!”\n\n\
You recognized the voice. It’s Commander Erwin.\n\n\
At the same time, the forest is lit up by flashes of light and shaken by tremendous explosions. They come from just behind you, on either side of the road. The immediate area fills with smoke.\n\n\
What in the world just happened?\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 167

    def P222(self, *option):
        if option == ():
            response = 'The Female Titan, liquid dripping from both eye sockets, quickly puts one of the giant trees behind her and covers the back of her neck with her arms. \
Most likely, she means to protect her weak spot at the nape of her neck while waiting for her eyes to regenerate. Not only is this Titan intelligent, she knows how to fight.\n\n\
Her eyes steam, starting to heal. The three soldiers, however, seem to have anticipated this. They launch themselves at her, one after another, refusing to allow any opening. \
They’re targeting the tendons in her arms.\n\n\
Chances are you have about a minute until the Titan gets her eyes back. They have to end this fight before then. This is a high-level battle conducted by experienced combatants. All you can do is watch…\n\n\
The combined attack succeeds in cutting the tendons of the Titan’s arms, which fall useless to her sides.\n\n\
It hasn’t even been thirty seconds yet. Victory is in sight.\n\n\
The soldiers prepare to strike the finishing blow…\n\n\
You…\n\n\
1️⃣ Watch, and pray for victory\n\n\
2️⃣ Jump into the fray yourself'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 214
        elif option[0] == 2:
            self.cur_page[0] = 109
        elif option[0] == 's':
            self.cur_page[0] = 208

    def P223(self, *option):
        if option == ():
            response = '**Your Affinity with Jean has increased by 1!**\n\n\
Armin and Reiner agree. Despite your collective shaking, you’re ready to face her.\n\n\
“Let’s put up our hoods to hide our faces,” Armin suggests. “If she doesn’t know which one of us might be Eren, she’ll have to avoid killing us.”\n\n\
“Well, gee, that makes me feel better,” Reiner says.\n\n\
The four of you follow his advice, putting up your hoods and approaching the Female Titan.\n\n\
“Okay, listen up. The name of the game is to slow her down,” Jean says. “If we can cut the tendons in her feet, that’ll be enough. Let’s not pretend we’re gonna finish this fight here.”\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.jean += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 126

    def P224(self, *option):
        if option == ():
            response = 'You come out to the surface. A massive hand approaches and grabs you. You struggle, trying to gain even the smallest amount of time.\n\n\
You’re lifted through the air. The Female Titan’s merciless eyes look at you.\n\n\
When she sees that you’re not Eren… she squeezes.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 146

    def P225(self, *option):
        if option == ():
            response = 'Connie smiles wryly. “She’s a nut, huh? She could’ve joined the MPs, but she goes Survey Corps? Well, I guess I’m not one to talk.”\n\n\
Mikasa, her expression never changing, says, “Sasha’s intuition is sometimes strikingly accurate. Usually for the worse.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 137

    def P226(self, *option):
        if option == ():
            response = '“I’ll… I’ll do it!” Eren yells.\n\n\
The members of Squad Levi look a bit panicked. Only Captain Levi himself gets a small, quiet smile on his face.\n\n\
Eren bites decisively into his own hand. There’s a roar like thunder, and the dim forest is filled with light.\n\n\
You all ride away on your horses. Behind you there’s a massive impact; the earth shakes.\n\n\
It’s Eren, now a Titan, blocking the path of the Female Titan, who has come running.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 231

    def P227(self, *option):
        if option == ():
            response = 'You’re riding alone.\n\n\
You see several smoke signals go up over the right wing. The whole formation seems to be falling apart.\n\n\
It’s hard to get a sense of your location within the formation as a whole, because it never stops moving. You waste a good deal of time getting lost, but at last you find your way to a unit at the center.\n\n\
You’ve come to…\n\n\
1️⃣ Squad Levi, which is protecting Eren\n\n\
2️⃣ The central command unit, where Hange and Commander Erwin are'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 234
        elif option[0] == 2:
            self.cur_page[0] = 238

    def P228(self, *option):
        if option == ():
            response = 'You volunteer to accompany Krista as reinforcements.\n\n\
Ymir looks at Bertolt, who’s growing more and more pale, and says, “I’ll stick with this guy. I’m worried about him.”\n\n\
You find this a little odd; Ymir is usually joined to Krista at the hip. But then again, there’s not much room for personal feelings when you have a job to do.\n\n\
You and Krista set out to help.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 283

    def P229(self, *option):
        if option == ():
            response = '**Your Affinity with Mikasa has increased by 1!**\n\n\
You and Mikasa proceed through the dim forest, huge trees rising up on every side.\n\n\
You hear noises far away. Given the distance, you can tell how loud they must be. Mikasa is heading straight for them, and you follow after her.\n\n\
The sounds get louder and louder. They seem to be coming from something striking so hard that even the massive trees of this forest are being broken in half.\n\n\
Then, suddenly, they stop.\n\n\
At the same instant, you emerge into an open, treeless area.\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.mikasa += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 236

    def P230(self, *option):
        if option == ():
            response = 'You consider climbing up the defensive barrier- Wall Sina. It would take most of the gas in your Vertical Maneuvering Equipment, not to mention a lot of time, \
to climb something as tall as the outer wall. But if you don’t position yourself up there, there’s a good chance you would be unable to catch up with the Female Titan if she made for the wall. \
Granted, if she goes anywhere else, your move will be for naught...\n\n\
You have the resupply squad give you more gas, then head for the outer wall and work your way up.\n\n\
The only question now is, have you made the right choice?\n\n\
From the top of Wall Sina, 50 meters up, you can look out over the whole town. You see many buildings reduced to rubble. The awfulness of a Titan rampaging through a human city finally comes home to you.\n\n\
**The Kill Count has increased by 20.**\n\n\
Type 1️⃣ to continue.'
            self.state.flags.killcount += 20
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 273

    def P231(self, *option):
        if option == ():
            response = 'Eren, in Titan form, shoves the Female Titan to the ground and holds her down. With an unearthly bellow, he moves in to take a bite out of her neck.\n\n\
The Female Titan grabs Eren’s arm with a lightning-quick movement. She twists her body to push him away, lifting him up, then kicks him back.\n\n\
Eren slams into a giant tree, but he immediately rises, winds up, and launches a punch. The Female Titan narrowly dodges, falling on the ground. Eren, too, tumbles over with his own momentum.\n\n\
Two 15-meter Titans are in front of you. You never imagined such large creatures could move and strike with such speed. The impact as they hit the ground shakes the air so violently that even you, \
floating some distance away, find yourself wavering with it.\n\n\
As for the forest floor, it must be shaking like an earthquake.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 232
    
    def P232(self, *option):
        if option == ():
            response = 'Two 15-meter Titans are engaged in a hand-to-hand battle the likes of which has never been seen before.\n\n\
Eren howls, and even that is enough to shake the air. Next to these monsters, the massive trees look no larger than their average-sized cousins.\n\n\
All you can do is watch this awesome combat. What could one small human, a mere rookie soldier, do?\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 278

    def P233(self, *option):
        if option == ():
            response = 'Krista, Ymir, and Bertolt are all in the unit you’ve been assigned to.\n\n\
You’re at the very back of the formation. There are many wagons carrying supplies to support the forward troops, along with plenty of extra horses. \
If someone in another unit loses their mount, a new one can be sent from here.\n\n\
Speaking of horses, Krista seems to have quite an affinity for them. During your month of training, not only her own animal, but many of the other horses grew to like her very much. \
Even the experienced members of the Survey Corps were impressed. Maybe that’s why they posted her here.\n\n\
You relax a little. This is the tail. If anyone’s going to run into any Titans, it will be the units in front of you. Your current spot seems awfully safe…\n\n\
You catch Krista murmuring, “I hope everyone’s okay… I would hate for us to be safe back here while they were dealing with all the danger…”\n\n\
What a sweet girl. You feel a little guilty for thinking only of yourself.\n\n\
“It’s a little early to relax,” Ymir says. “Who knows? Maybe some fleet-footed Titan will rush us from behind or something.” She doesn’t sound very pleased about the idea. \
Then she says, “And you, Krista. Worry about yourself before you go thinking about others. Outside the walls, there’s nowhere completely safe.”\n\n\
Bertolt, for his part, is muttering something to himself. You don’t blame him for being nervous: you’re taking your lives in your hands on this expedition.\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 133

    def P234(self, *option):
        if option == ():
            response = 'You link up with Captain Levi’s squadron. Eren is here, too.\n\n\
“I understand what you’re saying. Stay here with my unit,” Captain Levi says to you.\n\n\
It seems some new information arrived while you were wandering around. One of the other soldiers is kind enough to bring you up to speed: the formation’s right wing is in shambles, \
and the “Female Titan” has destroyed several units.\n\n\
“Thankfully, no one’s been killed- or so we’re told. I don’t know if it’s true,” Gunther, one of the soldiers, says.\n\n\
However that may be, this unexpected development prompts the entire formation to make a major change in direction. As you progress forward, you see giant trees in the distance.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 141

    def P235(self, *option):
        if option == ():
            response = '“Ohh… Of all the luck… To be posted here,” Sasha mutters.\n\n\
You ask her what she means.\n\n\
“We’re ‘outside the wall’ in terms of the whole formation. If any Titans wander by and attack us, they’ll come here for sure. Not that I’m saying I want them to attack my friends somewhere else…”\n\n\
You appreciate what she’s saying, but you wonder if maybe she’s being a little overanxious.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 179

    def P236(self, *option):
        if option == ():
            response = 'There you see two 15-meter-tall Titans.\n\n\
The trees around you, dozens of meters tall themselves, are bent and broken. The sounds you were hearing must have been these monsters fighting.\n\n\
One of them has long golden hair and a feminine body- the Female Titan.\n\n\
The other one is slumped on the ground and missing its head. Is that Eren in his Titan form?\n\n\
You realize there are corpses in the area, belonging to soldiers of the Survey Corps. There must have been a tremendous battle here- but it’s obviously over now.\n\n\
The Female Titan appears to have won.\n\n\
**The Kill Count has increased by 10.**\n\n\
The Female Titan opens her mouth wide and bites down on her defeated foe.\n\n\
“Eren!” Mikasa screams from beside you. So it was him.\n\n\
You take it all in: Eren’s body, being ripped from the fallen Titan… and swallowed by the Female Titan.\n\n\
When she has done this, the Female Titan stands up, her back to you. She runs into the forest in the opposite direction from where your friends in the Survey Corps are.\n\n\
“Wait… Don’t go, Eren…” Mikasa says in a thin voice, almost weeping.\n\n\
But this moment of vulnerability lasts for no more than an instant. Her face hardens into an expression of resolve, and with a burst of gas from her Vertical Maneuvering Equipment, \
she sets off after the Female Titan.\n\n\
You follow her.\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.petra = 'Dead'
            self.state.statuses.oluo = 'Dead'
            self.state.statuses.gunther = 'Dead'
            self.state.statuses.eld = 'Dead'
            self.state.flags.killcount += 10
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 153

    def P237(self, *option):
        if option == ():
            response = 'You doubt Mikasa expected a fellow soldier to interfere with her at this moment. She tumbles from the wall with an expression of shock. \
Halfway down, though, she fires her anchors, lodging them in the wall- but she’s too late. It will take her time to scale the wall again.\n\n\
With that window of opportunity, the Female Titan uses her remaining hand to climb to the top of the wall.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.affinities.annie >= 2:
                self.cur_page[0] = 314
            else:
                self.cur_page[0] = 209

    def P238(self, *option):
        if option == ():
            response = 'You head for the center-front commander squadron. In addition to Commander Erwin, Squad Leader Hange is there, along with Mike.\n\n\
“Thanks for your report,” Hange says, nodding at what you have to say. “So there’s a Titan who shows intelligence…” The researcher appears profoundly interested, but not surprised. \
Perhaps there had already been speculation about the existence of such a Titan.\n\n\
This unit is trailing a large number of wagons. You suppose they’re hauling resources for the supply depot.\n\n\
Hange spots you staring at the wagons and says, “Now that you’ve made contact with our unit, there isn’t much choice. For the sake of secrecy, you’d better stick with us.”\n\n\
Thus you end up joining the command unit. Information flows into it from every quarter- including news that the right wing has been shattered, and the “Female Titan” has destroyed several units…\n\n\
“The reports also claim, though, that this Titan hasn’t killed any humans,” Hange says. “Although we can’t be sure the information is correct…”\n\n\
After Commander Erwin hears your report, he seems to come to some kind of decision. He issues new orders, and the whole formation makes a major shift in direction.\n\n\
As you progress forward, you see giant trees in the distance.\n\n\
**Your Affinity with Hange has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.hange += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 197

    def P239(self, *option):
        if option == ():
            response = '“Yeah, you’re right… Maybe I can find my horse if I check the area.” Jean has a strained smile on his face. “Heh. To think… We all manage to cheat death, just to wind up like this.”\n\n\
The barb seems directed less at you than fate itself.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 168

    def P240(self, *option):
        if option == ():
            response = '“It’s easy to say what should have been done after you already know the outcome,” Armin says. “Maybe the commander is an unfeeling and terrible person. \
But he considered the possible developments and then made his choice. A hundred of the lives of our comrades? Or the entirety of humanity inside the walls? He had to decide. And he did.”\n\n\
Armin looks back at you. He seems so… adult.\n\n\
“I haven’t lived very long, but there’s something I’m sure of,” he says. “A person who can really change things is a person who’s able to give up what matters to them. \
People who can’t let go of anything are people who can’t change anything.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 309

    def P241(self, *option):
        if option == ():
            response = 'You see the body of a 15-meter Titan, headless and slumped against a giant tree. Then you realize: it’s Eren in his Titan form.\n\n\
All around you the trees, dozens of meters tall, are bent and broken. There’s a huge gouge in the earth. Did Eren transform and go into hand-to-hand combat with another Titan?\n\n\
“It’s the female,” Captain Levi says.\n\n\
But wasn’t the Female Titan eaten up by the horde of Titans earlier?\n\n\
“If she’s anything like Eren, then it wouldn’t be surprising if the human inside could escape in the confusion and transform again later.”\n\n\
He maneuvers down toward the ground. You follow him. The bodies of several soldiers wearing Survey Corps uniforms are there. They’re twisted and broken, dead.\n\n\
From there, Levi conducts a sweep of the area. There are four bodies in total. They account for the entire Special Operations Squad, Levi’s handpicked subordinates. The bodies hardly bear looking at.\n\n\
There was obviously a huge battle here- did they die protecting Eren?\n\n\
Levi says nothing, and there’s nothing you can say to him.\n\n\
**The Kill Count has increased by 4.**\n\n\
Finally Levi lands on the body of the Titan Eren. The body is dissipating in a cloud of steam, but it doesn’t seem to have been long since the fight ended.\n\n\
“I don’t see Eren,” Levi reports. “Let’s go.”\n\n\
With a burst of gas from his Vertical Maneuvering Equipment, he makes for the interior of the forest. You follow him.\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.petra = 'Dead'
            self.state.statuses.oluo = 'Dead'
            self.state.statuses.gunther = 'Dead'
            self.state.statuses.eld = 'Dead'
            self.state.flags.killcount += 4
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 154

    def P242(self, *option):
        if option == ():
            response = 'You hear Annie’s voice: “Haha!”\n\n\
You look in her direction. Somehow she is free of her gag.\n\n\
She looks at you, her eyes strangely sad. “There’s no going back now,” she says. “You should realize that, if you know about me. I made sure to have a few tricks ready.”\n\n\
It looks like Annie had the upper hand all along. Maybe she’s had these “tricks” ready since the moment you found out about her ring.\n\n\
You run, desperate to get away from that place.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 292

    def P243(self, *option):
        if option == ():
            response = 'To watch Levi and Mikasa move is astounding. While Mikasa has the Female Titan distracted, Levi gets in close. The Titan stretches out her arm, but he spins up it, \
drawing his swords, slashing at her face, driving his blades into both her eyes at once. Once he has blinded her, he brings his weapons around and starts cutting her body everywhere he can reach.\n\n\
Suddenly the Female Titan crouches on the ground, protecting her head with both hands. Levi doesn’t slow down, but strikes at her arms, cutting the tendons.\n\n\
Now her head and neck are exposed. Mikasa moves in to attack.\n\n\
“No, don’t!” Levi calls. The Female Titan’s arm comes up with incredible speed. It nearly catches Mikasa, but Levi protects her. There’s a dull thud.\n\n\
Levi cuts the Titan’s cheek. The mouth is open, exposing… something. A human body, drenched in liquid. Eren.\n\n\
Levi grabs Eren in his arms and quickly falls back.\n\n\
All of this takes hardly any time at all. You can only look on, dumbfounded.\n\n\
Levi’s voice draws you back to the present. “Come on, we’re getting out of here!”\n\n\
He’s still carrying the sopping Eren. The boy appears to be alive.\n\n\
Mikasa looks back at the Female Titan, hesitating for an instant.\n\n\
“Fall back,” Levi says to her. “Don’t forget what the real objective of this operation is. Your precious friend, right?”\n\n\
Finally, Mikasa nods.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 244

    def P244(self, *option):
        if option == ():
            response = 'The Female Titan leans against one of the massive trees, not moving her arms or legs, her ruined jaw agape.\n\n\
In this state, it seems as if even you could finish her off- but then again, she may yet be hiding some further strength or power. Steam rises from her body; second by second she heals herself.\n\n\
You presume Captain Levi’s judgement is correct. There are other Titans nearby. Right now, your priority should be to retreat and get Eren to a safe place.\n\n\
Mikasa is carrying Eren now. Levi is increasing your distance to the Titan, his swords out, keeping a vigilant watch on the area.\n\n\
The three of you leave that place. The Female Titan doesn’t pursue you. You sneak a last backward glance at the Female Titan before she disappears from view. A clear liquid is coming out of her eyes. \
It’s almost as if she’s crying.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 125

    def P245(self, *option):
        if option == ():
            response = '“Captain Levi, sir!” a middle-aged man calls out from the middle of the crowd, running up to the captain. “My daughter is in your care. I’m Petra’s father.”\n\n\
The man scratches his head as if embarrassed, then produces an envelope. “I just- ahem. I just wanted to get a word in with you before my daughter found me. \
She’s written a little letter, see? Talks about how she’s going to serve with you, give you her everything… Ha ha ha. It looks like the girl went and fell in love without a thought for her poor old Pa!”\n\n\
Petra’s father looks around, then focuses on Levi again.\n\n\
“Erm… well. It’s just that… as her father, I think it’s a bit soon for her to be a bride. She’s still so young, and she’s got so much ahead of her…”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.petra == 'Alive':
                self.cur_page[0] = 300
            else:
                self.cur_page[0] = 131

    def P246(self, *option):
        if option == ():
            response = 'You move toward Eren, intending to help him. Eren, in Titan form, is facing down the Female Titan. After every exchange of blows, they back away from each other again.\n\n\
Eren isn’t in a mad rage; he’s working in tandem with the soldiers flying around with their Vertical Maneuvering Equipment. When the soldiers manage to constrain the Female Titan, he attacks. \
He also seems to understand when they alert him to where the enemy is.\n\n\
You try to distract the enemy in hopes of helping Eren. He seems to see you.\n\n\
**Your Affinity with Eren has increased by 1!**\n\n\
You’re sure Mikasa and Armin must be around here, too, if they’re still alive. You do your best to help bring down the foe while aiding Eren.\n\n\
You think you hear two voices talking somewhere in the fray:\n\n\
“It looks like Eren was able to keep control of himself this time.”\n\n\
“It’s because I lost my head that the unit was robbed of its main fighting power. I’ll finish what I started.”\n\n\
Could that be Armin and Mikasa? You’ve been fighting with such intensity, though, that it’s possible you just imagined the conversation.\n\n\
Eren may not be berserk this time, but even so, when two 15-meter Titans go hand-to-hand, the battle is spectacular. Their bodies slam into tall buildings, every encounter producing more destruction.\n\n\
**The Kill Count has increased by 20.** All the buildings that are destroyed in this fight result in no small number of civilian casualties. This collateral damage is beyond your control….\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.eren += 1
            self.state.flags.killcount += 20
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 307

    def P247(self, *option):
        if option == ():
            response = 'You somehow manage to get back to Karanes District. You’re walking down the main boulevard.\n\n\
You’ve dismounted and are trudging along on exhausted feet, leading an equally fatigued horse by the reins. You look around: everyone appears as pathetic as you feel. \
Did even half of your number survive this expedition?\n\n\
The supply wagons are virtually gone. Eren is lying in one of the few that remain, Mikasa and Armin are tending to him. You see he’s opened his eyes. At least he’s alive.\n\n\
Citizens of Karanes District line both sides of the road. They seem to be there mostly to gawk.\n\n\
“They went out with all that pomp- and they come back like this?” someone says.\n\n\
“What the hell was this expedition supposed to do? Just waste our tax money?”\n\n\
The words are cruel, heartless. What do these people know…?\n\n\
Suddenly you hear another voice, a voice of welcome, coming from the crowd. You look and see two children, their eyes shining as they watch your procession.\n\n\
“Wow, cool! The Survey Corps is all beat up, but they’re still fighting!”\n\n\
The children raise their voices in heartfelt admiration. To those of you marching along, it hurts even more than the vicious criticism of the adults.\n\n\
Your comrades’ faces betray the heaviness of their hearts. In the supply wagon Eren, along with Armin and Mikasa, looks at the ground, hanging his head at some memory.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 245

    def P248(self, *option):
        if option == ():
            response = 'Commander Erwin is pulled into a different group of buzzing voices.\n\n\
“I’ve got a question, Commander!”\n\n\
“Did this expedition achieve anything to justify this number of losses?”\n\n\
“Don’t you care about all those dead soldiers?!”\n\n\
They’re reporters, come to learn the news about the expedition outside the walls. Again and again they repeat the same merciless criticisms of the Survey Corps. \
Commander Erwin’s expression never changes; he accepts it all quietly.\n\n\
The failure of this operation, compounded by your tremendous losses, does significant damage to the Survey Corps’ position. \
You receive word that Commander Erwin and all those under him who have been deemed responsible are being summoned to the capital, and that they are to hand over Eren…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 249

    def P249(self, *option):
        if option == ():
            response = 'Several days pass.\n\n\
Tomorrow is the day you are to be transported to Stohess District under guard.\n\n\
You and the other rookies from the 104th Training Corps are gathered in the temporary barracks in Karanes District. \
Eren is already in the custody of the Military Police Brigade, and is confined in another room. The rest of your friends, however, are all here.\n\n\
Every face is dark. The leaders of the Survey Corps are almost certain to receive some kind of disciplinary action. What will become of you new recruits? \
A few rookies were even summoned to the capital along with the commanders.\n\n\
The MPs gave you a list of those who were selected for the tribunal. It seems to consist mostly of people close to Eren. Mikasa, Armin, and Jean are on it- and for better or worse, so are you.\n\n\
Your friends are worried; Krista and Reiner genuinely seem to want to go with you, but they aren’t on the list, and you have to be careful not to do anything that might make the tribunal suspicious.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 2491

    def P2491(self, *option):
        if option == ():
            response = '“Everyone, listen to me,” Armin says, coming into the room with Mikasa and Hange. “We’ve got a plan to help Eren escape. \
Commander Erwin and the rest of the Survey Corps leaders have given their approval, and they’ll help us. What about the rest of you? Can we count on you?”\n\n\
Shock runs through the room. People fling questions at Armin.\n\n\
“Help him escape? Escape where? There’s nowhere inside the walls that would be safe,” Reiner says.\n\n\
“It would just be a temporary measure until circumstances change,” Armin says. “If Eren is taken to the capital, there’s a good chance they would execute him immediately. We need to avoid that.”\n\n\
“Do you have some way of getting him out of Stohess, then? Or are you planning an infiltration?” Jean’s question is eminently practical.\n\n\
“Well… I’m hoping you can all help me think of something,” Armin says uneasily. “And… I can’t reveal the entire plan to everyone. \
I know it’s a lot, asking you to help me when I can’t tell you what you’re helping with…”\n\n\
“Can’t trust even us, huh? That hurts,” Reiner says, frowning.\n\n\
“Heh! Fine by me,” Jean says. “I don’t want to end up tortured by the Military Police because I’ve heard your dumb secrets. Let Armin do that.”\n\n\
Everyone is surprised, but no one objects. You all want to help Eren.\n\n\
And so you set about concocting a plan to break him free…\n\n'
            if self.state.flags.keyA == 'Yes' and self.state.flags.keyY == 'Yes':
                response += '**You have both Keys A and Y! Add the numbers associated with them together. What do you get?**\n\n\
1️⃣ 117\n\n\
2️⃣ 140\n\n\
3️⃣ 177\n\n\
4️⃣ 217'
                self.choices[0] = [1,2,3,4]
            else:
                response += 'Type 1️⃣ to continue.'
                self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 250
        elif option[0] == 2:
            self.cur_page[0] = 250
        elif option[0] == 3:
            self.cur_page[0] = 177
        elif option[0] == 4:
            self.cur_page[0] = 250

    def P250(self, *option):
        if option == ():
            response = '“Please, everyone, help think of some way to help Eren escape,” Armin says.\n\n\
Your friends offer various ideas. What do you suggest?\n\n\
1️⃣ Get help from Annie, who’s with the MP Brigade now\n\n\
2️⃣ Have Eren turn into a Titan in the city and go on a rampage\n\n\
3️⃣ Have Jean act as a body double to buy time'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 171
        elif option[0] == 2:
            self.cur_page[0] = 310
        elif option[0] == 3:
            self.cur_page[0] = 305

    def P251(self, *option):
        if option == ():
            response = 'You continue your planning session.\n\n\
You collectively decide that Jean will dress up as Eren, while Eren will hide out in Stohess District in disguise. You’ll try to get help from Annie in the MP Brigade as well. \
You even figure out where you’ll get the disguises.\n\n\
There’s a lot of unknowns to this plan. It might even seem a little crazy. But you have no choice except to try.\n\n\
You make all your preparations and review once more.\n\n\
The next day arrives. You make a show of obeying the Military Police, accompanying the transit column as ordered…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 261

    def P252(self, *option):
        if option == ():
            response = 'The new Titan, the female one, moves with unexpected speed. Squad Leader Ness and Siss ride up on either side of her as they did with the other Titan, then place anchors in her body. \
They simultaneously fly at her with vertical maneuvering.\n\n\
The Female Titan, however, grabs Siss clean out of the air, crushing him. Then she reaches behind herself to grab the wire lodged in her back, slamming Squad Leader Ness into the ground.\n\n\
Her movements are cold, efficient. The bodies of the two experienced soldiers tremble along the ground, now nothing more than corpses.\n\n\
**The Kill Count has increased by 1.**\n\n\
A shock runs through you. This Titan almost seems to be intelligent. She hasn’t tried to eat her human victims, either, but has simply killed them out of necessity.\n\n\
Now, the Female Titan is running at you and Armin with undiminished speed.\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.dieter = 'Dead'
            self.state.statuses.lukesiss = 'Dead'
            self.state.flags.killcount += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 162

    def P253(self, *option):
        if option == ():
            response = 'You shout.\n\n\
You’re determined to bet on whatever action Eren chooses to take. Captain Levi seems to have the same thing in mind.\n\n\
Eren, resolved, nods at your words.\n\n\
**Your Affinity with Eren and Levi has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.eren += 1
            self.state.affinities.levi += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 135

    def P254(self, *option):
        if option == ():
            response = 'The group of men and women fall on Annie, trying to capture her. They pin her arms behind her back and stuff a gag in her mouth so she can’t bite her hands or her tongue.\n\n\
Annie struggles, wiggling her fingers. You see a large ring on the pointer finger of her right hand.\n\n\
That ring…\n\n\
“Run!” Mikasa shouts suddenly. She grabs Eren and Armin each by the sleeve and dives down the stairs as fast as she can. You follow her with equal fervor.\n\n\
You glance back. At the edge of your vision, you can see a small spray of blood from Annie’s right hand. You understand instantly: the ring had some kind of device in it. \
Pain is the stimulus needed to transform into a Titan.\n\n\
A light erupts behind you. You hear an explosion and feel an impact.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 207

    def P255(self, *option):
        if option == ():
            response = '“He’s such a weak little boy, and yet he’s still alive,” Ymir says, her voice laced with irony.\n\n\
“Don’t say that,” Krista replies. “Armin is a great man.”\n\n\
“He’s a stupid man. Why would someone as weak as him volunteer for the Survey Corps?”\n\n\
“He has really sharp eyes,” Bertolt says. “Sometimes he notices things I didn’t even think about. And he knows how terrifying the Titans are, but he chose this path anyway.” \
His voice is shaking as he speaks. “I think that’s really impressive.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 194

    def P256(self, *option):
        if option == ():
            response = 'You’re on guard with Armin and Jean.\n\n\
Jean seems to be in a bad mood. You can’t really blame him: you’ve been assigned a seemingly ridiculous task with almost no explanation.\n\n\
For a while, you stay there, keeping the Titans at bay. Maybe some of them possess the ability to learn, because eventually a few begin climbing the trees. \
Apparently this isn’t going to be a milk run. You keep distracting the Titans, avoiding the Titans… Somehow you manage to do your duty.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 181

    def P257(self, *option):
        if option == ():
            response = 'As you head towards the smoke signal, a single soldier emerges from the shadows of the giant trees using vertical maneuvering. \
They’re wearing a Survey Corps cape, but the hood is pulled up, so you can’t see their face. Could it be Captain Levi? No…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 176

    def P258(self, *option):
        if option == ():
            response = 'A blinding light fills the area, along with a sound like a thunderclap.\n\n\
Something breaks through the ceiling of the underground tunnel, expanding outward. You realize that a massive body has appeared and is protecting you.\n\n\
You look up. It’s a 15-meter Titan: Eren.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 289

    def P259(self, *option):
        if option == ():
            response = 'You’re not sure how much time has passed when something changes. A panoply of smoke signals goes up from the right wing in quick succession. \
They seem to have encountered some major threat.\n\n\
A single mounted messenger rides up. You can hear their report from where you are.\n\n\
“We were attacked. Multiple Titans. Powerful individuals confirmed.” Then, “Right wing destroyed in combat. We’ve lost our enemy-scouting capabilities in that zone!”\n\n\
**The Kill Count has increased by 5.**\n\n\
Nervousness runs through Squad Levi. A messenger is sent to inform the nearby squadrons. Another volley of smoke signals goes up from the right, closer than before. \
The danger is coming nearer, deep into the formation…\n\n\
You see another signal, this time from the front. It’s the order to change directions. The command unit, led by Commander Erwin, must have intuited the danger and reacted. \
The entire formation makes a major change in direction.\n\n\
“Hang on,” Gunther says. “Isn’t the… you know. Isn’t it this way?”\n\n\
As you progress forward, you see giant trees in the distance.\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.dieter = 'Dead'
            self.state.statuses.lukesiss = 'Dead'
            self.state.flags.killcount += 5
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 141

    def P260(self, *option):
        if option == ():
            response = 'Armin says, “Sure. I planned to stay behind all along.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 168

    def P261(self, *option):
        if option == ():
            response = 'You enter Stohess District, inside Wall Sina, watched closely by the Military Police Brigade.\n\n\
Eren is in a prison wagon, and also under heavy guard. Although Commander Erwin and the other members of the Survey Corps have been relieved of their weapons and equipment, \
they’re being treated as part of the attending detachment; the watch on them seems to be largely pro forma. At least for now.\n\n\
The first phase of your plan has gone staggeringly well. Partly it’s because you’ve done such a good job of appearing obedient, but it helps that the MPs aren’t working too hard at their duties, either.\n\n\
After you enter Stohess District, you find an opportune moment for Jean, in disguise, to switch places with Eren in the prison wagon. \
Eren runs away, using the hooded rain gear you’ve prepared to pass him off as a porter.\n\n\
Three other people here are wearing the same outfit: Armin, Mikasa… and you. Together, you vanish into Stohess’s twisting back streets.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 262

    def P262(self, *option):
        if option == ():
            response = 'You’re wearing the same disguise as Eren and the others, a hooded raincoat that covers your entire body, along with a large porter’s box on your back. \
The loose rain gear neatly covers your Vertical Maneuvering Equipment. Two long scabbards, when tucked horizontally across the body, are surprisingly inconspicuous.\n\n\
Once you’re safely in the side alleys, Armin breaks away to make contact with Annie.\n\n\
“I wonder if Annie will really help us,” Eren mutters. He sounds nervous.\n\n\
“If she refuses, we’ll decide what to do then,” Mikasa says dispassionately. “Even if she won’t come to us, Armin… \
Armin of all people should be able to get something useful from her. Information or something.”\n\n\
You wait, feeling as anxious as Eren. If anyone discovers you here, all you’ve done will be in vain. You don’t wait very long, but it feels like ages.\n\n\
At last, Armin comes back. He has Annie, wearing a Military Police Brigade uniform, in tow.\n\n\
“Armin told me what’s going on,” she says. “Count me in.”\n\n\
“Th-Thank goodness, Annie,” Eren says. He looks deeply relieved- and yet somewhat nervous. He seems glad to have Annie along, but not entirely trusting of her. \
Mikasa doesn’t speak, nor does her expression change.\n\n\
“Let’s go,” Armin says.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 303

    def P263(self, *option):
        if option == ():
            response = 'Using vertical maneuvering, you flee the forest. What more can a mere rookie do? Fortunately, you manage to find a horse before you run out of gas. \
You mount up and ride off, galloping out of the dark woods at full tilt.\n\n\
The sunlight that washes over you once more as you emerge from among the giant trees is a tremendous relief. The main unit, which had retreated, is there too. You make your report.\n\n\
At last information filters in. After you left, Mikasa linked up with Captain Levi and they were able to save Eren.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 130

    def P264(self, *option):
        if option == ():
            response = 'You get out of there as fast as you can.\n\n\
A few minutes later, you hear a sound like thunder and a scream, and another Titan appears. Eren has transformed.\n\n\
The two Titans begin to battle. You wonder whose side you should take…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 289

    def P265(self, *option):
        if option == ():
            response = 'Armin, Eren, and Mikasa hurry underground, but Annie stays at the top of the stairs. Is she watching for something?\n\n\
You take a look, too. The stairway is about four or five meters wide, and continues at that width down underground. It’s large enough for three people to walk abreast.\n\n\
“What are you doing?” Eren asks Annie when he notices that she hasn’t followed them. “Don’t tell me you’re claustrophobic.”\n\n\
“Yeah, that’s right, I’m scared,” Annie replies. “Not that I’d expect that suicidal bastard to understand the feelings of a delicate maiden like me.”\n\n\
Eren must think she’s kidding, because he shouts, “Don’t be stupid! Hurry up and get down here!” Yet Annie doesn’t come.\n\n\
“It’s too scary. Come back up here, or I won’t help you.”\n\n\
“What the hell are you even talking about?! Get down here already!”\n\n\
“Eren, don’t shout,” Mikasa says, trying to rein him in.\n\n\
Annie, however, says, “I’m sure it’s fine, Mikasa. For some reason this area’s been completely deserted for a while now.”\n\n\
You notice it, too. The immediate area is unnaturally empty.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 266

    def P266(self, *option):
        if option == ():
            response = '“Why are you looking at me like that, Armin? It hurts.” Annie’s voice is strange somehow.\n\n\
Armin responds with a question of his own. “Annie… Why did you have Marco’s Vertical Maneuvering Equipment?” He’s changing the subject. \
“We got our equipment together. I remember the scratches and dents on yours.”\n\n\
“Oh, that? I found it.”\n\n\
“And those two Titans we captured alive… Did you kill them, Annie?”\n\n\
“Hard to say… But if you suspected me a month ago, why didn’t you do anything then?”\n\n\
Armin looks at Annie, his eyes wide. “I can hardly believe it, even now… I want to think it’s… that it’s some mistake! That’s why I couldn’t…” He looks at the ground. \
Maybe he’s thinking of the things he might have prevented if he had listened to his gut. “But Annie,” he says to her, “you could have killed me once, and didn’t. That’s why we’re standing here now.”\n\n\
Now it’s Annie’s turn to murmur thoughtfully. “I know. And I just have to wonder… Why didn’t I…?”\n\n\
Does their conversation make any sense to you?\n\n\
“Hey!” Eren shouts. “There’s still a chance that you’re just… telling a really, really bad joke. So come here! You can prove yourself by just coming down in this tunnel!”\n\n\
“I’m sorry,” Annie says. “I can’t go down there. I wasn’t able to become a warrior.”\n\n\
“I told you to stop with the stupid drama already!”\n\n\
“Talk to us, Annie!” Armin pleads. “We can still discuss this!”\n\n\
“That’s enough. I can’t listen to this,” Mikasa says. She pulls off her rain gear and draws her sword. “I already cut you down to size once,” she spits at Annie. “And I’ll do it again… *Female Titan*.”\n\n\
Annie suddenly starts… laughing. You’ve never seen anything like it from her; she’s usually so expressionless.\n\n\
“Armin… It looks like you won your little bet,” she says. Yet she sounds triumphant as she looks down at you. “But my wager starts here.”\n\n\
Then she bares her teeth, and brings her hand to her mouth…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 275

    def P267(self, *option):
        if option == ():
            response = 'Reiner doesn’t argue. “You’re right, somebody has to stay behind,” he says. “And I’m the heaviest. It’d probably be tough even just riding double with me. It makes the most sense.”\n\n\
The tension among the four of you is palpable.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 168

    def P268(self, *option):
        if option == ():
            response = 'Before you realize what’s happening, the Titans who had been clustered around the edge of the forest ignore you and your companions and head for the interior en masse.\n\n\
It doesn’t look like there’s any point to staying here and trying to carry out your assigned orders. At length, you receive instructions to withdraw.\n\n\
You and the others jump on your horses and get out of there. It looks like the other units have all left their stations as well. There’s a flood of soldiers falling back from within the Titan Forest. \
Information filters in. You learn that a large number of casualties was suffered inside the woods. They say a horde of Titans attacked…\n\n\
They managed to bind the Female Titan once, at great cost, but she escaped and attacked again. Eren turned into a Titan and fought for them, but word is that he was defeated and captured. \
The elite Squad Levi was, you’re told, annihilated. Somehow, Captain Levi and Mikasa managed to rescue Eren… but now what?\n\n\
**The Kill Count has increased by 10.**\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.petra = 'Dead'
            self.state.statuses.oluo = 'Dead'
            self.state.statuses.gunther = 'Dead'
            self.state.statuses.eld = 'Dead'
            self.state.flags.killcount += 10
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 130

    def P269(self, *option):
        if option == ():
            response = 'At that instant, a great noise and a shock runs through the tunnel. Everything in front of you vanishes. A massive foot slams down into the space ahead of you. \
A pile of dust and debris is the result, the arms and legs of crushed soldiers sticking out here and there.\n\n\
Annie, the Female Titan, stomped down from above into the underground tunnel.\n\n\
“So, what?! Does she not care if Eren dies?!” Mikasa shouts.\n\n\
“I think she gambled that he wouldn’t be killed,” Armin says back. “Annie is hell-bent on stealing Eren from us.”\n\n\
Your group is at a desperate disadvantage now. Your escape route is blocked, and Annie is above you, watching both the stairs and this hole. \
Even if you were to jet upwards with your Vertical Maneuvering Equipment, she would attack you the moment you did so.\n\n\
“Stick close to me!” Eren calls. He raises his hand. He’s going to transform into a Titan. His transformation won’t explode the immediate area, you suspect. He’ll modulate his body to protect his friends.\n\n\
But no matter how many times Eren bites his hand, no matter that it is covered in blood, nothing happens.\n\n\
“I think you need to have your goal clearly in mind to be able to transform,” Armin says. You think you understand. Somewhere in Eren’s heart, he’s still reluctant to fight Annie.\n\n\
**The Kill Count has increased by 3.**\n\n\
Type 1️⃣ to continue.'
            self.state.flags.killcount += 3
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 285

    def P270(self, *option):
        if option == ():
            response = 'You shout to Eren. He has been hesitating, but your voice seems to resolve him.\n\n\
He turns toward the Female Titan and bites his hand in midair. There’s a flash of light and a boom, and then another TItan is standing there- Eren himself.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 231

    def P271(self, *option):
        if option == ():
            response = 'Using vertical maneuvering, you head into the Titan Forest.\n\n\
For the time being, you make for the center of the vast copse, where you heard that strange cry earlier. Sometimes you pause, perching on a massive branch to listen, to see if you can hear anything.\n\n\
You lose track of how long you spent repeating this process.\n\n\
You hear the sound of vertical maneuvering and head for it. A figure flashes among the trees. You can see a scarf trailing from its neck. It’s Mikasa. You approach her.\n\n\
“So you’re here, too,” she says, expressionless as ever.\n\n\
Mikasa’s good in a fight, and you’re glad to have her by your side.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 229

    def P272(self, *option):
        if option == ():
            response = '“Hey! What are you doing to my Krista?!”\n\n\
The voice comes suddenly, and almost as suddenly comes a blow from behind. It’s Ymir.\n\n\
You have no idea where she came from, but she has an uncanny ability to find Krista wherever she is…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 182

    def P273(self, *option):
        if option == ():
            response = 'The Female Titan knocks Eren down, then comes running towards the wall. Her speed seems to have taken even the Survey Corps by surprise.\n\n\
The Female Titan arrives at the wall, and takes a great leap onto it. She hardens the tips of her fingers, allowing her to dig into the wall and climb swiftly.\n\n\
Who could have imagined that she would be able to climb a wall while in Titan form?\n\n\
The Survey Corps has split into two units down in the city, trying to create a net to encircle her, but they can’t react quickly enough. \
The Female Titan is coming right up the wall you’re standing on, and fast.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.mikasa == 'Alive' and self.state.statuses.armin == 'Alive':
                self.cur_page[0] = 323
            else:
                self.cur_page[0] = 205

    def P274(self, *option):
        if option == ():
            response = 'There’s some kind of explosion from the woods. It sounds like cannon fire…\n\n\
A short while later, you hear something else: a bizarre cry. It sounds like a wild animal, but much bigger… Could it be the voice of a Titan?\n\n\
“I’ve heard that sound before,” Sasha says. She looks absolutely serious. “In the forest near my home… It’s the cry an animal makes when it’s cornered, and has nothing left to lose. \
I was always taught that when you’re hunting, it’s your quarry’s last moments you have to be most careful of.”\n\n\
Mikasa murmurs, “Your intuition is often right, Sasha… usually for the worse.” She lapses into thought for a moment, then says forcefully to you, “I’m going into the woods.”\n\n\
“Mikasa!” Sasha says. “Were you even listening to what I just said? If you take that forest too lightly, you’ll die!”\n\n\
The other girl is silent. You suspect she thinks her friends are in danger in those woods exactly because she heard what Sasha said.\n\n\
You…\n\n\
1️⃣ Get ready to run away with Sasha\n\n\
2️⃣ Go into the woods with Mikasa'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 268
        elif option[0] == 2:
            self.cur_page[0] = 229

    def P275(self, *option):
        if option == ():
            response = 'Suddenly, Armin produces a handgun and fires into the air. There’s a high-pitched sound- an acoustic signal round.\n\n\
Apparently on cue, several men and women appear and leap on Annie.\n\n\
Where were they hiding? They’re dressed in civilian clothes, but their movements are those of trained soldiers.\n\n\
Now, where have you been while the earlier conversation was taking place?\n\n\
1️⃣ At the mouth of the underground tunnel, near Annie\n\n\
2️⃣ Down the stairs in the underground tunnel, near Eren and Mikasa'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 312
        elif option[0] == 2:
            self.cur_page[0] = 254

    def P276(self, *option):
        if option == ():
            response = '“Oh! Thank God! And thank you!” Sasha exclaims. “I didn’t have any time to eat on horseback!”\n\n\
You’re amazed she can eat at all, given the circumstances…\n\n\
**Your Affinity with Sasha has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.sasha += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 274

    def P278(self, *option):
        if option == ():
            response = 'The battle… The battle between these two Titans defies the imagination. Eren gives himself over to his rage, while the Female Titan appears calm, responding with quick movements. \
This studied craft allows her to land a punch on Eren.\n\n\
Eren is just as powerful as she is, however. He winds up and punches back; the Female Titan goes flying through the air. There’s a crash as she slams against one of the trees.\n\n\
The Female Titan climbs to her feet again, assuming a fighting stance. Unlike most Titans, who rely blindly on their own strength, she looks like an accomplished martial artist.\n\n\
Suddenly, Eren stops moving. The chain of attacks he’s been launching ends. It’s almost as if he’s noticed something about the Female Titan, something that stays his hand…\n\n\
The Female Titan, is hardly one to let such an opening slip by. She brings her leg up to head height, performing a roundhouse kick with tremendous speed.\n\n\
Eren’s head goes flying as if it had been cut off with a sword. The head of a Titan is the size of a small horse, and now Eren’s is tumbling along the ground. \
You assume the Female Titan must have hardened her foot for the vicious kick.\n\n\
Eren’s massive body collapses to its knees. The Female Titan approaches cautiously- then opens her mouth wide. You can hear a popping sound as the flesh of her cheeks tears. \
With her mouth open unnaturally wide, the Female Titan bites down on the neck of Eren’s headless body.\n\n\
You see it: you see her extract Eren’s human body from the fallen Titan… and then swallow it.\n\n\
The Female Titan rises to her feet, her back to you. She sets off running deeper into the woods, in the opposite direction from where your Survey Corps friends are waiting.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 199

    def P279(self, *option):
        if option == ():
            response = 'Your actions succeed in distracting the assailants. Annie makes good use of the opportunity you’ve given her. She’s an accomplished martial artist, after all. \
She throws one of her attackers, then dispatches the others with a series of kicks.\n\n\
She turns to you with a sort of sneering grin.\n\n\
“Did you not know? Or is this all part of the act?” She scoffs and then says, “Get clear. I’m going to run as hard as I can.”\n\n\
You do as she says. A light shines and a roar sounds from where Annie was standing. When the dust clears, the Female Titan towers there.\n\n\
**Your Affinity with Annie has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.annie += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 264

    def P280(self, *option):
        if option == ():
            response = '“Yeah,” Reiner says with relief. “That’s the smart thing to do. We can’t die here. We have to live long enough to let them know what’s happened.”\n\n\
The four of you split up, each of you going to a different unit to report these events.\n\n\
(Your choice may have cost some of your comrades their lives, but what else could you do?)\n\n\
**The Kill Count has increased by 9.**\n\n\
Type 1️⃣ to continue.'
            self.state.flags.killcount += 9
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 227

    def P281(self, *option):
        if option == ():
            response = 'You shout your support for Captain Levi. You haven’t worked with him for very long, and you lack much experience of life- it’s possible you don’t really understand anything. \
But you could feel the weight in Levi’s words. He may claim not to know whether the choices he’s made were right, but you’re sure he could feel the responsibility he bore when making them.\n\n\
You don’t think his choices could have been wrong.\n\n\
Eren seems resolved by your words; he nods.\n\n\
**Your Affinity with Levi has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.levi += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 135

    def P282(self, *option):
        if option == ():
            response = 'Squad Leader Hange, wearing Vertical Maneuvering Equipment, has taken command of the situation.\n\n\
“It looks like Eren was able to access his powers without going berserk this time,” Hange says. “Excellent!”\n\n\
Jean is there, too: “Back up Eren! Pay attention to where he and the female are going, get there first, and cut off the escape routes!”\n\n\
You…\n\n\
1️⃣ Work with Hange\n\n\
2️⃣ Work with Jean\n\n\
3️⃣ Catch a glimpse of Levi as well'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 297
        elif option[0] == 2:
            self.cur_page[0] = 317
        elif option[0] == 3:
            self.cur_page[0] = 313

    def P283(self, *option):
        if option == ():
            response = '**Your Affinity with Krista has increased by 1!**\n\n\
You and Krista ride along, the spare horses in tow.\n\n\
You don’t see anyone for a while. Smoke signals go up here and there in the distance.\n\n\
The terrain turns grassy; you see a riderless horse.\n\n\
“That’s Jean’s horse,” Krista says.\n\n\
Krista likes horses, and back in training, all your horses seemed to like her. Jean’s animal looks scared, but it comes up to Krista. She pats its neck and it calms down.\n\n\
“Maybe Jean is nearby,” she says. “If he’s lost his horse, he’ll be in trouble. She looks deeply concerned.\n\n\
You have a bad feeling about this. The abandoned horse might mean Jean is already dead.\n\n\
A smoke signal goes up not far away, the color indicating “SOS.”\n\n\
“Let’s go!” says Krista.\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 118

    def P284(self, *option):
        if option == ():
            response = 'You’re worried about Eren and Squad Levi, and head in their direction. A smoke signal ordering a retreat was sent up, but they may not know exactly what’s going on here.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 201

    def P285(self, *option):
        if option == ():
            response = '“I’ve got a plan,” Armin says resolutely. “Mikasa and I split up. One of us comes out of that hole, and the other comes out of the entrance to the tunnel. \
Annie can only deal with one of us at a time. Then Eren can escape from whichever direction she’s not watching.”\n\n\
Mikasa nods.\n\n\
“Hey,” Eren says, ashen-faced. “That’s as good as sending one of you to your death.”\n\n\
Both of them know that, yet they each run to their place. If Eren can’t become a Titan, this is your next best bet for keeping him out of the hands of the enemy.\n\n\
“H-How… How can you guys fight?!” Eren yells.\n\n\
“What choice do we have?” Mikasa looks back at him, just for a second. “The world is a cruel place.”\n\n\
You…\n\n\
1️⃣ Join Mikasa as a decoy\n\n\
2️⃣ Join Armin as a decoy\n\n\
3️⃣ Stay with Eren'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 190
        elif option[0] == 2:
            self.cur_page[0] = 210
        elif option[0] == 3:
            self.cur_page[0] = 158

    def P286(self, *option):
        if option == ():
            response = 'Suddenly, the Female Titan takes a great inhalation- and then she screams, a blood-curdling howl that hardly seems as if it could be of this world.\n\n\
The soldiers around you cover their ears. What is she doing?\n\n\
The scream is absorbed by the forest around you… And then, as if in response, you hear a rumbling from all around: Titan footsteps. A horde of Titans is approaching from every corner of the woods.\n\n\
The Survey Corps draw their swords, but the Titans don’t so much as look at the humans. They flock to the female, biting into her body, tearing her apart.\n\n\
Titans would never normally do this. That noise the female just made… Does she have the power to command other Titans? And did she order them to consume her, \
in order to destroy whatever clues she might be hiding?\n\n\
“All hands, to battle!” Commander Erwin orders. “Protect the Female Titan with your lives!” And then, Vertical Maneuvering Equipment at the ready, he leaps into the fray himself.\n\n\
The Survey Corps commences combat with the crowd of Titans. Because the monsters are ignoring the humans, it’s a simple matter to cut them down, but there are dozens of them. Too many to deal with effectively.\n\n\
Most of the Female Titan’s body has been eaten. Between the steam rising from her body and that coming from the bodies of the defeated Titans around her, the entire area is thick with white haze. \
Everything is blurred and distorted…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 316

    def P287(self, *option):
        if option == ():
            response = 'You tell them you’ll stay behind.\n\n\
“I know someone has to stay, but…” Reiner trails off.\n\n\
Jean looks down and growls, “Damn!”\n\n\
“No,” Armin says. “I’ll do it. I’ll stay.”\n\n\
Type 1️⃣ to continue.'
            self.state.flags.stay_behind = True
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 168
            
    def P288(self, *option):
        if option == ():
            response = 'They burst out above ground, your two brave companions.\n\n\
The earth rumbles, and a massive hand smashes them mercilessly. You can see blood and chunks of flesh go flying.\n\n\
Beside you, Eren is howling. Anger and sadness: at the Female Titan, at this cruel world.\n\n\
Above all, at himself.\n\n\
Eren bites his hand. There is no more reluctance. The death of the friend he cherished has resolved him.\n\n\
Who did the Female Titan kill?\n\n\
1️⃣ Mikasa\n\n\
2️⃣ Armin'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.state.statuses.mikasa = 'Dead'
            self.cur_page[0] = 258
        elif option[0] == 2:
            self.state.statuses.armin = 'Dead'
            self.cur_page[0] = 258
            
    def P289(self, *option):
        if option == ():
            response = 'Two 15-meter Titans appear in the middle of Stohess District and start fighting each other. Nothing like it has ever happened before. \
The citizens must never have imagined that they would see Titans inside Wall Sina.\n\n\
The populace is screaming and trying to flee, but their flight is altogether disorderly. Some people stand stupefied, unable to move. Unlike Trost District, Stohess has never held a mock evacuation.\n\n\
Some soldiers from the Survey Corps show up. They weave through the city streets using vertical maneuvering.\n\n\
“Back up Eren! This time we’re not gonna let the Female get away!”\n\n\
You…\n\n\
1️⃣ Move to assist Eren\n\n\
2️⃣ Prioritize the citizens’ safety and try to coordinate the evacuation\n\n\
3️⃣ Defer to the Survey Corps leaders’ orders\n\n\
4️⃣ Focus on what the Female Titan is doing'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 246
        elif option[0] == 2:
            self.cur_page[0] = 298
        elif option[0] == 3:
            self.cur_page[0] = 282
        elif option[0] == 4:
            self.cur_page[0] = 311

    def P291(self, *option):
        if option == ():
            response = '“Best of luck!”\n\n\
You can hardly bring yourselves to do it, but you and Eren flee the area.\n\n\
The three members of Squad Levi, meanwhile, put on an incredible display. You glance back, just for an instant, to see that they’ve immobilized the Female Titan and are launching themselves at her, \
landing blow after blow. They’ve cut the tendons in her arms, rendering the limbs useless.\n\n\
Surely, that will be enough to…\n\n\
But when you look back a second later, you discover the Titan has struck back; one of the soldiers is in her mouth! The Titan takes another great leap and kicks a second squad member out of the air. \
That’s two people dead practically before you could blink, and now she’s coming right for you.\n\n\
Oluo, the last man standing, slices at her from behind, but his blade shatters, and he, too, dies a victim of one of her vicious kicks. \
The Female Titan, without the use of her arms, just dispatched three experienced soldiers in a matter of seconds…\n\n\
She must be desperate; why else would she be so ruthless and unrestrained?\n\n\
**The Kill Count has increased by 3.**\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.petra = 'Dead'
            self.state.statuses.oluo = 'Dead'
            self.state.statuses.eld = 'Dead'
            self.state.flags.killcount += 3
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 193

    def P292(self, *option):
        if option == ():
            response = 'You hurriedly run away.\n\n\
It’s the right choice. There’s a flash of light behind you, a roar and a shock wave. You’re blown forward, tumbling along the flagstones. If you had been any closer, you might have been killed.\n\n\
You look back from where you lie on the ground. Towering there in the middle of the city is the Female Titan.\n\n\
**The Kill Count has increased by 3.**\n\n\
Type 1️⃣ to continue.'
            self.state.flags.killcount += 3
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 127

    def P293(self, *option):
        if option == ():
            response = 'Squad Leader Ness and Siss set their vertical maneuvering anchors in the Titan and sweep around to attack from behind. You follow them. \
You’re not at their level, but having a third body along can’t hurt.\n\n\
The moment you try to approach the Titan’s nape, however, a massive hand grabs you.\n\n\
Titans don’t have eyes in the backs of their heads, do they? And their movements aren’t usually so quick…\n\n\
At the edge of your sight, you see Ness and Siss, already reduced to bloodly chunks of flesh. The huge fingers squeeze you, holding you immobile as the Titan looks down at you. \
She has the face of a woman, and her eyes display a human intelligence. Such cold, cold eyes.\n\n\
The Female Titan looks at your face for just a second- and then she crushes you.\n\n\
**You have died. To start over, type `~reset`.**'
            self.choices[0] = []
            return response

    def P294(self, *option):
        if option == ():
            response = 'Provisions that can be eaten on horseback were supposed to have been distributed for this expedition outside the walls, but when you ask Sasha about it, she replies, \
“I ate mine before we left. I was just so nervous…”\n\n\
With a touch of exasperation, you give her your provisions. They’re dried potatoes.\n\n\
“Oh, thank God- and thank you!” Sasha looks at you with immense gratitude for only a second before wolfing down the potatoes.\n\n\
“Hey, rookie,” one of the old hands says. “Don’t eat too much on horseback if you’re not used to it. You’ll just throw it back up.”\n\n\
“I would never throw up precious, precious food,” Sasha says. She looks uncharacteristically serious. Maybe she’s thinking back to the Battle of Trost, \
the terrible way the Titans ate people even though they didn’t need to, finally vomiting them up when their stomachs were full.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 137

    def P295(self, *option):
        if option == ():
            response = '“Yeah, that’s right.”\n\n\
Eren’s expression changes. Thinking of his friends and fellow soldiers- all those who have died- and seeing his companions in front of him, he seems to be resolved.\n\n\
There’s no more hesitation. He bites his own hand.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 258

    def P296(self, *option):
        if option == ():
            response = 'Armin and the others tell Krista about their encounter with the Female Titan, although it’s not possible to talk for long while also trying to ride at a quick pace.\n\n\
Krista’s own unit seems to have caught wind of the confusion that now reigns over the formation. Everything is in disarray. A smoke signal goes up, and the formation makes a major change in direction.\n\n\
“The Titan Forest is this way…” Armin says.\n\n\
It’s true: you see a massive forest rising up ahead of you.\n\n\
The Female Titan has done some damage, but you’ve helped keep it to a minimum.\n\n\
**The Kill Count has increased by 4.**\n\n\
Type 1️⃣ to continue.'
            self.state.flags.killcount += 4
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 150

    def P297(self, *option):
        if option == ():
            response = '“This time we’re not letting that Female Titan get away!” Hange begins giving clipped, precise orders. \
The squad leader seems to be a different person from the one who gives frenzied discourses on Titan research. “Capture that monster, whatever it takes!”\n\n\
Hange is steely-eyed. Maybe it’s because this isn’t just about data, it’s about the fate of humanity- or perhaps the squad leader simply wants revenge for lost comrades.\n\n\
**Your Affinity with Hange has increased by 1!**\n\n\
The destruction of buildings leads to no small number of civilian casualties. There’s nothing you could have done to prevent this…\n\n\
**The Kill Count has increased by 20.**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.hange += 1
            self.state.flags.killcount += 20
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 307

    def P298(self, *option):
        if option == ():
            response = 'You decide to coordinate the evacuation of civilians. Let the elite soldiers of the Survey Corps handle the fighting.\n\n\
The Military Police Brigade, supposedly the guardians of order in the city, are in chaos. Some of them have fled. All that strutting around, yet what good are they when you need them? \
A boy, however, one of the MP’s new recruits, is engaged in hard fighting. Evidently some of their rookies were the better soldiers after all.\n\n\
You hear a religionist, some Wallist type, shouting, “This is divine punishment for defiling the walls!”\n\n\
You use your Vertical Maneuvering Equipment to get to a high vantage point from which you can survey the situation, then shout to the people below, guiding them away from the Titans. \
Sometimes you dart down to help individual citizens. You rescue one elderly person whose leg has become stuck in the rubble, and save a crying child as well.\n\n\
These are small things, but several other soldiers and civilians cooperate with you.\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
**The Kill Count has increased by 18.** (This may seem like a large number, but your efforts have kept it from being any higher…)\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.krista += 1
            self.state.flags.killcount += 18
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 307

    def P299(self, *option):
        if option == ():
            response = 'Your squad is constantly on the back foot after this. The formation falls into disarray.\n\n\
By the time the squad leader finally decides to send reinforcements, the formation is no longer able to function.\n\n\
You take an extra horse and ride off to reinforce.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 129

    def P300(self, *option):
        if option == ():
            response = '“Agh! Dad, what are you talking about?” Petra asks furiously- and loudly. She came over when she spotted her father. She grabs the envelope, her face beet red. \
“Th-That’s not what I meant when I wrote- Captain! I apologize for my father’s lack of decorum!” She’s obviously flustered.\n\n\
“A bride, huh? He’s right. You’re definitely a little young.” This smug comment comes from Oluo, who has wandered up in the meantime. “It’ll be a long time before you’re the kind of woman I’m looking for.”\n\n\
“Who asked you?!” Petra, steaming, smacks him in the face.\n\n\
Blood flies from Oluo’s mouth. It looks like he’s bitten his tongue.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 319

    def P301(self, *option):
        if option == ():
            response = '“This way!” The soldiers lead Sasha to a safe place, and draw the Titan away with their horses. They ride skillfully between the abandoned buildings and the trees. \
Just as they intended, the crawling Titan slams into an empty building.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 203

    def P302(self, *option):
        if option == ():
            response = 'You get on your horse and retreat with the other nearby soldiers.\n\n\
You ride desperately through the dim forest. Then the cluster of giant trees ends, and with a rush of relief you emerge into the sunlight once more. \
You rendezvous with those among your comrades who were posted to duty outside the woods.\n\n\
As the soldiers gather, information starts to come in. Word is that the Female Titan appeared again. You saw her get eaten, so what can this mean? But the information is chaotic and confused.\n\n\
There’s another rumor, the one that shocks you: it says the elite Squad Levi has been annihilated. Apparently, Eren turned into a TItan and fought, but lost. \
After that, Captain Levi and Mikasa together somehow managed to rescue Eren… but what now?\n\n\
**The Kill Count has increased by 4.**\n\n\
Type 1️⃣ to continue.'
            self.state.statuses.petra = 'Dead'
            self.state.statuses.oluo = 'Dead'
            self.state.statuses.gunther = 'Dead'
            self.state.statuses.eld = 'Dead'
            self.state.flags.killcount += 4
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 130

    def P3021(self, *option):
        if option == ():
            response = '**Your Affinity with Armin has increased by 1!**\n\n\
You get on your horse and retreat with the other nearby soldiers.\n\n\
You ride desperately through the dim forest. Then the cluster of giant trees ends, and with a rush of relief you emerge into the sunlight once more. \
You rendezvous with those among your comrades who were posted to duty outside the woods.\n\n\
As the soldiers gather, information starts to come in. Word is that the Female Titan appeared again. You saw her get eaten, so what can this mean? But the information is chaotic and confused.\n\n\
There’s another rumor, the one that shocks you: it says the elite Squad Levi has been annihilated. Apparently, Eren turned into a TItan and fought, but lost. \
After that, Captain Levi and Mikasa together somehow managed to rescue Eren… but what now?\n\n\
**The Kill Count has increased by 4.**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.armin += 1
            self.state.statuses.petra = 'Dead'
            self.state.statuses.oluo = 'Dead'
            self.state.statuses.gunther = 'Dead'
            self.state.statuses.eld = 'Dead'
            self.state.flags.killcount += 4
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 130
    
    def P3022(self, *option):
        if option == ():
            response = '**Your Affinity with Jean has increased by 1!**\n\n\
You get on your horse and retreat with the other nearby soldiers.\n\n\
You ride desperately through the dim forest. Then the cluster of giant trees ends, and with a rush of relief you emerge into the sunlight once more. \
You rendezvous with those among your comrades who were posted to duty outside the woods.\n\n\
As the soldiers gather, information starts to come in. Word is that the Female Titan appeared again. You saw her get eaten, so what can this mean? But the information is chaotic and confused.\n\n\
There’s another rumor, the one that shocks you: it says the elite Squad Levi has been annihilated. Apparently, Eren turned into a TItan and fought, but lost. \
After that, Captain Levi and Mikasa together somehow managed to rescue Eren… but what now?\n\n\
**The Kill Count has increased by 4.**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.jean += 1
            self.state.statuses.petra = 'Dead'
            self.state.statuses.oluo = 'Dead'
            self.state.statuses.gunther = 'Dead'
            self.state.statuses.eld = 'Dead'
            self.state.flags.killcount += 4
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 130

    def P3023(self, *option):
        if option == ():
            response = '**Your Affinity with Sasha has increased by 1!**\n\n\
You get on your horse and retreat with the other nearby soldiers.\n\n\
You ride desperately through the dim forest. Then the cluster of giant trees ends, and with a rush of relief you emerge into the sunlight once more. \
You rendezvous with those among your comrades who were posted to duty outside the woods.\n\n\
As the soldiers gather, information starts to come in. Word is that the Female Titan appeared again. You saw her get eaten, so what can this mean? But the information is chaotic and confused.\n\n\
There’s another rumor, the one that shocks you: it says the elite Squad Levi has been annihilated. Apparently, Eren turned into a TItan and fought, but lost. \
After that, Captain Levi and Mikasa together somehow managed to rescue Eren… but what now?\n\n\
**The Kill Count has increased by 4.**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.sasha += 1
            self.state.statuses.petra = 'Dead'
            self.state.statuses.oluo = 'Dead'
            self.state.statuses.gunther = 'Dead'
            self.state.statuses.eld = 'Dead'
            self.state.flags.killcount += 4
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 130

    def P3024(self, *option):
        if option == ():
            response = '**Your Affinity with Krista has increased by 1!**\n\n\
You get on your horse and retreat with the other nearby soldiers.\n\n\
You ride desperately through the dim forest. Then the cluster of giant trees ends, and with a rush of relief you emerge into the sunlight once more. \
You rendezvous with those among your comrades who were posted to duty outside the woods.\n\n\
As the soldiers gather, information starts to come in. Word is that the Female Titan appeared again. You saw her get eaten, so what can this mean? But the information is chaotic and confused.\n\n\
There’s another rumor, the one that shocks you: it says the elite Squad Levi has been annihilated. Apparently, Eren turned into a TItan and fought, but lost. \
After that, Captain Levi and Mikasa together somehow managed to rescue Eren… but what now?\n\n\
**The Kill Count has increased by 4.**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.krista += 1
            self.state.statuses.petra = 'Dead'
            self.state.statuses.oluo = 'Dead'
            self.state.statuses.gunther = 'Dead'
            self.state.statuses.eld = 'Dead'
            self.state.flags.killcount += 4
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 130

    def P303(self, *option):
        if option == ():
            response = 'You’re in the back alleys of Stohess District.\n\n\
Annie, once a member of your training cohort and now a part of the Military Police Brigade, is walking along you, as are Eren, Armin, and Mikasa, who are all dressed as porters. \
Thankfully, there doesn’t seem to be anyone around; the streets are quiet. No one seems to have noticed you yet, but if anyone does, \
the presence of someone in an MP uniform greatly increases your chances of getting away without trouble.\n\n\
“Hey.” Annie, previously silent, suddenly speaks to Armin and Mikasa. “How did you plan to get past the wall if I hadn’t helped you?”\n\n\
“We were gonna force our way over with our Vertical Maneuvering Equipment,” Armin says.\n\n\
“That seems a little crazy. Anyway, wouldn’t it have been easier to escape before you came into Stohess District?”\n\n\
“This town has a complicated geography, and we were going to use it to our advantage,” Armin says without missing a beat. “And we weren’t going to just try to flee immediately. \
We were going to pretend to go along with them, get them to lower their guard, to buy us more time to escape.”\n\n\
“I see… That makes sense.”\n\n\
The four of you walk along, saying little. You’re glad that it’s so quiet here that there doesn’t seem to be any other people around.\n\n\
“There. This is it,” Armin says. You’ve come to a stairway just off the street that leads down into an ancient-looking tunnel. \
“This goes into the remains of an underground city they were planning to build once. It should take us right up to the outer door.”\n\n\
You, Armin, Eren, and Mikasa descend the stairs.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 265

    def P304(self, *option):
        if option == ():
            response = 'Annie, still bound, is carried underground. The confined space will ensure that she can’t transform into a Titan.\n\n\
Only then is her gag removed.\n\n\
“I wasn’t hard enough. You and the others were. That was the difference,” she says with a sarcastic laugh. “I shouldn’t have let any stupid sentiment interfere. \
I should have just killed you and all the other humans. Then no one would’ve suspected me.”\n\n\
The leaders of the Survey Corps surround Annie.\n\n\
“You’re going to be placed under the supervision of the Survey Corps. If you cooperate, nothing bad will happen to you,” Commander Erwin promises, but Annie gives him a spiteful laugh.\n\n\
“I have nothing to say to you. What are you going to do, torture me? How very human.”\n\n\
So this episode concludes. You and the others succeed in achieving your “special objective.” It was extremely fortunate that you were able to apprehend and stop Annie. \
If the Female Titan had appeared in the middle of Stohess District, the result might have been catastrophic.\n\n\
Problems remain, of course; a mountain of them. Eren’s custody is by no means resolved, and the capture of a new kind of human who can turn into a Titan will no doubt make the tribunal even messier.\n\n\
You don’t know what will happen to Annie now. She’s an enemy of humanity. Fortunately, however, she hasn’t yet killed any humans. Perhaps she could be enlisted to fight on your side as a Titan, just like Eren.\n\n\
Maybe you’ll still have a chance to talk.\n\n\
**🎉 Congratulations! You\'ve obtained the "A Sliver of Hope" Ending. 🎉**\n\n\
https://www.youtube.com/watch?v=mWZI17J46uU&ab_channel=k4h4r'
            self.response2[0] = '\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P305(self, *option):
        if option == ():
            response = '“You gotta be kidding me!” Jean says. “A double might work, but why me? Eren and I don’t look like anything like each other. We’ll get found out for sure!”\n\n\
“No,” Armin says, “you’re about the same height…”\n\n\
Everyone in the room nods. A chorus of agreement follows:\n\n\
“Yeah, you do kind of look like him.”\n\n\
“You’ve both got the same nasty eyes.”\n\n\
“I’ve always thought you looked like each other, ever since training.”\n\n\
“Y-You rats…” Jean doesn’t appear convinced, but finally he sighs and gives in. “Fine, looks like I got no choice. Now bow your heads, because we better pray the MPs aren’t very good at their jobs.”\n\n\
**Your Affinity with Jean has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.jean += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 251

    def P306(self, *option):
        if option == ():
            response = 'At that, Mikasa closes her mouth. For a second, Levi goes silent too, but then he says, “It’s my responsibility. I’ll finish what I’ve started.”\n\n\
**Your Affinity with Levi has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.levi += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 184

    def P307(self, *option):
        if option == ():
            response = 'The Female Titan thrusts Eren aside and makes a run for the wall. She’s faster than anyone expected, able to exploit a momentary opening.\n\n\
When she reaches the wall, the Female Titan jumps up and begins to climb. She hardens her fingers so that they can dig into the stone; up and up she goes.\n\n\
Could anyone have imagined a Titan climbing the wall? The Survey Corps soldiers, who fanned out in hopes of encircling her, are unable to do anything.\n\n\
“She’s going to get over the wall,” someone shouts. “Then we won’t be able to do anything!”\n\n\
The Female Titan is already most of the way up. Is she going to get away?\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            if self.state.statuses.mikasa == 'Alive' and self.state.statuses.armin == 'Alive':
                self.cur_page[0] = 335
            else:
                self.cur_page[0] = 328

    def P308(self, *option):
        if option == ():
            response = 'You use your Vertical Maneuvering Equipment, desperately trying to get the Female Titan’s attention somehow. \
You won’t be able to defeat her on your own, but maybe you can offer your friends underground something, anything…\n\n\
The Female Titan reaches out for you.\n\n\
You hear something like a shout from the tunnel.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 258

    def P309(self, *option):
        if option == ():
            response = 'No sooner has Armin spoken than, as if in answer, an eerie cry sounds from the woods. \
The piercing scream is like the call of a wild animal, but it’s so loud- is it the voice of a Titan?\n\n\
“The hell?” Jean asks, on edge. “Whatever that is, it doesn’t sound good.”\n\n\
Armin murmurs, “You have to give up something important in order to change something… Maybe everyone’s the same that way.”\n\n\
You…\n\n\
1️⃣ Head into the forest\n\n\
2️⃣ Get out of here'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 271
        elif option[0] == 2:
            self.cur_page[0] = 268

    def P310(self, *option):
        if option == ():
            response = '“That’s a fantastic idea! Plus we could get more data on Eren!” Hange exclaims with exceptional excitement.\n\n\
No one else speaks, though, until Armin says, “You’re joking, right?”\n\n\
It’s true, if Eren turned into a Titan, the Military Police Brigade would be no match for him. But the plan would put civilians in harm’s way as well, and that would make him an enemy of humanity…\n\n\
“Ha ha ha! Of course it was a joke! I’m sure our rookie friend here was just trying to lighten the mood a little. You’re all so serious.” Hange seems to want to pass the whole thing off.\n\n\
You think Hange sounded pretty convinced by your idea, though…\n\n\
Type 1️⃣ to go back and think of a different plan.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 250

    def P311(self, *option):
        if option == ():
            response = 'You watch the Female Titan’s movements closely. All the time she’s been fighting with Eren, she also seems to have been looking for a way to escape. \
She doesn’t seem interested in capturing Eren anymore, or in causing any more casualties than necessary.\n\n\
You…\n\n\
1️⃣ Circle around to the outer wall\n\n\
2️⃣ Prioritize the safety of the populace\n\n\
3️⃣ Follow your superiors’ instructions'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 230
        elif option[0] == 2:
            self.cur_page[0] = 298
        elif option[0] == 3:
            self.cur_page[0] = 282

    def P312(self, *option):
        if option == ():
            response = 'You’re close to Annie when a group of men and women jump on her and try to hold her down. \
They pin her arms from behind and stuff a gag in her mouth so she can’t bite her hands or tongue.\n\n\
Annie wiggles her fingers. You see a large ring on her right hand.\n\n\
You…\n\n\
1️⃣ Hurry and get out of there\n\n\
2️⃣ Fight the people who have mobbed Annie and help her\n\n\
3️⃣ Jump at Annie and help tie her up'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 292
        elif option[0] == 2:
            self.cur_page[0] = 279
        elif option[0] == 3:
            self.cur_page[0] = 119

    def P313(self, *option):
        if option == ():
            response = 'Captain Levi is in civilian clothes. He’s wounded and can’t take part in the battle.\n\n\
He watches things unfold with an impassive expression, but you see that his fist is balled up and shaking. It must gall him deeply not to be able to be a part of this.\n\n\
You don’t feel you can speak to him at this moment, but as he sees you make for the field of combat, he says, “You’d better not die, rookie.”\n\n\
You salute, then jump into the fray.\n\n'
            if self.state.affinities.levi >= 2 and self.state.flags.levi_watch == False:
                response += '**Your Affinity with Levi has increased by 1!**\n\n'
                self.state.affinities.levi += 1
                self.state.flags.levi_watch = True
            response += 'Type 1️⃣ to return and decide what to do next.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 289

    def P314(self, *option):
        if option == ():
            response = 'You jump on the Female Titan’s shoulder. Annie doesn’t stop you.\n\n\
Then she jumps down from the 50-meter height, and starts running away from the wall, into the great beyond. No human alive could catch her.\n\n\
“Did you think there was going to be some kind of paradise out here?”\n\n\
After you pass Wall Rose, Annie returns to her human form; she asks you this question. Her cold expression and sharp glances are the same as ever.\n\n\
“I’m not going to thank you,” she says. “I don’t have much with me, and I don’t know what happens now. But… Because of you, I’ve been able to come home.”\n\n\
You flee beyond the walls, into the world she and the others inhabit.\n\n\
What waits for you there? New possibilities? Or just one more circle of hell?\n\n\
You don’t know.\n\n\
**🎉 Congratulations! You\'ve obtained the "Beyond the Walls" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P315(self, *option):
        if option == ():
            response = 'Ness shouts, “No, you’ll never be able to-!”\n\n\
But there’s no time. He gives orders to Siss, then says to you, “No choice now. Back us up, rookie!”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 293

    def P316(self, *option):
        if option == ():
            response = 'Commander Erwin issues orders to the exhausted soldiers. “All troops, withdraw! Mount up while the Titans are distracted with the Female’s remains! Leave all the wagons here. \
We’ll rebuild the formation on the western edge of the woods! We’re heading back to Karanes District!”\n\n\
As sure and authoritative as he sounds, the words weigh heavily on the spent troops. This means failure. Defeat. Surely, it’s no easier for the commander to give the order that it is for you to hear it.\n\n\
A smoke signal goes up, indicating “retreat.” That should ensure the order reaches those standing guard and your friends assigned to various points around the woods, as well.\n\n\
You…\n\n\
1️⃣ Get on a horse and accompany the soldiers around you\n\n\
2️⃣ Take the retreat order to your friends stationed around the forest, and withdraw with them\n\n\
3️⃣ Go inform Squad Levi and Eren, who are standing guard some distance away, of the situation'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 134
        elif option[0] == 2:
            self.cur_page[0] = 321
        elif option[0] == 3:
            self.cur_page[0] = 284

    def P317(self, *option):
        if option == ():
            response = '“Hell, maybe we can keep each other from dying.” Jean smirks at you. His smile isn’t any friendlier than usual. \
Despite his cynical words, though, he leaps bravely into battle, into the place of danger.\n\n\
The fight between Titan Eren and the Female Titan is incredible to behold. When 15-meter monsters clash, the surrounding buildings suffer the consequences. \
Cascading rubble nearly comes down on top of you, but someone pulls you away at the last moment- it’s Jean.\n\n\
“Hey, keep clear. We’re just cannon fodder, remember?” he says as he drags you away.\n\n\
You can’t help thinking how different he is from when you were in training. You and Jean stand on the roof of a nearby building, watching the Titans fight.\n\n\
“It’s all you, Eren!” Jean shouts. He may not sound very friendly, but it’s his own kind of encouragement.\n\n\
**Your Affinity with Jean has increased by 1!**\n\n\
All the buildings that are destroyed in this fight result in no small number of civilian casualties. This collateral damage is beyond your control…\n\n\
**The Kill Count has increased by 20.**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.jean += 1
            self.state.flags.killcount += 20
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 307

    def P318(self, *option):
        if option == ():
            response = 'Suddenly, two figures come flying out of the tunnel, one of them from the entrance, the other from the hole the Female Titan produced moments ago.\n\n\
In a single swift movement, the Female Titan grabs and crushes one of them.\n\n\
In that instant, you understand. Mikasa and Armin, hoping to keep Eren safe, flew in two different directions. They must have known that least one of them would die.\n\n\
They have both been brave and noble comrades. And the Female Titan snuffed out one of their lives without so much as flinching.\n\n\
You look on, dumbfounded. A scream comes from the underground tunnel.\n\n\
Who did the Female Titan kill?\n\n\
1️⃣ Mikasa\n\n\
2️⃣ Armin'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.state.statuses.mikasa = 'Dead'
            self.cur_page[0] = 258
        elif option[0] == 2:
            self.state.statuses.armin = 'Dead'
            self.cur_page[0] = 258

    def P319(self, *option):
        if option == ():
            response = 'Levi watches all this without so much as a change of expression.\n\n\
“Family, is it?” You think you see the slightest hint of a smile tug at his mouth. Then he looks in your direction. He says only, “You did well, too.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 248

    def P320(self, *option):
        if option == ():
            response = 'For some time, you attempt to keep the Titans at bay. Maybe they have some capacity to learn, because they slowly begin to climb the trees. \
You managed to help Krista while also seeing to your own share of the duty.\n\n\
You’re not sure how much time has passed when you suddenly hear something like an explosion from inside the forest.\n\n\
“I hope nothing bad is happening in there,” Krista says uneasily.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 104

    def P321(self, *option):
        if option == ():
            response = 'You decide to go find your friends from the 104th Training Corps. The retreat order has been communicated by smoke signal, but you can’t be sure of anything under these circumstances, \
and you’re worried about the horses. You seek out one of your friends to see if they need help.\n\n\
Who do you go to?\n\n\
1️⃣ Armin\n\n\
2️⃣ Jean\n\n\
3️⃣ Sasha\n\n\
4️⃣ Krista'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 3021
        elif option[0] == 2:
            self.cur_page[0] = 3022
        elif option[0] == 3:
            self.cur_page[0] = 3023
        elif option[0] == 4:
            self.cur_page[0] = 3024

    def P322(self, *option):
        if option == ():
            response = 'The Female Titan comes crashing down and ceases to move.\n\n\
Eren, still in his Titan form, holds her down. Members of the Survey Corps surround her and begin hacking at the nape of her neck.\n\n\
At long last, everyone thinks, you’ll be able to take Annie into custody.\n\n\
At that moment, however, Annie’s body shines and there’s a rush of steam. Did she have some final power to use?\n\n\
When the steam clears, Annie is there, surrounded by what seems to be a huge, transparent crystal. Inside, she appears to be frozen, her eyes closed like Sleeping Beauty.\n\n\
“Dammit, that’s no fair! Come out of there!”\n\n\
Survey Corps soldiers attack the crystal with their weapons, but even Anti-Titan-grade steel doesn’t so much as scratch the surface. \
Maybe this thing works the same way as the Female Titan’s ability to harden parts of her body.\n\n\
So Annie lies in the crystal, seemingly asleep. Hanji Zoe spirits her away underground, there to keep her under close watch…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 3221

    def P3221(self, *option):
        if option == ():
            response = 'Thus, one battle at last comes to an end. Many sacrifice themselves, and although you defeated the Female TItan, Annie Leonhart is not going to be giving you any answers. \
She is asleep, leaving only mysteries behind her. Your victory is bitterly pyrrhic.\n\n\
Thanks to these events, however, the Survey Corps finds its position reversed. The appearance of a Titan within Wall Sheena, \
to say nothing of the revelation that a Titan sympathizer was hiding among the Military Police Brigade, is shocking. Naturally, some criticize the Survey Corps for taking matters into their own hands, \
as well as for the amount of damage done by fighting within Stohess District. But the majority of people recognize that their actions prevented an even greater crisis, \
and that without the Survey Corps it would have been impossible to repel this latest threat to humankind.\n\n\
The demand for Eren’s custody is revoked, and the Survey Corps is restored to good standing.\n\n\
At the same time, this places a great responsibility on the Survey Corps’ shoulders: the duty to break this deadlock and take the fight to the Titans.\n\n\
“We will hunt down and destroy every enemy within the walls,” Commander Erwin declares to the leaders of the Military Police Brigade.\n\n\
“Humanity’s attack on the Titans begins now.”\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 324

    def P323(self, *option):
        if option == ():
            response = 'At that very moment, a lone soldier comes flying up the wall from the town below.\n\n\
It’s Mikasa.\n\n\
You thought Vertical Maneuvering Equipment wasn’t supposed to have enough power to reach the top of a 50-meter wall! \
Looking down, though, you see what’s happened: Eren, in Titan form, has carried her to the base of the wall and then flung her upward. One of Armin’s ideas, you’re sure. \
It’s only feasible because of Mikasa’s supreme physical gifts, and it suggests the level of fine control Eren has achieved over his Titan form.\n\n\
Above all, she can do it because the three of them trust each other implicitly, so much so that they can attempt something this outrageous without so much as a practice run.\n\n\
Mikasa slices at the Female Titan’s fingers. Apparently they aren’t hardened at the point where the finger meets the hand. Then Mikasa sets her anchors in the wall. \
If she can sever the fingers of the other hand, the Female Titan will have nothing to support her, and will fall to the ground.\n\n\
You…\n\n\
1️⃣ Back Mikasa up\n\n\
2️⃣ Get in Mikasa’s way and help the Female Titan'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 138
        elif option[0] == 2:
            self.cur_page[0] = 237

    def P324(self, *option):
        if option == ():
            response = 'You’ve survived the battle. How does your adventure conclude?\n\n'
            self.choices[0] = [1]

            if self.state.affinities.eren >= 2:
                response += '**You have sufficient Affinity with Eren!**\n\n'
                self.choices[0].append(2)
            else:
                response += '**You do not have enough Affinity with Eren (2 needed).**\n\n'
            
            if self.state.statuses.mikasa == 'Alive':
                if self.state.affinities.mikasa >= 3:
                    response += '**You have sufficient Affinity with Mikasa!**\n\n'
                    self.choices[0].append(3)
                else:
                    response += '**You do not have enough Affinity with Mikasa (3 needed).**\n\n'

            if self.state.statuses.armin == 'Alive':
                if self.state.affinities.armin >= 3:
                    response += '**You have sufficient Affinity with Armin!**\n\n'
                    self.choices[0].append(4)
                else:
                    response += '**You do not have enough Affinity with Armin (3 needed).**\n\n'
            
            if self.state.affinities.jean >= 3:
                response += '**You have sufficient Affinity with Jean!**\n\n'
                self.choices[0].append(5)
            else:
                response += '**You do not have enough Affinity with Jean (3 needed).**\n\n'

            if self.state.affinities.hange >= 3:
                response += '**You have sufficient Affinity with Hange!**\n\n'
                self.choices[0].append(6)
            else:
                response += '**You do not have enough Affinity with Hange (3 needed).**\n\n'

            if self.state.affinities.levi >= 5:
                response += '**You have sufficient Affinity with Levi!**\n\n'
                self.choices[0].append(7)
            else:
                response += '**You do not have enough Affinity with Levi (5 needed).**\n\n'

            if self.state.affinities.krista >= 3:
                response += '**You have sufficient Affinity with Krista!**\n\n'
                self.choices[0].append(8)
            else:
                response += '**You do not have enough Affinity with Krista (3 needed).**\n\n'

            if self.state.affinities.sasha >= 2:
                response += '**You have sufficient Affinity with Sasha!**\n\n'
                self.choices[0].append(9)
            else:
                response += '**You do not have enough Affinity with Sasha (2 needed).**\n\n'

            response += '\nNow, which path do you take?\n\n\
1️⃣ Continue serving as a member of the Survey Corps\n\n'
            if self.state.affinities.eren >= 2:
                response += '2️⃣ Go with Eren\n\n'
            if self.state.statuses.mikasa == 'Alive' and self.state.affinities.mikasa >= 3:
                response += '3️⃣ Go with Mikasa\n\n'
            if self.state.statuses.armin == 'Alive' and self.state.affinities.armin >= 3:
                response += '4️⃣ Go with Armin\n\n'
            if self.state.affinities.jean >= 3:
                response += '5️⃣ Go with Jean\n\n'
            if self.state.affinities.hange >= 3:
                response += '6️⃣ Go with Hange\n\n'
            if self.state.affinities.levi >= 5:
                response += '7️⃣ Go with Levi\n\n'
            if self.state.affinities.krista >= 3:
                response += '8️⃣ Go with Krista\n\n'
            if self.state.affinities.sasha >= 2:
                response += '9️⃣ Go with Sasha\n\n'
            return response

        elif option[0] == 1:
            self.cur_page[0] = 336
        elif option[0] == 2:
            self.cur_page[0] = 325
        elif option[0] == 3:
            self.cur_page[0] = 331
        elif option[0] == 4:
            self.cur_page[0] = 333
        elif option[0] == 5:
            self.cur_page[0] = 326
        elif option[0] == 6:
            self.cur_page[0] = 332
        elif option[0] == 7:
            self.cur_page[0] = 334
        elif option[0] == 8:
            self.state.flags.krista_ending = True
            self.cur_page[0] = 185
        elif option[0] == 9:
            self.state.flags.sasha_ending = True
            self.cur_page[0] = 185

    def P325(self, *option):
        if option == ():
            response = '“Did I make the right choice?” Eren asks you.\n\n\
The battle in Stohess is over. Many lives have been lost, and you have suffered the shock of discovering that someone you thought was a friend deceived you all. \
Eren was effectively at the epicenter of everything, and it must weigh heavily on him, much more than it does on you.\n\n\
By now, though, you should know as well as anyone that there are no undeniably “right” choices. That in order to gain something, we must sacrifice something else. \
And that we cannot know the true outcome of any choice until we make it.\n\n\
You of all people may be qualified to tell him- tell him that he wasn’t wrong.\n\n\
After you speak, Eren nods.\n\n\
“Next time, I won’t hesitate,” he says.\n\n\
He will face other difficult choices in the future, agonizing ones.\n\n\
Will you be able to support him?\n\n\
**🎉 Congratulations! You\'ve obtained the "Eren Yeager’s Choice" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P326(self, *option):
        if option == ():
            response = 'You and Jean both survive. Back in training, he was a self-centered young man; he proclaimed that he was going to join the Military Police Brigade and live the pampered life of an elite. \
You think of all the courage he has shown since then. Is he really the same Jean?\n\n\
When you raise the subject with him, he only shrugs and responds with his usual acidity, “I haven’t changed a bit. What, you think I’m happy to go throw my life away now or something? \
The Survey Corps is the worst. Even now, I hate being here. It’s just…”\n\n\
You and Jean don’t get much time to just sit and talk. Life in the Survey Corps turns out to be an endless succession of crises. First, you receive word that Titans have appeared at Wall Rose, \
and deploy to fight them. When that’s over, you fight yourselves battling Titans concealed within humanity itself. Even other humans come after you for your life.\n\n\
And Jean? He takes on all these dangerous duties with characteristic ill humor. He helps his friends. He even saves you more than once.\n\n\
Sometime later, he says to you again, “I haven’t changed a bit.” But then he goes on. “I’ve just… started to get used to it. At least enough that *he* won’t be disappointed in me.”\n\n\
**🎉 Congratulations! You\'ve obtained the "Jean Kirstein’s Vow" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P327(self, *option):
        if option == ():
            response = '“Be careful,” Krista says as you go, tears in her eyes. “Don’t do anything dangerous.”\n\n\
You head into the forest.\n\n\
**Your Affinity with Krista has increased by 1!**\n\n\
Type 1️⃣ to continue.'
            self.state.affinities.krista += 1
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 271

    def P328(self, *option):
        if option == ():
            response = 'The Female Titan climbs over Wall Sina and runs away.\n\n\
You were so close. Everyone in the Survey Corps looks devastated.\n\n\
This outcome, however, has an unexpected effect. The shock of a Titan appearing in Stohess District is tremendous, \
and more than a few people speak out in support of the Survey Corps for driving the creature away. The damage in the district is extensive, \
but in its own way this stands as a condemnation of the Military Police Brigade and the softness of their defenses.\n\n\
Above all else, the thought that the Female Titan is still out there, alive and well, terrifies people. \
The royal government and the Military Police tribunal apparently decide that punishing the Survey Corps is less important than sending these experienced soldiers out to eliminate the threat.\n\n\
They return Eren to his unit, and Commander Erwin and the rest of the Survey Corps begin planning their next move…\n\n\
**🎉 Congratulations! You\'ve obtained the "Flight of the Female Titan" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P329(self, *option):
        if option == ():
            response = 'You successfully reunite with Sasha. You discover she’s been in a certain village, protecting children who were too late to run away - \
without the benefit of Vertical Maneuvering Equipment, using only an old-fashioned bow and arrow. You recall hearing that she came from a family of hunters, but her bravery and initiative surprise you.\n\n\
When you see her again, she looks different. She’s not wearing her military uniform, but a long skirt. What surprises you more, though, are the clear eyes of a hunter she now has.\n\n\
She speaks to others from her home, overjoyed to see them again. She sounds different from usual, too. You suspect her diligent formality was partly a ploy to hide a hometown drawl.\n\n\
She looks much more natural to you now. But her village was attacked by Titans. Even if it hadn’t been, forests with good hunting are rapidly disappearing here within the walls.\n\n\
When you ask her about it, Sasha smiles and says, “Whatever happens, wherever we go, as long as we’re alive, that’s enough. I’ve made some new friends, too. Er…” She looks a little embarrassed as she adds, \
“And, uh, I’m awfully hungry.”\n\n\
**🎉 Congratulations! You\'ve obtained the "The True Face of Sasha Blouse" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P330(self, *option):
        if option == ():
            response = 'You successfully reunite with Krista. This is tremendously good luck. Krista and the others were attacked by a horde of Titans led by an intelligent Titan, \
and spent the night in a fierce defensive action in and around an abandoned castle called Utgard. Most of the Survey Corps soldiers with her were killed; by the time a relief force arrived, \
her unit was on the cusp of annihilation.\n\n\
Ymir, the girl who had been so close to Krista, was badly wounded in this battle. You hear she did something dangerous in order to keep Krista safe. Krista is ever at her side.\n\n\
When things finally settle down and you have a chance to tell her about what happened in Stohess District, she only says, “To think Annie kept her true self hidden from us all that time…”\n\n\
Just like the other members of your training squad, she seems surprised, but where you expected this kindhearted girl to be hurt, she seems to feel something else instead.\n\n\
“Hey,” Krista says then. “If you found out that I had been deceiving everyone, too… What would you do?”\n\n\
She’s staring right at you. Her clear blue eyes and beautiful golden hair are the same as ever… And yet, she doesn’t look quite like the Krista you once knew.\n\n\
How will you answer her question?\n\n\
**🎉 Congratulations! You\'ve obtained the "The Girl Who Hid Herself" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P331(self, *option):
        if option == ():
            response = 'Mikasa sits before the bed in which Eren lies, asleep. After the fighting in Stohess District, Eren returned from his Titan form and fell into a sleep so deep he almost seems comatose. \
Mikasa sits quietly, watching over him.\n\n\
She’s such a fearsome presence on the battlefield, yet here she looks like a normal girl. Eren’s in the quiet, rhythmic breathing of sleep, and she looks at him with something like love.\n\n\
Your other friends were here to check on Eren not long ago, but perhaps out of courtesy, one by one they’ve left. It’s about time for you to go, too…\n\n\
“The world is… cruel,” Mikasa says softly.\n\n\
Is she talking about all the lives that were lost in these recent events? Or does she mean Annie, who was supposed to be your comrade but turned out to be deceiving all of you? Or…\n\n\
Or does she mean everything, all the experiences that have made her, forced her to become, the hardened soldier she is today?\n\n\
“... and also very beautiful,” she goes on.\n\n\
You think back on all that has happened, and you are sure she’s right.\n\n\
**🎉 Congratulations! You\'ve obtained the "A World Beautiful and Cruel" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P332(self, *option):
        if option == ():
            response = 'Your work with Squad Leader Hange Zoe caused you to see terrible things during the battle of Stohess District. When the Female Titan climbed the wall, \
she tore away a part of the surface… And from beneath, you saw a giant face. Are there Titans buried in the wall? You’re sure you saw that eyeball move...\n\n\
“Don’t let the sunlight hit that Titan! Block it with something! Anything!”\n\n\
The voice belongs to Nick, a minister of the Church of the Walls. You know- thanks to the work of none other than Hange Zoe- that Titans cease to move when completely cut off from sunlight. \
Have there been immobilized Titans inside the wall all this time?\n\n\
And how does a Wallist minister know about that, anyway? Have they been aware of the secret all along? Do they have information hidden even from the Survey Corps?\n\n\
When Hange finally gets a break from overseeing the work of covering the Titan’s face, the researcher turns to Nick in high dudgeon.\n\n\
“We in the Survey Corps have given everything for humanity. We haven’t begrudged even our own lives, if it holds out the slightest bit of hope! And somehow you knew about this, and kept silent! \
Do you know how many of my friends have been eaten by Titans?!”\n\n\
Hange looks ready to drop the minister off the 50-meter wall, and you don’t think the squad leader is just trying to intimidate him. The bright, cheerful Hange you know seems to have vanished completely.\n\n\
The minister quakes with fear, but appears resolved. He shouts that he will keep his secret even if he must plunge to his death to do it.\n\n\
“No, you don’t have to,” Hange says at last. “I was just… joking.” You’re almost as relieved as Nick to see the familiar Hange return.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 3321

    def P3321(self, *option):
        if option == ():
            response = 'Sometime later, you have a chance to talk with the squad leader.\n\n\
“I used to act that way all the time,” Hange says. “The expedition beyond the walls that I went on, my comrades got eaten. I let hatred guide my sword after that. \
Hatred for the Titans, and for this whole obscene world.\n\n\
“But one time, I saw a Titan, this impossibly unnatural living creature, and I had a sort of epiphany. I realize that what we see and what’s really there can be completely different things. \
I started to think… What if I found a different perspective, something other than fury, from which to view this world?”\n\n\
Still, you didn’t just imagine the enraged Hange atop the wall. Nor are you imagining the calm and thoughtful Hange before you now. So which one is real?\n\n\
“Ahh, but don’t worry about that. Come on, let’s share our thoughts on the Titans we encountered this time.” Hange grins broadly, then begins talking with characteristic zeal. “Ready? I think…”\n\n\
**🎉 Congratulations! You\'ve obtained the "Hange Zoë’s Truth" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P333(self, *option):
        if option == ():
            response = 'You and Armin manage to survive the battle. Knowing the secret side of recent events as you do, you were no doubt able to witness the keenness of his observations and his courage.\n\n\
Some time later, you and Armin have a chance to reflect on what happened.\n\n\
“Commander Erwin,” Armin murmurs. “He’s someone who was ready to give something up in order to achieve something important. I wonder if I could do the same.”\n\n\
No sooner has he spoken than he appears surprised at his own words.\n\n\
“Ha ha. What am I saying? Is that… really the kind of person I want to become?”\n\n\
Armin begins to open up to you. About a book he read when he was young. About his dream of the world outside the walls. \
Things that could be considered heresy here within them. Although he stopped speaking of them, he has never forgotten them; they’ve been in his heart all this time. \
No doubt they were responsible for driving this seemingly frail boy to a path as dangerous as the Survey Corps.\n\n\
“When I was a kid, I wanted to go outside the walls. I was sure there were amazing things out there… And now I know. I know it’s not as simple as that. \
To make your dreams come true, you have to pay an unimaginable price…”\n\n\
Will Armin give up his naive dreaming and face reality? Or will he give up something precious in order to make his dream come true? Or perhaps…\n\n\
**🎉 Congratulations! You\'ve obtained the "Armin Arlert’s Dream" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P334(self, *option):
        if option == ():
            response = 'Captain Levi must have formed some great expectations of you, because you end up as his direct subordinate. You and his other charges become known as “the Revived Squad Levi,” \
and although the name gives you great pride, it also comes with a welter of confusing emotions. Can you really learn to fight like the last Squad Levi- the Special Operations Squad?\n\n\
You throw yourself into your duties and training so as to live up to the name you’ve been given.\n\n\
Captain Levi- perhaps you should simply call him Captain now- is the same as ever; expressionless, keen-eyed, and curt. But you, at least, know that there’s more to the man than that.\n\n\
One night, you’re summoned to Levi’s private quarters.\n\n\
“Sorry,” he says. “I need some help. This is tough alone.”\n\n\
He removes his coat and pants to reveal compresses and bandages. He wants you to help him change them. The wounds he suffered in the battle with the Female Titan haven’t completely healed even now.\n\n\
You demur. You wonder if there isn’t someone around who knows him better, someone more practiced in medical matters.\n\n\
Levi seems to read your mind. “One of the experienced members of the Survey Corps would recognize how severe my injuries are, and how much they affect my ability to fight, \
and that would unsettle them. There would be no hiding it from the others. But a rookie like you? You won’t be able to tell the difference between when I’m hurt and when I’m healthy.”\n\n\
In other words, he’s so far above you he isn’t even worried…\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 3341

    def P3341(self, *option):
        if option == ():
            response = 'The thought depresses you a little, but you help change his dressings. Seeing Levi up close like this, you marvel anew at how toned and muscular his body is. But it’s also covered in scars. \
Some that seem to be from years ago overlap with others that are much newer. He may be the strongest of humanity’s soldiers, but unlike the Titans, humans can’t simply regenerate themselves. \
The injuries from this most recent fight aren’t completely healed yet, either.\n\n\
When you finish your work Levi says, almost in a whisper, “I hate people who are weak. They’re always the first to die.”\n\n\
The numberless scars on his body are testament to all the battles he has seen and survived.\n\n\
How many comrades has your invincible captain lost to death?\n\n\
He looks at you with his implacable gaze.\n\n\
“Don’t be one of them. That’s an order.”\n\n\
**🎉 Congratulations! You\'ve obtained the "Captain Levi’s Scars" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response

    def P335(self, *option):
        if option == ():
            response = 'A lone soldier appears in the air just above the Female Titan. It’s Mikasa.\n\n\
You thought Vertical Maneuvering Equipment wasn’t supposed to have enough power to get this high up! Looking down, though, you see what’s happened: \
Eren, in Titan form, has carried her to the base of the wall and then flung her upward. One of Armin’s ideas, you’re sure. It’s only feasible because of Mikasa’s supreme physical gifts, \
and it suggests the level of fine control Eren has achieved over his Titan form.\n\n\
Above all, she can do it because the three of them trust each other implicitly, so much so that they can attempt something this outrageous without so much as a practice run.\n\n\
Mikasa cuts at the Female Titan’s fingers with her sword as she flies. Apparently they aren’t hardened at the point where the finger meets the hand. Then Mikasa sets her anchors in the wall. \
With another great leap, she cuts off the Titan’s other hand.\n\n\
With nothing else to support her, the Female Titan plummets to the ground.\n\n\
Type 1️⃣ to continue.'
            self.choices[0] = [1]
            return response
        elif option[0] == 1:
            self.cur_page[0] = 322

    def P336(self, *option):
        if option == ():
            response = 'Long after the battle, you continue to serve as a member of the Survey Corps. The fighting in Stohess District may be over, but there’s no time to rest. \
You receive word that a horde of Titans has appeared inside Wall Rose.\n\n\
You and the rest of the Survey Corps deploy to push them back. You have to rescue those who were unable to evacuate before the monsters attacked.\n\n\
“The wall is ruined,” one of the more experienced soldiers moans. “Is this it for humanity?” The long years of service he has dedicated to the Survey Corps seem to magnify his despair.\n\n\
Your commander, Mike Zacharias, though, says, “Humanity loses when we stop fighting. Until that day, there’s still hope.”\n\n\
You nod. At Mike’s command, you mount your horse and draw your sword.\n\n\
You are a soldier of the Survey Corps.\n\n\
The Titans may be massive and the battles may be cruel, but you will continue to fight them.\n\n\
**🎉 Congratulations! You\'ve obtained the "A Soldier of the Survey Corps" Ending. 🎉**\n\n\
**To play again, type `~reset`.**'
            self.choices[0] = []
            return response