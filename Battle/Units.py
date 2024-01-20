import random
import sqlite3


class Unit:
    def __init__(self):
        self.total_damage = 0
        self.damage = 0
        self.unit_min_damage = 0
        self.unit_max_damage = 0
        self.unit_speed = 0
        self.unit_attack = 0
        self.unit_defence = 0
        self.hero_level = 0
        self.hero_attack = 0
        self.hero_defence = 0
        self.unit_id = 0
        self.the_sequence_of_the_move_list = []
        self.the_ability = 0
        self.unit_quantity = 0

    def the_sequence_of_the_move(self):
        conn = sqlite3.connect('../DataBase/game.db')
        cursor = conn.cursor()

        # Выполняем SQL-запрос и получаем кортежи с id и unit_speed т.е получаем скорость каждого юнита

        cursor.execute('SELECT id, unit_speed FROM units')
        rows = cursor.fetchall()
        conn.close()
        rows_3 = sorted(rows, key=get_first_element)
        rows_3 = rows_3[:10]
        rows_2 = sorted(rows_3, key=get_second_element)

        # Выводим содержимое таблицы
        for row in rows_2:
            self.the_sequence_of_the_move_list.append(row)

        # Закрываем соединение с базой данных
        return sorted(self.the_sequence_of_the_move_list, key=get_second_element)
        # вернули список последовательностей ходов юнитов по их id

    def get_total_damage(self, unit_1_id, unit_2_id):
        number = int(unit_1_id)
        number_2 = int(unit_2_id)

        conn = sqlite3.connect('../DataBase/game.db')
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT unit_min_damage, unit_max_damage, unit_attack FROM units WHERE id = '{number}'")
        fetch = cursor.fetchall()
        self.unit_min_damage = fetch[0][0]
        self.unit_max_damage = fetch[0][1]
        self.unit_attack = fetch[0][2]
        conn.close()

        conn = sqlite3.connect('../DataBase/game.db')
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT unit_defence FROM units WHERE id = '{number_2}'")
        fetch = cursor.fetchall()
        self.unit_defence = fetch[0][0]
        conn.close()
        conn = sqlite3.connect('../DataBase/game.db')
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT quantity FROM units_in_inventory WHERE inventory_cell_id = '{number}'")
        fetch = cursor.fetchall()
        self.unit_quantity = fetch[0][0]
        for one_unit_damage in range(int(self.unit_quantity)):
            self.total_damage += random.randint(self.unit_min_damage, self.unit_max_damage)
        self.total_damage *= (1 + (self.unit_attack - self.unit_defence) * 0.05)
        return int(self.total_damage)


def get_second_element(tuplle):
    return tuplle[1]


def get_first_element(tuplle):
    return tuplle[0]
