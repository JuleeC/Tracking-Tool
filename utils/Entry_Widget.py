import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from datetime import date

from tkinter import ttk
from settings import *
from colorchanger import ColorChanger

class Entry_Widget_Frame(ctk.CTkFrame):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color,border_width=20,border_color=ColorChanger.changing_color(1,2))
        
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
        self.current_date_and_time = date.today()

        Entry_Tree(self,self.tree_data)
        ctk.CTkEntry(self,placeholder_text_color="blue",placeholder_text=item_entry_def_var.get(),fg_color=ENTRY_COLOR_UI["gray"],textvariable=self.item_entry_var).grid(row=1,column=1,sticky="nsew",padx=15,pady=15)
        ctk.CTkEntry(self,placeholder_text=amount_entry_def_var.get(),fg_color=ENTRY_COLOR_UI["gray"],textvariable=self.amount_entry_var).grid(row=1,column=2,sticky="nsew",padx=15,pady=15)
        ctk.CTkEntry(self,placeholder_text=date_entry_def_var.get(),fg_color=ENTRY_COLOR_UI["gray"],textvariable=self.date_entry_var).grid(row=1,column=3,sticky="nsew",padx=15,pady=15)
        ctk.CTkButton(self,text="Submit",command=lambda:self.insert_data_toTree(item_var=self.item_entry_var.get(),amount_var=self.amount_entry_var.get(),date_var=self.date_entry_var.get())).grid(row=1,column=4,sticky="nsew",padx=15,pady=15)
        
        
    def insert_data_toTree(self,item_var,amount_var,date_var):
        
        if item_var == "":
            CTkMessagebox(title="Error!",message="item cannot be an empty value!",icon="cancel",option_1="Ok")
        elif amount_var == "":
            CTkMessagebox(title="Error!",message="amount cannot be an empty value!",icon="cancel",option_1="Ok")
        elif date_var == "":
            date_var = self.current_date_and_time
            date_calc_var = "".join(char for char in str(date_var) if char.isdigit())
            
            tree_one_data = (item_var,amount_var,date_calc_var)
            self.tree_data.append(tree_one_data)
            self.index += 1
            print(f"{self.index}-------------{self.tree_data}")
            entry_tree = Entry_Tree(self,self.tree_data)
            try:
                for i in range(self.index):
                    entry_tree.insert(parent="",index="end",values=self.tree_data[i])
            except IndexError:
                print("Error-Handling: array out of range")
        else:
            tree_one_data = (item_var,amount_var,date_var)
            self.tree_data.append(tree_one_data)
            self.index += 1
            print(f"{self.index}-------------{self.tree_data}")
            entry_tree = Entry_Tree(self,self.tree_data)
           
            try:
                for i in range(self.index):
                    entry_tree.insert(parent="",index="end",values=self.tree_data[i])
            except IndexError:
                print("Error-Handling: array out of range")
                   
       

class Entry_Tree(ttk.Treeview):
    def __init__(self,parent,tree_data):
        super().__init__(master=parent,columns=("items","amount","date"),show = "headings",style="Treeview",padding=11,displaycolumns="#all")
        self.tree_data = tree_data
        tree_style = ttk.Style(self)
        tree_style.theme_use("clam")

        #bind for delete
        self.bind("<Double-1>", self.delete_entry)

        # Style for the Treeview rows
        tree_style.configure(
            "Treeview",
            background=ENTRY_COLOR_UI["gray"],       
            foreground=WHITE,       
            fieldbackground=ENTRY_COLOR_UI["gray"],       
            rowheight=25,
            bordercolor = ENTRY_COLOR_UI["border_gray"],   
            lightcolor=ENTRY_COLOR_UI["border_gray"],
            darkcolor =ENTRY_COLOR_UI["border_gray"],
                       
        )
        
        # Style for the Treeview headings
        tree_style.configure(
            "Treeview.Heading",
            fieldbackground=ENTRY_COLOR_UI["gray"],
            background=ENTRY_COLOR_UI["gray"],       
            foreground=WHITE,       
            font=(f"{FONT}", 12, "bold"),
            bordercolor = ENTRY_COLOR_UI["border_gray"],
            lightcolor=ENTRY_COLOR_UI["border_gray"],
            darkcolor =ENTRY_COLOR_UI["border_gray"]
        )

       
        tree_style.map("Treeview.Heading",
                       background=[("active", ENTRY_COLOR_UI["blue"])])  
        
#--------------------------------------------------------------------------
       
         
        self.heading("items",text="items")
        self.heading("amount",text="amount")
        self.heading("date",text="date")
       

        self.column("items", anchor="center",stretch=True)
        self.column("amount", anchor="center",stretch=True)
        self.column("date", anchor="center",stretch=True)

        self.grid(row=2,column=1,columnspan=4,sticky="nsew",pady=10)


#--------------------------------------------------------------------------
    
    def delete_entry(self,event):
        entry_id = self.identify_row(event.y)
        if entry_id:
            entry_value = self.item(entry_id, "values")
            self.messagebox_delete_question(entry_id=entry_id,entry_value=entry_value)

    def messagebox_delete_question(self, entry_id, entry_value):
        delete_answer = CTkMessagebox(
            title="Delete?",
            message=f"Do you want to delete this entry?\n{entry_value}",
            icon="question",
            option_1="No",
            option_2="Yes",
            option_3="Cancel"
        )

        if delete_answer.get() == "Yes":

            print(f"Deleting  {entry_value}")

            
            self.delete(entry_id)   
            
            
            try:
                self.tree_data.remove(entry_value)
                print(f"Entry removed from array: {entry_value}")
            except ValueError:
                print(f"Entry {entry_value} not found in the array")

        else:
            print("Deletion canceled.")


    

 
            