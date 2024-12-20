import customtkinter as ctk

from settings import SETTINGS_COLOR_UI
from colorchanger import ColorChanger

from utils.setting_widgets.color_settings import Presets
from utils.setting_widgets.tool_settings import Tools
from utils.setting_widgets.aboutme_settings import AboutMe
from utils.setting_widgets.preferences_settings import Preferences

from settings import value

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
        ctk.CTkButton(self,text="sfdfd",hover_color=ColorChanger.changing_color(1,3)).pack()


        
class Calculator():
    def __init__(self_ni,self):
        ctk.CTkButton(self,text="").pack()
        
        
class Account():
    def __init__(self_ni,self):
        ctk.CTkButton(self,text="").pack()

class Settings(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__(master=parent,fg_color=SETTINGS_COLOR_UI["gray"])

        self.geometry("800x550")
        self.title("Settings")
        self.wm_attributes("-topmost",True)
        self.resizable(False,False)
        

        #line
        ctk.CTkFrame(self,fg_color=SETTINGS_COLOR_UI["border"],width=2,height=600).place(x=160,rely=0)
        #---
        #left side
        ctk.CTkButton(self,text="Presets",border_color=SETTINGS_COLOR_UI["gray"],fg_color=SETTINGS_COLOR_UI["gray"],bg_color=SETTINGS_COLOR_UI["gray"],hover_color=SETTINGS_COLOR_UI["border"],command=lambda:Presets(self)).place(x=5,y=5)
        ctk.CTkButton(self,text="Tools",border_color=SETTINGS_COLOR_UI["gray"],fg_color=SETTINGS_COLOR_UI["gray"],bg_color=SETTINGS_COLOR_UI["gray"],hover_color=SETTINGS_COLOR_UI["border"],command=lambda:Tools(self)).place(x=5,y=35)
        ctk.CTkButton(self,text="Preferences",border_color=SETTINGS_COLOR_UI["gray"],fg_color=SETTINGS_COLOR_UI["gray"],bg_color=SETTINGS_COLOR_UI["gray"],hover_color=SETTINGS_COLOR_UI["border"],command=lambda:Preferences(self)).place(x=5,y=65)
        ctk.CTkButton(self,text="About Me",border_color=SETTINGS_COLOR_UI["gray"],fg_color=SETTINGS_COLOR_UI["gray"],bg_color=SETTINGS_COLOR_UI["gray"],hover_color=SETTINGS_COLOR_UI["border"],command=lambda:AboutMe(self)).place(x=5,y=95)
        ctk.CTkButton(self,text="Debug",border_color=SETTINGS_COLOR_UI["gray"],fg_color=SETTINGS_COLOR_UI["gray"],bg_color=SETTINGS_COLOR_UI["gray"],hover_color=SETTINGS_COLOR_UI["border"],command=lambda:print(value)).place(x=5,y=125)
        #ctk.CTkFrame(self,fg_color=SETTINGS_COLOR_UI["dark_gray"],width=640,height=550).place(x=161,y=0)
        
        

        