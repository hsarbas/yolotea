import Tkinter
import ttk


class ViewAllAccountsFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        test = ttk.Label(self, text='View All Accounts Frame')
        test.grid(row=0, column=0)
