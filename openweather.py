
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

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