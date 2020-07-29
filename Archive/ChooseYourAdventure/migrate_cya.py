import sqlite3
from openpyxl import load_workbook

def migrate_data():
    wb = load_workbook("player data.xlsx")

    migrate_endings(wb)
    migrate_annie(wb)
    migrate_global(wb)

    print('Data migrated to SQLite!')


def migrate_endings(wb):
    endings_data = wb['Endings']

    conn = sqlite3.connect('cya_db.db')
    cursor = conn.cursor()

    endings_index_map = {'Joining the Garrison':0, 'An Ordinary Moment of Happiness':1, 'Jean Kirstein of the Survey Corps':2, 'A Narrow Victory':3, 'Armin Arlert\'s Dream':4,
    'Captain Levi\'s Recruit':5, 'Mikasa\'s True Face':6, 'Nameless Hero':7, 'Eren Yeager\'s Hand':8, 'Sasha Blouse\'s Promise':9, 'The Girl Who Hid Her True Self':10,
    'No Regrets':11, 'Jean of the Military Police':12, 'Trial of Eren and Mikasa':13, 'A Soldier\'s Duty':14, 'Failure of the Reclamation Plan':15, 'A Regular Soldier':16,
    '104th Annihilated at HQ':17, 'The Fall of Wall Rose':18, 'Failure to Reclaim Trost District':19, 'A Moment\'s Peace':20, 'Eren Flees':21, 'The Death of a Merchant':22,
    'Junior High':23}

    endings_db_map = {'Joining the Garrison':'joining_the_garrison', 'An Ordinary Moment of Happiness':'an_ordinary_moment_of_happiness', 
    'Jean Kirstein of the Survey Corps':'jean_kirstein_of_the_survey_corps', 'A Narrow Victory':'a_narrow_victory', 'Armin Arlert\'s Dream':'armin_arlerts_dream',
    'Captain Levi\'s Recruit':'captain_levis_recruit', 'Mikasa\'s True Face':'mikasas_true_face', 'Nameless Hero':'nameless_hero', 'Eren Yeager\'s Hand':'eren_yeagers_hand', 
    'Sasha Blouse\'s Promise':'sasha_blouses_promise', 'The Girl Who Hid Her True Self':'the_girl_who_hid_her_true_self', 'No Regrets':'no_regrets', 
    'Jean of the Military Police':'jean_of_the_military_police', 'Trial of Eren and Mikasa':'trial_of_eren_and_mikasa', 'A Soldier\'s Duty':'a_soldiers_duty', 
    'Failure of the Reclamation Plan':'failure_of_the_reclamation_plan', 'A Regular Soldier':'a_regular_soldier','104th Annihilated at HQ':'annihilated_at_hq', 
    'The Fall of Wall Rose':'the_fall_of_wall_rose', 'Failure to Reclaim Trost District':'failure_to_reclaim_trost_district', 'A Moment\'s Peace':'a_moments_peace', 
    'Eren Flees':'eren_flees', 'The Death of a Merchant':'the_death_of_a_merchant','Junior High':'junior_high'}

    i = 0
    for _ in endings_data:
        i += 1

        row_values = [
            endings_data['A' + str(i)].value,
            endings_data['B' + str(i)].value,
        ]
        check_row = 'SELECT * FROM endings WHERE player = ?'
        cursor.execute(check_row, (row_values[0],))
        data = cursor.fetchone()

        if data is None:
            insert_row = 'INSERT INTO endings VALUES ({})'.format(','.join('?' * 25))
            insert_position = endings_index_map[row_values[1]]
            insert_data = [row_values[0]] + [0] * insert_position + [1] + [0] * (25 - 2 - insert_position)
            cursor.execute(insert_row, insert_data)
        else:
            update_row = 'UPDATE endings SET {} = ? WHERE player = ?'.format(endings_db_map[row_values[1]])
            ending_index = 1 + endings_index_map[row_values[1]]
            update_data = [data[ending_index] + 1, data[0]]
            cursor.execute(update_row, update_data)
    
    conn.commit()
    conn.close()

def migrate_annie(wb):
    annie_data = wb['Annie progress']

    conn = sqlite3.connect('cya_db.db')
    cursor = conn.cursor()

    annie_map = {'two':1, 'three':2, 'four':3, 'five':4, 'victory':5}

    i = 0
    for _ in annie_data:
        i += 1

        row_values = [
            annie_data['A' + str(i)].value,
            annie_data['B' + str(i)].value,
        ]
        check_row = 'SELECT * FROM annie_progress WHERE player = ?'
        cursor.execute(check_row, (row_values[0],))
        data = cursor.fetchone()

        if data is None:
            insert_row = 'INSERT INTO annie_progress VALUES (?,?)'
            insert_data = [row_values[0], annie_map[row_values[1]]]
            cursor.execute(insert_row, insert_data)
        else:
            update_row = 'UPDATE annie_progress SET progress = ? WHERE player = ?'
            highest_progress = max(data[1], annie_map[row_values[1]])
            update_data = [highest_progress, data[0]]
            cursor.execute(update_row, update_data)

    conn.commit()
    conn.close()

def migrate_global(wb):
    global_data = wb['Global']

    conn = sqlite3.connect('cya_db.db')
    cursor = conn.cursor()

    i = 0
    for _ in global_data:
        i += 1

        row_values = [
            global_data['A' + str(i)].value,
            global_data['B' + str(i)].value,
        ]

        insert_row = 'INSERT INTO global VALUES (?,?)'
        insert_data = [row_values[0], row_values[1]]
        cursor.execute(insert_row, insert_data)

    conn.commit()
    conn.close()

migrate_data()