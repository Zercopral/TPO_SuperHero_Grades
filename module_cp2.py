import csv

#Блок чтения данных
def get_data():
    with open('files/grades.csv') as file:
        data_file = list(csv.reader(file,  delimiter=","))
        data_file = [list(map(float, (map(str.strip, row[3:8])))) for row in data_file[1:]]
    return data_file


DATA = get_data()


#Функция расчета среднего значения
from numpy import average
def avg_val(row): return average(row[:3])

#Создание списка средних значений
def avg_val_list():
    return [avg_val(row) for row in DATA]

#Получаем итоговые оценки
def get_final_marks():
    outer_list = []
    for row in DATA:
        outer_list.append(row[4])
    
    return outer_list

#Попарно объединяем расчитанные средние значения и средние значения из файлов
def get_zip_rows(): return list(zip(avg_val_list(), get_final_marks()))


if __name__ == '__main__':    
    for row in DATA:
        print(row)
        print(avg_val(row))
    print()
    print(avg_val_list())
    print(get_final_marks())
    print()
    print(get_zip_rows())
