__author__ = 'Windows User'

import Tkinter as tk
from Tkinter import *
from ttk import *
import ttk

from orders import *


class Yolotea(ttk.Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.m_str = StringVar()
        self.f_str = StringVar()
        self.h_str = StringVar()

        self.__init_style__()
        self.__init_account_details_container__()
        self.__init_notebook_container__()
        self.__init_cart_container__()
        self.__init_milktea_frame__()
        self.__init_fruittea_frame__()
        self.__init_hottea_frame__()
        self.__init_snacks_frame__()
        self.__init_combo_frame__()
        self.__init_milktea_details()
        self.__init_fruittea_details()
        self.__init_hottea_details()
        self.__init_snack_details()
        self.__init_combo_details()

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
        self.order_label = ttk.Label(self.labelframe_orderDetails)
        self.order_label.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.total_label = ttk.Label(self.labelframe_orderDetails, text="Total Amount: P0.00")
        self.total_label.pack(side=TOP, fill=Y, pady=10)
        self.checkout_btn = ttk.Button(self.labelframe_orderDetails, text='Checkout Order', command=None)
        self.checkout_btn.pack(side=BOTTOM, fill=BOTH, expand=TRUE, padx=10, pady=10)

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

    def __init_milktea_details(self):
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
        radiobox_L = ttk.Radiobutton(labelframe_size, text="Large (L)", value="Large", command=None)
        radiobox_XL = ttk.Radiobutton(labelframe_size, text="Extra Large (XL)", value="Extra Large", command=None)
        radiobox_L.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_XL.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        radiobox_full = ttk.Radiobutton(labelframe_sugarlevel, text="Full (100%)", value="Full", command=None)
        radiobox_half = ttk.Radiobutton(labelframe_sugarlevel, text="Half (50%)", value="Half", command=None)
        radiobox_none = ttk.Radiobutton(labelframe_sugarlevel, text="None (0%)", value="None", command=None)
        radiobox_full.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_half.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_none.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        label_quantity = ttk.Label(labelframe_numdrink, text="Quantity", anchor=tk.E)
        entry_quantity = ttk.Entry(labelframe_numdrink)
        label_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        entry_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

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

    def __init_fruittea_details(self):
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
        btn_addtocart = ttk.Button(f2, text="Add Order to Cart", command=None)

        labelframe_chosenflavor.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_size.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_sugarlevel.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_numdrink.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_sinkers.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        btn_addtocart.pack(side=BOTTOM, fill=BOTH, expand=TRUE, padx=5, pady=5, ipady=20)

        label_chosenflavor = ttk.Label(labelframe_chosenflavor, textvariable=self.f_str)
        label_chosenflavor.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_L = ttk.Radiobutton(labelframe_size, text="Large (L)", value="Large", command=None)
        radiobox_XL = ttk.Radiobutton(labelframe_size, text="Extra Large (XL)", value="Extra Large", command=None)
        radiobox_L.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_XL.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        radiobox_full = ttk.Radiobutton(labelframe_sugarlevel, text="Full (100%)", value="Full", command=None)
        radiobox_half = ttk.Radiobutton(labelframe_sugarlevel, text="Half (50%)", value="Half", command=None)
        radiobox_none = ttk.Radiobutton(labelframe_sugarlevel, text="None (0%)", value="None", command=None)
        radiobox_full.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_half.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_none.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        label_quantity = ttk.Label(labelframe_numdrink, text="Quantity", anchor=tk.E)
        entry_quantity = ttk.Entry(labelframe_numdrink)
        label_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        entry_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

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

    def __init_hottea_details(self):
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
        btn_addtocart = ttk.Button(f2, text="Add Order to Cart", command=None)
        labelframe_chosenflavor.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_size.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        labelframe_numdrink.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        btn_addtocart.pack(side=TOP, fill=BOTH, expand=TRUE, padx=10, pady=10, ipady=20)

        label_chosenflavor = ttk.Label(labelframe_chosenflavor, textvariable=self.h_str)
        label_chosenflavor.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_L = ttk.Radiobutton(labelframe_size, text="Large (L)", value=0, command=None)
        radiobox_XL = ttk.Radiobutton(labelframe_size, text="Extra Large (XL)", value=1, command=None)
        radiobox_L.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_XL.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        label_quantity = ttk.Label(labelframe_numdrink, text="Quantity", anchor=tk.E)
        entry_quantity = ttk.Entry(labelframe_numdrink)
        label_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        entry_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

    def __init_snack_details(self):
        pass

    def __init_combo_details(self):
        pass

    def set_flavor(self, flavor, stringvar):
        stringvar.set(flavor)
        return True

    def add_to_cart(self, src):
        if src == 'm':
            flavor = 'TEST_FLAVOR'
            sugar = None
            size = None
            quantity = None
            sinkers = []

            order = MilkTea(flavor=flavor, sugar=sugar, size=size, quantity=quantity, sinkers=sinkers)
            self.order_label.configure(text=order.flavor)

        elif src == 'f':
            flavor = None
            sugar = None
            size = None
            quantity = None
            sinkers = []
            order = FruitTea(flavor=flavor, sugar=sugar, size=size, quantity=quantity, sinkers=sinkers)

        elif src == 'h':
            flavor = None
            size = None
            quantity = None
            order = HotTea(flavor=flavor, size=size, quantity=quantity)

        elif src == 's':
            order = YoloSnack()

        elif src == 'c':
            order = YoloCOmbo()

        return True


def main():

    root = tk.Tk()
    app = Yolotea(root)
    root.state('zoomed')
    root.mainloop()

if __name__ == '__main__':
    main()