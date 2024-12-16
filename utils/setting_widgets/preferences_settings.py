import customtkinter as ctk
from settings import SETTINGS_COLOR_UI
class Preferences(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent,fg_color="red",width=640,height=550)
        self.place(x=161,y=0)