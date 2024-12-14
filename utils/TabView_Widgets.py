import customtkinter as ctk
from settings import *
from utils.Tab_Aktien_Frame import ChartFrame

class TabView(ctk.CTkTabview):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color,corner_radius=25)
        
        self.grid(row=0,column=2,sticky="nsew",rowspan=2,padx=10)
       
        aktien_tab = self.add("Aktien")
        erze_tab = self.add("Erze")
        anleihen_tab = self.add("Anleihen")
        self.set("Aktien")

        #DIE EINZELNEN CHARTS:
        ChartFrame(aktien_tab,fg_color="red")
        ChartFrame(erze_tab,fg_color="blue")
        ChartFrame(anleihen_tab,fg_color="green")        

       
      
