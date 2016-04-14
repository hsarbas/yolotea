import Tkinter as tk
from yolotea.ui.frames.view_order_frame import ViewOrderFrame
from yolotea.ui.frames.view_all_orders_frame import ViewAllOrdersFrame
from yolotea.ui.frames.about_frame import AboutFrame
from yolotea.ui.frames.documentation_frame import DocumentationFrame
from yolotea.ui.frames.take_order_frame import TakeOrderFrame
from yolotea.ui.frames.my_account_frame import MyAccountFrame
from yolotea.ui.frames.update_inventory_frame import UpdateInventoryFrame
from yolotea.ui.frames.view_all_accounts_frame import ViewAllAccountsFrame
from yolotea.ui.frames.view_inventory_frame import ViewInventoryFrame
from yolotea.ui.frames.view_sales_frame import ViewSalesFrame


class Menubar(object):

    def __init__(self, parent, curr_frame, account_logged_in):
        self.parent = parent
        self.curr_frame = curr_frame
        self.menu_val = None
        self.account_logged_in = account_logged_in

        menubar = tk.Menu(self.parent)

        order_menu = tk.Menu(menubar, tearoff=0)
        order_menu.add_command(label='Take Order', command=self.take_order_command)
        order_menu.add_separator()
        order_menu.add_command(label='View Order', command=self.view_order_command)
        order_menu.add_command(label='View All Orders', command=self.view_all_orders_command)
        menubar.add_cascade(label='Order', menu=order_menu)

        account_menu = tk.Menu(menubar, tearoff=0)
        account_menu.add_command(label='My Account', command=self.my_account_command)
        account_menu.add_command(label='View All Accounts', command=self.view_all_accounts_command)
        account_menu.add_separator()
        account_menu.add_command(label='Logout', command=None)
        menubar.add_cascade(label='Account', menu=account_menu)

        sales_and_inventory_menu = tk.Menu(menubar, tearoff=0)
        sales_and_inventory_menu.add_command(label='View End of Day Sales', command=self.view__sales_command)
        sales_and_inventory_menu.add_command(label='View Current Inventory', command=self.view_inventory_command)
        sales_and_inventory_menu.add_separator()
        sales_and_inventory_menu.add_command(label='Update Inventory', command=self.update_inventory_command)
        menubar.add_cascade(label='Sales and Inventory', menu=sales_and_inventory_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label='View Documentation', command=self.view_documentation_command)
        help_menu.add_command(label='About The Product', command=self.view_about_command)
        menubar.add_cascade(label='Help', menu=help_menu)

        self.parent.config(menu=menubar)

    def take_order_command(self):
        self.curr_frame.destroy()
        self.curr_frame = TakeOrderFrame(self.parent)
        self.curr_frame.pack()

    def view_order_command(self):
        self.curr_frame.destroy()
        self.curr_frame = ViewOrderFrame(self.parent)
        self.curr_frame.pack()

    def view_all_orders_command(self):
        self.curr_frame.destroy()
        self.curr_frame = ViewAllOrdersFrame(self.parent)
        self.curr_frame.pack()

    def my_account_command(self):
        self.curr_frame.destroy()
        self.curr_frame = MyAccountFrame(self.parent, self.account_logged_in)
        self.curr_frame.pack()

    def view_all_accounts_command(self):
        self.curr_frame.destroy()
        self.curr_frame = ViewAllAccountsFrame(self.parent)
        self.curr_frame.pack()

    def view__sales_command(self):
        self.curr_frame.destroy()
        self.curr_frame = ViewSalesFrame(self.parent)
        self.curr_frame.pack()

    def view_inventory_command(self):
        self.curr_frame.destroy()
        self.curr_frame = ViewInventoryFrame(self.parent)
        self.curr_frame.pack()

    def update_inventory_command(self):
        self.curr_frame.destroy()
        self.curr_frame = UpdateInventoryFrame(self.parent)
        self.curr_frame.pack()

    def view_documentation_command(self):
        self.curr_frame.destroy()
        self.curr_frame = DocumentationFrame(self.parent)
        self.curr_frame.pack()

    def view_about_command(self):
        self.curr_frame.destroy()
        self.curr_frame = AboutFrame(self.parent)
        self.curr_frame.pack()
