import customtkinter as ctk

class Settings_Manager(ctk.CTkFrame):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color,corner_radius=25)
        
        self.grid(row=0,column=1,sticky="nsew",rowspan=2,pady=5)
