import Tkinter as tk
from Tkinter import *
from ttk import *
import ttk
import tkMessageBox as tm


def popup_login(parent):
    class _popup(object):

        def __init__(self):
            self.top = Toplevel(parent, takefocus=True)
            self.top.resizable(0, 0)
            self.top.title("Login")
            self.value = None

            self.frame = ttk.Frame(self.top)
            self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.labelframe1 = ttk.LabelFrame(self.frame, text='Login form')
            self.labelframe1.pack(fill="both", expand="yes", padx=5, pady=5)
            self.username_label = Label(self.labelframe1, text="Username")
            self.username_label.grid(row=0, column=0, padx=3, pady=5)
            self.username_field = Entry(self.labelframe1)
            self.username_field.focus_set()
            self.username_field.grid(row=0, column=1, padx=3, pady=5)
            self.password_label = Label(self.labelframe1, text="Password")
            self.password_label.grid(row=1, column=0, padx=3, pady=5)
            self.password_field = Entry(self.labelframe1, show="*")
            self.password_field.grid(row=1, column=1, padx=3, pady=5)


            self.login_btn = Button(self.frame, text='Login', command=self.do)
            self.login_btn.pack(pady=10)
            self.top.bind("<Return>", self.do)
            self.top.grab_set()

        def do(self, event=None):
            #self.value = self.splits_field.get()

            username = self.username_field.get()
            password = self.password_field.get()

            if username == "harvs" and password == "123":
                tm.showinfo("Login success", "Welcome, " + username)
                self.top.grab_release()
                self.top.destroy()
            else:
                tm.showerror("Login error", "Incorrect username")

    pop = _popup()
    parent.wait_window(pop.top)

    value = pop.value
    del pop

    return value