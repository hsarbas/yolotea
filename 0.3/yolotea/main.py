import Tkinter as tk
from Tkinter import *
from ttk import *
import ttk


class Yolotea(ttk.Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.style_init()

    def style_init(self):
        self.parent.title("Yolotea Order Management System")
        style = Style()
        style.theme_use("clam")
        self.pack(fill=BOTH, expand=True)

    def menubar_init(self):
        pass

    def account_details_init(self):
        pass

    def notebook_init(self):
        pass

    def cart_init(self):
        pass


def main():
    root = tk.Tk()
    Yolotea(root)
    root.state('zoomed')
    root.mainloop()

if __name__ == '__main__':
    main()
