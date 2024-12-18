import customtkinter as ctk
from PIL import Image
from settings import ENTRY_COLOR_UI
from __init__ import on_CLick
from colorchanger import ColorChanger

class File_Manager(ctk.CTkFrame):
    def __init__(self,parent,fg_color,self1):
        super().__init__(master=parent,fg_color=fg_color)

        self.columnconfigure(0,weight=1000,uniform="a")
        self.columnconfigure(1,weight=100,uniform="a")
        self.rowconfigure((0,1,2,3),weight=10,uniform="b")
        file_image_open = Image.open("file_img/file_image.png").resize((100,100))
        file_image = ctk.CTkImage(light_image=file_image_open, dark_image=file_image_open)

        calc_image_open = Image.open("file_img/calc_image.png").resize((100,100))
        calc_image = ctk.CTkImage(light_image=calc_image_open,dark_image=calc_image_open)

        settings_image_open = Image.open("file_img/settings_image.png").resize((100,100))
        settings_image = ctk.CTkImage(light_image=settings_image_open,dark_image=settings_image_open)

        account_image_open = Image.open("file_img/account_image.png").resize((50,50))
        account_image = ctk.CTkImage(light_image=account_image_open,dark_image=account_image_open)
        ctk.CTkButton(self,text="",image=file_image,width=140,fg_color=ColorChanger.changing_color(1,2),hover_color=ColorChanger.changing_color(1,3),height=80,command=lambda:on_CLick.file_button_on_click(self1)).grid(row=0,column=0,sticky="nsew")
        ctk.CTkButton(self,text="",image=calc_image,width=140,fg_color=ColorChanger.changing_color(1,2),hover_color=ColorChanger.changing_color(1,3),height=80,command=lambda:on_CLick.calc_button_on_click(self1)).grid(row=1,column=0,sticky="nsew")
        ctk.CTkButton(self,text="",image=settings_image,width=140,fg_color=ColorChanger.changing_color(1,2),hover_color=ColorChanger.changing_color(1,3),height=80,command=lambda:on_CLick.settings_button_on_click(self1)).grid(row=2,column=0,sticky="nsew")
        ctk.CTkButton(self,text="",image=account_image,width=140,fg_color=ColorChanger.changing_color(1,2),hover_color=ColorChanger.changing_color(1,3),height=80,command=lambda:on_CLick.account_button_on_click(self1)).grid(row=3,column=0,sticky="nsew")
        #ctk.CTkLabel(self,text="",fg_color="black").grid(row=0,column=1,sticky="nsew")
        #self.grid(row=1,row=0,column=0,sticky="nsew",padx=5)
        