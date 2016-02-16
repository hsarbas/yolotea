import Tkinter
import ttk


class ViewOrderFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        test = ttk.Label(self, text='View Order Frame')
        test.grid(row=0, column=0)
