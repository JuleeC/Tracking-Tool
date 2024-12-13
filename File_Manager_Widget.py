import customtkinter as ctk
from PIL import Image,ImageTk
from settings import ENTRY_COLOR_UI,DARK_BLUE_UI
from main import Main


class File_Manager(ctk.CTkFrame):
    def __init__(self,parent,fg_color):
        super().__init__(master=parent,fg_color=fg_color)

        tracking_class = Main
        file_image_open = Image.open("file_img/file_image.png").resize((100,100))
        file_image = ctk.CTkImage(light_image=file_image_open, dark_image=file_image_open)

        calc_image_open = Image.open("file_img/calc_image.png").resize((100,100))
        calc_image = ctk.CTkImage(light_image=calc_image_open,dark_image=calc_image_open)

        settings_image_open = Image.open("file_img/settings_image.png").resize((100,100))
        settings_image = ctk.CTkImage(light_image=settings_image_open,dark_image=settings_image_open)

        account_image_open = Image.open("file_img/account_image.png").resize((50,50))
        account_image = ctk.CTkImage(light_image=account_image_open,dark_image=account_image_open)
        ctk.CTkButton(self,text="",image=file_image,width=140,fg_color=DARK_BLUE_UI["gray"],hover_color=DARK_BLUE_UI["border_gray"],height=80,command=lambda:tracking_class.file_button_on_click(self)).pack()
        ctk.CTkButton(self,text="",image=calc_image,width=140,fg_color=DARK_BLUE_UI["gray"],hover_color=DARK_BLUE_UI["border_gray"],height=80,command=tracking_class.calc_button_on_click).pack()
        ctk.CTkButton(self,text="",image=settings_image,width=140,fg_color=DARK_BLUE_UI["gray"],hover_color=DARK_BLUE_UI["border_gray"],height=80,command=tracking_class.settings_button_on_click).pack()
        ctk.CTkButton(self,text="",image=account_image,width=140,fg_color=DARK_BLUE_UI["gray"],hover_color=DARK_BLUE_UI["border_gray"],height=80,command=tracking_class.account_button_on_click).pack()
        self.grid(row=1,column=0,sticky="nsew",padx=5)


   

        
