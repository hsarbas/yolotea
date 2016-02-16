import Tkinter
import ttk


class DocumentationFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        test = ttk.Label(self, text='Documentation Frame')
        test.grid(row=0, column=0)
