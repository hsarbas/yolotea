import Tkinter
import ttk


class ViewAllOrdersFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        test = ttk.Label(self, text='View All Orders Frame')
        test.grid(row=0, column=0)
