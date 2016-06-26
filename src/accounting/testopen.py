import csv

from src.accounting.employee import Employee


class testOpen:
    employee = {}
    with open('hourly_employees.csv', 'r') as hourly_file:
        for line in hourly_file:
            while line != "":
                read_hourly = csv.reader(hourly_file, delimiter=",")
                employee_id, last, first, rate, dues, pay_meth = line.split(',')
                emp = Employee(employee_id, last, first, rate, pay_meth)
                employee.update(eval(hourly_file, emp))
        with open('salaried_employees.csv', 'r') as salary_file:
            for line in salary_file:
                while line != "":
                    read_salary = csv.reader(salary_file, delimiter=",")
                    employee_id, last, first, salary, commission, dues, pay_meth = line.split(',')
                    emp = Employee(employee_id, last, first, salary, commission, dues, pay_meth)
                    employee.update(eval(salary_file, emp))
                with open('timecards.csv', 'r') as time_file:
                    for line in time_file:
                        while line != "":
                            read_time_cards = csv.reader(time_file, delimiter=",")
                            employee_id, start, end, date = line.split(',')
                            emp = Employee(employee_id, start, end, date)
                            employee.update(eval(time_file, emp))
                        with open('receipts.csv', 'r') as receipt_file:
                            for line in receipt_file:
                                while line != "":
                                    read_receipts = csv.reader(receipt_file, delimiter=",")
                                    employee_id, last, item, units, cost, total = line.split(',')
                                    emp = Employee(employee_id, last, item, units, cost, total)
                                    employee.update(eval(receipt_file, emp))

def process_payroll(employee_id):




