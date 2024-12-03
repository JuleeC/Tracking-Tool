import customtkinter as ctk
from settings import *
from main import Main
import webbrowser
#from tracking_window import Tracking_Window_Tabs



class Login_Window(ctk.CTkFrame):
    def __init__(self,parent = None, controller = None):
        super().__init__(master=parent,bg_color=GREEN,corner_radius=70,border_color=GREEN,border_width=10,fg_color=BLACK)
        self.controller = controller
    
        main_window_font = ctk.CTkFont(family=FONT,size=MAIN_WINDOW_SIZE)
        tool_font = ctk.CTkFont(family=FONT,size=MAIN_WINDOW_SIZE-31)
        by_signing_font = ctk.CTkFont(family = FONT,size=MAIN_WINDOW_SIZE-60)
        jules_hummel_singature_font = ctk.CTkFont(family=FONT_JULES_HUMMEL,size=MAIN_WINDOW_SIZE-60)
        buttons_font = ctk.CTkFont(family=FONT,size=MAIN_WINDOW_SIZE-60)
        #widgets
       
        self.kapital_string = ctk.CTkLabel(self,text="Kapital",font=main_window_font,text_color=GREEN).place(relx=0.45,rely=0.10,anchor="center")
        self.tracking_string = ctk.CTkLabel(self,text="Tracking",font=main_window_font,text_color=GREEN).place(relx=0.5,rely=0.23,anchor="center")
        self.signing_string_by = ctk.CTkLabel(self,text="by",font=by_signing_font,text_color=GREEN).place(relx=0.39,rely=0.31,anchor="center")
        self.signing_string_jules_hummel = ctk.CTkLabel(self,text="jules hummel",font=jules_hummel_singature_font,text_color=LIGHT_GREEN).place(relx=0.46,rely=0.313,anchor="center")
        self.tool_string = ctk.CTkLabel(self,text="Tool",font=tool_font,text_color=GREEN).place(relx=0.59,rely=0.35,anchor="center")

        github_button = ctk.CTkButton(self,text="GitHub",width=125,height=50,corner_radius=12,font=buttons_font,fg_color=GREEN,text_color=BLACK,command=self.open_github_func,hover_color=LIGHT_GREEN)
        github_button.place(relx=0.35,rely=0.6)

        tracking_tool_button = ctk.CTkButton(self,text="Tracking Tool",width=125,height=50,corner_radius=12,font=buttons_font,fg_color=GREEN,text_color=BLACK,command=self.open_tracking_tool,hover_color=LIGHT_GREEN)
        tracking_tool_button.place(relx=0.56,rely=0.6)

        self.pack(expand=True,fill="both")

    def open_github_func(self):
      webbrowser.open("https://github.com/JuleeC")

    def open_tracking_tool(self):
        
        print("tracking tool")
        self.controller.show_page(Tracking_Window_Tabs)
        self.master.resizable(True, True)
        
       # Tracking_Window_Tabs()






class Tracking_Window_Tabs(ctk.CTkFrame):
    def __init__(self,parent=None,controller =None):
        super().__init__(master=parent,bg_color="blue")
        self.controller = controller
        self.pack(expand=True,fill="both")

        
        self.back_button = ctk.CTkButton(self,text="back",width=100,height=100, command = self.go_login_window)
        self.back_button.pack(padx=10,side="left")
        self.tracking_tabs = ctk.CTkTabview(self)
        tab1 = self.tracking_tabs.add("tab1")
        tab2 = self.tracking_tabs.add("tab2")
        self.tracking_tabs.pack(side="left",padx=10)
        
    
    def go_login_window(self):
        self.controller.show_page(Login_Window)
       
        
        