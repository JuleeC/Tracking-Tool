import customtkinter as ctk
from settings import SETTINGS_COLOR_UI
from PIL import Image
import tkinter as tk

class Color(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent,fg_color=SETTINGS_COLOR_UI["dark_gray"],width=640,height=550)
        self.place(x=161,y=0)
        self.rowconfigure((0,1,2,3,4,5),weight=1,uniform="a")
        self.columnconfigure((0,1,2,3,4,5),weight=1,uniform="a")

        #PRESETS
        preset1_frame = ctk.CTkFrame(self).grid(column=1,row=1,columnspan=2,sticky="nsew")

        black_blue_white_preset= Image.open("color_presets_img/Black_Blue_White_Preset.png")
        green_preset = Image.open("color_presets_img/Green_Preset.png")
        light_blue_preset = Image.open("color_presets_img/Light_Blue_Preset.png")
        pink_preset = Image.open("color_presets_img/Pink_Preset.png")


        black_blue_white_image = ctk.CTkImage(light_image=black_blue_white_preset,dark_image=black_blue_white_preset)
        green_image = ctk.CTkImage(light_image=green_preset,dark_image=green_preset)
        light_blue_image = ctk.CTkImage(light_image=light_blue_preset,dark_image=light_blue_preset)
        pink_image = ctk.CTkImage(light_image=pink_preset,dark_image=pink_preset)

        black_blue_white_image.pack(preset1_frame,expand=True,fill="both")