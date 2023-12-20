import Functions.display as display
from content.scripts.visual import colour, clear

def acquire(slot,cat,guy):
    if cat == "melee":  #Player will always have a melee weapon, so always ask for confirmation
        print("Taking the "+slot[0]+" will replace the currently equipped "+guy.wep.name+".\nThe "+guy.wep.name+"'s stats are listed below for comparison.\n")
        display.melee(guy)
        
        approve = input("\nAre you sure you want to buy the "+slot[0]+"? ")
        approve = approve.lower()
        if approve == "y" or approve == "yes":
            pick_melee(slot, guy)
            cont = True
        else:
            cont = False

    elif cat == "ranged" and not guy.ranged.name == "":  #Only ask for confirmation if player has a ranged weapon
        print("Taking the "+slot[0]+" will replace the currently equipped "+guy.ranged.name+".\nThe "+guy.ranged.name+"'s stats are listed below for comparison.\n")
        display.ranged(guy)

        approve = input("\nAre you sure you want to buy the "+slot[0]+"? ")
        approve = approve.lower()
        if approve == "y" or approve == "yes":
            pick_ranged(slot, guy)
            cont = True
        else:
            cont = False
    
    elif cat == "magic" and len(guy.magics) == 3:    #Only ask for confirmation if player is at maximum 3 magics
        clear() #This confirmation takes up a lot of space, so clear the screen and enter a "new window"
        print(guy.name+" is trying to acquire a new magical technique, but they already have the maximum of three. One must be discarded to continue.")
        print("The technique "+guy.name+" is trying to acquire is:\n")
        print(slot[0], end="")
        display.magic_name(slot)
        display.magic_stats(slot)
        print("\nThe techniques "+guy.name+"already has are:\n")

        for x in range(0,len(guy.magics)):
            print(str(x+1)+". "+guy.magics[x][0], end="")
            display.magic_name(guy.magics[x])
            display.magic_stats(guy.magics[x])
            print("")
        
        approve = input("Choose the number of the technique to discard, or type anything else to cancel. ")
        try:
            approve = int(approve)
            approve -= 1
            guy.magics.pop(approve)
            guy.magics.append(slot)
            cont = True
        except:
            cont = False

    elif cat == "item" and len(guy.items) == 5:  #Only ask for confirmation if player is at maximum 5 items
        clear() #This confirmation takes up a lot of space, so clear the screen and enter a "new window"
        print(guy.name+" is trying to acquire a new item, but they already have the maximum of five. One must be discarded to continue.")
        print("The item "+guy.name+" is trying to acquire is:\n")
        print(slot[0], end="")
        display.item_name(slot)
        display.item_stats(slot)
        print("\nThe items "+guy.name+"already has are:\n")

        for x in range(0,len(guy.items)):
            print(str(x+1)+". "+guy.items[x][0], end="")
            display.item_name(guy.items[x])
            display.item_stats(guy.items[x])
            print("")
        
        approve = input("Choose the number of the item to discard, or type anything else to cancel. ")
        try:
            approve = int(approve)
            approve -= 1
            guy.items.pop(approve)
            guy.items.append(slot)
            cont = True
        except:
            cont = False
            
    else:   #If there is nothing to confirm then go right ahead
        cont = True

    return cont


def pick_melee(equip, guy):
    guy.wep.name = equip[0]
    guy.wep.light_dmg = equip[1]
    guy.wep.heavy_dmg = equip[2]
    guy.wep.light_cost = equip[3]
    guy.wep.heavy_cost = equip[4]
    guy.wep.crit_chance = equip[5]
    guy.wep.crit_bonus = equip[6]

def pick_ranged(equip, guy):
    guy.ranged.name = equip[0]
    guy.ranged.dmg = equip[1]
    guy.ranged.cost = equip[2]
    guy.ranged.ammo = equip[3]
    guy.ranged.max_ammo = equip[3]
    guy.ranged.crit_chance = equip[4]
    guy.ranged.crit_bonus = equip[5]


#Print out things available in shop
def print_shop(slots, categories, showcost):
    for x in range (0,len(slots)):
        g = 6   #the list position that favour cost is stored in
        
        print(str(x+1)+". "+slots[x][0], end="")

        #Compare slots list to categories list to display information correctly
        #Both melee and ranged display functions take variables from Char class and not list so they cant be used here
        if categories[x] == "melee":
            g = 7
            print(" (Melee Weapon)")
            print("\tLight Attack Damage: "+colour.RED+str(slots[x][1])+colour.END)
            print("\tLight Attack Energy Cost: "+colour.BLUE+str(slots[x][3])+colour.END)
            print("\tHeavy Attack Damage: "+colour.RED+str(slots[x][2])+colour.END)
            print("\tHeavy Attack Energy Cost: "+colour.BLUE+str(slots[x][4])+colour.END)
            print("\tCritical Strike Chance: "+colour.GOLD+str(slots[x][5])+"%"+colour.END)
            print("\tCritical Damage Bonus: "+colour.RED+str(slots[x][6])+"%"+colour.END)
            
        elif categories[x] == "ranged":
            print(" (Ranged Weapon)")
            print("\tDamage: "+colour.RED+str(slots[x][1])+colour.END)
            print("\tEnergy Cost: "+colour.BLUE+str(slots[x][2])+colour.END)
            print("\tAmmunition: "+colour.CYAN+str(slots[x][3])+colour.END)
            print("\tCritical Shot Chance: "+colour.GOLD+str(slots[x][4])+"%"+colour.END)
            print("\tCritical Damage Bonus: "+colour.RED+str(slots[x][5])+"%"+colour.END)

        #this can be done through functions
        elif categories[x] == "magic":
            display.magic_name(slots[x])
            display.magic_stats(slots[x])

        #so can this
        else:
            g = 4
            display.item_name(slots[x])
            display.item_stats(slots[x])

        if showcost == True:
            print("\tFavour Cost: "+colour.GOLD+str(slots[x][g])+colour.END)

        print("\n")
