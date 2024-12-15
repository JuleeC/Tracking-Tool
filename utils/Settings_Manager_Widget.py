import customtkinter as ctk
from settings import DARK_BLUE_UI




class Settings_Manager(ctk.CTkFrame):
    def __init__(self,parent,layer,fg_color):
        super().__init__(master=parent,corner_radius=2,fg_color=fg_color)
        self.layer = layer
        
        
        match self.layer:
            case "File":
                File(self)
            case "Calculator":
                Calculator(self)
            case "Account":
                Account(self)
            case "Settings":
                print("sda")
                Settings(self)
                print("sd")


class File():
    def __init__(self_ni,self):
        ctk.CTkButton(self,text="").pack()


        
class Calculator():
    def __init__(self_ni,self):
        ctk.CTkButton(self,text="").pack()
        
        
class Account():
    def __init__(self_ni,self):
        ctk.CTkButton(self,text="").pack()

class Settings(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__(master=parent)
        self.geometry("600x400")
        self.title("Settings")
        self.wm_attributes("-topmost",True)


        
        

        
