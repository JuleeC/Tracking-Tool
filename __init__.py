
from settings import *
from windows import Tracking_Window_Tabs


class on_CLick():
    def open_file_manager(self):
        File_Manager(self,fg_color=DARK_BLUE_UI["gray"])

        
    def file_button_on_click(self1):
        print("file")
        Tracking_Window_Tabs.file_button_on_click(self1)
        

    def calc_button_on_click(self1):
        print("calc")
        Tracking_Window_Tabs.calc_button_on_click(self1)

    def settings_button_on_click(self1):
        print("settings")
        Tracking_Window_Tabs.settings_button_on_click(self1)

    def account_button_on_click(self1):
        print("account")
        Tracking_Window_Tabs.account_button_on_click(self1)

from utils.File_Manager_Widget import File_Manager
class File_Import():
    def open_file_manager(self,self1):
        File_Manager(self,self1=self1,fg_color=DARK_BLUE_UI["gray"]).grid(row=1,column=0,sticky="nsew")