import customtkinter as ctk

class File_Manager(ctk.CTkFrame):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color,corner_radius=25)
        
        self.grid(row=2,column=0,sticky="nsew",pady=10,padx=5)
