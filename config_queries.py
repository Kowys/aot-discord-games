import sqlite3

def initialize_dbs():
    databases = {
        'config_db.db': [
            ('instances', ['server integer', 'channel integer', 'game text'])
        ],
        'AttackonWikia/aow_db.db': [
            ('players', ['player integer', 'exp integer', 'correct_answers integer', 'challenges_played integer', 'challenges_won integer', 'hangman_correct integer', 'images_correct integer']),
            ('achievements', ['player integer', 'one_clue integer', 'challenges_played integer', 'last_play text', 'current_streak integer', 'max_streak integer', 'perfect_hangman integer',
            'one_clue_gm integer', 'challenges_gm integer', 'streak_gm integer', 'hangman_gm integer']),
            ('dailies', ['player integer', 'last_play text', 'standard integer', 'hangman integer', 'challenge integer', 'image integer']),
            ('overall', ['questions_asked integer', 'questions_correct integer', 'challenges_completed integer', 'challenge_questions integer', 'challenge_questions_correct integer',
            'hangman_games_played integer', 'hangman_games_won integer', 'images_generated integer', 'images_correct integer'])
        ],
        'ChooseYourAdventure/cya_db.db': [
            ('endings', ['player integer', 'joining_the_garrison integer', 'an_ordinary_moment_of_happiness integer', 'jean_kirstein_of_the_survey_corps integer', 'a_narrow_victory integer',
            'armin_arlerts_dream integer', 'captain_levis_recruit integer', 'mikasas_true_face integer', 'nameless_hero integer', 'eren_yeagers_hand integer', 'sasha_blouses_promise integer',
            'the_girl_who_hid_her_true_self integer', 'no_regrets integer', 'jean_of_the_military_police integer', 'trial_of_eren_and_mikasa integer', 'a_soldiers_duty integer', 
            'failure_of_the_reclamation_plan integer', 'a_regular_soldier integer', 'annihilated_at_hq integer', 'the_fall_of_wall_rose integer', 'failure_to_reclaim_trost_district integer', 
            'a_moments_peace integer', 'eren_flees integer', 'the_death_of_a_merchant integer', 'junior_high integer']),
            ('endings2', ['player integer', 'a_cruel_world integer', 'destruction_of_the_survey_corps integer', 'traitors_friend integer', 'a_soldier_in_the_trost_district_garrison integer',
            'a_silver_of_hope integer', 'beyond_the_walls integer', 'eren_yeagers_choice integer', 'jean_kirsteins_vow integer', 'flight_of_the_female_titan integer', 'the_true_face_of_sasha_blouse integer',
            'the_girl_who_hid_herself integer', 'a_world_beautiful_and_cruel integer', 'hange_zoes_truth integer', 'armin_arlerts_dream integer', 'captain_levis_scars integer', 
            'a_soldier_of_the_survey_corps integer']),
            ('annie_progress', ['player integer', 'progress integer']),
            ('global', ['ending text', 'count integer']),
            ('global2', ['ending text', 'count integer'])
        ],
        'Jaegermore/jaegermore_db.db': [
            ('players', ['player integer', 'eren integer', 'mikasa integer', 'armin integer', 'jean integer', 'krista integer', 'sasha integer', 'levi integer', 'annie integer', 'erwin integer']),
            ('global', ['eren integer', 'mikasa integer', 'armin integer', 'jean integer', 'krista integer', 'sasha integer', 'levi integer', 'annie integer', 'erwin integer', 'total integer'])
        ],
        'WarriorsvsSoldiers/wvs_db.db': [
            ('players', ['player integer', 'rating integer', 'current_streak integer', 'best_streak integer', 'soldier_wins integer', 'soldier_games integer', 
            'warrior_wins integer', 'warrior_games integer', 'coordinate_wins integer', 'coordinate_games integer', 'queen_wins integer', 'queen_games integer', 
            'warchief_wins integer', 'warchief_games integer', 'ymir_wins integer', 'ymir_games integer', 'false_king_wins integer', 'false_king_games integer', 
            'ackerman_wins integer', 'ackerman_games integer', 'mike_wins integer', 'mike_games integer', 'scout_wins integer', 'scout_games integer', 'spy_wins integer', 'spy_games integer',
            'hunter_wins integer', 'hunter_games integer', 'saboteur_wins integer', 'saboteur_games integer']),
            ('global', ['number_of_players integer', 'soldiers integer', 'warriors_walls integer', 'warriors_kidnap integer']),
            ('servers', ['server integer', 'soldiers_5 integer', 'warriors_walls_5 integer', 'warriors_kidnap_5 integer',
            'soldiers_6 integer', 'warriors_walls_6 integer', 'warriors_kidnap_6 integer',
            'soldiers_7 integer', 'warriors_walls_7 integer', 'warriors_kidnap_7 integer',
            'soldiers_8 integer', 'warriors_walls_8 integer', 'warriors_kidnap_8 integer',
            'soldiers_9 integer', 'warriors_walls_9 integer', 'warriors_kidnap_9 integer',
            'soldiers_10 integer', 'warriors_walls_10 integer', 'warriors_kidnap_10 integer',
            'soldier_wins integer', 'soldier_games integer', 'warrior_wins integer', 'warrior_games integer', 'coordinate_wins integer', 'coordinate_games integer',
            'queen_wins integer', 'queen_games integer', 'warchief_wins integer', 'warchief_games integer', 'ymir_wins integer', 'ymir_games integer',
            'false_king_wins integer', 'false_king_games integer', 'ackerman_wins integer', 'ackerman_games integer', 'mike_wins integer', 'mike_games integer',
            'scout_wins integer', 'scout_games integer', 'spy_wins integer', 'spy_games integer', 'hunter_wins integer', 'hunter_games integer', 'saboteur_wins integer', 'saboteur_games integer']),
            ('timers', ['channel integer', 'next_expedition integer', 'selection integer', 'approval integer', 'decision integer', 'kidnap integer', 'blessing integer', 'paths integer', 'saboteur integer'])
        ]
    }

    for db in databases:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

        for table in databases[db]:
            # Create table if it doesn't exist
            table_cols = ', '.join(table[1])
            create_table = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(table[0], table_cols)
            cursor.execute(create_table)

        conn.commit()
        conn.close()

    init_aow_global()
    init_cya_global()
    init_jaegermore_global()
    init_wvs_global()

    print('All databases initialized.')

def init_aow_global():
    conn = sqlite3.connect('AttackonWikia/aow_db.db')
    cursor = conn.cursor()

    select_aow_global_query = 'SELECT * FROM overall'
    cursor.execute(select_aow_global_query)
    global_stats = cursor.fetchall()

    if len(global_stats) == 0:
        insert_aow_global_query = 'INSERT INTO overall VALUES ({})'.format(','.join('?' * 9))
        insert_aow_global_data = [0] * 9
        cursor.execute(insert_aow_global_query, insert_aow_global_data)

        conn.commit()
        conn.close()

def init_cya_global():
    conn = sqlite3.connect('ChooseYourAdventure/cya_db.db')
    cursor = conn.cursor()

    select_cya_global_query = 'SELECT * FROM global'
    cursor.execute(select_cya_global_query)
    global_stats = cursor.fetchall()

    if len(global_stats) == 0:
        insert_cya_global_query = 'INSERT INTO global VALUES ({})'.format(','.join('?' * 2))
        insert_cya_global_data = [
            ['Joining the Garrison', 0], 
            ['An Ordinary Moment of Happiness', 0],
            ['Jean Kirstein of the Survey Corps', 0],
            ['A Narrow Victory', 0],
            ['Armin Arlert\'s Dream', 0],
            ['Captain Levi\'s Recruit', 0],
            ['Mikasa\'s True Face', 0],
            ['Nameless Hero', 0],
            ['Eren Yeager\'s Hand', 0],
            ['Sasha Blouse\'s Promise', 0],
            ['The Girl Who Hid Her True Self', 0],
            ['No Regrets', 0],
            ['Jean of the Military Police', 0],
            ['Trial of Eren and Mikasa', 0],
            ['A Soldier\'s Duty', 0],
            ['Failure of the Reclamation Plan', 0],
            ['A Regular Soldier', 0],
            ['104th Annihilated at HQ', 0],
            ['The Fall of Wall Rose', 0],
            ['Failure to Reclaim Trost District', 0],
            ['A Moment\'s Peace', 0],
            ['Eren Flees', 0],
            ['The Death of a Merchant', 0],
            ['Junior High', 0]
        ]
        for row in insert_cya_global_data:
            cursor.execute(insert_cya_global_query, row)

        conn.commit()
    
    select_cya_global_query2 = 'SELECT * FROM global2'
    cursor.execute(select_cya_global_query2)
    global_stats2 = cursor.fetchall()

    if len(global_stats2) == 0:
        insert_cya_global_query2 = 'INSERT INTO global2 VALUES ({})'.format(','.join('?' * 2))
        insert_cya_global_data2 = [
            ['A Cruel World', 0], 
            ['Destruction of the Survey Corps', 0],
            ['Traitor’s Friend', 0],
            ['A Soldier in the Trost District Garrison', 0],
            ['A Sliver of Hope', 0],
            ['Beyond the Walls', 0],
            ['Eren Yeager’s Choice', 0],
            ['Jean Kirstein’s Vow', 0],
            ['Flight of the Female Titan', 0],
            ['The True Face of Sasha Blouse', 0],
            ['The Girl Who Hid Herself', 0],
            ['A World Beautiful and Cruel', 0],
            ['Hange Zoë’s Truth', 0],
            ['Armin Arlert’s Dream', 0],
            ['Captain Levi’s Scars', 0],
            ['A Soldier of the Survey Corps', 0]
        ]
        for row in insert_cya_global_data2:
            cursor.execute(insert_cya_global_query2, row)

        conn.commit()
    
    conn.close()

def init_jaegermore_global():
    conn = sqlite3.connect('Jaegermore/jaegermore_db.db')
    cursor = conn.cursor()

    select_jaegermore_global_query = 'SELECT * FROM global'
    cursor.execute(select_jaegermore_global_query)
    global_stats = cursor.fetchall()

    if len(global_stats) == 0:
        insert_jaegermore_global_query = 'INSERT INTO global VALUES ({})'.format(','.join('?' * 10))
        insert_jaegermore_global_data = [0] * 10
        cursor.execute(insert_jaegermore_global_query, insert_jaegermore_global_data)

        conn.commit()
        conn.close()

def init_wvs_global():
    conn = sqlite3.connect('WarriorsvsSoldiers/wvs_db.db')
    cursor = conn.cursor()

    select_wvs_global_query = 'SELECT * FROM global'
    cursor.execute(select_wvs_global_query)
    global_stats = cursor.fetchall()

    if len(global_stats) == 0:
        insert_wvs_global_query = 'INSERT INTO global VALUES ({})'.format(','.join('?' * 4))
        insert_wvs_global_data = [[5,0,0,0],[6,0,0,0],[7,0,0,0],[8,0,0,0],[9,0,0,0],[10,0,0,0]]
        for row in insert_wvs_global_data:
            cursor.execute(insert_wvs_global_query, row)

        conn.commit()
        conn.close()

def get_instances():
    conn = sqlite3.connect('config_db.db')
    cursor = conn.cursor()

    get_instances = 'SELECT * FROM instances'
    cursor.execute(get_instances)
    instance_data = cursor.fetchall()

    conn.close()

    return instance_data

def update_config(server_id, channel_id, game):
    # Swap game if found in instances, otherwise append to it
    conn = sqlite3.connect('config_db.db')
    cursor = conn.cursor()

    get_instance = 'SELECT * FROM instances WHERE channel = ?'
    cursor.execute(get_instance, (channel_id,))
    instance_data = cursor.fetchall()

    if game != 'None':
        if len(instance_data) == 0:
            # Add new instance
            insert_data = 'INSERT INTO instances VALUES (?,?,?)'
            cursor.execute(insert_data, (server_id, channel_id, game))
        else:
            # Update game for instance
            update_data = 'UPDATE instances SET game = ? WHERE channel = ?'
            cursor.execute(update_data, (game, channel_id))
    elif len(instance_data) != 0:
        # Delete instance
        delete_data = 'DELETE FROM instances WHERE channel = ?'
        cursor.execute(delete_data, (channel_id,))
    
    conn.commit()
    conn.close()