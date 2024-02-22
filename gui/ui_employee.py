#import module
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from ttkbootstrap.tableview import Tableview
from tkinter import Toplevel
from Project1.gui.validation_ui import ValidationUtils
from Project1.db.crud import check_in
#create second window
class Bill(Toplevel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.items=[]

        
        self.product_label=ttk.Label(self,text="Product")
        self.product_label.grid(row=0,column=0,padx=10,pady=10)
        self.product_entry=ttk.Entry(self,)
        self.product_entry.grid(row=1,column=0,padx=10,pady=10)


        self.quantity_label=ttk.Label(self,text="Quantity",)
        self.quantity_label.grid(row=0,column=1,padx=10,pady=10)
        self.quantity_entry=ttk.Entry(self,)
        self.quantity_entry.grid(row=1,column=1,padx=10,pady=10)


        self.price_label=ttk.Label(self,text="Price")
        self.price_label.grid(row=0,column=2,padx=10,pady=10)
        self.price_entry=ttk.Entry(self,)
        self.price_entry.grid(row=1,column=2,padx=10,pady=10)


        self.add_item_btn=ttk.Button(self,text="Add Item",command=self.add_item_action)
        self.add_item_btn.grid(row=0,column=3,)


        self.caculate_btn=ttk.Button(self,text="Caculate Total",command=self.caculate_action)
        self.caculate_btn.grid(row=0,column=4)
    def add_item_action(self):
        product=self.product_entry.get()
        quantity=self.quantity_entry.get()
        price=self.price_entry.get()
        if product and quantity and price:
            total_price=int(quantity)*int(price)
            self.items.append(total_price)
            self.product_entry.delete(0,ttk.END)
            self.quantity_entry.delete(0,ttk.END)
            self.price_entry.delete(0,ttk.END)


    def caculate_action(self):
        total=sum(self.items)
        print(total)    

#create main window
class Employee(ttk.Frame):
    #**config_container is optional
    def __init__(self,master,**config_container):
        #inherit class Frame
        super().__init__(master,**config_container,padding=10)
        self.pack(fill=BOTH,expand=YES)
        #set variable
        self.config_container={'master':self}
        #data type in ttk
        self.ID=ttk.StringVar(value="")  
        self.check_validation=ttk.BooleanVar(value=False)
        #set style 
        ttk.Style().configure('TButton', font=('sans', 20))
        ttk.Style().configure('TLabel',font=('sans', 20))
        ttk.Style().configure('TEntry',font=('sans', 20))
        #call function
        self.all_entry() 
        self.all_btn()
    #check in
    def all_entry(self):
        container_entry=ttk.Frame(**self.config_container,padding=20)
        container_entry.pack()

        label_employee_inf = ttk.Label(container_entry, text="Hi! Please check in before working")
        label_employee_inf.pack()

        label_ID = ttk.Label(container_entry,text="ID")
        label_ID.pack()

        entry_ID = ttk.Entry(container_entry,textvariable=self.ID,show='*')
        entry_ID.pack()

        #validate entry
        ValidationUtils.check_ID(entry_ID,self.check_validation)
    
    def all_btn(self):
        container_btn=ttk.Frame(**self.config_container,padding=20)
        container_btn.pack()

        btn_roll_call=ttk.Button(container_btn,text="RollCall",command=self.action_check_in)
        btn_roll_call.pack(side=LEFT)
        ValidationUtils.button_submit=btn_roll_call

        btn_bill=ttk.Button(container_btn,text="Bill",command=self.action_caculate)
        btn_bill.pack(side=LEFT)

        btn_product=ttk.Button(container_btn,text="Product",)
        btn_product.pack(side=LEFT)


    def action_check_in(self):
        ID=self.ID.get()
        if self.check_validation.get():
            check_in(ID)
        else:
            message_label=ttk.Label(master=self,text='Invalid data')
            message_label.pack()
    def action_caculate(self):
        # new_win=Toplevel(self.master)
        # new_win.title("Bill")
        bill=Bill(self.master,)
        bill.title("Bill")
        bill.geometry("900x900")
if __name__=='__main__':
    config_win={
        "title":"Employee",
        "themename":"vapor",
        "size":(800,800),
        "resizable":(False,False),
        "position":(1000,50),
    }
    #The reason you use app=ttk.Window(**config_win) and then employee=Employee(app) instead of directly doing employee=Employee(ttk.Window, **config_win) is that ttk.Window is a class, and you need to create an instance of that class
    app=ttk.Window(**config_win)
    employee=Employee(app)
    app.mainloop()
