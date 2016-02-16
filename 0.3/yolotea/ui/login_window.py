import Tkinter as tk
import ttk
import json


class LoginWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.account_logged_in = dict(id=None, password=None, name=None, type=None)
        frame = ttk.Frame(self.root)
        style = ttk.Style()
        style.theme_use('clam')
        frame.pack()
        self.root.title('Login')

        self.welcome = ttk.Label(frame, text='Welcome to Yolotea!')
        self.welcome.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        labelframe = ttk.LabelFrame(frame, text='Login Details')
        labelframe.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.user_label = ttk.Label(labelframe, text='Account ID:')
        self.user_label.grid(row=0, column=0, padx=10, pady=5)
        self.user_entry = ttk.Entry(labelframe)
        self.user_entry.grid(row=0, column=1, padx=10, pady=5)
        self.user_entry.focus_set()

        self.password_label = ttk.Label(labelframe, text='Password:')
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = ttk.Entry(labelframe)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.btn = ttk.Button(frame, text='Login', command=self.btn_command)
        self.btn.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.root.bind('<Return>', self.btn_command)

        self.root.mainloop()

    def btn_command(self, event=None):
        entered_user = self.user_entry.get()
        entered_pass = self.password_entry.get()
        success = 0

        with open('files/accounts.json') as f:
            accounts = json.load(f)
        f.close()

        for account in accounts:
            if success == 0:
                if account['id'] == entered_user:
                    if account['password'] == entered_pass:
                        print 'Login Success'
                        success = 1
                        self.root.destroy()
                        self.account_logged_in = account

        if success == 0:
            print 'Login Fail'
