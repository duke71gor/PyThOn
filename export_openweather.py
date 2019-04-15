
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
from pprint import pprint
import requests
import html2text, html
import time
import sqlite3, re


#2 - Cтроки из файла city.list.json и работа с ю-зверем:
def readJson():
    with open('city.list.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        return data

print('''Правила ввода:
    Страна - двумя заглавными латинскими литерами, напр. RU - Россия.
    Город - латинскими литерами с первой заглавной буквы...''')

start_time = time.time()
while (time.time() - start_time) < 1:
    for x in readJson():
            print(x['country'])

answ = input('Введите код страны, чтобы посмотреть города \n:')
for x in readJson():
    if x['country'] == answ:
        print(x['name'])

answ = input('Введите город, чтобы посмотреть id \n:')
city_choice = []
for x in readJson():
    if x['name'] == answ:
        city_choice.append(x['id'])
        print(city_choice)
        print(type(city_choice))
print('Do you need weather for another city?')
while True:
    answ = input('Введите имя or press [q] to exit \n:')
    if answ == 'q':
        break
    else:
        for x in readJson():
            if x['name'] == answ:
                city_choice.append(x['id'])
                print(city_choice)
                print(type(city_choice))
city_choice = (','.join(map(str, city_choice)))


# достаем app.id = d7fde0b03882c910ea7b6e113faa2de0 from app.id file
#f = open('app.id', 'r', encoding='utf-8')
#id = f.read()
#print(id)
#f.close()
#или явно
id = 'd7fde0b03882c910ea7b6e113faa2de0'

S = requests.get(f'http://api.openweathermap.org/data/2.5/weather?id={city_choice}&units=metric&appid={id}')
print(S.text)
S = (S.text).split(',')
print('id_weather', S[2][-3:])
print('temperature', S[7][-5:-1])
print('date', S[18][-10:])
print('id_city', S[23][-6:])

name_city_str = ''.join(S[24])
result1 = re.findall(r'"name":"(\w+)"', name_city_str)
result1 = ''.join(result1)
print('name_city', result1)

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = sqlite3.connect('weather.db')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()
try:
    #Создаем новую таблицу WEATHER c 5тью колонками
    cursor.execute("""CREATE TABLE weather
    (id_city integer primary key, city varchar(255), date_column date, temperature integer, id_weather integer)  
                """)
except:
    #Работа с уже созданной таблицей - Вставляем данные в таблицу
    cursor.execute(f'''INSERT INTO weather
                      VALUES ('{S[23][-6:]}', '{result1}', '{S[18][-10:]}',
                      '{S[7][-5:-1]}', '{S[2][-3:]}')'''
                   )

    # Сохраняем изменения
    conn.commit()

# закрыть соединение с базой данных
conn.close()