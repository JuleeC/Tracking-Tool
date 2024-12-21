import customtkinter as ctk


from settings import Black_Preset,Pink_Preset,Green_Preset,Light_Blue_Preset

from utils.Entry_Widget import Entry_Widget_Frame
from settings import RELHEIGHT,RELWIDTH,WHITE,BLACK,APP_SIZE

global value

value = 1
class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}")
        self.resizable(False,False)
        self.title("Tracking-DDDTool")
        self.iconbitmap("images/greenbumbleinvestlogo.png")
        
        
        
        

        
       # self.creating_main_labels()
        from colorchanger import ColorChanger
        from windows import Login_Window
        self.entry_widget_var = Entry_Widget_Frame(parent=self,fg_color=ColorChanger.changing_color(value,1))
        self.active_frame = None
        self.show_page(Login_Window)
        
        
        
        self.entry_widget_var.pack(expand=True,fill="both")
        print(f"VAL:{value}")
       
    def show_page(self,page_class):
        if self.active_frame:
            self.active_frame.destroy()
        self.active_frame = page_class(parent=self,controller=self)
        self.active_frame.place(relheight=RELHEIGHT,relwidth=RELWIDTH,anchor="nw")
    
    def value_check(value):
        print(value)
#-------------------------------------------------
#ERROR TO FIX:
    def black_preset_change(self):
        self.configure(fg_color = Pink_Preset["1"])
        self.configure(title="dsa")
        self.update()


    def set_fg_color(self, color):
        self.fg_color = color  
        self.title= "dsa"  
        print("dsadASDDS")
#-------------------------------------------------
def value_ow():
    return value
        
    
   
    

if __name__ == "__main__":
   app = Main()
   app.mainloop()


#Next Tasks:

#do color presets 
#first  step (save) the color presets



#Chart Frame:
#Create it
#Style it
#Give it the data


#On File Manager(not essential):
#setting to add new tab
#also set start amount






