import customtkinter as ctk

from tkinter import ttk
from settings import *


class Entry_Widget_Frame(ctk.CTkFrame):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color,border_width=20,border_color=DARK_BLUE_UI["black"])
        
        self.rowconfigure(0,weight=10,uniform="a")
        self.rowconfigure(1,weight=10,uniform="a")
        self.rowconfigure(2,weight=70,uniform="a")
        self.rowconfigure(3,weight=5,uniform="a")
       
        self.columnconfigure((0,1,2,3,4,5),weight=20,uniform="b")

    #VARIABLES
        item_entry_def_var = ctk.StringVar(value="item")
        self.item_entry_var =ctk.StringVar()
        amount_entry_def_var =ctk.StringVar(value="amount")
        self.amount_entry_var = ctk.StringVar()
        date_entry_def_var = ctk.StringVar(value="date")
        self.date_entry_var = ctk.StringVar()
        self.index = 0
        self.tree_data = []

        ctk.CTkEntry(self,placeholder_text=item_entry_def_var.get(),textvariable=self.item_entry_var).grid(row=1,column=1,sticky="nsew",padx=15,pady=15)
        ctk.CTkEntry(self,placeholder_text=amount_entry_def_var.get(),textvariable=self.amount_entry_var).grid(row=1,column=2,sticky="nsew",padx=15,pady=15)
        ctk.CTkEntry(self,placeholder_text=date_entry_def_var.get(),textvariable=self.date_entry_var).grid(row=1,column=3,sticky="nsew",padx=15,pady=15)
        ctk.CTkButton(self,text="Submit",command=lambda:self.insert_data_toTree(item_var=self.item_entry_var.get(),amount_var=self.amount_entry_var.get(),date_var=self.date_entry_var.get())).grid(row=1,column=4,sticky="nsew",padx=15,pady=15)
   
        
    def insert_data_toTree(self,item_var,amount_var,date_var):
       
        tree_one_data = (item_var,amount_var,date_var)
        self.tree_data.append(tree_one_data)
        self.index += 1
        print(f"{self.index}-------------{self.tree_data}")
        entry_tree = Entry_Tree(self)
        for i in range(self.index):
            
            entry_tree.insert(parent="",index="end",values=self.tree_data[i])

class Entry_Tree(ttk.Treeview):
    def __init__(self,parent):
        super().__init__(master=parent,columns=("items","amount","date"),show = "headings",displaycolumns = '#all',style="Entry.Treeview")

        tree_style = ttk.Style(self)

        tree_style.configure(
            "Entry.Treeview",
            background=DARK_BLUE_UI["gray"],
            foreground=GREEN_UI["white"],
            fieldbackground=DARK_BLUE_UI["gray"],
            rowheight=25)
        
        tree_style.configure(
            "Entry.Treeview.Heading",
            background=DARK_BLUE_UI["gray"],
            foreground=GREEN_UI["white"],
            font=(f"{FONT}",12,"bold"),
        )

        tree_style.map("Entry.Treeview.Heading",
                       background=[("active", DARK_BLUE_UI["light_blue"])],)
        
        self.heading("items",text="items")
        self.heading("amount",text="amount")
        self.heading("date",text="date")
       
        self.grid(row=2,column=1,columnspan=4,sticky="nsew",pady=10)

    
        