import json

#считываем файл и сохраняем его
with open('files/SuperHero.json') as file:
    #file_data = file.read()
    file_data = json.load(file)

#Создаем двух новых героев
new_heroes = [{
      "name": "Han Tilk",
      "age": 120,
      "secretIdentity": "Jastin Bober",
      "powers": ["Radiation dance", "Hipnotic disco"]
    }, {
      "name": "Matilda Red",
      "age": 45,
      "secretIdentity": "Marta Jhons",
      "powers": ["Round-the-world trip", "brave speeches", "Radiation cookies"]
    }]

#Обновляем данные
file_data["members"] += new_heroes

#Записываем данные в новый файл
with open('files/SuoerHero_plus_2.json', 'w') as out_file:
    out_file.write(json.dumps(file_data, indent=4))


#Отсортируем героев по возрасту
#Кастомная сортировка
def key_sort(hero):
    return hero.get("age", 0)

#Применяем сотрировку
file_data["members"].sort(key=key_sort)

print("Sotred: ", file_data)

#Записываем отсортированные данные в файл
with open('files/superhero_plus_2_sorted.json', 'w') as out_file:
    out_file.write(json.dumps(file_data, indent=4))