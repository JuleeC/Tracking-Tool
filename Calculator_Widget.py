import customtkinter as ctk

class Calculator(ctk.CTkFrame):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color,corner_radius=25)
        
        self.grid(row=2,column=3,sticky="nsew",pady=10)
