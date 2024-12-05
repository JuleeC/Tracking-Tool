import customtkinter as ctk
import darkdetect

from windows import Login_Window, Tracking_Window_Tabs
from windows import *
from settings import *


class Main(ctk.CTk):
    def __init__(self,is_dark):
        super().__init__(fg_color=(GREEN_UI["white"],GREEN_UI["black"]))
        ctk.set_appearance_mode("dark") if is_dark else ctk.set_appearance_mode("light")
        self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}")
        self.resizable(False,False)
        self.title("Tracking-Tool")
        self.iconbitmap("images/greenbumbleinvestlogo.png")

        
       # self.creating_main_labels()
        self.active_frame = None
        self.show_page(Login_Window)
        
        
        
    def show_page(self,page_class):
        if self.active_frame:
            self.active_frame.destroy()
        self.active_frame = page_class(parent=self,controller=self)
        self.active_frame.place(relheight=RELHEIGHT,relwidth=RELWIDTH,anchor="nw")



if __name__ == "__main__":
   app = Main(darkdetect.isDark())
   app.mainloop()