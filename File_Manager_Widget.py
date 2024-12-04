import customtkinter as ctk

class File_Manager(ctk.CTkFrame):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color)
        
        self.grid(row=1,column=0,sticky="nsew",padx=5)
