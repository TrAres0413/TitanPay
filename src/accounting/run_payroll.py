

from src.accounting.employee import Employee
from src.accounting.payment_method import PaymentMethod


class RunPayroll:
    employee_dict = {}
    with open('hourly_employees.csv', 'r') as hourly_file:
        for line in hourly_file:
            employee_id, last, first, rate, dues, pay_meth = line.split(',')

            emp = Employee(employee_id, last, first, rate, pay_meth)
            employee_dict.update(eval(hourly_file, emp))

    with open('salaried_employees.csv', 'r') as salary_file:
        for line in salary_file:
            employee_id, last, first, salary, commission, dues, pay_meth = line.split(',')

            emp = Employee(employee_id, last, first, salary, commission, dues, pay_meth)
            employee_dict.update(eval(salary_file, emp))

    with open('timecards.csv', 'r') as time_file:
        for line in time_file:
            if employee_id == employee_dict.employee_id:
                employee_dict.update(employee_id)

    with open('receipts.csv', 'r') as receipt_file:
        for line in receipt_file:
            if employee_dict.employee_id == employee_id:
                employee_dict.update(employee_id)

    for emp in employee_dict:
        PaymentMethod(emp)

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