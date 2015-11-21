__author__ = 'Harvs'

import Tkinter as tk
from Tkinter import *
from ttk import *
import ttk
import tkMessageBox as tm


def popup_add_to_cart(parent):
    class Popup(object):

        def __init__(self):
            self.top = Toplevel(parent, takefocus=True)
            self.top.resizable(0, 0)
            self.top.title("Add To Cart")
            self.customer = None

            self.frame = ttk.Frame(self.top)
            self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.labelframe1 = ttk.LabelFrame(self.frame)
            self.labelframe1.pack(fill='both', expand='yes', padx=5, pady=5)
            self.customer_name_label = Label(self.labelframe1, text='Name of customer:')
            self.customer_name_label.grid(row=0, column=0, padx=5, pady=5)
            self.customer_name_field = Entry(self.labelframe1)
            self.customer_name_field.focus_set()
            self.customer_name_field.grid(row=0, column=1, padx=5, pady=5)

            self.labelframe2 = ttk. LabelFrame(self.frame)
            self.labelframe2.pack(fill='both', expand='yes', padx=5, pady=5)
            self.add_label = ttk.Label(self.labelframe2, text='Add order to cart?')
            self.add_label.pack(side=TOP, padx=5, pady=5)
            self.yes_btn = Button(self.labelframe2, text='Yes', command=self.do)
            self.no_btn = Button(self.labelframe2, text='No', command=self.no)
            self.yes_btn.pack(side=RIGHT, padx=5, pady=5)
            self.no_btn.pack(side=LEFT, padx=5, pady=5)
            self.yes_btn.focus_set()
            self.top.bind("<Return>", self.do)
            self.top.grab_set()

        def do(self):
            self.customer = self.customer_name_field.get()
            if len(self.customer) > 0:
                self.top.grab_release()
                self.top.destroy()
            else:
                tm.showerror("Add to cart error", "Invalid Customer Name", parent=self.top)

        def no(self):
            self.top.grab_release()
            self.top.destroy()

    pop = Popup()
    parent.wait_window(pop.top)

    customer = pop.customer
    del pop

    return customer


def popup_cancel_order(parent):
    class Popup(object):

        def __init__(self):
            self.top = Toplevel(parent, takefocus=True)
            self.top.resizable(0, 0)
            self.top.title("Cancel Order")
            self.value = None

            self.frame = ttk.Frame(self.top)
            self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.labelframe1 = ttk.LabelFrame(self.frame, text='Confirm Action')
            self.labelframe1.pack(fill="both", expand="yes", padx=5, pady=5)
            self.customer_name_label = Label(self.labelframe1, text="Cancel Order?")
            self.customer_name_label.grid(row=0, column=0, padx=3, pady=5)

            self.yes_btn = Button(self.frame, text='Yes', command=self.do)
            self.no_btn = Button(self.frame, text='No', command=self.no)
            self.yes_btn.pack(side=RIGHT, padx=5, pady=10)
            self.no_btn.pack(side=RIGHT, padx=5, pady=10)
            self.yes_btn.focus_set()
            self.top.bind("<Return>", self.do)
            self.top.grab_set()

        def do(self):
            self.value = 1
            self.top.grab_release()
            self.top.destroy()

        def no(self):
            self.value = 0
            self.top.grab_release()
            self.top.destroy()

    pop = Popup()
    parent.wait_window(pop.top)

    value = pop.value
    del pop

    return value


def popup_incomplete_details_error(parent):
    tm.showerror("Add to cart error", "Incomplete Order Details", parent=parent)
