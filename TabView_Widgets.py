import customtkinter as ctk
from settings import *
from Tab_Aktien_Frame import Tab_Aktien

class TabView(ctk.CTkTabview):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color,corner_radius=25)
        
        self.grid(column=1,sticky="nsew")
       
        aktien_tab = self.add("Aktien")
        erze_tab = self.add("Erze")
        self.set("Aktien")
        #Tab_Aktien(aktien_tab)
        

       
      
