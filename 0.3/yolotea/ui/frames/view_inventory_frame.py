import Tkinter
import ttk


class ViewInventoryFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        test = ttk.Label(self, text='View Inventory Frame')
        test.grid(row=0, column=0)
