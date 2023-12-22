import sqlite3
number = 2
conn = sqlite3.connect('../DataBase/game.db')

cursor = conn.cursor()

cursor.execute(f"SELECT quantity, unit_min_damage, unit_max_damage, unit_attack FROM units WHERE id = '{number}'")
# Выполняем SQL-запрос и получаем количество атакующих юнитов
units_quantity = cursor.fetchall()
conn.close()
print(units_quantity)
