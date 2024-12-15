import customtkinter as ctk
from settings import DARK_BLUE_UI

class Settings_Manager(ctk.CTkFrame):
    def __init__(self,parent,layer,fg_color):
        super().__init__(master=parent,corner_radius=2,fg_color=fg_color)
        self.layer = layer
        
        
        match self.layer:
            case "File":
                ctk.CTkButton(self,text="aa").pack()
            case "Calculator":
                ctk.CTkButton(self,text="aaa").pack()
            case "Account":
                ctk.CTkButton(self,text="aaaa").pack()
            case _:
                pass
        

