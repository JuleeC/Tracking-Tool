import customtkinter as ctk

class AboutMe(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent,fg_color="green",width=640,height=550)
        self.place(x=161,y=0)