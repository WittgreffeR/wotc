import os

def clear():    #Clear the screen - only works if run directly from the file, does NOT work in python shell
    if os.name == "nt":
        _ = os.system("cls")

    else:
        _ = os.system("clear")

class colour:   #Colours only display properly when run directly from the file, they bug out in shell
    GREEN = "\033[92m"      #Health and healing
    RED = "\033[91m"        #Damage
    GOLD = "\033[93m"       #Favour + Crit Chance
    BLUE = "\033[94m"       #Energy
    CYAN = "\033[96m"       #Ammunition or use limit
    PURPLE = "\033[95m"     #Armour
    END = "\033[0m"         #Stop use of colour (return to white)
    
#Colours are used like this:    "text"+colour.RED+"text"+colour.END
