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
            self.top.title("Yolotea Login")
            self.value = None

            self.frame = ttk.Frame(self.top)
            self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.labelframe1 = ttk.LabelFrame(self.frame, text='Login form')
            self.labelframe1.pack(fill="both", expand="yes", padx=10, pady=10)
            self.username_label = ttk.Label(self.labelframe1, text="Username")
            self.username_label.grid(row=0, column=0, padx=3, pady=5)
            self.username_field = ttk.Entry(self.labelframe1)
            self.username_field.focus_set()
            self.username_field.grid(row=0, column=1, padx=3, pady=5)
            self.password_label = ttk.Label(self.labelframe1, text="Password")
            self.password_label.grid(row=1, column=0, padx=3, pady=5)
            self.password_field = ttk.Entry(self.labelframe1, show="*")
            self.password_field.grid(row=1, column=1, padx=3, pady=5)

            self.login_btn = ttk.Button(self.frame, text='Login', command=self.do)
            self.login_btn.pack(fill=X, padx=10, pady=10)
            self.top.bind("<Return>", self.do)
            self.top.grab_set()

        def do(self, event=None):

            username = self.username_field.get()
            password = self.password_field.get()

            if username == "harvs" and password == "123":
                tm.showinfo("Login success", "Welcome, " + username)
                self.top.grab_release()
                self.top.destroy()
            else:
                tm.showerror("Login error", "Incorrect username/password", parent=self.top)

    pop = _popup()
    parent.wait_window(pop.top)

    value = pop.value
    del pop

    return value

def popup_checkout(parent):
    class _popup(object):

        def __init__(self):
            self.top = Toplevel(parent, takefocus=True)
            self.top.resizable(0, 0)
            self.top.title("Checkout Order")
            self.value = None

            self.frame = ttk.Frame(self.top)
            self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.labelframe1 = ttk.LabelFrame(self.frame, text='Checkout Order')
            self.labelframe1.pack(fill="both", expand="yes", padx=5, pady=5)
            self.customer_name_label = Label(self.labelframe1, text="Customer Name")
            self.customer_name_label.grid(row=0, column=0, padx=3, pady=5)
            self.customer_name_field = Entry(self.labelframe1)
            self.customer_name_field.focus_set()
            self.customer_name_field.grid(row=0, column=1, padx=3, pady=5)

            self.submit_btn = Button(self.frame, text='Submit', command=self.do)
            self.submit_btn.pack(pady=10)
            self.top.bind("<Return>", self.do)
            self.top.grab_set()

        def do(self, event=None):
            customer_name = self.customer_name_field.get()

            if len(customer_name) > 0:
                self.value = customer_name
                tm.showinfo("Checkout Success", "Order successfully placed")
                self.top.grab_release()
                self.top.destroy()
            else:
                tm.showerror("Checkout Error", "Enter Customer Name", parent=self.top)

    pop = _popup()
    parent.wait_window(pop.top)

    value = pop.value
    del pop

    return value

def popup_add_to_cart(parent):
    class _popup(object):

        def __init__(self):
            self.top = Toplevel(parent, takefocus=True)
            self.top.resizable(0, 0)
            self.top.title("Add To Cart")
            self.value = None

            self.frame = ttk.Frame(self.top)
            self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.labelframe1 = ttk.LabelFrame(self.frame, text='Confirm Action')
            self.labelframe1.pack(fill="both", expand="yes", padx=5, pady=5)
            self.customer_name_label = Label(self.labelframe1, text="Add Order to Cart?")
            self.customer_name_label.grid(row=0, column=0, padx=3, pady=5)

            self.yes_btn = Button(self.frame, text='Yes', command=self.do)
            self.no_btn = Button(self.frame, text='No', command=self.no)
            self.yes_btn.pack(side=LEFT, padx=5, pady=10)
            self.no_btn.pack(side=LEFT, padx=5, pady=10)
            self.yes_btn.focus_set()
            self.top.bind("<Return>", self.do)
            self.top.grab_set()

        def do(self, event=None):
            self.value = 1
            self.top.grab_release()
            self.top.destroy()

        def no(self, event=None):
            self.value = 0
            self.top.grab_release()
            self.top.destroy()

    pop = _popup()
    parent.wait_window(pop.top)

    value = pop.value
    del pop

    return value