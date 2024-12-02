import customtkinter as ctk
from settings import *
import webbrowser
#WIDGETS IMPORTEN
from File_Manager_Widget import File_Manager
from Settings_Manager_Widget import Settings_Manager
from Chart_Widget import Chart
from Calculator_Widget import Calculator






class Login_Window(ctk.CTkFrame):
    def __init__(self,parent = None, controller = None):
        super().__init__(master=parent,bg_color=GREEN_UI["green"],corner_radius=70,border_color=GREEN_UI["green"],border_width=10,fg_color=GREEN_UI["black"])
        self.controller = controller
    
        main_window_font = ctk.CTkFont(family=FONT,size=MAIN_WINDOW_SIZE)
        tool_font = ctk.CTkFont(family=FONT,size=MAIN_WINDOW_SIZE-31)
        by_signing_font = ctk.CTkFont(family = FONT,size=MAIN_WINDOW_SIZE-60)
        jules_hummel_singature_font = ctk.CTkFont(family=FONT_JULES_HUMMEL,size=MAIN_WINDOW_SIZE-60)
        buttons_font = ctk.CTkFont(family=FONT,size=MAIN_WINDOW_SIZE-60)
        #widgets
       
        self.kapital_string = ctk.CTkLabel(self,text="Kapital",font=main_window_font,text_color=GREEN_UI["green"]).place(relx=0.45,rely=0.10,anchor="center")
        self.tracking_string = ctk.CTkLabel(self,text="Tracking",font=main_window_font,text_color=GREEN_UI["green"]).place(relx=0.5,rely=0.23,anchor="center")
        self.signing_string_by = ctk.CTkLabel(self,text="by",font=by_signing_font,text_color=GREEN_UI["green"]).place(relx=0.39,rely=0.31,anchor="center")
        self.signing_string_jules_hummel = ctk.CTkLabel(self,text="jules hummel",font=jules_hummel_singature_font,text_color=GREEN_UI["light_green"]).place(relx=0.46,rely=0.313,anchor="center")
        self.tool_string = ctk.CTkLabel(self,text="Tool",font=tool_font,text_color=GREEN_UI["green"]).place(relx=0.59,rely=0.35,anchor="center")

        github_button = ctk.CTkButton(self,text="GitHub",width=125,height=50,corner_radius=12,font=buttons_font,fg_color=GREEN_UI["green"],text_color=GREEN_UI["black"],command=self.open_github_func,hover_color=GREEN_UI["light_green"])
        github_button.place(relx=0.35,rely=0.6)

        tracking_tool_button = ctk.CTkButton(self,text="Tracking Tool",width=125,height=50,corner_radius=12,font=buttons_font,fg_color=GREEN_UI["green"],text_color=GREEN_UI["black"],command=self.open_tracking_tool,hover_color=GREEN_UI["light_green"])
        tracking_tool_button.place(relx=0.56,rely=0.6)

        self.pack(expand=True,fill="both")

    def open_github_func(self):
      webbrowser.open("https://github.com/JuleeC")

    def open_tracking_tool(self):
        
        print("tracking tool")
        self.controller.show_page(Tracking_Window_Tabs)
        self.master.resizable(True, True)
        self.master.minsize(700,400)


class Tracking_Window_Tabs(ctk.CTkFrame):
    def __init__(self,parent=None,controller =None):
        super().__init__(master=parent)
        self.controller = controller
        self.pack(expand=True,fill="both")
        
    
        self.rowconfigure(0,weight=15,uniform="a")
        self.rowconfigure(1,weight=10,uniform="a")
        self.rowconfigure(2,weight=100,uniform="a")
        self.columnconfigure(0,weight=15,uniform="b")
        self.columnconfigure(1,weight=30,uniform="b")
        self.columnconfigure(2,weight=100,uniform="b")
        self.columnconfigure(3,weight=35,uniform="b")

        ctk.CTkButton(self,fg_color= BLUE_UI["dark_blue"],corner_radius=5,command=self.go_login_window).grid(row=0,column=0,sticky="nsew")

        File_Manager(self,
                     fg_color=BLUE_UI["dark_blue"]
                    )
        Settings_Manager(self,
                         fg_color=BLUE_UI["dark_blue"])
    
        Chart(self,
              fg_color=BLUE_UI["dark_blue"])
        
        Calculator(self,
              fg_color=BLUE_UI["dark_blue"])
        #EXAMPLE
        # ctk.CTkFrame(self,fg_color= "red").grid(row=0,column=1,sticky="nsew",columnspan=3,padx=30)
        # ctk.CTkFrame(self,fg_color="green").grid(row=2,column=0,sticky="nsew",pady=10,padx=10)
        # ctk.CTkFrame(self,fg_color="blue").grid(row=2,column=1,sticky="nsew",pady=10,padx=10)
        # ctk.CTkFrame(self,fg_color="green").grid(row=2,column=2,sticky="nsew",pady=10,padx=10)
        # ctk.CTkFrame(self,fg_color="red").grid(row=2,column=3,sticky="nsew",pady=10,padx=10)



    def go_login_window(self):
        self.controller.show_page(Login_Window)

        
      







       
        
        