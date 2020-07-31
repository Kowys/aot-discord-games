import sqlite3
from openpyxl import load_workbook

def migrate_data():
    wb = load_workbook("database.xlsx")

    migrate_players(wb)
    migrate_global(wb)

    print('Data migrated to SQLite!')

def migrate_players(wb):
    conn = sqlite3.connect('wvs_db.db')
    cursor = conn.cursor()

    players_data = wb['Player records']

    i = 0
    for _ in players_data:
        i += 1
        if i == 1:
            continue

        row_values = [
            players_data['A' + str(i)].value,
            players_data['B' + str(i)].value,

            players_data['S' + str(i)].value,
            players_data['T' + str(i)].value,

            players_data['I' + str(i)].value,
            players_data['J' + str(i)].value,
            players_data['K' + str(i)].value,
            players_data['L' + str(i)].value,
            players_data['M' + str(i)].value,
            players_data['N' + str(i)].value,

            players_data['O' + str(i)].value,
            players_data['P' + str(i)].value,
            players_data['Q' + str(i)].value,
            players_data['R' + str(i)].value,

            players_data['U' + str(i)].value,
            players_data['V' + str(i)].value,
            players_data['W' + str(i)].value,
            players_data['X' + str(i)].value,

            players_data['Y' + str(i)].value,
            players_data['Z' + str(i)].value,
            players_data['AA' + str(i)].value,
            players_data['AB' + str(i)].value,

            players_data['AC' + str(i)].value,
            players_data['AD' + str(i)].value,
            players_data['AE' + str(i)].value,
            players_data['AF' + str(i)].value
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
    conn = sqlite3.connect('wvs_db.db')
    cursor = conn.cursor()

    global_data = wb['Game records']

    transposed_data = [[0 for i in range(4)] for j in range(6)]
    i = 0
    for _ in global_data:
        i += 1
        if i in [1,2,4,6]:
            row_values = [
                global_data['B' + str(i)].value,
                global_data['C' + str(i)].value,
                global_data['D' + str(i)].value,
                global_data['E' + str(i)].value,
                global_data['F' + str(i)].value,
                global_data['G' + str(i)].value
            ]
            for j in range(len(row_values)):
                transposed_data[j][i // 2] = row_values[j]

    for row in transposed_data:
        insert_row_query = 'INSERT INTO global VALUES ({})'.format(','.join('?' * len(row)))
        cursor.execute(insert_row_query, row)

    conn.commit()
    conn.close()

migrate_data()