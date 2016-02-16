import Tkinter
import ttk


class MyAccountFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        test = ttk.Label(self, text='My Account Frame')
        test.grid(row=0, column=0)
