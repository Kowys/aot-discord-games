import sqlite3
from openpyxl import load_workbook

def migrate_data():
    wb = load_workbook("config.xlsx")
    instance_data = wb['Instances']

    conn = sqlite3.connect('config_db.db')
    cursor = conn.cursor()

    i = 0
    for _ in instance_data:
        i += 1
        if i == 1:
            continue

        row_values = [
            instance_data['A' + str(i)].value,
            instance_data['B' + str(i)].value,
            instance_data['C' + str(i)].value
        ]
        check_row = 'SELECT * FROM instances WHERE channel=?'
        cursor.execute(check_row, (row_values[1],))
        data = cursor.fetchall()

        if len(data) == 0:
            placeholder = ','.join('?' * len(row_values))
            insert_row = 'INSERT INTO instances VALUES ({})'.format(placeholder)
            cursor.execute(insert_row, row_values)
    
    conn.commit()
    conn.close()

    print('Data migrated to SQLite!')

migrate_data()