import Tkinter as tk
import ttk


def customer_popup(parent):
    class Popup(tk.Toplevel):
        def __init__(self):
            tk.Toplevel.__init__(self, parent)
            self.title('Customer')
            self.customer = None

            frame = ttk.Frame(self)
            frame.pack()

            customer_labelframe = ttk.LabelFrame(frame)
            customer_labelframe.grid(row=0, column=0, padx=10, pady=5)
            customer_label = ttk.Label(customer_labelframe, text='Customer Name: ')
            customer_label.grid(row=0, column=0, padx=5, pady=5)
            self.customer_entry = ttk.Entry(customer_labelframe)
            self.customer_entry.grid(row=0, column=1, padx=5, pady=5)
            self.customer_entry.focus_set()

            add_to_cart_labelframe = ttk.LabelFrame(frame)
            add_to_cart_labelframe.grid(row=1, column=0, padx=10, pady=10)
            add_to_cart_label = ttk.Label(add_to_cart_labelframe, text='Add Order To Cart?')
            add_to_cart_label.grid(row=0, column=0, padx=5, pady=10, columnspan=2)
            no_btn = ttk.Button(add_to_cart_labelframe, text='No', command=self.no_command)
            no_btn.grid(row=1, column=0, padx=10, pady=10)
            yes_btn = ttk.Button(add_to_cart_labelframe, text='Yes', command=self.yes_command)
            yes_btn.grid(row=1, column=1, padx=10, pady=10)

            self.grab_set()

        def yes_command(self):
            self.customer = self.customer_entry.get()
            self.grab_release()
            self.destroy()

        def no_command(self):
            self.customer = None
            self.grab_release()
            self.destroy()

    popup = Popup()
    parent.wait_window(popup)
    customer = popup.customer

    return customer
