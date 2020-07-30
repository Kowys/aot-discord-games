import sqlite3
from openpyxl import load_workbook

def migrate_data():
    wb = load_workbook("records.xlsx")

    migrate_players(wb)
    migrate_global(wb)

    print('Data migrated to SQLite!')


def migrate_players(wb):
    conn = sqlite3.connect('jaegermore_db.db')
    cursor = conn.cursor()

    players_data = wb['Players']

    i = 0
    for _ in players_data:
        i += 1
        if i == 1:
            continue

        row_values = [
            players_data['A' + str(i)].value,
            players_data['B' + str(i)].value,
            players_data['C' + str(i)].value,
            players_data['D' + str(i)].value,
            players_data['E' + str(i)].value,
            players_data['F' + str(i)].value,
            players_data['G' + str(i)].value,
            players_data['H' + str(i)].value,
            players_data['I' + str(i)].value,
            players_data['J' + str(i)].value
        ]
        check_row = 'SELECT * FROM players WHERE player = ?'
        cursor.execute(check_row, (row_values[0],))
        data = cursor.fetchone()

        if data is None:
            insert_row = 'INSERT INTO players VALUES ({})'.format(','.join('?' * len(row_values)))
            cursor.execute(insert_row, row_values)

    conn.commit()
    conn.close()

def migrate_global(wb):
    conn = sqlite3.connect('jaegermore_db.db')
    cursor = conn.cursor()

    global_data = wb['Global']

    i = 0
    for _ in global_data:
        i += 1
        if i == 1:
            continue

        row_values = [
            global_data['B' + str(i)].value,
            global_data['C' + str(i)].value,
            global_data['D' + str(i)].value,
            global_data['E' + str(i)].value,
            global_data['F' + str(i)].value,
            global_data['G' + str(i)].value,
            global_data['H' + str(i)].value,
            global_data['I' + str(i)].value,
            global_data['J' + str(i)].value,
            global_data['K' + str(i)].value
        ]

        insert_row = 'INSERT INTO global VALUES ({})'.format(','.join('?' * len(row_values)))
        cursor.execute(insert_row, row_values)

    conn.commit()
    conn.close()

migrate_data()