# this is my fourth filled with code python file
# в этом файле я пробовала писать приложение (сентябрь 2024)
import black

# blah blah
"""import tkinter as tk

def on_button_click():
    label.config(text="Привет, мир!")

root = tk.Tk()
root.title("Простое приложение")

label = tk.Label(root, text="Нажмите кнопку")
label.pack()

button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack()

root.mainloop()"""
"""
import tkinter as tk

def on_button_click():
    user_text = entry.get()
    check_state = "включен" if checkbox_var.get() else "выключен"
    label.config(text=f"Привет, {user_text}! Флажок {check_state}.")

root = tk.Tk()
root.title("Простое приложение")

label = tk.Label(root, text="Введите ваше имя и нажмите кнопку")
label.pack()

entry = tk.Entry(root)
entry.pack()

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Флажок", variable=checkbox_var)
checkbox.pack()

button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack()

root.mainloop()"""

"""import tkinter as tk

def on_key_press(event):
    label.config(text=f"Вы нажали клавишу: {event.char}")

root = tk.Tk()
root.title("Простое приложение")

label = tk.Label(root, text="Нажмите любую клавишу")
label.pack()

root.bind("<KeyPress>", on_key_press)

root.mainloop()"""
"""
import tkinter as tk
from tkinter import messagebox

# Функция для обработки кнопки
def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Информация", f"Привет, {user_input}!")
    else:
        messagebox.showwarning("Предупреждение", "Введите что-нибудь!")

# Создаем главное окно
root = tk.Tk()
root.title("Простое приложение")
root.geometry("300x200")  # Устанавливаем размер окна

# Добавляем метку (label)
label = tk.Label(root, text="Введите ваше имя:")
label.pack(pady=10)

# Добавляем поле для ввода (entry)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Добавляем кнопку (button)
button = tk.Button(root, text="Поприветствовать", command=on_button_click)
button.pack(pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()"""
"""
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Функция для обработки нажатий кнопок
def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Приветствие", f"Привет, {user_input}!")
    else:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите ваше имя!")

def clear_entry():
    entry.delete(0, tk.END)

# Создаем главное окно
root = tk.Tk()
root.title("Красивое приложение")
root.geometry("600x400")
root.resizable(False, False)

# Настраиваем стиль с помощью ttk
style = ttk.Style()
style.theme_use("clam")  # Выбор темы оформления

# Добавляем меню
menu = tk.Menu(root)
root.config(menu=menu)

# Добавляем пункт меню "Файл"
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Выход", command=root.quit)

# Добавляем пункт меню "О программе"
about_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="О программе", menu=about_menu)
about_menu.add_command(label="О приложении", command=lambda: messagebox.showinfo("О программе", "Это красивое приложение на Python!"))

# Создаем верхнюю рамку для ввода и кнопок
top_frame = ttk.Frame(root, padding=20)
top_frame.pack(fill=tk.X)

# Добавляем метку (label)
label = ttk.Label(top_frame, text="Введите ваше имя:", font=("Helvetica", 12))
label.pack(side=tk.LEFT, padx=(0, 10))

# Добавляем поле для ввода (entry)
entry = ttk.Entry(top_frame, width=30)
entry.pack(side=tk.LEFT)

# Добавляем кнопки
button_frame = ttk.Frame(top_frame)
button_frame.pack(side=tk.LEFT, padx=(20, 0))

greet_button = ttk.Button(button_frame, text="Приветствовать", command=on_button_click)
greet_button.pack(side=tk.LEFT, padx=(0, 10))

clear_button = ttk.Button(button_frame, text="Очистить", command=clear_entry)
clear_button.pack(side=tk.LEFT)

# Добавляем нижнюю рамку для изображения
bottom_frame = ttk.Frame(root, padding=20)
bottom_frame.pack(fill=tk.BOTH, expand=True)

# Загружаем изображение
image = Image.open("/Users/victoria/Documents/python/example_image.jpg")  # Замените на путь к вашему изображению
image = image.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Добавляем изображение в приложение
image_label = ttk.Label(bottom_frame, image=photo)
image_label.image = photo  # Сохраняем ссылку на изображение, чтобы его не уничтожил сборщик мусора
image_label.pack(pady=(20, 0))

# Запускаем главное окно
root.mainloop()"""

# уже более-менее (написано ChatGPT)
"""
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# Функция для создания базы данных и таблицы, если она не существует
def create_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS finance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            amount REAL,
            category TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Функция для добавления записи
def add_record():
    amount = entry_amount.get()
    category = entry_category.get()
    record_type = record_type_var.get()
    if not amount or not category:
        messagebox.showwarning("Ошибка", "Заполните все поля!")
        return
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Ошибка", "Введите корректную сумму!")
        return

    date = datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO finance (type, amount, category, date)
        VALUES (?, ?, ?, ?)
    ''', (record_type, amount, category, date))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Запись добавлена!")
    update_balance()
    clear_entries()

# Функция для очистки полей ввода
def clear_entries():
    entry_amount.delete(0, tk.END)
    entry_category.delete(0, tk.END)

# Функция для обновления баланса
def update_balance():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(amount) FROM finance WHERE type="Доход"')
    income = cursor.fetchone()[0]
    cursor.execute('SELECT SUM(amount) FROM finance WHERE type="Расход"')
    expense = cursor.fetchone()[0]
    conn.close()

    if income is None:
        income = 0
    if expense is None:
        expense = 0

    total_balance = income - expense
    label_balance.config(text=f"Баланс: {total_balance:.2f} руб.")
    label_income.config(text=f"Доход: {income:.2f} руб.")
    label_expense.config(text=f"Расход: {expense:.2f} руб.")

# Функция для отображения всех записей
def view_records():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM finance')
    records = cursor.fetchall()
    conn.close()

    for i in tree.get_children():
        tree.delete(i)

    for record in records:
        tree.insert('', tk.END, values=record)

# Создаем главное окно
root = tk.Tk()
root.title("Приложение для учета финансов")
root.geometry("600x400")
root.resizable(False, False)

# Создаем базу данных
create_db()

# Верхняя часть интерфейса для ввода данных
top_frame = ttk.Frame(root, padding=10)
top_frame.pack(fill=tk.X)

ttk.Label(top_frame, text="Сумма:").grid(row=0, column=0, padx=5, pady=5)
entry_amount = ttk.Entry(top_frame, width=20)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(top_frame, text="Категория:").grid(row=1, column=0, padx=5, pady=5)
entry_category = ttk.Entry(top_frame, width=20)
entry_category.grid(row=1, column=1, padx=5, pady=5)

record_type_var = tk.StringVar(value="Доход")
ttk.Radiobutton(top_frame, text="Доход", variable=record_type_var, value="Доход").grid(row=0, column=2, padx=5, pady=5)
ttk.Radiobutton(top_frame, text="Расход", variable=record_type_var, value="Расход").grid(row=1, column=2, padx=5, pady=5)

ttk.Button(top_frame, text="Добавить запись", command=add_record).grid(row=2, column=1, pady=10)

# Средняя часть интерфейса для отображения текущего баланса
middle_frame = ttk.Frame(root, padding=10)
middle_frame.pack(fill=tk.X)

label_balance = ttk.Label(middle_frame, text="Баланс: 0 руб.", font=("Helvetica", 14))
label_balance.pack(side=tk.LEFT)

label_income = ttk.Label(middle_frame, text="Доход: 0 руб.", font=("Helvetica", 10))
label_income.pack(side=tk.LEFT, padx=(20, 0))

label_expense = ttk.Label(middle_frame, text="Расход: 0 руб.", font=("Helvetica", 10))
label_expense.pack(side=tk.LEFT, padx=(20, 0))

# Нижняя часть интерфейса для отображения таблицы
bottom_frame = ttk.Frame(root, padding=10)
bottom_frame.pack(fill=tk.BOTH, expand=True)

columns = ('ID', 'Тип', 'Сумма', 'Категория', 'Дата')
tree = ttk.Treeview(bottom_frame, columns=columns, show='headings', height=10)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

scrollbar = ttk.Scrollbar(bottom_frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscroll=scrollbar.set)

ttk.Button(root, text="Показать записи", command=view_records).pack(pady=10)

# Инициализация и запуск приложения
update_balance()
root.mainloop()"""

"""main.ui.
Сконвертируйте .ui файл в Python код:
bash
Копировать код
pyuic5 main.ui -o ui_main.py"""
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QDate
from ui_main import Ui_MainWindow  # Импорт сгенерированного интерфейса
from database import Database
from models import Transaction
import pandas as pd
import matplotlib.pyplot as plt

# Класс основного окна приложения
class FinanceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Инициализация базы данных
        self.db = Database()

        # Связываем кнопки с действиями
        self.ui.btn_add.clicked.connect(self.add_transaction)
        self.ui.btn_export.clicked.connect(self.export_data)
        self.ui.btn_show_chart.clicked.connect(self.show_chart)

        # Загружаем транзакции в таблицу
        self.load_transactions()

    # Функция для добавления транзакции
    def add_transaction(self):
        amount = self.ui.amount_input.value()
        category = self.ui.category_input.text()
        trans_type = self.ui.type_combobox.currentText()
        date = self.ui.date_input.date().toString("yyyy-MM-dd")

        if not category:
            QMessageBox.warning(self, "Ошибка", "Введите категорию!")
            return

        new_transaction = Transaction(
            type=trans_type,
            amount=amount,
            category=category,
            date=date
        )
        self.db.add_transaction(new_transaction)
        self.load_transactions()

    # Функция для загрузки всех транзакций в таблицу
    def load_transactions(self):
        transactions = self.db.get_all_transactions()
        self.ui.table_transactions.setRowCount(len(transactions))

        for row, trans in enumerate(transactions):
            self.ui.table_transactions.setItem(row, 0, trans.date)
            self.ui.table_transactions.setItem(row, 1, trans.type)
            self.ui.table_transactions.setItem(row, 2, trans.category)
            self.ui.table_transactions.setItem(row, 3, str(trans.amount))

        # Обновляем баланс
        balance = self.db.get_balance()
        self.ui.label_balance.setText(f"Баланс: {balance:.2f} руб.")

    # Экспорт данных в CSV
    def export_data(self):
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить CSV", "", "CSV Files (*.csv)")
        if path:
            transactions = self.db.get_all_transactions_as_df()
            transactions.to_csv(path, index=False)
            QMessageBox.information(self, "Успех", "Данные успешно экспортированы!")

    # Отображение диаграммы расходов
    def show_chart(self):
        data = self.db.get_all_transactions_as_df()
        expenses = data[data['type'] == 'Расход']
        expenses_by_category = expenses.groupby('category')['amount'].sum()

        plt.figure(figsize=(6, 6))
        expenses_by_category.plot(kind='pie', autopct='%1.1f%%')
        plt.title("Расходы по категориям")
        plt.show()


# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinanceApp()
    window.show()
    sys.exit(app.exec_())

from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    amount = Column(Float)
    category = Column(String)
    date = Column(Date)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Transaction
import pandas as pd

class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///finance.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_transaction(self, transaction):
        session = self.Session()
        session.add(transaction)
        session.commit()
        session.close()

    def get_all_transactions(self):
        session = self.Session()
        transactions = session.query(Transaction).all()
        session.close()
        return transactions

    def get_balance(self):
        session = self.Session()
        income = session.query(Transaction).filter_by(type='Доход').all()
        expenses = session.query(Transaction).filter_by(type='Расход').all()
        balance = sum([i.amount for i in income]) - sum([e.amount for e in expenses])
        session.close()
        return balance

    def get_all_transactions_as_df(self):
        session = self.Session()
        transactions = session.query(Transaction).all()
        session.close()

        data = [{
            'type': t.type,
            'amount': t.amount,
            'category': t.category,
            'date': t.date
        } for t in transactions]

        return pd.DataFrame(data)"""


# Введение в ООП (egoroff_chanel)  9-10.10.2024
"""class Bank_Acc:
    
    def __init__(self, name='Bob', age=25, gender='male', balance=0, job='enterpreneur'):
        self.__name = name  # приватное значение
        self.age = age
        self.gender = gender
        self.__balance = balance
        self._job = job  # защищенное знач.
    
    
    def get_balance(self):  # геттер 
        print('Getting balance:', end='\t')
        print(self.__balance)
    
    def set_balance(self, value):  # сеттер
        print(f'Setting balance of value {self.__balance}')
        if isinstance(value, (int, float)):
            self.__balance = value
        else:
            raise ValueError('Пожалуйста, введите численное значение')
            #def set_balance(self, value)
    
    def delete_balance(self):  # делитер 
        print('Deleting balance')
        del self.__balance
    
    #balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
    balance = property()
    balance = balance.getter(get_balance)
    balance = balance.setter(set_balance)
    balance = balance.deleter(delete_balance)

acc1 = Bank_Acc()

for balance in range(799, 1100, 100):
    acc1.get_balance()
    acc1.set_balance(balance)
    print()
acc2 = Bank_Acc()
acc2.balance = 700
acc2.balance = 899
acc2.balance = 900
acc2.balance = 999
print(acc2.balance)



    # еще лучше:
class My_Bank_Acc:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('Getting balance')
        return self.__balance
    
    @my_balance.setter
    def my_balance(self,value):
        print('Setting balance')

        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом!')
        self.__balance = value

new_acc = My_Bank_Acc('Volkswagen', 782)
print(new_acc.my_balance)
new_acc = 445
print(new_acc)
new_acc = 337
print(new_acc)
new_acc = 683
print(new_acc)


class Square:  # Вычисляемые Property
    def __init__(self, side):
        self.__side = side
        self.__area = None
    
    @property  # Вычисляемые св-ва Property (calculated properties)
    def side(self):
        return self.__side
    
    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print('Calculating area is in process..')
            self.__area = self.side ** 2
        return self.__area
    
area1 = Square(7)
print(area1.area)
area1.side = 9
print(area1.area)
"""
"""

class Wallet:
    def __init__(self, name="Marusya", currency="USD", balance=0):
        self.name = name
        self.currency = currency
        self.balance = balance

    def show_balance(self):
        print(
            "Имя:", self.name, "\nНа Вашем балансе есть:", self.balance, self.currency
        )

    def top_up_balance(self, how_much):
        self.balance += how_much
        print("Успешно пополнено на:", how_much, self.currency)

    def top_down(self, howmuch):
        if self.balance - howmuch >= 0:
            self.balance -= howmuch
            print("Успешно снято:", howmuch, self.currency)
            print("Текущий баланс:", self.balance)

        else:
            print(
                "Пожалуйста, укажите сумму поменьше, т.к. на счету недостаточно средств!"
            )
            raise ValueError("Недостаточно средств!")"""

# def __del__(self):
#    print('Кошелек удален!')
#    print('Текущий баланс:', self.balance)


"""user1 = Wallet()
user1.show_balance()
user1.top_up_balance(900)
user1.top_down(788)
print(user1.name)
user1.name = 'Vikusik'
print('Имя владельца кошелька изменено на:', user1.name)"""

"""
#(class Verification):
class Verification:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError("Слабый пароль")

    def save(self):
        with open("Users.txt", "a", encoding="UTF-8") as curr_file:  #'w'
            curr_file.write(f"{self.login, self.password}", "\n")

from inheritable_class_Users import Verification

class Verification2(Verification):

    def __init__(self, login, password, age):
        Verification.__init__(self, login, password)  # super().__init__(login,password)
        self.__save()
        self.age = age
    
    def __save(self):
        with open("Users.txt", "a", encoding="UTF-8") as curr_file:
            for item in curr_file:
                if f'{self.login, self.password}' + '\n' == item:
                    raise ValueError('Такие логин и пароль уже существуют!')
        Verification.save(self)  # super().save() 
        print(self.__class__.__mro__)  # поиск в глубину

    def show(self):
        return self.login, self.password
    

User1 = Verification2('Samantha', 'InTheCity', 45)
print(Verification2.__mro__)  # gорядок поиска методов в классах родителей (поиск в глубину)"""

"""from tkinter import Tk, Button

class My_app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('200x200')
        self.setUI()

    def setUI(self):
        Button(self, text='Ok').pack()  # композиция
root = My_app()  # стандартное название - root
root.mainloop()
"""
"""
from datetime import datetime as dt

print(dt.now())


class Player:

    __LVL, __HEALTH = 1, 100
    __slots__ = ["__lvl", "__health", "__was_born"]

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__was_born = dt.now()

    @property  # декоратор, с ним- понятнее и лучше
    def lvl(self):
        print(self.__lvl), f"{dt.now() - self.__was_born}"

    @lvl.setter  # декоратор, с ним- понятнее и лучше
    def lvl(self, num):
        self.__lvl += Player.__typeTest(num)
        print(f"Текущий уровень был увеличен и составляет:{self.__lvl}")
        if self.__lvl >= 100:
            self.__lvl = 100

    @classmethod  # декоратор, с ним- понятнее и лучше
    def set_cls_field(
        cls, lvl=1, health=100
    ):  # cls- как и self- общепринятые(но cls определяет название исп-мого класса, а self- имя экземпляра)
        cls.__LVL = Player.__typeTest(lvl)
        cls.__HEALTH = Player.__typeTest(health)

    @staticmethod  # декоратор, с ним- понятнее и лучше  # статикметод проверяет, число ли значение
    def __typeTest(value):
        if isinstance(value, (int, float)):
            return value
        else:
            raise TypeError("Must be integer or float.")


x = Player()
x.lvl()
x.lvl = 5
x.lvl"""
