import customtkinter as ctk

class Chart(ctk.CTkFrame):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color,corner_radius=25)
        
        self.grid(row=0,column=2,sticky="nsew",pady=10,padx=15)
