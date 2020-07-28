import sqlite3
from openpyxl import load_workbook

def migrate_data():
    wb = load_workbook("records.xlsx")

    migrate_players(wb)
    migrate_achievements(wb)
    migrate_dailies(wb)
    migrate_overall(wb)

    print('Data migrated to SQLite!')

def migrate_players(wb):
    player_data = wb['Players']

    conn = sqlite3.connect('aow_db.db')
    cursor = conn.cursor()

    i = 0
    for _ in player_data:
        i += 1
        if i == 1:
            continue

        row_values = [
            player_data['A' + str(i)].value,
            player_data['B' + str(i)].value,
            player_data['C' + str(i)].value,
            player_data['D' + str(i)].value,
            player_data['E' + str(i)].value,
            player_data['F' + str(i)].value,
            player_data['G' + str(i)].value
        ]
        check_row = 'SELECT * FROM players WHERE player=?'
        cursor.execute(check_row, (row_values[0],))
        data = cursor.fetchall()

        if len(data) == 0:
            placeholder = ','.join('?' * len(row_values))
            insert_row = 'INSERT INTO players VALUES ({})'.format(placeholder)
            cursor.execute(insert_row, row_values)
    
    conn.commit()
    conn.close()

def migrate_achievements(wb):
    achievements_data = wb['Achievements']

    conn = sqlite3.connect('aow_db.db')
    cursor = conn.cursor()

    i = 0
    for _ in achievements_data:
        i += 1
        if i == 1:
            continue

        row_values = [
            achievements_data['A' + str(i)].value,
            achievements_data['B' + str(i)].value,
            achievements_data['C' + str(i)].value,
            achievements_data['D' + str(i)].value,
            achievements_data['E' + str(i)].value,
            achievements_data['F' + str(i)].value,
            achievements_data['G' + str(i)].value,
            achievements_data['H' + str(i)].value if achievements_data['H' + str(i)].value != None else 0,
            achievements_data['I' + str(i)].value if achievements_data['I' + str(i)].value != None else 0,
            achievements_data['J' + str(i)].value if achievements_data['J' + str(i)].value != None else 0,
            achievements_data['K' + str(i)].value if achievements_data['K' + str(i)].value != None else 0
        ]
        check_row = 'SELECT * FROM achievements WHERE player=?'
        cursor.execute(check_row, (row_values[0],))
        data = cursor.fetchall()

        if len(data) == 0:
            placeholder = ','.join('?' * len(row_values))
            insert_row = 'INSERT INTO achievements VALUES ({})'.format(placeholder)
            cursor.execute(insert_row, row_values)
    
    conn.commit()
    conn.close()

def migrate_dailies(wb):
    dailies_data = wb['Dailies']

    conn = sqlite3.connect('aow_db.db')
    cursor = conn.cursor()

    i = 0
    for _ in dailies_data:
        i += 1
        if i == 1:
            continue

        row_values = [
            dailies_data['A' + str(i)].value,
            dailies_data['B' + str(i)].value,
            dailies_data['C' + str(i)].value,
            dailies_data['D' + str(i)].value,
            dailies_data['E' + str(i)].value,
            dailies_data['F' + str(i)].value
        ]
        check_row = 'SELECT * FROM dailies WHERE player=?'
        cursor.execute(check_row, (row_values[0],))
        data = cursor.fetchall()

        if len(data) == 0:
            placeholder = ','.join('?' * len(row_values))
            insert_row = 'INSERT INTO dailies VALUES ({})'.format(placeholder)
            cursor.execute(insert_row, row_values)
    
    conn.commit()
    conn.close()

def migrate_overall(wb):
    overall_data = wb['Overall']

    conn = sqlite3.connect('aow_db.db')
    cursor = conn.cursor()

    i = 0
    for _ in overall_data:
        i += 1
        if i == 1:
            continue

        row_values = [
            overall_data['A' + str(i)].value,
            overall_data['B' + str(i)].value,
            overall_data['C' + str(i)].value,
            overall_data['D' + str(i)].value,
            overall_data['E' + str(i)].value,
            overall_data['F' + str(i)].value,
            overall_data['G' + str(i)].value,
            overall_data['H' + str(i)].value,
            overall_data['I' + str(i)].value
        ]

        placeholder = ','.join('?' * len(row_values))
        insert_row = 'INSERT INTO overall VALUES ({})'.format(placeholder)
        cursor.execute(insert_row, row_values)
    
    conn.commit()
    conn.close()

migrate_data()