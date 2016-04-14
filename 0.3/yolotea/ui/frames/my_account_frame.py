import Tkinter
import ttk


class MyAccountFrame(ttk.Frame):

    def __init__(self, parent, account_logged_in):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.account_logged_in = account_logged_in

        frame = ttk.Frame(self)
        frame.grid(row=0, column=0)

        account_id = ttk.Label(frame, text='ID: ' + account_logged_in['id'])
        account_id.grid(row=0, column=0)
        account_name = ttk.Label(frame, text='Name: ' + account_logged_in['name'])
        account_name.grid(row=1, column=0)
        account_type = ttk.Label(frame, text='Type: ' + account_logged_in['type'])
        account_type.grid(row=2, column=0)
