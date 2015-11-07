import Tkinter as tk
from Tkinter import *
from ttk import *
import ttk
import popups


class Yolotea(ttk.Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.order_num = 0
        self.order = dict()

        """
        self.flavor = None
        self.size = None
        self.sugar_level = None
        self.quantity = None
        self.sinkers = None
        """

        self.chosen_flavor = None
        self.chosen_size = StringVar()
        self.chosen_sugar = StringVar()
        self.chosen_num = None

        self.parent = parent
        self.init_menubar()
        self.pack(fill=BOTH)
        self.initUI()
        self.start_login()
        self.init_paned_window()
        
    def initUI(self):
      
        self.parent.title("Yolotea Order Management System")
        self.style = Style()
        self.style.theme_use("clam")
        self.pack(fill=BOTH, expand=1)

    def start_login(self):
        value = popups.popup_login(self)

    def init_menubar(self):
        self.menubar = tk.Menu(self.parent)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.sim_menu = tk.Menu(self.menubar, tearoff=0)

        self.filemenu.add_command(label='New Map', command=None)
        self.filemenu.add_command(label='Save Map...', command=None)
        self.filemenu.add_command(label='Load Map...', command=None)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Load ADN...', command=None)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Import OSM...', command=None)
        self.filemenu.add_command(label='Remove OSM', command=None)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit')

        self.sim_menu.add_command(label='Run simulator...', command=None)
        self.sim_menu.add_separator()
        self.sim_menu.add_command(label='Play', command=None)
        self.sim_menu.add_command(label='Pause', command=None)
        self.sim_menu.add_command(label='Stop', command=None)

        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.menubar.add_cascade(label='Simulation', menu=self.sim_menu)

        self.parent.config(menu=self.menubar)

    def init_paned_window(self):
        # account labelframe
        self.labelframe_account = ttk.LabelFrame(self, text="Account Details")
        self.labelframe_account.pack(side=TOP, fill=X, padx=10, pady=10)
        self.logo = ttk.Label(self.labelframe_account, text="YOLOTEA LOGO", width=20)
        self.employee_name = ttk.Label(self.labelframe_account, text="Employee Name: EMPLOYEE NAME", width=100)
        self.employee_id = ttk.Label(self.labelframe_account, text = "ID Number: ID NUMBER", width=100)
        self.logo.grid(row=0, column=0, columnspan=3, rowspan=3, padx=10, pady=10)
        self.employee_name.grid(row=0, column=4, padx=10, pady=5)
        self.employee_id.grid(row=1, column=4, padx=10, pady=5)

        # main notebook
        self.notebook = ttk.Notebook(self)
        self.frame_milktea()
        self.frame_fruittea()
        self.frame_hottea()
        self.frame_snacks()
        self.frame_combos()

        self.notebook.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        # cart details labelframe
        self.labelframe_orderDetails = ttk.LabelFrame(self, text="Cart Details")
        self.labelframe_orderDetails.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)
        # self.order_listbox = tk.Label(self.labelframe_orderDetails, height=28, width=60, bg="white")
        # self.order_listbox.pack(side=TOP, padx=5, pady=5)
        self.order_label = ttk.Label(self.labelframe_orderDetails)
        self.order_label.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.total_label = ttk.Label(self.labelframe_orderDetails, text="Total Amount: P0.00")
        self.total_label.pack(side=TOP, fill=Y, pady=10)
        self.checkout_btn = ttk.Button(self.labelframe_orderDetails, text='Checkout Order', command=self.checkout)
        self.checkout_btn.pack(side=BOTTOM, fill=BOTH, expand=TRUE, padx=10, pady=10)

    def checkout(self):
        value = popups.popup_checkout(self)
        self.order['customer'] = value
        print self.order['customer']
        self.create_file()

    def create_file(self):
        f = open("orders/"+str(self.order_num)+".txt", "w")

        f.write("Flavor: " + self.order['flavor'] + "\n")
        f.write("Size: " + self.order['size'] + "\n")
        f.write("Sugar Level: " + self.order['sugar_level'] + "\n")
        f.write("Customer: " + self.order['customer'])

        f.close()
        self.order_num = self.order_num + 1

    def set_flavor(self, flavor, val):
        # self.flavor = flavor
        self.order['flavor'] = flavor
        val.configure(text=flavor)

    def set_size(self):
        # self.size = self.chosen_size.get()
        self.order['size'] = self.chosen_size.get()
        print self.order['size']

    def set_sugar(self):
        # self.sugar_level = self.chosen_sugar.get()
        self.order['sugar_level'] = self.chosen_sugar.get()
        print self.order['sugar_level']

    def add_to_cart(self):
        value = popups.popup_add_to_cart(self)
        if value == 1:
            self.order_label.configure(text="Flavor: " + self.order['flavor'] + "\n" +
                                            "Size: " + self.order['size'] + "\n" +
                                            "Sugar Level: " + self.order['sugar_level'] + "\n" +
                                            "Quantity: " + self.order['quantity'] + "\n" +
                                            "Sinkers: " + self.order['sinkers'])
            # self.order_label.configure(text=self.order)

    # order details labelframe for milktea and fruit tea
    def labelframe_order_details_milktea_fruittea(self, f):

        labelframe = ttk.LabelFrame(f, text="Order Details")
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
        btn_addtocart = ttk.Button(f2, text="Add Order to Cart", command=self.add_to_cart)

        labelframe_chosenflavor.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_size.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_sugarlevel.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_numdrink.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        labelframe_sinkers.pack(side=TOP, fill=BOTH, expand=TRUE, padx=5, pady=5)
        btn_addtocart.pack(side=BOTTOM, fill=BOTH, expand=TRUE, padx=5, pady=5, ipady=20)

        label_chosenflavor = ttk.Label(labelframe_chosenflavor)
        label_chosenflavor.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_L = ttk.Radiobutton(labelframe_size, text="Large (L)", value="Large", variable=self.chosen_size, command=self.set_size)
        radiobox_XL = ttk.Radiobutton(labelframe_size, text="Extra Large (XL)", value="Extra Large", variable=self.chosen_size, command=self.set_size)
        radiobox_L.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_XL.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        radiobox_full = ttk.Radiobutton(labelframe_sugarlevel, text="Full (100%)", value="Full", variable=self.chosen_sugar, command=self.set_sugar)
        radiobox_half = ttk.Radiobutton(labelframe_sugarlevel, text="Half (50%)", value="Half", variable=self.chosen_sugar, command=self.set_sugar)
        radiobox_none = ttk.Radiobutton(labelframe_sugarlevel, text="None (0%)", value="None", variable=self.chosen_sugar, command=self.set_sugar)
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

        return label_chosenflavor

    # order details labelframe for hottea
    def labelframe_order_details_hottea(self, f):
        labelframe = ttk.LabelFrame(f, text="Order Details")
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

        label_chosenflavor = ttk.Label(labelframe_chosenflavor)
        label_chosenflavor.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_L = ttk.Radiobutton(labelframe_size, text="Large (L)", value=0, command=None)
        radiobox_XL = ttk.Radiobutton(labelframe_size, text="Extra Large (XL)", value=1, command=None)
        radiobox_L.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        radiobox_XL.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        label_quantity = ttk.Label(labelframe_numdrink, text="Quantity", anchor=tk.E)
        entry_quantity = ttk.Entry(labelframe_numdrink)
        label_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        entry_quantity.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

        return label_chosenflavor

    def frame_milktea(self):
        f = ttk.Frame(self.notebook)

        # milktea flavors
        labelframe = ttk.LabelFrame(f, text="Flavors")
        labelframe.pack(side=LEFT, fill=BOTH, padx=10, pady=10)
        for x in range(0, 9):
            Grid.grid_columnconfigure(labelframe, x, weight=1)
            Grid.grid_rowconfigure(labelframe, x, weight=1)

        btn = ttk.Button(labelframe, text='Yolavit', command=lambda: self.set_flavor("Yolavit", val))
        btn2 = ttk.Button(labelframe, text='Yolowinter', command=lambda: self.set_flavor("Yolowinter", val))
        btn3 = ttk.Button(labelframe, text='YoloTaro', command=lambda: self.set_flavor("YoloTaro", val))
        btn4 = ttk.Button(labelframe, text='Yolaberry', command=lambda: self.set_flavor("Yolaberry", val))
        btn5 = ttk.Button(labelframe, text='Yolonilla', command=lambda: self.set_flavor("Yolonilla", val))
        btn6 = ttk.Button(labelframe, text='Yolomatcha', command=lambda: self.set_flavor("Yolomatcha", val))
        btn7 = ttk.Button(labelframe, text='Carpe Diem', command=lambda: self.set_flavor("Carpe Diem", val))
        btn8 = ttk.Button(labelframe, text='WYSIWYG', command=lambda: self.set_flavor("WYSIWYG", val))
        btn9 = ttk.Button(labelframe, text="C'est la vie", command=lambda: self.set_flavor("C'est la vie", val))
        btn10 = ttk.Button(labelframe, text='YoloChoco', command=lambda: self.set_flavor("YoloChoco", val))
        btn11 = ttk.Button(labelframe, text='Jasmint', command=lambda: self.set_flavor("Jasmint", val))
        btn12 = ttk.Button(labelframe, text='YoloMocha', command=lambda: self.set_flavor("YoloMocha", val))
        btn13 = ttk.Button(labelframe, text='YoloFoam', command=lambda: self.set_flavor("YoloFoam", val))
        btn14 = ttk.Button(labelframe, text='YoloCaramel', command=lambda: self.set_flavor("YoloCaramel", val))
        btn15 = ttk.Button(labelframe, text='La Dolce Vita', command=lambda: self.set_flavor("La Dolce Vita", val))
        btn16 = ttk.Button(labelframe, text='YoloKkaido', command=lambda: self.set_flavor("YoloKkaido", val))
        btn17 = ttk.Button(labelframe, text='YoloChocoNana', command=lambda: self.set_flavor("YoloChocoNana", val))

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

        val = self.labelframe_order_details_milktea_fruittea(f)
        self.notebook.add(f, text='MilkTea')

    def frame_fruittea(self):
        f = ttk.Frame(self.notebook)

        # fruittea flavors
        labelframe = ttk.LabelFrame(f, text="Flavors")
        labelframe.pack(side=LEFT, fill=Y, padx=5, pady=5)
        for x in range(0, 5):
            Grid.grid_columnconfigure(labelframe, x, weight=1)
            Grid.grid_rowconfigure(labelframe, x, weight=1)

        btn = ttk.Button(labelframe, text='YoloBlue', command=lambda:self.flavor_cmd("YoloBlue", val))
        btn2 = ttk.Button(labelframe, text='YoloApple', command=lambda:self.flavor_cmd("YoloApple", val))
        btn3 = ttk.Button(labelframe, text='YoLychee', command=lambda:self.flavor_cmd("YoLychee", val))
        btn4 = ttk.Button(labelframe, text='Hakuna Matata', command=lambda:self.flavor_cmd("Hakuna Matata", val))
        btn5 = ttk.Button(labelframe, text='Eurika', command=lambda:self.flavor_cmd("Eurika", val))

        btn.grid(row=0, column=0, padx=5, pady=5, ipadx=60, sticky=N+S+E+W)
        btn2.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn3.grid(row=2, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn4.grid(row=3, column=0, padx=5, pady=5, sticky=N+S+E+W)
        btn5.grid(row=4, column=0, padx=5, pady=5, sticky=N+S+E+W)

        val = self.labelframe_order_details_milktea_fruittea(f)
        self.notebook.add(f, text='FruitTea')

    def frame_hottea(self):
        f = ttk.Frame(self.notebook)

        # hottea flavors
        labelframe = ttk.LabelFrame(f, text="Flavors")
        labelframe.pack(side=LEFT, fill=Y, padx=5, pady=5)
        for x in range(0, 2):
            Grid.grid_columnconfigure(labelframe, x, weight=1)
            Grid.grid_rowconfigure(labelframe, x, weight=1)

        btn = ttk.Button(labelframe, text='Assam/Jasmine', command=lambda:self.flavor_cmd("Assam/Jasmine", val))
        btn2 = ttk.Button(labelframe, text='Stash Tea Bag', command=lambda:self.flavor_cmd("Stash Tea Bag", val))

        btn.grid(row=0, column=0, padx=5, pady=5, ipadx=52, sticky=N+S+E+W)
        btn2.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)

        val = self.labelframe_order_details_hottea(f)
        self.notebook.add(f, text='HotTea')

    def frame_snacks(self):
        f = ttk.Frame(self.notebook)

        # snacks
        labelframe = ttk.LabelFrame(f, text="Flavors")
        labelframe.pack(side=LEFT, fill=Y, padx=5, pady=5)
        for x in range(0, 2):
            Grid.grid_columnconfigure(labelframe, x, weight=1)
            Grid.grid_rowconfigure(labelframe, x, weight=1)

        btn = ttk.Button(labelframe, text='Belgian Waffle', command=None)
        btn2 = ttk.Button(labelframe, text='Nachos', command=None)

        btn.grid(row=0, column=0, padx=5, pady=5, ipadx=55, sticky=N+S+E+W)
        btn2.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)

        self.labelframe_order_details_milktea_fruittea(f)
        self.notebook.add(f, text='YoloSnacks')

    def frame_combos(self):
        f = ttk.Frame(self.notebook)

        # combos
        labelframe = ttk.LabelFrame(f, text="Flavors")
        labelframe.pack(side=LEFT, fill=Y, padx=5, pady=5)
        for x in range(0, 2):
            Grid.grid_columnconfigure(labelframe, x, weight=1)
            Grid.grid_rowconfigure(labelframe, x, weight=1)

        btn = ttk.Button(labelframe, text='XL + BW', command=None)
        btn2 = ttk.Button(labelframe, text=' XL + Nachos', command=None)

        btn.grid(row=0, column=0, padx=5, pady=5, ipadx=60, sticky=N+S+E+W)
        btn2.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)

        self.labelframe_order_details_milktea_fruittea(f)
        self.notebook.add(f, text='YoloCombos')


def main():
  
    root = tk.Tk()
    root.geometry("1000x500")
    root.withdraw()
    app = Yolotea(root)
    root.state('zoomed')
    root.deiconify()
    root.mainloop()

if __name__ == '__main__':
    main()  