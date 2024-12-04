import customtkinter as ctk
from settings import *
#WIDGETS IMPORTEN

from Chart_Widget import Chart
from Calculator_Widget import Calculator

class Tab_Aktien(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent,fg_color="red")
        self.pack(expand=True,fill="both")

        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=50,uniform="b")
        self.columnconfigure(1,weight=20,uniform="b")
        

        Chart(self,
             fg_color=DARK_BLUE_UI["gray"])
        
        Calculator(self,
             fg_color=DARK_BLUE_UI["gray"])

       
        
