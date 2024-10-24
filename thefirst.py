#Викусики ...

milk = not True

cereals = True
eggs = False


if (milk and cereals) or eggs:
    if eggs:
        if milk:
            breakfast = "- омлет"
        else:
            breakfast = "- яичница"
    else:
        breakfast = "- хлопья с молоком"
else:
    if milk:
        breakfast = "- стакан молока"
    elif cereals:
        breakfast = "можно погрызть сухих хлопьев"
    else:
        breakfast = "ничего не будет: разгрузочный день"

print("Сегодня на завтрак", breakfast)


flat = [1.22, 4.56, 7.12, 1.22, 4.56, 4.56,7.12]
room_size = 1.22
count = 0

for room in flat:
    if room == room_size:
        count = count + 1
print('Комнат площадью', room_size, 'кв. метров:', count)

def rooms_equal(room_size, room_list):
    
# Перенесите следующий код в тело функции, которую вы объявили
    count = 0

    for room in room_list:
        if room == room_size:
            count = count + 1
    print('Комнат площадью', room_size, 'кв.м:', count)


# Следующий код не изменяйте и не переносите в тело функции
flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]

rooms_equal(5.55, flat)
# Добавьте ещё один вызов функции rooms_equal()
# Передайте в функцию искомую площадь - 9.2 кв.м и список hut
rooms_equal(9.2, hut)

# Функция для вычисления периметра куба.
def calc_cube_perimeter(side):
    return side * 12


# Функция для вычисления площади куба.
def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area

# Основная функция, которая принимает длину ребра куба
def calc_cube(side):
    # Вызываем функцию, рассчитывающую периметр
    # и передаём в неё размер куба
    one_cube_perimeter = calc_cube_perimeter(side)
    full_length = one_cube_perimeter * 8

    # Вызываем функцию, рассчитывающую площадь стекла
    # и передаём в неё размер куба
    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * 8

    print('Для 8 кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area, '.')

# В результате остался лишь один вызов "основной" функции,
# а она уже вызовет две вспомогательные
calc_cube(5)


def calc_cube_perimeter(side):
    return side * 12


def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area


def calc_cube(side, number):
    one_cube_perimeter = calc_cube_perimeter(side)
    full_length = one_cube_perimeter * number
    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * number
    print('Для', number, 'кубов понадобится палок (м):', (int(full_length)), 'и стекла (кв.м):', (int(full_area)))


# Ниже напишите три вызова функции calc_cube().
# Каждый вызов должен быть на отдельной строке.
calc_cube(2, 4)
calc_cube(0.5, 26)
calc_cube(0.61, 6)


def get_together_games(list1, list2):
    new_set1= set(list1)
    new_set2= set(list2)
    return new_set1.intersection(new_set2)
    # Напишите здесь код функции для поиска пересечений

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
together_games = get_together_games(anfisa_games, alisa_games)
# Напечатайте итоговый перечень игр в цикле
for game in together_games:
    print('👾', game)


friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

# Объявлен пустой словарь, его нужно будет наполнить элементами,
# каждый из которых составлен по схеме "имя: город"
friends = {}

# Допишите ваш код сюда
for i in range(0, len(friends_names)):
    friends[friends_names[i]] = friends_cities[i]
    
print('Лена живет в городе: ' + friends['Лена'])

for name, city in friends.items():
    print(name, 'живёт в городе', city)



favorite_songs = {
    'Серёга': ['Unforgiven', 'Holiday', 'Highway to hell'],
    'Соня': ['Shake it out', 'The Show Must Go On', 'Наше лето'],
    'Дима': ['Владимирский централ', 'Мурка', 'Третье сентября']
}
# Ниже напишите код, который напечатает на экран, сколько у Димы любимых песен
print(len(favorite_songs['Дима']))
# Ниже напишите код, который построчно напечатает
# все любимые песни Сони.
fav = favorite_songs['Соня']
for song in fav:
    print(song)



friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Хабаровск',
    'Егор': 'Пермь'
}

def is_anyone_in(collection, city):
    for friend in friends:
        if collection[friend] == city:
            print('В городе', collection[friend], 'живёт'+ ' ' + friend + '. Обязательно зайду в гости!')
        else:
            print('В городе', collection[friend], 'у меня есть друг, но мне туда не надо.')
    
is_anyone_in(friends, 'Хабаровск')





mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}
home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}
not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}

result_catalog = {}

# Допишите функцию выборки поддерживаемого девайса из словаря
def get_supported_catalog(dict_devices, device):
    supported_catalog = {}
    if device in dict_devices and device not in not_supported_devices:
        supported_catalog[device] = dict_devices[device]
    return supported_catalog

all_devices = set(mobile_devices).union(set(home_devices))
supported_devices= all_devices.difference(not_supported_devices)

for device in supported_devices:
    supported_mob_dev = get_supported_catalog(mobile_devices, device)
    # Добавьте значение в словарь result_catalog
    result_catalog.update(supported_mob_dev)
    supported_home_dev = get_supported_catalog(home_devices, device)
    # Добавьте значение в словарь result_catalog
    result_catalog.update(supported_home_dev)

print('Каталог поддерживаемых девайсов: ')
print(result_catalog)



DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        # Из словаря DATABASE создайте строку с помощью join();
        # имена друзей разделите запятой и пробелом.
        # Запишите эту строку в переменную friends_string (вместо пустых кавычек).
        friends_string = ', '.join(DATABASE)
        return 'Твои друзья: ' + friends_string
        

        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        # Из сета unique_cities создайте строку с помощью join();
        # названия городов разделите запятой и пробелом.
        # Запишите эту строку в переменную cities_string (вместо пустых кавычек).
        cities_string = ', '.join(unique_cities)

        

        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))

 
def check_query(query):
# Допишите код тела функции
    elements  = (query.split())
    if elements[0] == 'Анфиса,':
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'



# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

# Напечатаем результат.
# Переберём список вопросов в цикле
for q in queries:
    # Каждый из вопросов передадим аргументом
    # в функцию check_query()
    result = check_query(q)
    # И для каждого вызова напечатаем вопрос и, через дефис - вердикт программы
    print(q, '-', result)





def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    summ = 0
    for i in range(len(listened)):
        summ += (int(listened[i]))
    print(f'Вы прослушали {len(listened)} песен общей продолжительностью {summ//60} минут.')
    
calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198])






DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья"
# в зависимости от того, какое число передано в аргументе friends_count
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'
  
def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        # Вызовите функцию format_friends_count() и передайте в неё count.
        # Отредактируйте строку ниже: в ней должно использоваться выражение,
        # которое вернёт функция format_friends_count()
        function = format_friends_count(count)
        return f'У тебя {function}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'
    
def process_query(query):
    elements = query.split(', ')
    name = elements[0]
    if name == 'Анфиса':
        query = query.strip('Анфиса, ')
        return process_anfisa(elements[1])
    else:
        return process_friend(name, elements[1])
    
def process_friend(name, query):
    if name in DATABASE:
        if query == 'ты где?':
            city = DATABASE[name]
            return f'{name} в городе {city}'
        else: return '<неизвестный запрос>'
    else: return f'У тебя нет друга по имени {name}'
    
    
print('Привет, я Анфиса!')
print(process_anfisa('Анфиса, сколько у меня друзей?'))
print(process_anfisa('Анфиса, кто все мои друзья?'))
print(process_anfisa('Анфиса, где все мои друзья?'))
print(process_anfisa('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?'))




import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(city):
    time = dt.datetime.utcnow()
    time_2 = dt.timedelta(hours= UTC_OFFSET[city])
    time_3 = time+time_2
    return time_3
    # Напишите код тела функции;
    # она должна вернуть текущее время в городе city



#Полная Анфиса:
import datetime as dt

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'

def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_count_friends(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city in UTC_OFFSET: return f'Там сейчас {what_time(city)}'
            else:
                return f'<не могу определить время в городе {DATABASE [name]}>'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?'
    ]
    for query in queries:
        print(query, '-', process_query(query))

runner()





import urllib.parse

strings = [
    'Что такое backend',
    'Привет!',
    ' ',        # Просто пробел.
    'letiště',  # Аэропорт по-чешски.
    'München',  # Крупнейший город Баварии.
    'Champs-Élysées',  # Елисейские поля.
    '東京',     # А это Токио.
]

for s in strings:
    encoded = urllib.parse.quote(s)          # Зашифрованная строка.
    decoded = urllib.parse.unquote(encoded)  # Расшифрованная обратно строка.
    print(decoded, '-', encoded)



  
  
import requests
url = 'https://wttr.in/'
weather_parameters = {
    'u':'', #'0':'',
    'T':'',
    'M':'',
}
request_headers ={
    'Accept-Language': 'ru'
}

response = requests.get(url, params=weather_parameters, headers=request_headers)
print(response.text)

#         \    /              \   /
#          .--.            __ /"".-.
#      -- (    ) --           \_(   ).
#          `--'               /(___(__)
#         /    \
  
  
  
  
# вот функция, которая может выбросить исключение
def calc_share(apples, friends):
    # от строки откусываем число и приводим к типу int
    friends_number = int(friends.split()[0])
    return apples/friends_number

# есть 17 яблок
apples = 17

# будем считать, сколько достанется каждому другу
# вызовем функцию calc_share() для разных наших знакомых,
# с различным числом друзей
for friends in ['7 друзей', '2 друга', '0 друзей', 'один враг']:
        try:
                print('Каждому достанется по', calc_share(apples, friends), 'яблока')
        except ZeroDivisionError:
                print('На ноль делить нельзя.')
        except ValueError:
                print(f'Из строки "{friends}" не получилось достать число.')


#FINAL EXERCISE(of Yandex.Praktikum):
import datetime as dt
import requests
DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}
UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}

def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'

def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time

def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text
    else:
        return '<ошибка на сервере погоды>'

def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_count_friends(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'

def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city not in UTC_OFFSET:
                return f'<не могу определить время в городе {city}>'
            time = what_time(city)
            return f'Там сейчас {time}'
        elif query == 'как погода?':
            weather = what_weather(city)
            return weather
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'

def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])

def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?',
        'Коля, как погода?',
        'Соня, как погода?',
        'Антон, как погода?'
    ]
    for query in queries:
        print(query, '-', process_query(query))
runner()


#Не все добираются до последнего урока и видят это сообщение:
#Вы справились с финальным заданием и преодолели курс!
#Вы создали Анфису, и, благодаря вам, она зажила своей жизнью. Путь от "Hello, world" до работающей программы не был простым, но вы прошли его. Остаётся лишь узнать, что будет дальше, по окончании вводного курса.
#[Здесь салют, фанфары и килограмм мороженого]



#                                    --- Я.Практикум(бесплатная часть) - Всё! ---
#                                    потраченное время: 53 дня (28.07 - 18.09.2023)
                            



#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <unistd.h>
#             k;double sin()
#         ,cos();main(){float A=
#       0,B=0,i,j,z[1760];char b[
#     1760];printf("\x1b[2J");for(;;
#  ){memset(b,32,1760);memset(z,0,7040)
#  ;for(j=0;6.28>j;j+=0.07)for(i=0;6.28
# >i;i+=0.02){float c=sin(i),d=cos(j),e=
# sin(A),f=sin(j),g=cos(A),h=d+2,D=1/(c*
# h*e+f*g+5),l=cos      (i),m=cos(B),n=
#sin(B),t=c*h*g-f*        e;int x=40+30*D*
#3(l*h*m-t*n),y=            12+15*D*(l*h*n
#+t*m),o=x+80*y,          N=8*((f*e-c*d*g
# )*m-c*d*e-f*g-l        *d*n);if(22>y&&
# y>0&&x>0&&80>x&&D>z[o]){z[o]=D;;;b[o]=
# ".,-~:;=!*#$@"[N>0?N:0];}}/*#****!!-*/
#  printf("\x1b[H");for(k=0;1761>k;k++)
#   putchar(k%80?b[k]:10);A+=0.04;B+=
#     0.02;}}/*****####*******!!=;:~
#       ~::==!!!**********!!!==::-
#         .,~~;;;========;;;:~-.
#             ..,--------,*/
#
#открывать на сайте https://www.onlinegdb.com/online_c_compiler 
