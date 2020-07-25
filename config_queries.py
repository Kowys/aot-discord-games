import sqlite3

def initialize_dbs():
    databases = {
        'config_db.db': [
            ('instances', ['server integer', 'channel integer', 'game text'])
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