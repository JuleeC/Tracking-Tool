import customtkinter as ctk
from settings import *
import webbrowser
from PIL import Image


from utils.TabView_Widgets import TabView
from utils.Settings_Manager_Widget import *

from colorchanger import ColorChanger




class Login_Window(ctk.CTkFrame):
    def __init__(self,parent = None, controller = None):
        super().__init__(master=parent,bg_color=GREEN_UI["green"],corner_radius=70,border_color=GREEN_UI["green"],border_width=10,fg_color=BLACK)
        self.controller = controller
    
        main_window_font = ctk.CTkFont(family=FONT,size=MAIN_WINDOW_SIZE)
        tool_font = ctk.CTkFont(family=FONT,size=MAIN_WINDOW_SIZE-31)
        by_signing_font = ctk.CTkFont(family = FONT,size=MAIN_WINDOW_SIZE-60)
        jules_hummel_singature_font = ctk.CTkFont(family=FONT_JULES_HUMMEL,size=MAIN_WINDOW_SIZE-60)
        buttons_font = ctk.CTkFont(family=FONT,size=MAIN_WINDOW_SIZE-60)
        
      


        self.kapital_string = ctk.CTkLabel(self,text="Kapital",font=main_window_font,text_color=GREEN_UI["green"]).place(relx=0.45,rely=0.10,anchor="center")
        self.tracking_string = ctk.CTkLabel(self,text="Tracking",font=main_window_font,text_color=GREEN_UI["green"]).place(relx=0.5,rely=0.23,anchor="center")
        self.signing_string_by = ctk.CTkLabel(self,text="by",font=by_signing_font,text_color=GREEN_UI["green"]).place(relx=0.39,rely=0.31,anchor="center")
        self.signing_string_jules_hummel = ctk.CTkLabel(self,text="jules hummel",font=jules_hummel_singature_font,text_color=GREEN_UI["light_green"]).place(relx=0.46,rely=0.313,anchor="center")
        self.tool_string = ctk.CTkLabel(self,text="Tool",font=tool_font,text_color=GREEN_UI["green"]).place(relx=0.59,rely=0.35,anchor="center")

        github_button = ctk.CTkButton(self,text="GitHub",width=125,height=50,corner_radius=12,font=buttons_font,fg_color=BLACK,text_color=BLACK,command=self.open_github_func,hover_color=GREEN_UI["light_green"])
        github_button.place(relx=0.35,rely=0.6)

        tracking_tool_button = ctk.CTkButton(self,text="Tracking Tool",width=125,height=50,corner_radius=12,font=buttons_font,fg_color=GREEN_UI["green"],text_color=BLACK,command=self.open_tracking_tool,hover_color=GREEN_UI["light_green"])
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
        super().__init__(master=parent,fg_color=ColorChanger.changing_color(1,1))
        self.controller = controller
        
        
       
        
        
        #LAYOUT
        self.rowconfigure(0,weight=WEIGHT_ROW_BUTTON,uniform="a")
        self.rowconfigure(1,weight=WEIGHT_ROW_SETTINGS_FRAME,uniform="a")
        self.rowconfigure(2,weight=100,uniform="a")
        self.columnconfigure(0,weight=WEIGHT_FILE_MANAGER_TAB,uniform="a")
        self.columnconfigure(1,weight=WEIGHT_SETTINGS_MANAGER_TAB,uniform="a")
        self.columnconfigure(2,weight=WEIGHT_CHART_TAB,uniform="a")
        open_arrow_image = Image.open("images/arrow_back.png").resize((60,60))
        arrow_back_image = ctk.CTkImage(light_image=open_arrow_image, dark_image=open_arrow_image)


        #---EXAMPLE---
        # ctk.CTkFrame(self,fg_color="red").grid(row=0,column=0,sticky="nsew")
        # ctk.CTkFrame(self,fg_color="blue").grid(row=0,column=1,sticky="nsew")
        # ctk.CTkFrame(self,fg_color="red").grid(row=0,column=2,sticky="nsew")

        #START END POSTIONS
        self.chart_start_pos_y =  0
        self.chart_end_pos_y = -0.93
        self.in_start_pos = True
        self.pos_chart_frame = self.chart_start_pos_y


        #entry button font
        entry_button_font =("Cascadia Mono",20)
       
        
        TabView(self,fg_color = ColorChanger.changing_color(1,2))
        ctk.CTkButton(self,fg_color= ColorChanger.changing_color(1,2),corner_radius=15,command=self.go_login_window,image=arrow_back_image,text="",hover_color=ColorChanger.changing_color(1,3)).grid(row=0,column=0,sticky="nsew",padx=4,pady=4)
        ctk.CTkButton(self,text="Entry",fg_color=ColorChanger.changing_color(1,2),command=self.animate_entry,font=entry_button_font,hover_color=ColorChanger.changing_color(1,3)).grid(row=2,column=0,sticky="nsew",padx=4,pady=4,columnspan=3)
        from __init__ import File_Import
        self1 = self
        File_Import.open_file_manager(self,self1)

        Settings_Manager(self,
                         fg_color=ColorChanger.changing_color(1,2),
                         layer="File").grid(row=1,column=1,sticky="nsew",pady=5,padx=5)      
        
        
    

    def animate_entry(self):
        if self.in_start_pos:
           self.animate_forward()
        else:
           self.animate_backwards()
           
    def animate_backwards(self):
        if self.pos_chart_frame < self.chart_start_pos_y:
            self.pos_chart_frame += 0.011
            
            self.place(relx=0,rely= self.pos_chart_frame,relwidth=1,relheight=1)
            self.after(5,self.animate_backwards)
        else: 
            self.in_start_pos = True
            

    def animate_forward(self):

        if self.pos_chart_frame > self.chart_end_pos_y:
            self.pos_chart_frame -= 0.011
          
            self.place(relx=0,rely= self.pos_chart_frame,relwidth=1,relheight=1)      
            self.after(5,self.animate_forward)
        else: 
            self.in_start_pos = False
            

  
    def go_login_window(self):
        self.controller.show_page(Login_Window)

        
    def file_button_on_click(self):
        Settings_Manager(self,layer="File",fg_color=ColorChanger.changing_color(1,2)).grid(row=1,column=1,sticky="nsew",pady=5,padx=5)      

    def calc_button_on_click(self):
        Settings_Manager(self,layer="Calculator",fg_color=ColorChanger.changing_color(1,2)).grid(row=1,column=1,sticky="nsew",pady=5,padx=5)

    def settings_button_on_click(self):
        Settings_Manager(self,layer="Settings",fg_color=ColorChanger.changing_color(1,2))

    def account_button_on_click(self):
        Settings_Manager(self,layer="Account",fg_color=ColorChanger.changing_color(1,2)).grid(row=1,column=1,sticky="nsew",pady=5,padx=5)  

        
      







       
        
        