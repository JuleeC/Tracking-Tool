import customtkinter as ctk
import darkdetect
from windows import Tracking_Window_Tabs,Login_Window

from Entry_Widget import Entry_Widget_Frame
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
        self.entry_widget_var = Entry_Widget_Frame(parent=self,fg_color=DARK_BLUE_UI["gray"])
        self.active_frame = None
        self.show_page(Login_Window)
        
        
        
        self.entry_widget_var.pack(expand=True,fill="both")
        
       
    def show_page(self,page_class):
        if self.active_frame:
            self.active_frame.destroy()
        self.active_frame = page_class(parent=self,controller=self)
        self.active_frame.place(relheight=RELHEIGHT,relwidth=RELWIDTH,anchor="nw")

   
    def file_button_on_click(self):
        Tracking_Window_Tabs.file_button_on_click()
        pass
    def calc_button_on_click(self):
        pass

    def settings_button_on_click(self):
        pass

    def account_button_on_click(self):
        pass


if __name__ == "__main__":
   app = Main(darkdetect.isDark())
   app.mainloop()


#Next Tasks:

#Settings & File Manager:
#Picture Design (Files,Calc,Settings) / DONE (SHIT IMAGES)
#Visualizing it and design the buttons that are the pictures on
#doing the settings manager frame for files,calc (settings not important for now)


#Chart Frame:
#Create it
#Style it
#Give it the data


#On File Manager(not essential):
#setting to add new tab
#also set start amount




   

        



