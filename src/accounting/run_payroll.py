import sqlite3
import csv

conn = sqlite3.connect('titan.db')
curs = conn.cursor()


def create_table():
    curs.execute('CREATE TABLE IF NOT EXISTS hourly_employee(employee_id INT PRIMARY KEY, last TEXT NOT NULL, first TEXT NOT NULL, dues REAL, pay_method TEXT, hourly_rate REAL')
    curs.execute('CREATE TABLE IF NOT EXISTS time_cards(date TEXT PRIMARY KEY, time_in REAL, time_out REAL)')
    curs.execute('CREATE TABLE IF NOT EXISTS salary_employees(employee_id INT PRIMARY KEY, last TEXT NOT NULL,'
                 ' first TEXT NOT NULL, dues REAL, pay_method TEXT, salary INT, comm REAL)')
    curs.execute('CREATE TABLE IF NOT EXISTS receipts(date TEXT PRIMARY KEY, amt REAL)')


def data_entry():
    with open('hourly_employees.csv', 'r') as hourly_file:
        reader = csv.DictReader(hourly_file)
        for row in reader:
            if row != '':
                curs.execute('INSERT INTO hourly_employee() VALUES (?, ?, ?, ?, ?, ?)')
    with open('salaried_employees.csv', 'r') as salary_file:
        reader = csv.DictReader(salary_file)
        for row in reader:
            curs.execute('INSERT INTO salary_employee() VALUES (?, ?, ?, ?, ?, ?, ?)')
    with open('timecards.csv', 'r') as time_file:
        reader = csv.DictReader(time_file)
        for row in reader:
            curs.execute('INSERT INTO time_cards(date, time_in, time_out) VALUES (?, ?, ?)')
    with open('receipts.csv', 'r') as receipt_file:
        reader = csv.DictReader(receipt_file)
        for row in reader:
            curs.execute('INSERT INTO receipts(date, amt) VALUES (?, ?)')

"""
with open('hourly_employees.csv', 'r') as hourly_file:
    read_hourly = csv.reader(hourly_file, delimiter=",")


    employee_id = []
    last_name = []
    first_name = []
    hourly_rate = []
    dues = []
    payment_method = []

    for row in hourly_file:
       emp = Employee(employee_id, last_name, first_name, hourly_rate, dues, payment_method)

with open('salaried_employees.csv') as salary_file:
    read_salary = csv.reader(salary_file, delimiter=",")

    for row in salary_file:
        print(row)

with open('receipts.csv') as receipt_file:
    read_receipts = csv.reader(receipt_file, delimiter=",")

    for row in receipt_file:
        rec = Receipt(employee_id, last_name, item, unit_sold, unit_cost, commission)


with open('time_cards.csv') as time_file:
    read_time = csv.reader(time_file, delimiter=",")

    for row in time_file:
        print(row)

"""