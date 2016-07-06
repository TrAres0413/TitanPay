import tkinter
import tkinter.messagebox

'''from src.accounting.run_payroll import RunPayroll'''
from src.accounting.test_db import data_entry

class TitanGUI:
    def __init__(self):
        self.__first_window = tkinter.Tk()
        self.__button = tkinter.Button(self.__first_window, text='Process Payroll', fg="green", command=self.commit_payroll)
        self.__button.pack(side=tkinter.BOTTOM)
        self.__button = tkinter.Button(self.__first_window, text='Import Employees', fg="blue",
                                       command=self.import_employees)
        self.__button.pack(side=tkinter.TOP)
        tkinter.mainloop()

    def import_employees(self):
        data_entry()

    def commit_payroll(self):
        self.__second_window = tkinter.Tk()
        self.__button = tkinter.Button(self.__second_window, text='Commit Payroll', fg="red", command=self.finish_payroll)
        self.__button.pack()

    def finish_payroll(self):
        tkinter.messagebox.showinfo('Processing Payroll')
        RunPayroll()



titan_gui = TitanGUI()


