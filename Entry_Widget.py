import customtkinter as ctk

from tkinter import ttk
from settings import *

class Entry_Widget_Frame(ctk.CTkFrame):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color,border_width=20,border_color=DARK_BLUE_UI["black"])
        
        self.rowconfigure(0,weight=20,uniform="a")
        self.rowconfigure(1,weight=10,uniform="a")
        self.rowconfigure(2,weight=70,uniform="a")
       
        self.columnconfigure((0,1,2,3,4,5),weight=20,uniform="b")

    #VARIABLES
        item_entry_def_var = ctk.StringVar(value="item")
        item_entry_var =ctk.StringVar()
        amount_entry_def_var =ctk.StringVar(value="amount")
        amount_entry_var = ctk.StringVar()
        date_entry_def_var = ctk.StringVar(value="date")
        date_entry_var = ctk.StringVar()


    
        ctk.CTkEntry(self,placeholder_text=item_entry_def_var.get(),textvariable=item_entry_var).grid(row=1,column=1,sticky="nsew",padx=15,pady=15)
        ctk.CTkEntry(self,placeholder_text=amount_entry_def_var.get(),textvariable=amount_entry_var).grid(row=1,column=2,sticky="nsew",padx=15,pady=15)
        ctk.CTkEntry(self,placeholder_text=date_entry_def_var.get(),textvariable=date_entry_var).grid(row=1,column=3,sticky="nsew",padx=15,pady=15)
        ctk.CTkButton(self,text="Submit").grid(row=1,column=4,sticky="nsew",padx=15,pady=15)

class Entry_Tree(ttk.Treeview):
    def __init__(self,parent):
        super().__init__(master=parent)
        
