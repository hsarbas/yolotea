__author__ = 'Harvs'

import Tkinter as tk
from Tkinter import *
from ttk import *
import ttk

from orders import *
import popups


class Yolotea(ttk.Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.m_str = StringVar()
        self.f_str = StringVar()
        self.h_str = StringVar()

        self.temp_flavor = None
        self.temp_size = None
        self.temp_sugar = None
        self.temp_quantity = None
        self.temp_sinkers = []

        self.customer = None
        self.orders = []

        self.__init_style__()
        self.__init_account_details_container__()
        self.__init_notebook_container__()
        self.__init_cart_container__()
        self.__init_milktea_frame__()
        self.__init_fruittea_frame__()
        self.__init_hottea_frame__()
        self.__init_snacks_frame__()
        self.__init_combo_frame__()
        self.__init_milktea_details__()
        self.__init_fruittea_details__()
        self.__init_hottea_details__()
        self.__init_snack_details__()
        self.__init_combo_details__()

    def __init_style__(self):
        self.parent.title("Yolotea Order Management System")
        style = Style()
        style.theme_use("clam")
        self.pack(fill=BOTH, expand=True)

    def __init_account_details_container__(self):
        self.labelframe_account = ttk.LabelFrame(self, text="Account Details")
        self.labelframe_account.pack(side=TOP, fill=X, padx=10, pady=10)
        self.logo = ttk.Label(self.labelframe_account, text="YOLOTEA LOGO", width=20)
        self.employee_name = ttk.Label(self.labelframe_account, text="Employee Name: EMPLOYEE NAME", width=100)
        self.employee_id = ttk.Label(self.labelframe_account, text="ID Number: ID NUMBER", width=100)
        self.logo.grid(row=0, column=0, columnspan=3, rowspan=3, padx=10, pady=10)
        self.employee_name.grid(row=0, column=4, padx=10, pady=5)
        self.employee_id.grid(row=1, column=4, padx=10, pady=5)

    def __init_notebook_container__(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

    def __init_cart_container__(self):
        self.labelframe_orderDetails = ttk.LabelFrame(self, text="Cart Details")
        self.labelframe_orderDetails.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)
        self.items = ttk.LabelFrame(self.labelframe_orderDetails, text="Items")
        self.items.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.order_listbox = Listbox(self.items)
        self.order_listbox.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.total_label = ttk.Label(self.labelframe_orderDetails, text="Total Amount: P0.00")
        self.total_label.pack(side=TOP, fill=Y, pady=10)
        self.delete_btn = ttk.Button(self.labelframe_orderDetails, text='Cancel Order', command=self.cancel_order)
        self.delete_btn.pack(side=TOP, fill=BOTH, expand=TRUE, padx=10, pady=10)
        self.checkout_btn = ttk.Button(self.labelframe_orderDetails, text='Checkout Order', command=self.checkout)
        self.checkout_btn.pack(side=TOP, fill=BOTH, expand=TRUE, padx=10, pady=10)

    def __init_milktea_frame__(self):
        self.mf = ttk.Frame(self.notebook)

        # milktea flavors
        labelframe = ttk.LabelFrame(self.mf, text="Flavors")
        labelframe.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        for x in range(0, 9):
            Grid.grid_columnconfigure(labelframe, x, weight=1)
            Grid.grid_rowconfigure(labelframe, x, weight=1)

        btn = ttk.Button(labelframe, text='Yolavit', command=lambda: self.set_flavor('Yolavit', self.m_str))
        btn2 = ttk.Button(labelframe, text='Yolowinter', command=lambda: self.set_flavor('Yolowinter', self.m_str))
        btn3 = ttk.Button(labelframe, text='YoloTaro', command=lambda: self.set_flavor('YoloTaro', self.m_str))
        btn4 = ttk.Button(labelframe, text='Yolaberry', command=lambda: self.set_flavor('Yolaberry', self.m_str))
        btn5 = ttk.Button(labelframe, text='Yolonilla', command=lambda: self.set_flavor('Yolonilla', self.m_str))
        btn6 = ttk.Button(labelframe, text='Yolomatcha', command=lambda: self.set_flavor('Yolomatcha', self.m_str))
        btn7 = ttk.Button(labelframe, text='Carpe Diem', command=lambda: self.set_flavor('Carpe Diem', self.m_str))
        btn8 = ttk.Button(labelframe, text='WYSIWYG', command=lambda: self.set_flavor('WYSIWYG', self.m_str))
        btn9 = ttk.Button(labelframe, text="C'est la vie", command=lambda: self.set_flavor("C'est la vie", self.m_str))
        btn10 = ttk.Button(labelframe, text='YoloChoco', command=lambda: self.set_flavor('YoloChoco', self.m_str))
        btn11 = ttk.Button(labelframe, text='Jasmint', command=lambda: self.set_flavor('Jasmint', self.m_str))
        btn12 = ttk.Button(labelframe, text='YoloMocha', command=lambda: self.set_flavor('YoloMocha', self.m_str))
        btn13 = ttk.Button(labelframe, text='YoloFoam', command=lambda: self.set_flavor('YoloFoam', self.m_str))
        btn14 = ttk.Button(labelframe, text='YoloCaramel', command=lambda: self.set_flavor('YoloCaramel', self.m_str))
        btn15 = ttk.Button(labelframe, text='La Dolce Vita', command=lambda: self.set_flavor('La Dolce Vita',
                                                                                             self.m_str))
        btn16 = ttk.Button(labelframe, text='YoloKkaido', command=lambda: self.set_flavor('YoloKkaido', self.m_str))
        btn17 = ttk.Button(labelframe, text='YoloChocoNana', command=lambda: self.set_flavor('YoloChocoNana',
                                                                                             self.m_str))

        btn.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn2.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn3.grid(row=2, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn4.grid(row=3, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn5.grid(row=4, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn6.grid(row=5, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn7.grid(row=6, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn8.grid(row=7, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn9.grid(row=8, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn10.grid(row=0, column=1, padx=5, pady=5, sticky=N+S+E+W)
        btn11.grid(row=1, column=1, padx=5, pady=5, sticky=N+S+E+W)
        btn12.grid(row=2, column=1, padx=5, pady=5, sticky=N+S+E+W)
        btn13.grid(row=3, column=1, padx=5, pady=5, sticky=N+S+E+W)
        btn14.grid(row=4, column=1, padx=5, pady=5, sticky=N+S+E+W)
        btn15.grid(row=5, column=1, padx=5, pady=5, sticky=N+S+E+W)
        btn16.grid(row=6, column=1, padx=5, pady=5, sticky=N+S+E+W)
        btn17.grid(row=7, column=1, padx=5, pady=5, sticky=N+S+E+W)

        self.notebook.add(self.mf, text='MilkTea')

    def __init_fruittea_frame__(self):
        self.ff = ttk.Frame(self.notebook)

        labelframe = ttk.LabelFrame(self.ff, text="Flavors")
        labelframe.pack(side=LEFT, fill=Y, padx=5, pady=5)
        for x in range(0, 5):
            Grid.grid_columnconfigure(labelframe, x, weight=1)
            Grid.grid_rowconfigure(labelframe, x, weight=1)

        btn = ttk.Button(labelframe, text='YoloBlue', command=lambda: self.set_flavor('YoloBlue', self.f_str))
        btn2 = ttk.Button(labelframe, text='YoloApple', command=lambda: self.set_flavor('YoloApple', self.f_str))
        btn3 = ttk.Button(labelframe, text='YoLychee', command=lambda: self.set_flavor('YoLychee', self.f_str))
        btn4 = ttk.Button(labelframe, text='Hakuna Matata', command=lambda: self.set_flavor('Hakuna Matata',
                                                                                            self.f_str))
        btn5 = ttk.Button(labelframe, text='Eurika', command=lambda: self.set_flavor('Eurika', self.f_str))

        btn.grid(row=0, column=0, padx=5, pady=5, ipadx=60, sticky=N+S+E+W)
        btn2.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn3.grid(row=2, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn4.grid(row=3, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn5.grid(row=4, column=0, padx=5, pady=5, sticky=N+S+E+W)

        self.notebook.add(self.ff, text='FruitTea')

    def __init_hottea_frame__(self):
        self.hf = ttk.Frame(self.notebook)

        labelframe = ttk.LabelFrame(self.hf, text="Flavors")
        labelframe.pack(side=LEFT, fill=Y, padx=5, pady=5)
        for x in range(0, 2):
            Grid.grid_columnconfigure(labelframe, x, weight=1)
            Grid.grid_rowconfigure(labelframe, x, weight=1)

        btn = ttk.Button(labelframe, text='Assam/Jasmine', command=lambda: self.set_flavor('Assam/Jasmine', self.h_str))
        btn2 = ttk.Button(labelframe, text='Stash Tea Bag', command=lambda: self.set_flavor('Stash Tea Bag',
                                                                                            self.h_str))

        btn.grid(row=0, column=0, padx=5, pady=5, ipadx=52, sticky=N+S+E+W)
        btn2.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)

        self.notebook.add(self.hf, text='HotTea')

    def __init_snacks_frame__(self):
        self.sf = ttk.Frame(self.notebook)

        # snacks
        labelframe = ttk.LabelFrame(self.sf, text="Flavors")
        labelframe.pack(side=LEFT, fill=Y, padx=5, pady=5)
        for x in range(0, 2):
            Grid.grid_columnconfigure(labelframe, x, weight=1)
            Grid.grid_rowconfigure(labelframe, x, weight=1)

        btn = ttk.Button(labelframe, text='Belgian Waffle', command=None)
        btn2 = ttk.Button(labelframe, text='Nachos', command=None)

        btn.grid(row=0, column=0, padx=5, pady=5, ipadx=55, sticky=N+S+E+W)
        btn2.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)

        self.notebook.add(self.sf, text='YoloSnacks')

    def __init_combo_frame__(self):
        self.cf = ttk.Frame(self.notebook)

        # combos
        labelframe = ttk.LabelFrame(self.cf, text="Flavors")
        labelframe.pack(side=LEFT, fill=Y, padx=5, pady=5)
        for x in range(0, 2):
            Grid.grid_columnconfigure(labelframe, x, weight=1)
            Grid.grid_rowconfigure(labelframe, x, weight=1)

        btn = ttk.Button(labelframe, text='XL + BW', command=None)
        btn2 = ttk.Button(labelframe, text=' XL + Nachos', command=None)

        btn.grid(row=0, column=0, padx=5, pady=5, ipadx=60, sticky=N+S+E+W)
        btn2.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)

        self.notebook.add(self.cf, text='YoloCombos')

    def __init_milktea_details__(self):
        labelframe = ttk.LabelFrame(self.mf, text="Order Details")
        labelframe.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=10, pady=10)

        f1 = ttk.Frame(labelframe)  # order details frame
        f2 = ttk.Frame(labelframe)  # add to cart button frame
        f3 = ttk.Frame(f1)  # left frame
        f4 = ttk.Frame(f1)  # right frame
        f5 = ttk.Frame(labelframe)  # chosen flavor frame
        f5.pack(side=TOP, fill=BOTH)
        f1.pack(side=TOP, fill=BOTH)
        f2.pack(side=TOP, fill=BOTH)
        f3.pack(side=LEFT, fill=BOTH, expand=TRUE)
        f4.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        labelframe_chosenflavor = ttk.LabelFrame(f5, text="Chosen Flavor")
        labelframe_size = ttk.LabelFrame(f3, text="Size")
        labelframe_sugarlevel = ttk.LabelFrame(f3, text="Sugar Level")
        labelframe_numdrink = ttk.LabelFrame(f3, text="Number of Drinks")
        labelframe_sinkers = ttk.LabelFrame(f4, text="Sinkers")
        btn_addtocart = ttk.Button(f2, text="Add Order to Cart", command=lambda: self.add_to_cart('m'))

        labelframe_chosenflavor.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_size.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_sugarlevel.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_numdrink.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_sinkers.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        btn_addtocart.pack(side=BOTTOM, fill=BOTH, expand=TRUE, padx=5, pady=5, ipady=20)

        label_chosenflavor = ttk.Label(labelframe_chosenflavor, textvariable=self.m_str)
        label_chosenflavor.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobutton_l = ttk.Radiobutton(labelframe_size, text="Large (L)", variable=self.temp_size, value=0,
                                        command=lambda: self.set_size('Large'))
        radiobutton_xl = ttk.Radiobutton(labelframe_size, text="Extra Large (XL)", variable=self.temp_size, value=1,
                                         command=lambda: self.set_size('Extra Large'))
        radiobutton_l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobutton_xl.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        radiobutton_full = ttk.Radiobutton(labelframe_sugarlevel, text="Full (100%)", variable=self.temp_sugar, value=2,
                                           command=lambda: self.set_sugar('Full'))
        radiobutton_half = ttk.Radiobutton(labelframe_sugarlevel, text="Half (50%)", variable=self.temp_sugar, value=3,
                                           command=lambda: self.set_sugar('Half'))
        radiobutton_none = ttk.Radiobutton(labelframe_sugarlevel, text="None (0%)", variable=self.temp_sugar, value=4,
                                           command=lambda: self.set_sugar('None'))
        radiobutton_full.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobutton_half.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobutton_none.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        label_quantity = ttk.Label(labelframe_numdrink, text="Quantity", anchor=tk.E)
        self.entry_quantity_m = ttk.Entry(labelframe_numdrink)
        label_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        self.entry_quantity_m.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        checkbutton_popping_bobba = ttk.Checkbutton(labelframe_sinkers, text="Popping Bobba")
        checkbutton_black_pearls = ttk.Checkbutton(labelframe_sinkers, text="Black Pearls")
        checkbutton_nata_crystals = ttk.Checkbutton(labelframe_sinkers, text="Nata Crystals")
        checkbutton_foam = ttk.Checkbutton(labelframe_sinkers, text="Foam")
        checkbutton_panacotta = ttk.Checkbutton(labelframe_sinkers, text="Panacotta")
        label_sinker_quantity_popping_bobba = ttk.Label(labelframe_sinkers, text="Quantity", anchor=tk.E)
        label_sinker_quantity_black_pearls = ttk.Label(labelframe_sinkers, text="Quantity", anchor=tk.E)
        label_sinker_quantity_nata_crystals = ttk.Label(labelframe_sinkers, text="Quantity", anchor=tk.E)
        label_sinker_quantity_foam = ttk.Label(labelframe_sinkers, text="Quantity", anchor=tk.E)
        label_sinker_quantity_panacotta = ttk.Label(labelframe_sinkers, text="Quantity", anchor=tk.E)

        checkbutton_popping_bobba.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+E+W)
        checkbutton_black_pearls.grid(row=1, column=0, padx=10, pady=10, sticky=N+S+E+W)
        checkbutton_nata_crystals.grid(row=2, column=0, padx=10, pady=10, sticky=N+S+E+W)
        checkbutton_foam.grid(row=3, column=0, padx=10, pady=10, sticky=N+S+E+W)
        checkbutton_panacotta.grid(row=4, column=0, padx=10, pady=10, sticky=N+S+E+W)
        label_sinker_quantity_popping_bobba.grid(row=0, column=1, padx=10, pady=10, sticky=N+S+E+W)
        label_sinker_quantity_black_pearls.grid(row=1, column=1, padx=10, pady=10, sticky=N+S+E+W)
        label_sinker_quantity_nata_crystals.grid(row=2, column=1, padx=10, pady=10, sticky=N+S+E+W)
        label_sinker_quantity_foam.grid(row=3, column=1, padx=10, pady=10, sticky=N+S+E+W)
        label_sinker_quantity_panacotta.grid(row=4, column=1, padx=10, pady=10, sticky=N+S+E+W)

        entry_popping_bobba = ttk.Entry(labelframe_sinkers)
        entry_black_pearls = ttk.Entry(labelframe_sinkers)
        entry_nata_crystals = ttk.Entry(labelframe_sinkers)
        entry_foam = ttk.Entry(labelframe_sinkers)
        entry_panacotta = ttk.Entry(labelframe_sinkers)
        entry_popping_bobba.grid(row=0, column=2, padx=10, pady=10, sticky=N+S+E+W)
        entry_black_pearls.grid(row=1, column=2, padx=10, pady=10, sticky=N+S+E+W)
        entry_nata_crystals.grid(row=2, column=2, padx=10, pady=10, sticky=N+S+E+W)
        entry_foam.grid(row=3, column=2, padx=10, pady=10, sticky=N+S+E+W)
        entry_panacotta.grid(row=4, column=2, padx=10, pady=10, sticky=N+S+E+W)

    def __init_fruittea_details__(self):
        labelframe = ttk.LabelFrame(self.ff, text="Order Details")
        labelframe.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=10, pady=10)

        f1 = ttk.Frame(labelframe)  # order details frame
        f2 = ttk.Frame(labelframe)  # add to cart button frame
        f3 = ttk.Frame(f1)  # left frame
        f4 = ttk.Frame(f1)  # right frame
        f5 = ttk.Frame(labelframe)  # chosen flavor frame
        f5.pack(side=TOP, fill=BOTH)
        f1.pack(side=TOP, fill=BOTH)
        f2.pack(side=TOP, fill=BOTH)
        f3.pack(side=LEFT, fill=BOTH, expand=TRUE)
        f4.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        labelframe_chosenflavor = ttk.LabelFrame(f5, text="Chosen Flavor")
        labelframe_size = ttk.LabelFrame(f3, text="Size")
        labelframe_sugarlevel = ttk.LabelFrame(f3, text="Sugar Level")
        labelframe_numdrink = ttk.LabelFrame(f3, text="Number of Drinks")
        labelframe_sinkers = ttk.LabelFrame(f4, text="Sinkers")
        btn_addtocart = ttk.Button(f2, text="Add Order to Cart", command=lambda: self.add_to_cart('f'))

        labelframe_chosenflavor.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_size.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_sugarlevel.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_numdrink.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_sinkers.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        btn_addtocart.pack(side=BOTTOM, fill=BOTH, expand=TRUE, padx=5, pady=5, ipady=20)

        label_chosen_flavor = ttk.Label(labelframe_chosenflavor, textvariable=self.f_str)
        label_chosen_flavor.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobutton_l = ttk.Radiobutton(labelframe_size, text="Large (L)", variable=self.temp_size,
                                        command=lambda: self.set_size('Large'))
        radiobutton_xl = ttk.Radiobutton(labelframe_size, text="Extra Large (XL)", variable=self.temp_size,
                                         command=lambda: self.set_size('Extra Large'))
        radiobutton_l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobutton_xl.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        radiobutton_full = ttk.Radiobutton(labelframe_sugarlevel, text="Full (100%)", variable=self.temp_sugar,
                                           command=lambda: self.set_sugar('Full'))
        radiobutton_half = ttk.Radiobutton(labelframe_sugarlevel, text="Half (50%)", variable=self.temp_sugar,
                                           command=lambda: self.set_sugar('Half'))
        radiobutton_none = ttk.Radiobutton(labelframe_sugarlevel, text="None (0%)", variable=self.temp_sugar,
                                           command=lambda: self.set_sugar('None'))
        radiobutton_full.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobutton_half.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobutton_none.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        label_quantity = ttk.Label(labelframe_numdrink, text="Quantity", anchor=tk.E)
        self.entry_quantity_f = ttk.Entry(labelframe_numdrink)
        label_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        self.entry_quantity_f.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        checkbutton_popping_bobba = ttk.Checkbutton(labelframe_sinkers, text="Popping Bobba")
        checkbutton_black_pearls = ttk.Checkbutton(labelframe_sinkers, text="Black Pearls")
        checkbutton_nata_crystals = ttk.Checkbutton(labelframe_sinkers, text="Nata Crystals")
        checkbutton_foam = ttk.Checkbutton(labelframe_sinkers, text="Foam")
        checkbutton_panacotta = ttk.Checkbutton(labelframe_sinkers, text="Panacotta")
        label_sinker_quantity_popping_bobba = ttk.Label(labelframe_sinkers, text="Quantity", anchor=tk.E)
        label_sinker_quantity_black_pearls = ttk.Label(labelframe_sinkers, text="Quantity", anchor=tk.E)
        label_sinker_quantity_nata_crystals = ttk.Label(labelframe_sinkers, text="Quantity", anchor=tk.E)
        label_sinker_quantity_foam = ttk.Label(labelframe_sinkers, text="Quantity", anchor=tk.E)
        label_sinker_quantity_panacotta = ttk.Label(labelframe_sinkers, text="Quantity", anchor=tk.E)

        checkbutton_popping_bobba.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+E+W)
        checkbutton_black_pearls.grid(row=1, column=0, padx=10, pady=10, sticky=N+S+E+W)
        checkbutton_nata_crystals.grid(row=2, column=0, padx=10, pady=10, sticky=N+S+E+W)
        checkbutton_foam.grid(row=3, column=0, padx=10, pady=10, sticky=N+S+E+W)
        checkbutton_panacotta.grid(row=4, column=0, padx=10, pady=10, sticky=N+S+E+W)
        label_sinker_quantity_popping_bobba.grid(row=0, column=1, padx=10, pady=10, sticky=N+S+E+W)
        label_sinker_quantity_black_pearls.grid(row=1, column=1, padx=10, pady=10, sticky=N+S+E+W)
        label_sinker_quantity_nata_crystals.grid(row=2, column=1, padx=10, pady=10, sticky=N+S+E+W)
        label_sinker_quantity_foam.grid(row=3, column=1, padx=10, pady=10, sticky=N+S+E+W)
        label_sinker_quantity_panacotta.grid(row=4, column=1, padx=10, pady=10, sticky=N+S+E+W)

        entry_popping_bobba = ttk.Entry(labelframe_sinkers)
        entry_black_pearls = ttk.Entry(labelframe_sinkers)
        entry_nata_crystals = ttk.Entry(labelframe_sinkers)
        entry_foam = ttk.Entry(labelframe_sinkers)
        entry_panacotta = ttk.Entry(labelframe_sinkers)
        entry_popping_bobba.grid(row=0, column=2, padx=10, pady=10, sticky=N+S+E+W)
        entry_black_pearls.grid(row=1, column=2, padx=10, pady=10, sticky=N+S+E+W)
        entry_nata_crystals.grid(row=2, column=2, padx=10, pady=10, sticky=N+S+E+W)
        entry_foam.grid(row=3, column=2, padx=10, pady=10, sticky=N+S+E+W)
        entry_panacotta.grid(row=4, column=2, padx=10, pady=10, sticky=N+S+E+W)

    def __init_hottea_details__(self):
        labelframe = ttk.LabelFrame(self.hf, text="Order Details")
        labelframe.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=10, pady=10)

        f1 = ttk.Frame(labelframe)  # order details frame
        f2 = ttk.Frame(labelframe)  # add to cart button frame
        f3 = ttk.Frame(f1)  # size frame
        f4 = ttk.Frame(f1)  # quantity frame
        f5 = ttk.Frame(f1)
        f5.pack(side=TOP, fill=BOTH)
        f1.pack(side=TOP, fill=BOTH)
        f2.pack(side=TOP, fill=BOTH)
        f3.pack(side=LEFT, fill=BOTH, expand=TRUE)
        f4.pack(side=LEFT, fill=BOTH, expand=TRUE)

        labelframe_chosenflavor = ttk.LabelFrame(f5, text="Chosen Flavor")
        labelframe_size = ttk.LabelFrame(f3, text="Size")
        labelframe_numdrink = ttk.LabelFrame(f4, text="Number of Drinks")
        btn_addtocart = ttk.Button(f2, text="Add Order to Cart", command=lambda: self.add_to_cart('h'))

        labelframe_chosenflavor.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_size.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        labelframe_numdrink.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        btn_addtocart.pack(side=TOP, fill=BOTH, expand=TRUE, padx=10, pady=10, ipady=20)

        label_chosenflavor = ttk.Label(labelframe_chosenflavor, textvariable=self.h_str)
        label_chosenflavor.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobutton_l = ttk.Radiobutton(labelframe_size, text="Large (L)", command=lambda: self.set_size('Large'))
        radiobutton_xl = ttk.Radiobutton(labelframe_size, text="Extra Large (XL)",
                                         command=lambda: self.set_size('Extra LArge'))
        radiobutton_l.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobutton_xl.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        label_quantity = ttk.Label(labelframe_numdrink, text="Quantity", anchor=tk.E)
        self.entry_quantity_h = ttk.Entry(labelframe_numdrink)
        label_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        self.entry_quantity_h.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

    def __init_snack_details__(self):
        pass

    def __init_combo_details__(self):
        pass

    def set_flavor(self, flavor, stringvar):
        stringvar.set(flavor)
        self.temp_flavor = flavor
        return True

    def set_size(self, size):
        self.temp_size = size
        return True

    def set_sugar(self, sugar):
        self.temp_sugar = sugar
        return True

    def set_quantity(self, quantity):
        self.temp_quantity = quantity
        return self.temp_quantity

    def set_sinkers(self, sinkers):
        self.temp_sinkers = sinkers

    def add_to_cart(self, src):

        if self.temp_flavor and self.temp_sugar and self.temp_size:
            customer = popups.popup_add_to_cart(self)

            if customer and src == 'm':
                flavor = self.temp_flavor
                sugar = self.temp_sugar
                size = self.temp_size
                quantity = self.set_quantity(self.entry_quantity_m.get())
                sinkers = []

                order = MilkTea(flavor=flavor, sugar=sugar, size=size, quantity=quantity, sinkers=sinkers,
                                customer=customer)
                self.orders.append(order)
                self.print_to_cart(order)

            elif customer and src == 'f':
                flavor = self.temp_flavor
                sugar = self.temp_sugar
                size = self.temp_size
                quantity = self.set_quantity(self.entry_quantity_f.get())
                sinkers = []
                order = FruitTea(flavor=flavor, sugar=sugar, size=size, quantity=quantity, sinkers=sinkers,
                                 customer=customer)
                self.orders.append(order)
                self.print_to_cart(order)

            elif customer and src == 'h':
                flavor = self.temp_flavor
                size = self.temp_size
                quantity = self.set_quantity(self.entry_quantity_h.get())
                order = HotTea(flavor=flavor, size=size, quantity=quantity, customer=customer)
                self.orders.append(order)
                self.print_to_cart(order)

            elif customer and src == 's':
                pass

            elif customer and src == 'c':
                pass

        else:
            popups.popup_incomplete_details_error(self)

        return True

    def print_to_cart(self, order):
        entry = order.flavor + ' - ' + order.customer
        self.order_listbox.insert(END, entry)

        return True

    def cancel_order(self):
        item = []
        value = popups.popup_cancel_order(self)
        if value == 1:
            item = map(int, self.order_listbox.curselection())
            self.order_listbox.delete(ANCHOR)
        self.orders.pop(item[0])

    def checkout(self):
        for order in self.orders:
            save = order.serialize()
            print save


def main():

    root = tk.Tk()
    Yolotea(root)
    root.state('zoomed')
    root.mainloop()

if __name__ == '__main__':
    main()
