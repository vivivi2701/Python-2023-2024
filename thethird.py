# coding=utf-8
import this  # the filosophy/zen of python

"""#Курс по программированию Тимофея Хирьянова (28 лекций)
import graphics as gr
window = gr.GraphWin('Russian game', 600, 600)
alpha = 0,2 #общепринятое значение alpha. 0.2 == 1/5
def fractal_rectangle(A, B, C, D, deep = 10):
    if deep < 1:
        return
    #Вместо:
    gr.Line(gr.Point(*A), gr.Point(*B).draw(window))
    gr.Line(gr.Point(*B), gr.Point(*C).draw(window))
    gr.Line(gr.Point(*C), gr.Point(*D).draw(window))
    gr.Line(gr.Point(*D), gr.Point(*A).draw(window))
    #Можно смело написать:
    for M, N in (A, B), (B, C), (C, D), (D, A):          #Можно в квадратные скобки оформить четыре пары скобок но необяз-но.
        gr.Line(gr.Point(*M), gr.Point(*N).draw(window)) #Можно двумя переменными пробежаться по кортежу.

    A1 = (A[0]*(1-aplha) + B[0]*alpha, A[1]*(1-aplha) + B[1]*alpha)
    B1 = (B[0]*(1-aplha) + C[0]*alpha, B[1]*(1-aplha) + C[1]*alpha)
    C1 = (C[0]*(1-aplha) + D[0]*alpha, C[1]*(1-aplha) + D[1]*alpha)
    D1 = (D[0]*(1-aplha) + A[0]*alpha, D[1]*(1-aplha) + A[1]*alpha)
"""
"""
# получение данных сайта:
import requests

p = requests.get("http://stepic.org")  # простой GET-запрос
print(p.text)  # вывод ответа от сервера


url = "http://example.com"
par = {"key1": "value1", "key2": "value2"}
r = requests.get(url, params=par)  # передача параметров в запрос
print(r.url)  # сформированный url-адрес с учетом параметров GET-запроса


url = "http://httpbin.org/cookies"
cookies = {"cookies_are": "working"}
r = requests.get(url, cookies=cookies)  # отправка сформированных cookies на сервер
print(r.text)


# print(r.cookies['example_cookie_name'])  #использование cookies, полученных от сервера


def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, d = 0, 0, 0
    for i in range(1, n * n + 1):
        matrix[x][y] = i
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0:
            x, y = nx, ny
        else:
            d = (d + 1) % 4
            x, y = x + dx[d], y + dy[d]
    return matrix


generate_spiral_matrix(9) """

##### НАЧАЛО КУРСА '"Поколение Python": курс для начинающих'; 20.12.2023 #####

# 2.1.Веб-приложения. С помощью дополнительных фреймворков на языке Python (Django, Flask, Pyramid) можно создавать полнофункциональные сайты;  --- позже выучить  данные фреймворки
# Приложения баз данных. В Python имеются интерфейсы доступа ко всем основным реляционным базам данных: Sybase, Oracle, Informix, ODBC, MySQL, PostgreSQL, SQLite и многим другим. С их помощью можно создавать приложения баз данных. --- выучить позже
"""Проекты, в которых используется Python
Компания Google использует Python в своей поисковой системе;

Компании Intel, Cisco, Hewlett-Packard, Seagate, Qualcomm и IBM, используют Python для тестирования аппаратного обеспечения;

Сервис YouTube в значительной степени реализован на Python;

Агентство национальной безопасности (NSA) использует Python для шифрования и анализа данных;

Компании JPMorgan Chase, UBS, Getco и Citadel применяют Python для прогнозирования финансового рынка;

Программа BitTorrent для обмена файлами в пиринговых сетях написана на языке Python;

NASA, Los Alamos, JPL и Fermilab используют Python для научных вычислений."""


###!!! ДЛЯ ТОГО, ЧТОБЫ КОРЯВЫЙ КОД ПРЕОБРАЗОВАТЬ В КРАСИВЫЙ В VS STUDIO - МОЖНО ВОСПОЛЬЗОВАТЬСЯ |command| + |s| НА КЛАВИАТУРЕ (mac OS). (Ctrl+s на windows)!!!###
# pip install matplotlib_venn
##import matplotlib.pyplot as plt
# from matplotlib_venn import venn3
# venn3(subsets=(9,4,2,6,3,1,3), set_labels=('math','physics','informatics'))
# plt.show()


"""
К сожалению, в этом уроке конкретно не говорилось про время и память всех трёх типов данных.

Я написал небольшой код, где они сравниваются. 
Вы также можете и скинуть свои выводы, изменив count и foriner. 
У меня достаточно слабый процессор и видеокарта. 
Причём код всего лишь перебирает значения из for ... in range(foriner) (комментарий от https://stepik.org/users/219854320/profile?auth=login Артур Давлетов)"""

"""Сравниваем множества, списки и кортежи"""
"""
from time import time
from sys import getsizeof

# Просьба не ставить большие числа. В count хранится правая граница range для объектов.
# В foriner – правая граница for ... in range

count = 10000000
foriner = count

print(
    "В этом алгоритме сравниваются множество, список и кортеж на скорость и время",
    end="\n\n",
)
print("Правая граница интервала —", count)
my_set = set(range(1, count + 1))
my_list = list(range(1, count + 1))
my_tuple = tuple(range(1, count + 1))

my_set_size = getsizeof(my_set)
my_list_size = getsizeof(my_list)
my_tuple_size = getsizeof(my_tuple)

print()
print(
    f"Память {{множес.}} = {my_set_size} байт = {round(my_set_size / 1024, 3)} Кб \
    = {round(my_set_size / 1024 / 1024, 3)} Мб"
)
print(
    f"Память [списка]  = {my_list_size} байт = {round(my_list_size / 1024, 3)} Кб \
    = {round(my_list_size / 1024 / 1024, 3)} Мб"
)
print(f"Память (кортежа) = {my_tuple_size} байт = {round(my_tuple_size / 1024, 3)} Кб \ = {round(my_tuple_size / 1024 / 1024, 3)} Мб")

print()

t = time()
for i in range(foriner):
    if i in my_set:
        pass
print(f"Время с множеством: {time() - t} секунд")
my_set.clear()

t = time()
for i in range(foriner):
    if i in my_list:
        pass
print(f"Время с списком:    {time() - t} секунд")
my_list.clear()

t = time()
for i in range(foriner):
    if i in my_tuple:
        pass
print(f"Время с кортежом:   {time() - t} секунд") """


"""Made with ❤️ in BEEGEEK
1. s = input(): эта строка запрашивает у пользователя ввод и сохраняет его в переменной s.
2. len(s) != len(set(s)): здесь мы сравниваем длину исходной строки s с длиной множества, созданного из этой строки. 
Множество set(s) содержит только уникальные символы из строки s. 
Если длины не совпадают, это означает, что в строке s есть повторяющиеся символы.
3. "YNEOS"[len(s) != len(set(s))::2]: 
это выражение использует результат сравнения длин (True или False) для выбора символов из строки "YNEOS". 
В Python True эквивалентен 1, а False эквивалентен 0. 
Таким образом, если в строке есть повторяющиеся символы, мы начинаем с 1-го символа ("N"), 
а если нет – с 0-го ("Y"). 
Шаг ::2 означает, что мы берем каждый второй символ, поэтому в результате получаем либо "YES", либо "NO".

Таким образом, этот код проверяет, есть ли во введенной пользователем строке повторяющиеся символы, 
и выводит "YES", если повторений нет, и "NO", если они есть.
Верное решение #1128312348
Python 3.10

s = input()
print("YNEOS"[len(s) != len(set(s))::2])

"""

# print('YNEOS'[len(i)!=len(set(i))::2])

# почему-то в курсе не упоминается функция dir(),
# в которую передавая в качестве аргумента любой тип данных,
# выведет доступные этому типу методы. Кроме того, через функцию help(),
# в которую можно передать любой тип данных и указав сам метод, мы можем получить описание самого метода.
# Оч полезно, и всегда под рукой
# url на картинку - https://ucarecdn.com/db15d574-45c0-481b-a00b-1f338fa82991/

# https://www.notion.so/Python-midle-notes-0a2f316d6f64438a82dcfbe9b82e4a01
"""
В прошлых уроках мы изучили пять типа коллекций в Python:

списки (list) – изменяемые коллекции элементов, индексируемые, не уникальные;
строки (string) – неизменяемые коллекции символов, индексируемые, не уникальные;
кортежи (tuple) – неизменяемые коллекции элементов, индексируемые, не уникальные;
множества (set) – изменяемые коллекции уникальных элементов, неиндексируемые, уникальные;
неизменяемые множества (frozenset) - неизменяемые коллекции уникальных элементов, неиндексируемые, уникальные."""

# dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information') - создает словарь с тремя элементами,
# где ключи — строки 'name', 'age', 'job',
# а соответствующие им значения: 'Missed information', 'Missed information', 'Missed information'.

# Создать словарь на основании двух списков (кортежей) можно с помощью встроенной функции-упаковщика zip().
"""
keys = ['name', 'age', 'job']
values = ['Timur', 28, 'Teacher']

info = dict(zip(keys, values))

print(info)
выводит (порядок элементов может отличаться):

{'name': 'Timur', 'age': 28, 'job': 'Teacher'}
В случае несовпадения длины списков функция самостоятельно отсечет лишние элементы.  """


import cmath

z = 2 + 3j
print(cmath.phase(z))  # полярный угол
print(cmath.polar(z))  # полярные координаты


# рисуем планеты
""" 
import turtle as t
import random as r
import math as m

def cosmos_bg(stars_count):
    t.bgcolor('black')
    width, height = t.window_width(), t.window_height()
    for _ in range(stars_count):
        t.up()
        t.goto(
            r.randrange(-width // 2, width // 2),
            r.randrange(-height // 2, height // 2)
        )
        t.down()
        t.color(
            r.randrange(150, 256),
            r.randrange(150, 256),
            r.randrange(150, 256)
        )
        t.begin_fill()
        t.circle(r.randrange(width // 2000, width // 500))
        t.end_fill()

def drawing_sun():
    sun_size = 2500
    t.up()
    t.setpos(-1600, 0)
    t.down()
    for i in range(0, 256, 5):
        t.color(i, i, i // 2)
        t.dot(sun_size)
        sun_size -= 5
    for i in range(0, 128, 10):
        t.color(255, 255, 127 + i)
        t.dot(sun_size)
        sun_size -= 2
    for i in range(0, 256, 5):
        t.color(255, 255, 255 - i)
        t.dot(sun_size)
        sun_size -= 5

# Позаимствовано отсюда: https://pythonturtle.academy/drawing-general-ellipse-with-python-turtle/
# (cx,cy): center of ellipse, a: wi0dth, b:height, angle: tilt
def ellipse(cx, cy, a, b, angle):
    # draw the first point with pen up
    t.up()
    turn = 0
    x = cx + a * m.cos(turn) * m.cos(m.radians(angle)) - b * m.sin(turn) * m.sin(m.radians(angle))
    y = cy + a * m.cos(turn) * m.sin(m.radians(angle)) + b * m.sin(turn) * m.cos(m.radians(angle))
    t.up()
    t.goto(x, y)
    t.down()
    n = 2000
    # draw the rest with pen down
    for i in range(n):
        x = cx + a * m.cos(turn) * m.cos(m.radians(angle)) - b * m.sin(turn) * m.sin(m.radians(angle))
        y = cy + a * m.cos(turn) * m.sin(m.radians(angle)) + b * m.sin(turn) * m.cos(m.radians(angle))
        if 0 <= i <= n // 7 or n - n // 7 <= i <= n:
            t.up()
        else:
            t.down()
        t.goto(x, y)
        turn += 2 * m.pi / n

def drawing_planets():
    t.up()
    t.setpos(-350, 0)
    t.right(90)
    # Расчет расстояния между планетками в зависимости от ширины окна
    free_space = t.window_width() / 2 + 350 - sum(planets.values()) / 490
    for name, size in planets.items():
        r, g, b = colours[name]
        for i in range(50):
            t.begin_fill()
            rad = size / 980
            t.color(
                r + i * (255 - r) // 100,
                g + i * (255 - g) // 100,
                b + i * (255 - b) // 100
            )
            t.circle(rad - i * rad / 100)
            t.end_fill()
        if name == 'Saturn':
            pos = t.xcor()
        t.setx(t.xcor() + size / 490 + free_space / 10)
    # рисуем кольца Сатурна
    t.color(colours['Sauturn rings'])
    for i in range(0, 150, 5):
        ellipse(pos + 123, 0, 30, 160 + i, 120)



# constants
planets = {
    'Mercury': 4900,
    'Venus': 12_000,
    'Earth': 12_750,
    'Mars': 6800,
    'Jupiter': 143_000,
    'Saturn': 120_550,
    'Uranus': 51_000,
    'Neptune': 49_500
}
colours = {
    'Mercury': (255, 69, 0),
    'Venus': (85, 107, 47),
    'Earth': (0, 139, 139),
    'Mars': (178, 34, 34),
    'Jupiter': (205, 133, 63),
    'Saturn': (218, 165, 32),
    'Sauturn rings': (255, 228, 181),
    'Uranus': (75, 0, 130),
    'Neptune': (70, 130, 180)
}

# setup
[t.setup(1200, 400), t.colormode(255), t.tracer(150)]


cosmos_bg(stars_count=300)
drawing_sun()
drawing_planets()
t.hideturtle()

t.update()
t.exitonclick()"""


"""
from heapq import heapify, heapreplace
from random import expovariate, gauss
from statistics import mean, quantiles

average_arrival_interval = 5.6
average_service_time = 15.0
stdev_service_time = 3.5
num_servers = 3

waits = []
arrival_time = 0.0
servers = [0.0] * num_servers  # time when each server becomes available
heapify(servers)
for i in range(1_000_000):
    arrival_time += expovariate(1.0 / average_arrival_interval)
    next_server_available = servers[0]
    wait = max(0.0, next_server_available - arrival_time)
    waits.append(wait)
    service_duration = max(0.0, gauss(average_service_time, stdev_service_time))
    service_completed = arrival_time + wait + service_duration
    heapreplace(servers, service_completed)

print(f'Mean wait: {mean(waits):.1f}   Max wait: {max(waits):.1f}')
print('Quartiles:', [round(q, 1) for q in quantiles(waits)])
"""


# язык Python за десять минут
"""
# ввод-вывод cтрок
first_word = input()
second_word = input()
spell = first_word + ' ' + second_word + '!'
print(spell)

# ввод-вывод чисел
first_number = int(input())
second_number = float(input())
print(first_number + second_number)

# смешанный вывод чисел и строк
platform = first_number + second_number
print('Платформа №' + str(platform))
print('Платформа №', platform, sep='')

# числа
radius = 5
pi = 3.14159
square = pi * radius ** 2

# строки
s = 'Tom Marvolo Riddle'
tokens = s.split()
first_name = tokens[0]
middle_name = tokens[1]
last_name = tokens[2]
s2 = first_name + ' ' + middle_name + ' ' + last_name

# конструкция 'if'. важно ставить отступы!
if (s == s2):
    print('две строки равны')
else:
    print('так не бывает')

# списки (изменяемые последовательности)
houses = ['Ravenclaw', 'Hufflepuff', 'Gryffindor']
houses.append('Slytherin')

# цикл 'for'. отступы вновь важны!
for house in houses:
    print('Ten points to', house, end='!\n')

# set (неупорядоченные коллекции)
birth_name = 'Tom Marvolo Riddle'
birth_name_letters = set(birth_name)
birth_name_lower_letters = set(birth_name.lower())
nickname_lower_letters = set('I am Lord Voldemort'.lower())
print(birth_name_lower_letters == nickname_lower_letters)

fib_numbers = set([1, 1, 2, 3, 5, 8, 13, 21])
prime_numbers = set([2, 3, 5, 7, 11, 13, 17, 19])
union = fib_numbers | prime_numbers
intersection = fib_numbers & prime_numbers
difference = fib_numbers - prime_numbers
symmetric_difference = fib_numbers ^ prime_numbers

# проверка принадлежности
print(3 in prime_numbers)
print(4 in prime_numbers)
print('ratio' in 'transfiguration')

# сортировка
houses.sort() # сортировка на месте
sorted_letters = sorted(houses[0]) # новый список

# словарь - соответствие из ключей в значения
# это как список, только индексы могут быть не только числами
dictionary = {}
dictionary['half-blood'] = 'полукровка'
dictionary['cauldron'] = 'котёл'
dictionary['potion'] = 'зелье'
print(dictionary['cauldron'])"""
