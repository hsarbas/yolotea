import Tkinter as tk
import ttk
from yolotea.ui.notebook_pages.milktea_page import MilkTeaPage
from yolotea.ui.notebook_pages.fruittea_page import FruitTeaPage
from yolotea.ui.notebook_pages.hottea_page import HotTeaPage
from yolotea.ui.notebook_pages.combo_page import ComboPage
from yolotea.ui.notebook_pages.snacks_page import SnacksPage
from yolotea.orders.order_manager import OrderManager


class TakeOrderFrame(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        self.order_manager = OrderManager()

        cart_labelframe = ttk.LabelFrame(self, text='Cart Details')
        cart_labelframe.grid(row=0, column=1, padx=20, pady=20, sticky=tk.N)

        self.order_listbox = tk.Listbox(cart_labelframe)
        self.order_listbox.config(width=30)
        self.order_listbox.grid(row=0, column=0, padx=10, pady=10)

        self.cancel_btn = ttk.Button(cart_labelframe, text='Cancel Order', command=self.cancel_order)
        self.cancel_btn.grid(row=1, column=0, padx=10, pady=10)

        self.checkout_btn = ttk.Button(cart_labelframe, text='Checkout Order', command=self.checkout)
        self.checkout_btn.grid(row=2, column=0, padx=10, pady=10)

        # Notebook

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, padx=20, pady=20, sticky=tk.N)

        self.milktea_page = MilkTeaPage(self.notebook, self.order_listbox, self.order_manager)
        self.notebook.add(self.milktea_page, text='MilkTea')

        self.fruittea_page = FruitTeaPage(self.notebook)
        self.notebook.add(self.fruittea_page, text='FruitTea')

        self.hottea_page = HotTeaPage(self.notebook)
        self.notebook.add(self.hottea_page, text='HotTea')

        self.combo_page = ComboPage(self.notebook)
        self.notebook.add(self.combo_page, text='Combos')

        self.snacks_page = SnacksPage(self.notebook)
        self.notebook.add(self.snacks_page, text='Snacks')

    def cancel_order(self):
        self.order_listbox.delete(self.order_listbox.curselection())

    def checkout(self):
        self.order_manager.create_file()
        del self.order_manager
