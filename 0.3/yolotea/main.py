import Tkinter
import ttk
from yolotea.ui.frames.take_order_frame import TakeOrderFrame
from yolotea.ui.login_window import LoginWindow
from yolotea.ui.menubar import Menubar


class YoloteaApp(object):

    def __init__(self):
        self.root = Tkinter.Tk()
        style = ttk.Style()
        style.theme_use("clam")
        self.frame = TakeOrderFrame(self.root)
        self.frame.pack()
        self.menubar = Menubar(self.root, self.frame)

        self.root.title('Yolotea Order Management App')
        self.root.mainloop()


def main():

    login_details = LoginWindow()
    # CreateAccountFrame()
    if login_details.account_logged_in['id'] is not None:
        print 'id:', login_details.account_logged_in['id']
        print 'password:', login_details.account_logged_in['password']
        print 'name:', login_details.account_logged_in['name']
        print 'type:', login_details.account_logged_in['type']

        YoloteaApp()


if __name__ == '__main__':
    main()
