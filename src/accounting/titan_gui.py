import tkinter
import tkinter.messagebox
from src.accounting.run_payroll import RunPayroll


class TitanGUI:
    def __init__(self):
        RunPayroll.prepare_tables()
        self.__main_window = tkinter.Tk()
        self.__frame = tkinter.Frame(self.__main_window)
        self.__label = tkinter.Label(self.__frame, text='Titan Pay')
        self.__create_emp_button = tkinter.Button(self.__frame, bg='green', text='New Hire')
        self.__import_emp = tkinter.Button(bg='green', text='Import Employees',
                                           command=RunPayroll.import_employees)
        self.__import_time = tkinter.Button(bg='green', text='Import Time Cards',
                                            command=RunPayroll.import_time)
        self.__import_receipts = tkinter.Button(bg='green', text='Import Receipts',
                                                command=RunPayroll.import_receipts)
        self.__process_payroll = tkinter.Button(bg='green', text='Process Payroll')

        self.__frame.pack()
        self.__label.pack()
        self.__create_emp_button.pack()
        self.__import_emp.pack()
        self.__import_receipts.pack()
        self.__import_time.pack()
        self.__process_payroll.pack()

        tkinter.mainloop()


titan_gui = TitanGUI()
