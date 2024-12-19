
from settings import *



class on_CLick():
    def open_file_manager(self):
        File_Manager(self,fg_color=ColorChanger.changing_color(1,2))

        
    def file_button_on_click(self1):
        print("file")
        from windows import Tracking_Window_Tabs
        Tracking_Window_Tabs.file_button_on_click(self1)
        

    def calc_button_on_click(self1):
        print("calc")
        from windows import Tracking_Window_Tabs
        Tracking_Window_Tabs.calc_button_on_click(self1)

    def settings_button_on_click(self1):
        print("settings")
        from windows import Tracking_Window_Tabs
        Tracking_Window_Tabs.settings_button_on_click(self1)

    def account_button_on_click(self1):
        print("account")
        from windows import Tracking_Window_Tabs
        Tracking_Window_Tabs.account_button_on_click(self1)

from colorchanger import ColorChanger 
from utils.File_Manager_Widget import File_Manager


class File_Import():
    def open_file_manager(self,self1):
        File_Manager(self,self1=self1,fg_color=ColorChanger.changing_color(1,2)).grid(row=1,column=0,sticky="nsew")


        
class Transfer_Color():

    def transfer_value_check(value):
        from main import Main
        self_value=value
        Main.value_check(self_value)
   