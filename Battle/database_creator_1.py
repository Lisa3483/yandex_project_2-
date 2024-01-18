import sqlite3


class DataBasecreator:
    def __init__(self):
        pass

    def create(self):
        conn = sqlite3.connect('../DataBase/game.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS units_in_inventory (
                inventory_cell_id INTEGER PRIMARY KEY AUTOINCREMENT,
                unit_id INTEGER,
                quantity INTEGER
            )
        ''')
        cursor.execute('''
                INSERT INTO units_in_inventory (unit_id, quantity)
                VALUES (1, 100)
            ''')
        cursor.execute('''
                INSERT INTO units_in_inventory (unit_id, quantity)
                VALUES (2, 100)
            ''')
        cursor.execute('''
                INSERT INTO units_in_inventory (unit_id, quantity)
                VALUES (3, 100)
            ''')
        cursor.execute('''
                INSERT INTO units_in_inventory (unit_id, quantity)
                VALUES (4, 100)
            ''')
        cursor.execute('''
                INSERT INTO units_in_inventory (unit_id, quantity)
                VALUES (5, 100)
            ''')
        conn.commit()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS enemy_units_in_battle (
                number_of_battle INTEGER PRIMARY KEY AUTOINCREMENT,
                enemy_unit_id_1,
                enemy_unit_quantity_1,
                enemy_unit_id_2,
                enemy_unit_quantity_2,
                enemy_unit_id_3,
                enemy_unit_quantity_3,
                enemy_unit_id_4,
                enemy_unit_quantity_4,
                enemy_unit_id_5,
                enemy_unit_quantity_5
            )
        ''')
        cursor.execute('''
                INSERT INTO enemy_units_in_battle (enemy_unit_id_1,
                enemy_unit_quantity_1,
                enemy_unit_id_2,
                enemy_unit_quantity_2,
                enemy_unit_id_3,
                enemy_unit_quantity_3,
                enemy_unit_id_4,
                enemy_unit_quantity_4,
                enemy_unit_id_5,
                enemy_unit_quantity_5)
                VALUES (6, 100, 7, 20, 8, 8, 9, 7, 10, 44)
            ''')
        cursor.execute('''
                INSERT INTO enemy_units_in_battle (enemy_unit_id_1,
                enemy_unit_quantity_1,
                enemy_unit_id_2,
                enemy_unit_quantity_2,
                enemy_unit_id_3,
                enemy_unit_quantity_3,
                enemy_unit_id_4,
                enemy_unit_quantity_4,
                enemy_unit_id_5,
                enemy_unit_quantity_5)
                VALUES (6, 100, 7, 20, 8, 8, 9, 7, 10, 43)
            ''')
        conn.commit()
        conn.close()

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
                quantity INTEGER,
                unit_hp INTEGER
            )
        ''')
        creature_list = [['0 - ', ]]
        cursor.execute('''
                INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability,
                 quantity, unit_hp)
                VALUES (1, 3, 3, 3, 3, 1, 0, 4)
            ''')
        cursor.execute('''
                INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability,
                 quantity, unit_hp)
                VALUES (3, 6, 3, 5, 3, 2, 0, 7)
            ''')
        cursor.execute('''
                INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability,
                 quantity, unit_hp)
                VALUES (9, 12, 5, 7, 4, 3, 0, 12)
            ''')
        cursor.execute('''
                INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability,
                 quantity, unit_hp)
                VALUES (12, 13, 6, 10, 7, 2, 0, 30)
            ''')
        cursor.execute('''
                INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability,
                 quantity, unit_hp)
                VALUES (20, 30, 9, 14, 12, 1, 0, 120)
            ''')
        cursor.execute('''
                INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability,
                 quantity, unit_hp)
                VALUES (1, 2, 3, 8, 0, 1, 0, 4)
            ''')
        cursor.execute('''
                INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability,
                 quantity, unit_hp)
                VALUES (3, 5, 5, 2, 9, 3, 0, 8)
            ''')
        cursor.execute('''
                INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability,
                 quantity, unit_hp)
                VALUES (7, 9, 8, 9, 7, 3, 0, 9)
            ''')
        cursor.execute('''
                INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability,
                 quantity, unit_hp)
                VALUES (11, 15, 4, 14, 5, 2, 0, 33)
            ''')
        cursor.execute('''
                INSERT INTO units (unit_min_damage, unit_max_damage, unit_speed, unit_attack, unit_defence, the_ability,
                 quantity, unit_hp)
                VALUES (15, 22, 9, 15, 9, 3, 0, 100)
            ''')
        conn.commit()
        conn.close()
