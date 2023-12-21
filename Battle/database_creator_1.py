import sqlite3

conn = sqlite3.connect('../DataBase/game.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS units (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        unit_min_damage INTEGER,
        unit_max_damage INTEGER,
        unit_speed INTEGER,
        unit_attack INTEGER,
        unit_defence INTEGER,
        the_ability INTEGER,
        quantity INTEGER
    )
''')
creature_list = [['0 - ', ]]
cursor.execute('''
        INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability, quantity)
        VALUES (1, 3, 3, 3, 3, 1, 1)
    ''')
cursor.execute('''
        INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability, quantity)
        VALUES (3, 6, 3, 5, 3, 2, 1)
    ''')
cursor.execute('''
        INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability, quantity)
        VALUES (9, 12, 5, 7, 4, 3, 1)
    ''')
cursor.execute('''
        INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability, quantity)
        VALUES (12, 13, 6, 10, 7, 2, 1)
    ''')
cursor.execute('''
        INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability, quantity)
        VALUES (20, 30, 9, 14, 12, 1, 1)
    ''')
cursor.execute('''
        INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability, quantity)
        VALUES (1, 2, 3, 8, 0, 1, 1)
    ''')
cursor.execute('''
        INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability, quantity)
        VALUES (3, 5, 5, 2, 9, 3, 1)
    ''')
cursor.execute('''
        INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability, quantity)
        VALUES (7, 9, 8, 9, 7, 3, 1)
    ''')
cursor.execute('''
        INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability, quantity)
        VALUES (11, 15, 4, 14, 5, 2, 1)
    ''')
cursor.execute('''
        INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability, quantity)
        VALUES (15, 22, 9, 15, 9, 3, 1)
    ''')
conn.commit()
conn.close()

conn = sqlite3.connect('../DataBase/game.db')
cursor = conn.cursor()

# Выполняем SQL-запрос и получаем все строки таблицы, то-есть проверяем содержимое
cursor.execute('SELECT * FROM units')
rows = cursor.fetchall()

# Выводим содержимое таблицы
for row in rows:
    print(row)

# Закрываем соединение с базой данных
conn.close()
