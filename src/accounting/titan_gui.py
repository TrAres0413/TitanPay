import tkinter
import tkinter.messagebox


class TitanGUI:
    def __init__(self):
        self.__first_window = tkinter.Tk()
        self.__button = tkinter.Button(self.__first_window, text='Process Payroll', command=self.commit_payroll)
        self.__button.pack()
        tkinter.mainloop()

    def commit_payroll(self):
        self.__second_window = tkinter.Tk()
        self.__button = tkinter.Button(self.__second_window, text='Commit Payroll', command=self.finish_payroll)
        self.__button.pack()
        tkinter.mainloop()

    def finish_payroll(self):
        tkinter.messagebox.showinfo('Processing Payroll')


titan_gui = TitanGUI()


