import Tkinter
import ttk
from yolotea.ui.frames.take_order_frame import TakeOrderFrame
from yolotea.ui.popups.login_form import login_form
from yolotea.ui.menubar import Menubar


class YoloteaApp(object):

    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.withdraw()
        style = ttk.Style()
        style.theme_use("clam")

        frame = TakeOrderFrame(self.root)
        frame.pack()
        account_logged_in = login_form(self.root)
        self.menubar = Menubar(self.root, frame, account_logged_in)

        self.root.title('Yolotea Order Management App')
        self.root.deiconify()
        self.root.mainloop()


def main():
    YoloteaApp()

if __name__ == '__main__':
    main()
