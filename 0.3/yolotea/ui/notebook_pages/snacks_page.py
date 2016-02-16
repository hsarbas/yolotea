import Tkinter
import ttk


class SnacksPage(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        test = ttk.Label(self, text='Snacks Page')
        test.grid(row=0, column=0)
