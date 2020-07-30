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
            ('annie_progress', ['player integer', 'progress integer']),
            ('global', ['ending text', 'count integer'])
        ],
        'Jaegermore/jaegermore_db.db': [
            ('players', ['player integer', 'eren integer', 'mikasa integer', 'armin integer', 'jean integer', 'krista integer', 'sasha integer', 'levi integer', 'annie integer', 'erwin integer']),
            ('global', ['eren integer', 'mikasa integer', 'armin integer', 'jean integer', 'krista integer', 'sasha integer', 'levi integer', 'annie integer', 'erwin integer', 'total integer'])
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

    print('All databases initialized.')

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

    get_instance = 'SELECT * FROM instances WHERE channel=?'
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