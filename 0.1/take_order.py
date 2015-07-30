import Tkinter as tk
from Tkinter import *
from ttk import *
import ttk
import popups


class Yolotea(ttk.Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.pack(fill=BOTH)
        self.parent = parent
        self.initUI()
        self.start_login()
        self.init_menubar()
        self.init_paned_window()
        
    def initUI(self):
      
        self.parent.title("Yolotea Order System")
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
        #account labelframe
        self.labelframe_account = ttk.LabelFrame(self, text="Account Details")
        self.labelframe_account.pack(side=TOP, fill=X, padx=10, pady=10)
        self.logo = ttk.Label(self.labelframe_account, text="YOLOTEA LOGO", width=20)
        self.employee_name = ttk.Label(self.labelframe_account, text="Employee Name: EMPLOYEE NAME", width=100)
        self.employee_id = ttk.Label(self.labelframe_account, text = "ID Number: ID NUMBER", width=100)
        self.logo.grid(row=0, column=0, columnspan=3, rowspan=3, padx=10, pady=10)
        self.employee_name.grid(row=0, column=4, padx=10, pady=5)
        self.employee_id.grid(row=1, column=4, padx=10, pady=5)

        #main notebook
        self.notebook = ttk.Notebook(self)
        self.frame_milktea()
        self.frame_fruittea()
        self.frame_hottea()
        self.frame_snacks()
        self.frame_combos()

        self.notebook.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        #order details labelframe
        self.labelframe_orderDetails = ttk.LabelFrame(self, text="Order Details")
        self.labelframe_orderDetails.pack(side=RIGHT, fill=Y, padx=10, pady=10)
        self.order_listbox = tk.Label(self.labelframe_orderDetails, height=28, width=40, bg="white")
        self.order_listbox.pack(side=TOP, padx=5, pady=5)
        self.total_label = ttk.Label(self.labelframe_orderDetails, text="Total Amount: P0.00")
        self.total_label.pack(side=TOP, fill=Y, pady=10)
        self.checkout_btn = ttk.Button(self.labelframe_orderDetails, text='Checkout', command=None)
        self.checkout_btn.pack(side=BOTTOM, padx=10, pady=10)

    def frame_milktea(self):
        f = ttk.Frame(self.notebook)

        #milktea flavors
        labelframe = ttk.LabelFrame(f, text="Flavors")
        labelframe.pack(side=LEFT, fill=Y, padx=5, pady=5)

        btn = ttk.Button(labelframe, text='Yolavit', command=None)
        btn2 = ttk.Button(labelframe, text='Yolowinter', command=None)
        btn3 = ttk.Button(labelframe, text='YoloTaro', command=None)
        btn4 = ttk.Button(labelframe, text='Yolaberry', command=None)
        btn5 = ttk.Button(labelframe, text='Yolonilla', command=None)
        btn6 = ttk.Button(labelframe, text='Yolomatcha', command=None)
        btn7 = ttk.Button(labelframe, text='Carpe Diem', command=None)
        btn8 = ttk.Button(labelframe, text='WYSIWYG', command=None)
        btn9 = ttk.Button(labelframe, text="C'est la vie", command=None)
        btn10 = ttk.Button(labelframe, text='YoloChoco', command=None)
        btn11 = ttk.Button(labelframe, text='Jasmint', command=None)
        btn12 = ttk.Button(labelframe, text='YoloMocha', command=None)
        btn13 = ttk.Button(labelframe, text='YoloFoam', command=None)
        btn14 = ttk.Button(labelframe, text='YoloCaramel', command=None)
        btn15 = ttk.Button(labelframe, text='La Dolce Vita', command=None)
        btn16 = ttk.Button(labelframe, text='YoloKkaido', command=None)
        btn17 = ttk.Button(labelframe, text='YoloChocoNana', command=None)

        btn.grid(row=0, column=0, padx=5, pady=5)
        btn2.grid(row=1, column=0, padx=5, pady=5)
        btn3.grid(row=2, column=0, padx=5, pady=5)
        btn4.grid(row=3, column=0, padx=5, pady=5)
        btn5.grid(row=4, column=0, padx=5, pady=5)
        btn6.grid(row=5, column=0, padx=5, pady=5)
        btn7.grid(row=6, column=0, padx=5, pady=5)
        btn8.grid(row=7, column=0, padx=5, pady=5)
        btn9.grid(row=8, column=0, padx=5, pady=5)
        btn10.grid(row=0, column=1, padx=5, pady=5)
        btn11.grid(row=1, column=1, padx=5, pady=5)
        btn12.grid(row=2, column=1, padx=5, pady=5)
        btn13.grid(row=3, column=1, padx=5, pady=5)
        btn14.grid(row=4, column=1, padx=5, pady=5)
        btn15.grid(row=5, column=1, padx=5, pady=5)
        btn16.grid(row=6, column=1, padx=5, pady=5)
        btn17.grid(row=7, column=1, padx=5, pady=5)

        labelframe2 = ttk.LabelFrame(f)
        labelframe2.pack(side=RIGHT, fill=BOTH, expand=TRUE, padx=5,pady=5)
        self.notebook.add(f, text='MilkTea')


    def frame_fruittea(self):
        f = ttk.Frame(self.notebook)
        self.notebook.add(f, text='FruitTea')

    def frame_hottea(self):
        f = ttk.Frame(self.notebook)
        self.notebook.add(f, text='HotTea')

    def frame_snacks(self):
        f = ttk.Frame(self.notebook)
        self.notebook.add(f, text='YoloSnacks')

    def frame_combos(self):
        f = ttk.Frame(self.notebook)
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