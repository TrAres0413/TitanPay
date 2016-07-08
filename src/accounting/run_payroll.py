import sqlite3
import csv

conn = sqlite3.connect('titan_pay.db')
curs = conn.cursor()


class RunPayroll:
    def __init__(self):
        RunPayroll.prepare_tables()

    @staticmethod
    def prepare_tables():
        curs.execute('DROP TABLE IF EXISTS hourly_employee')
        curs.execute('DROP TABLE IF EXISTS time_cards')
        curs.execute('DROP TABLE IF EXISTS salary_employee')
        curs.execute('DROP TABLE IF EXISTS receipts')
        curs.execute('CREATE TABLE IF NOT EXISTS hourly_employee(employee_id INT PRIMARY KEY, last TEXT NOT NULL,'
                     ' first TEXT NOT NULL, hourly REAL, dues TEXT, pay_method REAL)')
        curs.execute('CREATE TABLE IF NOT EXISTS time_cards(employee_id INT, time_in REAL, time_out REAL, date TEXT)')
        curs.execute('CREATE TABLE IF NOT EXISTS salary_employee(employee_id INT PRIMARY KEY, last TEXT,'
                     ' first TEXT, salary INT, comm REAL, dues REAL, pay_method TEXT)')
        curs.execute('CREATE TABLE IF NOT EXISTS receipts(employee_id INT, last TEXT NOT NULL, item TEXT, units INT,'
                     ' unit_cost REAL, total REAL)')

    @staticmethod
    def import_employees():
        with open('hourly_employees.csv', 'r') as hourly_file:
            hourly_emp = csv.reader(hourly_file, delimiter=',')
            for row in hourly_emp:
                emp = row
                employee_id = emp[0]
                last = emp[1]
                first = emp[2]
                hourly_rate = emp[3]
                dues = emp[4]
                pay_method = emp[5]
                curs.execute('INSERT INTO hourly_employee VALUES (?, ?, ?, ?, ?, ?)', (employee_id, last, first,
                                                                                       hourly_rate, dues, pay_method))
                conn.commit()
        with open('salaried_employees.csv', 'r') as salary_file:
            salary_emp = csv.reader(salary_file, delimiter=',')
            for row in salary_emp:
                emp = row
                employee_id = emp[0]
                last = emp[1]
                first = emp[2]
                salary = emp[3]
                comm = emp[4]
                dues = emp[5]
                pay_method = emp[6]
                curs.execute('INSERT INTO salary_employee VALUES (?, ?, ?, ?, ?, ?, ?)',
                             (employee_id, last, first,salary, comm, dues, pay_method))
                conn.commit()

    @staticmethod
    def import_time():
        with open('timecards.csv', 'r') as time_file:
            time = csv.reader(time_file, delimiter=',')
            for row in time:
                time = row
                employee_id = time[0]
                time_in = time[1]
                time_out = time[2]
                date = time[3]
                curs.execute('INSERT INTO time_cards VALUES (?, ?, ?, ?)',
                             (employee_id, time_in, time_out, date))
                conn.commit()

    @staticmethod
    def import_receipts():
        with open('receipts.csv', 'r') as receipts:
            receipts = csv.reader(receipts, delimiter=',')
            for row in receipts:
                rec = row
                employee_id = rec[0]
                last = rec[1]
                item = rec[2]
                units = rec[3]
                unit_cost = rec[4]
                total = rec[5]
                curs.execute('INSERT INTO receipts VALUES (?, ?, ?, ?, ?, ?)',
                             (employee_id, last, item, units, unit_cost, total))
                conn.commit()




