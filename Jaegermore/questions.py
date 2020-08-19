import discord
import random

class Question():
    def __init__(self, state):
        # Constants
        self.intro_msg = 'Listen up cadets! You are about to take a test that will determine your suitability for various roles in the military.\n\n\
In this assessment, you will be asked a series of questions that aims to determine your personality, and match it to the personalities of one of the heroes in the military, \
all of whom I\'m sure you are familiar with by now.\n\n\
Be sure to give your most honest response to get the most accurate result. \n\n\
**If you\'re ready, type `~start` to begin the assessment.**\n\n\
❗Tip: Type `~help` for the full list of commands.'

        self.reset_msg = discord.Embed(title = 'Assessment Reset!', description = 'Type **`~start`** to begin a new test.\nType **`~intro`** for more information about the test.', colour=0x5CFFE9)

        self.EC = {'0️⃣':0, '1️⃣':1, '2️⃣':2, '3️⃣':3, '4️⃣':4, '5️⃣':5, '6️⃣':6, '7️⃣':7, '8️⃣':8, '9️⃣':9, '🔟':10, '⏩':11, '㊙':'s'}
        self.EC2 = {0:'0️⃣', 1:'1️⃣', 2:'2️⃣', 3:'3️⃣', 4:'4️⃣', 5:'5️⃣', 6:'6️⃣', 7:'7️⃣', 8:'8️⃣', 9:'9️⃣', 10:'🔟', 11:'⏩', 's':'㊙'}

        self.all_qns = {0:self.Q0, 1:self.Q1, 2:self.Q2, 3:self.Q3, 4:self.Q4, 5:self.Q5, 6:self.Q6, 7:self.Q7, 8:self.Q8, 9:self.Q9, 10:self.Q10, 
        11:self.Q11, 12:self.Q12, 13:self.Q13, 14:self.Q14, 15:self.Q15, 16:self.Q16, 17:self.Q17, 18:self.Q18, 19:self.Q19, 20:self.Q20, 
        21:self.Q21, 22:self.Q22, 23:self.Q23, 24:self.Q24, 25:self.Q25, 26:self.Q26, 27:self.Q27, 28:self.Q28, 29:self.Q29, 30:self.Q30,
        31:self.Q31, 32:self.Q32, 33:self.Q33, 34:self.Q34, 35:self.Q35, 36:self.Q36, 37:self.Q37, 38:self.Q38, 39:self.Q39, 40:self.Q40, 'result':self.result}

        self.total_qns = 40

        # Variables
        self.num_qns = 0
        self.curplayer = None
        self.cur_qn = [0]
        self.choices = [[]]
        self.qns_played = []
        self.state = state

    def question_handler(self, option):
        # Records the choice and updates scores
        self.all_qns[self.cur_qn[0]](option)

        # Choose a random number and update cur_qn (until qn limit is reached, in which case go to results)
        if len(self.qns_played) >= self.num_qns:
            self.cur_qn[0] = 'result'
        else:
            choice = random.randint(1, self.total_qns)
            while choice in self.qns_played:
                choice = random.randint(1, self.total_qns)
            self.qns_played.append(choice)
            self.cur_qn[0] = choice

        # Plays the next qn
        return self.all_qns[self.cur_qn[0]]()

    # Cumulative scores
    # Eren: 51
    # Mikasa: 48
    # Armin: 51
    # Jean: 48
    # Krista: 42
    # Sasha: 39
    # Levi: 30
    # Annie: 40
    # Erwin: 40

    def Q0(self, option):
        pass

    def Q1(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
If you were living in the world of Attack on Titan, which branch of the military would you be in?\n\n\
:one: Survey Corps\n\n\
:two: Garrison\n\n\
:three: Military Police\n\n\
:four: I\'d rather be a civilian'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 2
            self.state.scores.armin += 1
            self.state.scores.levi += 1
            self.state.scores.erwin += 1
            self.state.scores.krista += 1
        elif option[0] == 2:
            self.state.scores.marco += 1
        elif option[0] == 3:
            self.state.scores.jean += 1
            self.state.scores.annie += 1
            self.state.scores.marco += 1
        elif option[0] == 4:
            self.state.scores.armin += 1
            self.state.scores.annie += 2

    def Q2(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
Which of the following beverages do you drink the most?\n\n\
:one: Water\n\n\
:two: Fruit juice\n\n\
:three: Tea\n\n\
:four: Wine/Beer'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 1
            self.state.scores.mikasa += 1
            self.state.scores.annie += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
            self.state.scores.sasha += 1
        elif option[0] == 3:
            self.state.scores.levi += 1
        elif option[0] == 4:
            self.state.scores.jean += 1
            self.state.scores.erwin += 1

    def Q3(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
The Survey Corps have recently scored a major victory against the Titans. As a soldier, what role did you play in that battle?\n\n\
:one: The hero who defeated the most powerful Titan\n\n\
:two: The strategist whose plan ensured success in the battle\n\n\
:three: The leader who kept the morale of the troops up in the face of overwhelming odds\n\n\
:four: The ordinary soldier who did his/her part to contribute to the victory'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.levi += 1
            self.state.scores.mikasa += 1
            self.state.scores.eren += 1
        elif option[0] == 2:
            self.state.scores.armin += 2
            self.state.scores.erwin += 1
        elif option[0] == 3:
            self.state.scores.erwin += 2
            self.state.scores.jean += 2
        elif option[0] == 4:
            self.state.scores.armin += 1
            self.state.scores.jean += 1
            self.state.scores.sasha += 1

    def Q4(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
During an expedition outside the Walls, you see a group of Titans running at high speed towards the scouting formation. As squad leader, what would you have your squad do?\n\n\
:one: Order a full-on charge to bring the Titans down before they do too much damage\n\n\
:two: Call for reinforcements to help battle the Titans\n\n\
:three: Split your squad up to distract the Titans from the main formation\n\n\
:four: Order a full retreat to prevent further losses'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
        elif option[0] == 3:
            self.state.scores.jean += 1
            self.state.scores.erwin += 1
        elif option[0] == 4:
            self.state.scores.krista += 1
            self.state.scores.jean += 1

    def Q5(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You are fighting the Titan responsible for the destruction of the Walls. However, in order to defeat it, you and your squad will have to act as bait \
to distract it long enough for one of the elite soldiers to reach its nape. You know that doing so will cost you your life.\n\n\
Are you willing to sacrifice your life for humanity?\n\n\
:one: Yes\n\n\
:two: No'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.state.scores.armin += 2
            self.state.scores.erwin += 1
            self.state.scores.eren += 1
            self.state.scores.krista += 1
        elif option[0] == 2:
            self.state.scores.jean += 1
            self.state.scores.annie += 1
            self.state.scores.sasha += 1

    def Q6(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You manage to capture a Titan shifter who has infiltrated the Walls. What do you do with them?\n\n\
:one: Kill them, they are too dangerous to be kept alive\n\n\
:two: Interrogate them for information about the Titans\n\n\
:three: Try and convince them to join your side'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.state.scores.levi += 1
            self.state.scores.mikasa += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
            self.state.scores.erwin += 1
        elif option[0] == 3:
            self.state.scores.krista += 2
            self.state.scores.armin += 1

    def Q7(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
Imagine if Titans broke through the Walls and humanity is about to be annhiliated. How do you spend your final moments?\n\n\
:one: With my family\n\n\
:two: Indulging myself with food and booze\n\n\
:three: Praying in a church\n\n\
:four: Fighting against the Titans in a heroic last stand\n\n\
:five: Trying to survive for as long as possible'
            self.choices[0] = [1,2,3,4,5]
            return response
        elif option[0] == 1:
            self.state.scores.mikasa += 3
            self.state.scores.krista += 1
            self.state.scores.annie += 2
        elif option[0] == 2:
            self.state.scores.sasha += 2
            self.state.scores.jean += 1
        elif option[0] == 3:
            self.state.scores.jean += 1
        elif option[0] == 4:
            self.state.scores.eren += 1
            self.state.scores.krista += 1
        elif option[0] == 5:
            self.state.scores.jean += 1
            self.state.scores.annie += 2

    def Q8(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
Which type of person do you respect and admire the most?\n\n\
:one: Someone who is courageous\n\n\
:two: Someone who is loyal to their friends\n\n\
:three: Someone who is honest to themselves and others\n\n\
:four: Someone who is strong and independent'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.armin += 1
            self.state.scores.eren += 1
        elif option[0] == 2:
            self.state.scores.mikasa += 2
            self.state.scores.jean += 1
        elif option[0] == 3:
            self.state.scores.krista += 2
        elif option[0] == 4:
            self.state.scores.annie += 2
            self.state.scores.levi += 1
            

    def Q9(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
Which type of food is your favourite?\n\n\
:one: Meat\n\n\
:two: Bread\n\n\
:three: Potatoes\n\n\
:four: Cake\n\n\
:five: I don\'t care much for food'
            self.choices[0] = [1,2,3,4,5]
            return response
        elif option[0] == 1:
            self.state.scores.sasha += 2
        elif option[0] == 2:
            self.state.scores.sasha += 1
        elif option[0] == 3:
            self.state.scores.sasha += 2
        elif option[0] == 4:
            self.state.scores.jean += 1
            self.state.scores.sasha += 1
        elif option[0] == 5:
            self.state.scores.annie += 1
            self.state.scores.mikasa += 1


    def Q10(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
What is your opinion on the Titans?\n\n\
:one: They are a menace to humanity and must be eradicated\n\n\
:two: They are a fascinating species and we should find out as much as we can about them\n\n\
:three: I\'m terrified at the mere mention of Titans and hope I never have to fight against them\n\n\
:four: I really couldn\'t care less about them'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 2
            self.state.scores.levi += 1
            self.state.scores.erwin += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
        elif option[0] == 3:
            self.state.scores.jean += 1
            self.state.scores.sasha += 1
        elif option[0] == 4:
            self.state.scores.annie += 1

    def Q11(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You have decided to join the Military Police Brigade. What is your reason for doing so?\n\n\
:one: To enjoy a good life in the Interior\n\n\
:two: To reform the MPs and get rid of the corruption within the ranks\n\n\
:three: For the respect and prestige that comes with it\n\n\
:four: None of the above, I have my own reasons for doing so'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.jean += 2
            self.state.scores.sasha += 1
        elif option[0] == 2:
            self.state.scores.eren += 1
            self.state.scores.erwin += 1
            self.state.scores.marco += 1
        elif option[0] == 3:
            self.state.scores.marco += 1
        elif option[0] == 4:
            self.state.scores.annie += 1

    def Q12(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
In the future, there might come a time where we will be forced to fight other humans over ideological differences. If that time comes, are you willing to take another human\'s life in service to the cause?\n\n\
:one: Yes\n\n\
:two: No'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 1
            self.state.scores.annie += 1
            self.state.scores.armin += 1
            self.state.scores.levi += 1
            self.state.scores.erwin += 2
            self.state.scores.mikasa += 1
        elif option[0] == 2:
            self.state.scores.krista += 2
            self.state.scores.jean += 1
            self.state.scores.sasha += 1

    def Q13(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You have a day off from your duties and training. How do you spend it?\n\n\
:one: Going to town with my friends\n\n\
:two: Continue with training to maintain my physique and keep my skills sharp\n\n\
:three: Reading books\n\n\
:four: On my own pursuits outside the military'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.jean += 2
            self.state.scores.sasha += 1
            self.state.scores.krista += 1
        elif option[0] == 2:
            self.state.scores.eren += 1
            self.state.scores.mikasa += 2
        elif option[0] == 3:
            self.state.scores.armin += 2
            self.state.scores.erwin += 1
        elif option[0] == 4:
            self.state.scores.annie += 2

    def Q14(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
During an expedition, the Survey Corps formation is ambushed by Titans. You see both your best friend since childhood and the commander grabbed by Titans right in front of you. You realize you only have \
time to save one of them. Who do you save?\n\n\
:one: Your best friend\n\n\
:two: The commander'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 2
            self.state.scores.mikasa += 2
            self.state.scores.krista += 1
            self.state.scores.levi += 1
        elif option[0] == 2:
            self.state.scores.armin += 2
            self.state.scores.erwin += 2


    def Q15(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
If you were participating in the pivotal Battle of Trost, where in the town\'s defense would you be assigned to, given the choice?\n\n\
:one: The vanguard, where I can be the first to slay some Titans\n\n\
:two: The middle guard, with the rest of my fellow recruits\n\n\
:three: The rear guard, to protect the inner gate and the evacuating civilians\n\n\
:four: On the other side of the wall, where it\'s the safest'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 2
        elif option[0] == 2:
            self.state.scores.krista += 1
            self.state.scores.mikasa += 1
            self.state.scores.marco += 1
        elif option[0] == 3:
            self.state.scores.marco += 1
        elif option[0] == 4:
            self.state.scores.annie += 1
            self.state.scores.jean += 1

    def Q16(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You are face to face with a Titan which to your surprise speaks to you in a polite manner. How do you respond?\n\n\
:one: Fight it, a Titan is a Titan\n\n\
:two: Attempt to communicate\n\n\
:three: Surrender and hope the Titan shows mercy\n\n\
:four: Freak out and run away as fast as possible'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 2
            self.state.scores.levi += 1
            self.state.scores.mikasa += 2
        elif option[0] == 2:
            self.state.scores.armin += 1
            self.state.scores.erwin += 1
        elif option[0] == 3:
            self.state.scores.krista += 1
            self.state.scores.jean += 1
        elif option[0] == 4:
            self.state.scores.sasha += 2
            

    def Q17(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
In a physical aptitude test, what would be your speciality?\n\n\
:one: Weight lifting\n\n\
:two: Sprints\n\n\
:three: Endurance run\n\n\
:four: Agility related tests\n\n\
:five: I\'m terrible at physical aptitude tests'
            self.choices[0] = [1,2,3,4,5]
            return response
        elif option[0] == 1:
            self.state.scores.levi += 1
            self.state.scores.mikasa += 1
        elif option[0] == 2:
            self.state.scores.mikasa += 1
        elif option[0] == 3:
            self.state.scores.eren += 2
        elif option[0] == 4:
            self.state.scores.mikasa += 1
        elif option[0] == 5:
            self.state.scores.armin += 1

    def Q18(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
Hypothetically, if you were an enemy, who would you fear the most?\n\n\
:one: Eren\n\n\
:two: Mikasa\n\n\
:three: Armin\n\n\
:four: Sasha\n\n\
:five: Erwin\n\n\
:six: I fear no one'
            self.choices[0] = [1,2,3,4,5,6]
            return response
        elif option[0] == 1:
            self.state.scores.jean += 1
            self.state.scores.erwin += 1
        elif option[0] == 2:
            self.state.scores.eren += 1
            self.state.scores.armin += 1
            self.state.scores.sasha += 1
        elif option[0] == 3:
            self.state.scores.annie += 1
        elif option[0] == 4:
            self.state.scores.jean += 1
        elif option[0] == 5:
            self.state.scores.annie += 1
            self.state.scores.armin += 1
        elif option[0] == 6:
            self.state.scores.levi += 1
            self.state.scores.mikasa += 1

    def Q19(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
What keeps you going in life?\n\n\
:one: My family\n\n\
:two: My friends\n\n\
:three: My ambitions\n\n\
:four: I\'m barely holding on'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.mikasa += 2
            self.state.scores.annie += 1
        elif option[0] == 2:
            self.state.scores.krista += 1
            self.state.scores.jean += 1
            self.state.scores.marco += 1
        elif option[0] == 3:
            self.state.scores.eren += 1
            self.state.scores.armin += 1
            self.state.scores.erwin += 2
        elif option[0] == 4:
            self.state.scores.krista += 2

    def Q20(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
While on patrol duty, you are confronted by a group of thugs in a dark alley. What is your weapon of choice to defend yourself?\n\n\
:one: Blades\n\n\
:two: Firearms\n\n\
:three: My hand-to-hand combat skills\n\n\
:four: None, I\'d rather avoid violence if I can'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.levi += 1
            self.state.scores.mikasa += 1
        elif option[0] == 2:
            self.state.scores.jean += 1
            self.state.scores.sasha += 2
        elif option[0] == 3:
            self.state.scores.annie += 2
            self.state.scores.eren += 1
        elif option[0] == 4:
            self.state.scores.krista += 1
            self.state.scores.marco += 1
            self.state.scores.armin += 1

    def Q21(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
In a hypothetical skirmish against a Titan, what role do you see yourself playing within your squad?\n\n\
:one: I\'ll be the one leading the attack on the Titan\n\n\
:two: I\'ll be coordinating my squad mates\' efforts\n\n\
:three: I\'ll be the bait to help distract the Titan\n\n\
:four: I\'ll be in charge of resupplying my squad, far from the battle'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.levi += 1
            self.state.scores.eren += 1
            self.state.scores.mikasa += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
            self.state.scores.jean += 1
            self.state.scores.erwin += 1
        elif option[0] == 3:
            self.state.scores.armin += 1
            self.state.scores.jean += 1
            self.state.scores.krista += 1
        elif option[0] == 4:
            self.state.scores.sasha += 2
            self.state.scores.jean += 1

    def Q22(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
*"The world is a cruel place."* This is a well-known quote by a former top student in the Trainee Corps. Do you agree with this sentiment?\n\n\
:one: Yes\n\n\
:two: No'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.state.scores.mikasa += 2
            self.state.scores.eren += 1
            self.state.scores.levi += 1
            self.state.scores.annie += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
            self.state.scores.erwin += 1
            self.state.scores.sasha += 1

    def Q23(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You are eating in the soldier\'s mess when you notice two of your fellow trainees getting into a heated argument nearby. It quickly escalates into a physical one as they start to trade blows. What do you do?\n\n\
:one: Ignore them, it\'s none of my business\n\n\
:two: Call out to them to stop fighting\n\n\
:three: Try to pull them apart\n\n\
:four: Stop the fight by kicking both their asses'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.annie += 2
            self.state.scores.mikasa += 1
            self.state.scores.jean += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
            self.state.scores.krista += 1
        elif option[0] == 3:
            self.state.scores.mikasa += 1
            self.state.scores.eren += 1
            self.state.scores.jean += 1
        elif option[0] == 4:
            self.state.scores.levi += 1

    def Q24(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You are sent as a representative of the Walls to negotiate a peace treaty with the leader of the Titan shifters. What is your negotiating strategy?\n\n\
:one: Threaten them with a declaration of war if they do not agree to your terms\n\n\
:two: Have a comprehensive discussion to find a middle ground that both sides would be agreeable to\n\n\
:three: Organize parties and drinking sessions to get into the other side\'s good graces\n\n\
:four: Try to appease the other side, and avoid offending them at all costs'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 2
            self.state.scores.levi += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
            self.state.scores.erwin += 1
        elif option[0] == 3:
            self.state.scores.sasha += 2
            self.state.scores.jean += 1
        elif option[0] == 4:
            self.state.scores.krista += 2

    def Q25(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You discover that your comrade is actually the Titan shifter responsible for the destruction of the Walls. What do you say to them when you next meet?\n\n\
:one: "TRAITOOOR!"\n\n\
:two: "Why did you do something like this? There must be a reason, isn\'t there?"\n\n\
:three: "I thought we were friends! How could you betray us like this?"\n\n\
:four: Nothing. I\'ll kill them first'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 2
        elif option[0] == 2:
            self.state.scores.armin += 2
            self.state.scores.erwin += 1
        elif option[0] == 3:
            self.state.scores.jean += 1
            self.state.scores.krista += 1
            self.state.scores.sasha += 1
        elif option[0] == 4:
            self.state.scores.mikasa += 2
            self.state.scores.levi += 2

    def Q26(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You wake up one day to realize that you have been granted the power to control the Titans. What do you do with it?\n\n\
:one: Use it to exterminate every last Titan from the face of the earth\n\n\
:two: Use the strength of the Titans to serve humanity\n\n\
:three: Inform the military about my newfound powers, and let them make the decision\n\n\
:four: Conceal it the best I can. No one, even myself, should be trusted with that kind of power.'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 2
            self.state.scores.levi += 1
            self.state.scores.mikasa += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
            self.state.scores.erwin += 1
        elif option[0] == 3:
            self.state.scores.jean += 1
            self.state.scores.krista += 1
        elif option[0] == 4:
            self.state.scores.krista += 2
            self.state.scores.annie += 1
            
    def Q27(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
When making decisions in life, which of these quotes do you follow the closest?\n\n\
:one: *"Those who can\'t throw something away, can never hope to change anything."*\n\n\
:two: *"I don\'t know what is the right choice. All we can do is choose whatever we believe will leave us with no regrets."*\n\n\
:three: *"Live your life with your head held high."*\n\n\
:four: *"When in doubt, follow your instincts."*'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.armin += 2
            self.state.scores.erwin += 1
            self.state.scores.jean += 1
        elif option[0] == 2:
            self.state.scores.levi += 1
            self.state.scores.eren += 1
        elif option[0] == 3:
            self.state.scores.krista += 2
        elif option[0] == 4:
            self.state.scores.sasha += 2
            self.state.scores.eren += 1
            self.state.scores.mikasa += 1

    def Q28(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
Titans have invaded the headquarters of the Survey Corps. In the rush to escape, you have just enough time to retrieve one thing. What do you choose?\n\n\
:one: Gas canisters to save my trapped comrades\n\n\
:two: The officers\' stock of meat and booze\n\n\
:three: The only written record of the past five years of expeditions and Titan research\n\n\
:four: My personal effects from my hometown'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.krista += 2
            self.state.scores.mikasa += 1
            self.state.scores.jean += 1
        elif option[0] == 2:
            self.state.scores.sasha += 2
            self.state.scores.jean += 1
        elif option[0] == 3:
            self.state.scores.armin += 1
            self.state.scores.erwin += 1
        elif option[0] == 4:
            self.state.scores.annie += 1

    def Q29(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
If your squad leader gave you an order you disagreed with, would you obey?\n\n\
:one: Yes. I\'m a soldier and it\'s an order after all.\n\n\
:two: I would hesitate but carry out the order. My squad leader is likely acting on intelligence I do not know about.\n\n\
:three: I would question the rationale of the order and only carry it out if I am satisfied with my squad leader\'s explanation.\n\n\
:four: No. I would stand my ground against such a foolish decision.'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.krista += 1
            self.state.scores.jean += 1
            self.state.scores.sasha += 1
        elif option[0] == 2:
            self.state.scores.armin += 2
            self.state.scores.erwin += 1
            self.state.scores.jean += 1
            self.state.scores.eren += 1
            self.state.scores.levi += 1
        elif option[0] == 3:
            self.state.scores.erwin += 2
            self.state.scores.armin += 1
            self.state.scores.mikasa += 1
        elif option[0] == 4:
            self.state.scores.annie += 2

    def Q30(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
When choosing your lifelong partner, what is the most important criteria for you?\n\n\
:one: How attractive he/she is in my eyes\n\n\
:two: That we love each other deeply\n\n\
:three: Our compatibility within society\n\n\
:four: I prefer to remain single'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.jean += 1
        elif option[0] == 2:
            self.state.scores.krista += 1
            self.state.scores.mikasa += 1
        elif option[0] == 3:
            self.state.scores.armin += 1
        elif option[0] == 4:
            self.state.scores.erwin += 1
            self.state.scores.levi += 1
            self.state.scores.eren += 1

    def Q31(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
A family member you love very much wants to join the Survey Corps, which has a fatality rate of over 90%. What do you do?\n\n\
:one: Do your best to persuade them not to join \n\n\
:two: Respect their decision\n\n\
:three: Join yourself in order to protect them\n\n\
:four: Break both their legs to prevent them from joining. Sometimes tough love is needed'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.armin += 1
            self.state.scores.mikasa += 1
            self.state.scores.krista += 1
        elif option[0] == 2:
            self.state.scores.jean += 1
            self.state.scores.annie += 1
            self.state.scores.eren += 1
            self.state.scores.erwin += 1
        elif option[0] == 3:
            self.state.scores.mikasa += 2
        elif option[0] == 4:
            self.state.scores.levi += 1
            
    def Q32(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You discover that your superior has been selling military equipment to the black market. Do you expose them?\n\n\
:one: Yes, they need to be brought to justice\n\n\
:two: No, it\'s not worth the effort and risk of attracting trouble to myself'
            self.choices[0] = [1,2]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 1
            self.state.scores.erwin += 1
        elif option[0] == 2:
            self.state.scores.krista += 1
            self.state.scores.annie += 1

    def Q33(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
When do you come up with your best ideas?\n\n\
:one: In the heat of battle\n\n\
:two: While meditating in a quiet room\n\n\
:three: In the midst of discussion with others\n\n\
:four: While having fun and enjoying myself'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 1
            self.state.scores.mikasa += 1
            self.state.scores.jean += 1
        elif option[0] == 2:
            self.state.scores.erwin += 1
        elif option[0] == 3:
            self.state.scores.armin += 1
            self.state.scores.krista += 1
        elif option[0] == 4:
            self.state.scores.sasha += 1

    def Q34(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
People tend to question your...\n\n\
:one: Judgment\n\n\
:two: Confidence\n\n\
:three: Self-control\n\n\
:four: Ability to relax'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 1
            self.state.scores.sasha += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
            self.state.scores.krista += 1
        elif option[0] == 3:
            self.state.scores.eren += 1
            self.state.scores.mikasa += 1
            self.state.scores.sasha += 2
        elif option[0] == 4:
            self.state.scores.levi += 1  
            self.state.scores.mikasa += 1 
            self.state.scores.annie += 1
            self.state.scores.eren += 1

    def Q35(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You are challenged to a friendly game of strategy against the commander. How would you win?\n\n\
:one: By intimidating them\n\n\
:two: Using my wits to beat them fair and square\n\n\
:three: Letting the commander underestimate me\n\n\
:four: I\'d lose on purpose to get on their good side'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.eren += 1
            self.state.scores.jean += 1
            self.state.scores.levi += 1
        elif option[0] == 2:
            self.state.scores.eren += 1
            self.state.scores.mikasa += 1
        elif option[0] == 3:
            self.state.scores.annie += 1
            self.state.scores.armin += 1
        elif option[0] == 4:
            self.state.scores.armin += 2
            self.state.scores.erwin += 1
            self.state.scores.krista += 1

    def Q36(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
Imagine that you have found a key and are holding it in your hand. How does it appear to you?\n\n\
:one: Dark and foreboding\n\n\
:two: Ornate and beautiful\n\n\
:three: Shiny and intriguing\n\n\
:four: Ordinary looking - like every other key'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.mikasa += 1
            self.state.scores.levi += 1
            self.state.scores.erwin += 1
        elif option[0] == 2:
            self.state.scores.sasha += 1
            self.state.scores.krista += 1
        elif option[0] == 3:
            self.state.scores.armin += 1
            self.state.scores.erwin += 1
            self.state.scores.sasha += 1
        elif option[0] == 4: 
            self.state.scores.annie += 1
            self.state.scores.jean += 1
            self.state.scores.krista += 1

    def Q37(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
All of your squad mates just lost their lives in the recent expedition, with you being the only survivor. How do you handle it?\n\n\
:one: I\'ll fall into depression from survivor\'s guilt\n\n\
:two: I\'ll shrug it off and move on\n\n\
:three: I\'ll push myself even harder to ensure their sacrifices had meaning'
            self.choices[0] = [1,2,3]
            return response
        elif option[0] == 1:
            self.state.scores.krista += 1
            self.state.scores.sasha += 1
            self.state.scores.annie += 1
            self.state.scores.mikasa += 1
        elif option[0] == 2:
            self.state.scores.levi += 1
            self.state.scores.erwin += 1
            self.state.scores.annie += 1
        elif option[0] == 3:
            self.state.scores.jean += 2
            self.state.scores.levi += 1
            self.state.scores.eren += 1

    def Q38(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
Imagine yourself standing on top of the Walls, looking out at the world beyond. What do you see?\n\n\
:one: A vast countryside, stretching out to the horizon\n\n\
:two: A snowy forest\n\n\
:three: A beautiful meadow\n\n\
:four: A Titan-infested landscape'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.armin += 2
            self.state.scores.erwin += 1
        elif option[0] == 2:
            self.state.scores.annie += 2
            self.state.scores.krista += 1
        elif option[0] == 3:
            self.state.scores.krista += 1
            self.state.scores.sasha += 1
        elif option[0] == 4:
            self.state.scores.eren += 2
            self.state.scores.levi += 1
            self.state.scores.mikasa += 1

    def Q39(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
Some trainees under your charge have been caught misbehaving. As their instructor, how do you punish them?\n\n\
:one: Get them to clean the entire barracks\n\n\
:two: Deny them food for the whole day\n\n\
:three: Put them in solitary confinement\n\n\
:four: Assign them to additional menial duties'
            self.choices[0] = [1,2,3,4]
            return response
        elif option[0] == 1:
            self.state.scores.levi += 1
        elif option[0] == 2:
            self.state.scores.sasha += 2
        elif option[0] == 3:
            self.state.scores.eren += 2
            self.state.scores.mikasa += 1
        elif option[0] == 4:
            self.state.scores.erwin += 1
            self.state.scores.armin += 1
            self.state.scores.jean += 1

    def Q40(self, *option):
        if option == ():
            response = '**Question ' + str(len(self.qns_played)) + '**\n\n\
You are on a routine training mission with your fellow trainees when you find out that you are lost. What do you do?\n\n\
:one: Refuse to believe it and keep walking\n\n\
:two: Attempt to backtrack to the last known location using landmarks\n\n\
:three: Get everyone to think of ideas to get out of the situation\n\n\
:four: Freak out and panic\n\n\
:five: Nothing. My squad will get out of this, no problem\n\n\
:six: Send up a signal flare and wait for rescue'
            self.choices[0] = [1,2,3,4,5,6]
            return response
        elif option[0] == 1:
            self.state.scores.jean += 1
            self.state.scores.eren += 1
        elif option[0] == 2:
            self.state.scores.armin += 1
        elif option[0] == 3:
            self.state.scores.jean += 1
            self.state.scores.krista += 1
        elif option[0] == 4:
            self.state.scores.sasha += 1
        elif option[0] == 5:
            self.state.scores.annie += 1
        elif option[0] == 6:
            self.state.scores.erwin += 1
            self.state.scores.armin += 1

    def result(self, *option):
        if option == ():
            response = 'Collating responses...\n\n\
Result obtained!\n\n\
Type `~result` to see your Attack on Titan persona!'
            self.choices[0] = []
            return response

