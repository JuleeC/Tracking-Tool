import customtkinter as ctk
from settings import *





class Presets(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=SETTINGS_COLOR_UI["dark_gray"], width=640, height=550)
       
        self.place(x=161, y=0)
        
        
        
        preset_font = (FONT, 30)
        or_just_font = (FONT_JULES_HUMMEL, 20,"bold")
        ctk.CTkLabel(self, text="Presets", font=preset_font).place(x=320, y=50, anchor="center")
        ctk.CTkFrame(self, width=580, height=2, fg_color=SETTINGS_COLOR_UI["border"]).place(x=30, y=80)

        # Preset Black_White_Blue
        ctk.CTkFrame(self, width=60, height=40, fg_color=Black_Preset["1"], corner_radius=0).place(x=70, y=150)
        ctk.CTkFrame(self, width=60, height=30, fg_color=Black_Preset["2"], corner_radius=0).place(x=70, y=185)
        ctk.CTkFrame(self, width=60, height=20, fg_color=Black_Preset["3"], corner_radius=0).place(x=70, y=215)
        ctk.CTkFrame(self, width=60, height=10, fg_color=Black_Preset["4"], corner_radius=0).place(x=70, y=235)

        # Preset Green
        ctk.CTkFrame(self, width=60, height=40, fg_color=Green_Preset["1"], corner_radius=0).place(x=220, y=150)
        ctk.CTkFrame(self, width=60, height=30, fg_color=Green_Preset["2"], corner_radius=0).place(x=220, y=185)
        ctk.CTkFrame(self, width=60, height=20, fg_color=Green_Preset["3"], corner_radius=0).place(x=220, y=215)
        ctk.CTkFrame(self, width=60, height=10, fg_color=Green_Preset["4"], corner_radius=0).place(x=220, y=235)

        # Preset Light_Blue
        ctk.CTkFrame(self, width=60, height=40, fg_color=Light_Blue_Preset["1"], corner_radius=0).place(x=370, y=150)
        ctk.CTkFrame(self, width=60, height=30, fg_color=Light_Blue_Preset["2"], corner_radius=0).place(x=370, y=185)
        ctk.CTkFrame(self, width=60, height=20, fg_color=Light_Blue_Preset["3"], corner_radius=0).place(x=370, y=215)
        ctk.CTkFrame(self, width=60, height=10, fg_color=Light_Blue_Preset["4"], corner_radius=0).place(x=370, y=235)

        # Preset Pink
        ctk.CTkFrame(self, width=60, height=40, fg_color=Pink_Preset["1"], corner_radius=0).place(x=520, y=150)
        ctk.CTkFrame(self, width=60, height=30, fg_color=Pink_Preset["2"], corner_radius=0).place(x=520, y=185)
        ctk.CTkFrame(self, width=60, height=20, fg_color=Pink_Preset["3"], corner_radius=0).place(x=520, y=215)
        ctk.CTkFrame(self, width=60, height=10, fg_color=Pink_Preset["4"], corner_radius=0).place(x=520, y=235)
        
       
        
        self.tk_value = ctk.IntVar(value=value)
        
        
        global tk_int_value
        tk_int_value = self.tk_value.get()
        #from main import value_check
        


        self.black_white_blue_checkbox = ctk.CTkRadioButton(self, text="", variable=self.tk_value,value=1, command=self.preset_change_event)
        self.black_white_blue_checkbox.place(x=90, y=260)

        self.green_checkbox = ctk.CTkRadioButton(self, text="", variable=self.tk_value, value=2, command=self.preset_change_event)
        self.green_checkbox.place(x=240, y=260)

        self.light_blue_checkbox = ctk.CTkRadioButton(self, text="", variable=self.tk_value, value=3, command=self.preset_change_event)
        self.light_blue_checkbox.place(x=390, y=260)

        self.pink_checkbox = ctk.CTkRadioButton(self, text="", variable=self.tk_value, value=4, command=self.preset_change_event)
        self.pink_checkbox.place(x=540, y=260)
#----------------------------------------------------------
        ctk.CTkLabel(self, text="or just...", font=or_just_font).place(x=320, y=320, anchor="center")

        ctk.CTkFrame(self, width=60, height=40, fg_color=Dark_Preset["1"], corner_radius=0).place(x=215, y=380) #150
        ctk.CTkFrame(self, width=60, height=30, fg_color=Dark_Preset["2"], corner_radius=0).place(x=215, y=415) #185
        ctk.CTkFrame(self, width=60, height=20, fg_color=Dark_Preset["3"], corner_radius=0).place(x=215, y=435) #215
        ctk.CTkFrame(self, width=60, height=10, fg_color=Dark_Preset["4"], corner_radius=0).place(x=215, y=455) #235

        ctk.CTkFrame(self, width=60, height=40, fg_color=Light_Preset["1"], corner_radius=0).place(x=380, y=380) #150
        ctk.CTkFrame(self, width=60, height=30, fg_color=Light_Preset["2"], corner_radius=0).place(x=380, y=415) #185
        ctk.CTkFrame(self, width=60, height=20, fg_color=Light_Preset["3"], corner_radius=0).place(x=380, y=435)   #215
        ctk.CTkFrame(self, width=60, height=10, fg_color=Light_Preset["4"], corner_radius=0).place(x=380, y=455) #235
        
        self.dark_checkbox = ctk.CTkRadioButton(self, text="", variable=self.tk_value, value=5, command=self.preset_change_event)
        self.dark_checkbox.place(x=235, y=480)

        self.light_checkbox = ctk.CTkRadioButton(self, text="", variable=self.tk_value, value=6, command=self.preset_change_event)
        self.light_checkbox.place(x=400, y=480)
        
        self.update()
    def tk_int_method():
            return tk_int_value 
    # Function to display the selected radio option.
    def preset_change_event(self):
       
        from __init__ import Transfer_Color
        from main import Main
        from windows import Tracking_Window_Tabs
        from utils.Settings_Manager_Widget import Settings_Manager
        from colorchanger import ColorChanger
        global value
        main = Main()
        tracking_window = Tracking_Window_Tabs()
        file = Settings_Manager(self,0,ColorChanger.changing_color(value,1))
        match(self.tk_value.get()):
            case 1:
                #ERRROR TO FIX
                #dont know what to do
                
                main.configure(fg_color="blue")
                main.update()
                main.destroy()
                
                
                value = 1
                Transfer_Color.transfer_value_check(value)
                

            case 2:
                
                value = 2
                Transfer_Color.transfer_value_check( value)
            case 3:
               
                value = 3
                Transfer_Color.transfer_value_check(value)
            case 4:
               
                value = 4
                Transfer_Color.transfer_value_check(value)
            case 5:
              
                value = 5
                Transfer_Color.transfer_value_check(value)
            case 6:
               
                value = 6
                Transfer_Color.transfer_value_check(value)
            case _:
                pass
            
class PresetUpdate():
    def __init__():
        pass


#Überall wo die Farbe geändert wird soll diese MEthode aufgerufen werden und der value soll sich in der preset_change_event ändern