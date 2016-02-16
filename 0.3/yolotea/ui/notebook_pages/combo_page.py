import Tkinter
import ttk


class ComboPage(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        test = ttk.Label(self, text='Combo Page')
        test.grid(row=0, column=0)
