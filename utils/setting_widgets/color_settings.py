import customtkinter as ctk
from settings import SETTINGS_COLOR_UI
from PIL import Image
from settings import *

class Color(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent,fg_color=SETTINGS_COLOR_UI["dark_gray"],width=640,height=550)
        self.place(x=161,y=0)
        

        #PRESETS
        

        # black_blue_white_preset = Image.open("color_presets_img/Black_Preset.png").resize((10, 10))
        # green_preset = Image.open("color_presets_img/Green_Preset.png")
        # light_blue_preset = Image.open("color_presets_img/Light_Blue_Preset.png")
        # pink_preset = Image.open("color_presets_img/Pink_Preset.png")


        # black_image = ctk.CTkImage(light_image=black_blue_white_preset,dark_image=black_blue_white_preset)
        # green_image = ctk.CTkImage(light_image=green_preset,dark_image=green_preset)
        # light_blue_image = ctk.CTkImage(light_image=light_blue_preset,dark_image=light_blue_preset)
        # pink_image = ctk.CTkImage(light_image=pink_preset,dark_image=pink_preset)


        #Preset Black_White_Blue
        ctk.CTkFrame(self,width=60,height=40,fg_color=Black_Preset["1"],corner_radius=0).place(x=50,y=10)
        ctk.CTkFrame(self,width=60,height=30,fg_color=Black_Preset["2"],corner_radius=0).place(x=50,y=45)
        ctk.CTkFrame(self,width=60,height=20,fg_color=Black_Preset["3"],corner_radius=0).place(x=50,y=75)
        ctk.CTkFrame(self,width=60,height=10,fg_color=Black_Preset["4"],corner_radius=0).place(x=50,y=95)
