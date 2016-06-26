import tkinter
import tkinter.messagebox

'''from src.accounting.run_payroll import RunPayroll'''


class TitanGUI:
    def __init__(self):
        self.__first_window = tkinter.Tk()
        self.__button = tkinter.Button(self.__first_window, text='Process Payroll', fg="green", command=self.commit_payroll)
        self.__button.pack(side=tkinter.BOTTOM)
        tkinter.mainloop()

    def commit_payroll(self):
        self.__second_window = tkinter.Tk()
        self.__button = tkinter.Button(self.__second_window, text='Commit Payroll', fg="red", command=self.finish_payroll)
        self.__button.pack()

    def finish_payroll(self):
        tkinter.messagebox.showinfo('Processing Payroll')
        '''run_payroll = RunPayroll()
        return run_payroll'''


titan_gui = TitanGUI()


