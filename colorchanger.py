from settings import *

class ColorChanger():
    def __init__(self):
        pass
        
    def changing_color(value,layout_format):
        match(value):
            case 1:
                match(layout_format):
                    case 1:
                        return Black_Preset["1"]
                    case 2:
                        return Black_Preset["2"]
                    case 3:
                        return Black_Preset["3"]
                    case 4: 
                        return Black_Preset["4"]
            case 2:
                match(layout_format):
                    case 1:
                        return Green_Preset["1"]
                    case 2:
                        return Green_Preset["2"]
                    case 3:
                        return Green_Preset["3"]
                    case 4: 
                        return Green_Preset["4"]
            case 3:
                match(layout_format):
                    case 1:
                        return Light_Blue_Preset["1"]
                    case 2:
                        return Light_Blue_Preset["2"]
                    case 3:
                        return Light_Blue_Preset["3"]
                    case 4: 
                        return Light_Blue_Preset["4"]
            case 4:
                match(layout_format):
                    case 1:
                        return Pink_Preset["1"]
                    case 2:
                        return Pink_Preset["2"]
                    case 3:
                        return Pink_Preset["3"]
                    case 4: 
                        return Pink_Preset["4"]