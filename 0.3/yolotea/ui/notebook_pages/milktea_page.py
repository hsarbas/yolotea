import Tkinter as tk
import ttk
from yolotea.orders.concrete import *
from yolotea.ui.popups.customer_popup import customer_popup


class MilkTeaPage(ttk.Frame):

    def __init__(self, parent, listbox, order_manager):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.listbox = listbox
        self.order_manager = order_manager

        labelframe = ttk.LabelFrame(self, text='Order Details')
        labelframe.grid(row=0, column=0, padx=10, pady=20)

        flavor_label = ttk.Label(labelframe, text='Flavor:')
        flavor_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.flavor = ttk.Combobox(labelframe)
        self.flavor['values'] = ('Yolavit', 'YoloChoco', 'Yolowinter', 'Jasmint', 'YoloTaro', 'YoloMocha', 'Yolaberry',
                                 'YoloFoam', 'Yolonilla', 'YoloCaramel', 'Yolomatcha', 'La Dolce Vita', 'Carpe Diem',
                                 'YoloKkaido', 'WYSIWYG', 'YoloChocoNana', "C'est la vie")
        self.flavor.grid(row=0, column=1, padx=10, pady=5)

        size_label = ttk.Label(labelframe, text='Size:')
        size_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.size = ttk.Combobox(labelframe)
        self.size['values'] = ('Small', 'Medium', 'Large')
        self.size.grid(row=1, column=1, padx=10, pady=5)

        sugar_level_label = ttk.Label(labelframe, text='Sugar Level:')
        sugar_level_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.sugar_level = ttk.Combobox(labelframe)
        self.sugar_level['values'] = ('Full (100%)', 'Medium (50%)', 'None (0%)')
        self.sugar_level.grid(row=2, column=1, padx=10, pady=5)

        sinkers_labelframe = ttk.LabelFrame(labelframe, text='Sinkers')
        sinkers_labelframe.grid(row=0, rowspan=7, column=2, padx=10, pady=10, sticky=tk.W)

        popping_bobba_label = ttk.Label(sinkers_labelframe, text='Popping Bobba')
        popping_bobba_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.popping_bobba_entry = ttk.Entry(sinkers_labelframe)
        self.popping_bobba_entry.grid(row=0, column=1, padx=10, pady=5)

        black_pearls_label = ttk.Label(sinkers_labelframe, text='Black Pearls')
        black_pearls_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.black_pearls_entry = ttk.Entry(sinkers_labelframe)
        self.black_pearls_entry.grid(row=1, column=1, padx=10, pady=5)

        nata_crystals_label = ttk.Label(sinkers_labelframe, text='Nata Crystals')
        nata_crystals_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.nata_crystals_entry = ttk.Entry(sinkers_labelframe)
        self.nata_crystals_entry.grid(row=2, column=1, padx=10, pady=5)

        foam_label = ttk.Label(sinkers_labelframe, text='Foam')
        foam_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.foam_entry = ttk.Entry(sinkers_labelframe)
        self.foam_entry.grid(row=3, column=1, padx=10, pady=5)

        panacotta_label = ttk.Label(sinkers_labelframe, text='Panacotta')
        panacotta_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.panacotta_entry = ttk.Entry(sinkers_labelframe)
        self.panacotta_entry.grid(row=4, column=1, padx=10, pady=5)

        self.add_to_cart_btn = ttk.Button(self, text='Add Order To Cart', command=self.add_to_cart_command)
        self.add_to_cart_btn.grid(row=1, column=0, padx=10, pady=10)

    def add_to_cart_command(self):
        customer = customer_popup(self)

        if customer is not None:
            flavor = self.flavor.get()
            size = self.size.get()
            sugar_level = self.sugar_level.get()
            popping_bobba = self.popping_bobba_entry.get()
            black_pearls = self.black_pearls_entry.get()
            nata_crystals = self.nata_crystals_entry.get()
            foam = self.foam_entry.get()
            panacotta = self.panacotta_entry.get()
            sinkers = []

            if len(popping_bobba) > 0:
                sinkers.append(dict(name='popping_bobba', quantity=popping_bobba))
            if len(black_pearls) > 0:
                sinkers.append(dict(name='black_pearls', quantity=black_pearls))
            if len(nata_crystals) > 0:
                sinkers.append(dict(name='nata_crystals', quantity=nata_crystals))
            if len(foam) > 0:
                sinkers.append(dict(name='foam', quantity=foam))
            if len(panacotta) > 0:
                sinkers.append(dict(name='panacotta', quantity=panacotta))

            order = MilkTea(flavor, size, sugar_level, sinkers, customer)
            self.order_manager.add_order(order)
            self.listbox.insert(tk.END, order.flavor + ' - ' + order.customer)
            print 'order successfully placed'
        else:
            print 'order not placed'
