import sqlite3
import csv


conn = sqlite3.connect('.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS hourly_employee(employee_id INT PRIMARY KEY, last TEXT NOT NULL, first TEXT NOT NULL,"
              " dues REAL, pay_method TEXT, hourly_rate REAL)")


def data_entry():
    with open('hourly_employees.csv', 'r') as hourly_file:
        hourly_emp = csv.reader(hourly_file, delimiter=',')
        next(hourly_emp)
        for row in hourly_emp:
            emp = row
            employee_id = emp[0]
            last = emp[1]
            first = emp[2]
            hourly_rate = emp[3]
            dues = emp[4]
            pay_method = emp[5]
            c.execute('INSERT INTO hourly_employee VALUES (?, ?, ?, ?, ?, ?)',
                    (employee_id, last, first, hourly_rate, dues, pay_method))

create_table()
data_entry()
conn.commit()
