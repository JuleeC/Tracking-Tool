
from settings import *
from Settings_Manager_Widget import Settings_Manager

class on_CLick():
    def open_file_manager(self):
        File_Manager(self,fg_color=DARK_BLUE_UI["gray"])

        
    def file_button_on_click(self):
        Settings_Manager(self,layer="File",fg_color=DARK_BLUE_UI["gray"],on_open=False)
        print("dasds")

    def calc_button_on_click(self):
        Settings_Manager(self,layer="Calculator",fg_color=DARK_BLUE_UI["gray"],on_open=False)

    def settings_button_on_click(self):
        pass

    def account_button_on_click(self):
        Settings_Manager(self,layer="Account",fg_color=DARK_BLUE_UI["gray"],on_open=False)   

from File_Manager_Widget import File_Manager
class File_Import():
    
    def open_file_manager(self):
        File_Manager(self,fg_color=DARK_BLUE_UI["gray"])