import random
import os

###TEXT VISUALS
class colour:   #Colours only display properly when run directly from the file, they bug out in shell
    GREEN = "\033[92m"      #Health and healing
    RED = "\033[91m"        #Damage
    GOLD = "\033[93m"       #Favour + Crit Chance
    BLUE = "\033[94m"       #Energy
    CYAN = "\033[96m"       #Ammunition or use limit
    PURPLE = "\033[95m"     #Armour
    END = "\033[0m"         #Stop use of colour (return to white)
    
#Colours are used like this:    "text"+colour.RED+"text"+colour.END

def clear():    #Clear the screen - only works if run directly from the file, does NOT work in python shell
    if os.name == "nt":
        _ = os.system("cls")

    else:
        _ = os.system("clear")


###READ FROM TXT FILES
my_location = os.path.dirname(__file__) #Where the script is located

#Condensing these into functions to reduce clutter
def read_from_file(relative_location): 
    with open(os.path.join(my_location,relative_location), "r") as read_file:
        export = read_file.read().split("\n")
    return export

def file_to_list(importlist, dlist, start, stop):
    for x in range (0,len(importlist)):
        join = list(importlist[x].split(","))
        for i in range (start,stop):
            join[i] = int(join[i])
        dlist.append(join)

        
male_names = read_from_file("Data/Names/MaleNames.txt")

female_names = read_from_file("Data/Names/FemaleNames.txt")

melee_weps = []
all_melee = read_from_file("Data/Weapons/Melee.txt")
file_to_list(all_melee,melee_weps,1,8)
melee_count = len(melee_weps)-1

#Melee weapon values in file:
#[name,light_dmg,heavy_dmg,light_cost,heavy_cost,crit_chance,crit_bonus,favour]


ranged_weps = []
all_ranged = read_from_file("Data/Weapons/Ranged.txt")
file_to_list(all_ranged,ranged_weps,1,7)
ranged_count = len(ranged_weps)-1

#Ranged weapon values in file:
#[name,dmg,cost,ammo,crit_chance,crit_bonus,favour]


magic = []
all_mage = read_from_file("Data/Weapons/Magic.txt")
file_to_list(all_mage,magic,2,7)
magic_count = len(magic)-1

#Magic values in file:
#[name,type,cost,dmg/heal/armour, dot, dot duration,favour]
#Types: plasma, shadow, plague, frost, heal, shield

item = []
all_item = read_from_file("Data/Weapons/Item.txt")
file_to_list(all_item,item,2,5)
item_count = len(item)-1

#Item values in file:
#[name,type,dmg/heal/energy/armour/favour gain, armour efficiency,favour]
#Types: dmg, heal, energy, armour,favour


###CHARACTER SETUP
class Char:
    health = 100
    max_health = 100
    armour = 0
    max_armour = 100
    arm_eff = 30   #Armour efficiency - how much damage armour absorbs
    max_eff = 50   #Maximum armour efficiency
    energy = 100
    max_energy = 100
    e_regen = 5    #Energy regeneration per turn
    dodge = 4      #Dodge chance
    favour = 20

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.magics = []
        self.items = []

    class wep:  #melee weapon
        name = ""
        light_dmg = 10
        heavy_dmg = 15
        light_cost = 8
        heavy_cost = 16
        crit_chance = 4
        crit_bonus = 20

    class ranged:   #ranged weapon
        name = ""
        dmg = 10
        cost = 6
        ammo = 8
        max_ammo = 8
        crit_chance = 4
        crit_bonus = 20


def choose_race():
    player_race = ""

    while player_race == "":
        clear()
        print("""As a Dread Titan, you can draw from any of the mortal races to create a new champion.\n
        """+colour.GOLD+"""Humans"""+colour.END+""" are mundane and average, but are great in numbers and are known for their tenacity and adaptability.\n
        """+colour.GOLD+"""Orcs"""+colour.END+""" are strong and hardy, but their intimidating size also makes them an easy target.\n
        """+colour.GOLD+"""Elves"""+colour.END+""" are slender and a little frail, but are blessed with magic and impressive stamina.\n
        """+colour.GOLD+"""Limkas"""+colour.END+""" are small in stature, but are agile and nimble.\n
        """)
        player_race = input("What race does your champion hail from? ")
        player_race = player_race.lower()

        if player_race == "human" or player_race == "humans" or player_race == "man" or player_race == "men" or player_race == "mankind" or player_race == "humanity":
            print("\nHumans have no special buffs or debuffs; they have 100 health, 100 energy and regenerate 5 energy per turn.")
            player_race = "Human"
            player_race = confirm_race(player_race)
            
        elif player_race == "orc" or player_race == "orcs" or player_race == "orcish":
            print("\nOrcs have a higher health of 120 and a higher energy of 110, and regenerate 5 energy per turn as normal. However, their armour efficiency is reduced by 10% and cannot go above 40%, and their starting dodge chance is reduced to 3%.")
            player_race = "Orc"
            player_race = confirm_race(player_race)

        elif player_race == "elf" or player_race == "elves" or player_race == "elvish" or player_race == "elfkin" or player_race == "elfkind":
            print("\nElves have a lower health of 90 and a lower maximum armour of 90. However, they regenerate 6 energy per turn rather than 5, and all magic costs 25% less energy to use.")
            player_race = "Elf"
            player_race = confirm_race(player_race)

        elif player_race == "limka" or player_race == "limkas" or player_race == "limkian":
            print("\nThe small Limkas have a lower health of 80 and a lower maximum armour of 70. However, they regenerate 7 stamina per turn rather than 5, their armour efficiency can go up to 60%, and they have an increased starting dodge chance of 6%.")
            player_race = "Limka"
            player_race = confirm_race(player_race)

        else:
            player_race = ""
            input("\nInput not recognised. ")

    return player_race
    

def confirm_race(race):     #Defined as a seprate function to avoid repeating myself
    confirm = input("\nAre you sure you want to continue as a "+race+"? ")
    confirm = confirm.lower()

    if confirm == "yes" or confirm == "y":
        return race
        
    else:
        race = ""
        return race

def player_stat_setup(player):  #Separate function to avoid clutter
    if player.race == "Orc":
        player.health = 120
        player.max_health = 120
        player.energy = 110
        player.max_energy = 110
        player.arm_eff = 20
        player.max_eff = 40

    elif player.race == "Elf":
        player.health = 90
        player.max_health = 90
        player.max_armour = 90
        player.e_regen = 6

    elif player.race == "Limka":
        player.health = 80
        player.max_health = 80
        player.max_armour = 70
        player.max_eff = 60
        player.e_regen = 7
        player.dodge = 6


##SHOP
def weapon_select():    #Selecting weapon for the first time
    drawn_weps = []

    #Randomly select 3 melee weapons and ensure that duplicates cannot be drawn
    while len(drawn_weps) < 3:
        select = melee_weps[random.randint(0,melee_count)]
        if select not in drawn_weps:
            drawn_weps.append(select)

    while player.wep.name == "":
        print("Before your champion spends "+colour.GOLD+"Favour"+colour.END+" to acquire boons, they must first select a starting melee weapon from three choices.\n\n")

        for x in range(0,len(drawn_weps)):
            print(str(x+1)+". "+drawn_weps[x][0])
            print("\tLight Attack Damage: "+colour.RED+str(drawn_weps[x][1])+colour.END)
            print("\tLight Attack Energy Cost: "+colour.BLUE+str(drawn_weps[x][3])+colour.END)
            print("\tHeavy Attack Damage: "+colour.RED+str(drawn_weps[x][2])+colour.END)
            print("\tHeavy Attack Energy Cost: "+colour.BLUE+str(drawn_weps[x][4])+colour.END)
            print("\tCritical Strike Chance: "+colour.GOLD+str(drawn_weps[x][5])+"%"+colour.END)
            print("\tCritical Damage Bonus: "+colour.RED+str(drawn_weps[x][6])+"%"+colour.END)
            print("\n")
            
        try:
            choice = int(input("Please choose a weapon from one of the above. "))
                         
            choice -= 1
            pick_melee(drawn_weps[choice])
            
            input(player.name+" now wields the "+player.wep.name+". ")
            
        except:
            input("Invalid input! ")
            
        clear()
        

def shop():
    categories = []
    slots = []
    
    #Randomly select stuff
    #First assemble list of categories
    while len(categories) < 4:
        roll = random.randint(1,4)
        if roll == 1:
            select = "melee"
        elif roll == 2:
            select = "ranged"
        elif roll == 3:
            select = "magic"
        else:
            select = "item"

        #Do not let there be more than two of the same type
        if categories.count(select) <= 2:
            categories.append(select)

    #Then actually pick equipment, and don't let there be duplicates or the same as what the player already has
    for x in range (0,4):
        choosing = True
        while choosing == True:
            if categories[x] == "melee":
                select = melee_weps[random.randint(0,melee_count)]
                if select not in slots and select[0] != player.wep.name:
                    choosing = False
                    
            elif categories[x] == "ranged":
                select = ranged_weps[random.randint(0,ranged_count)]
                if select not in slots and select[0] != player.ranged.name:
                    choosing = False

            elif categories[x] == "magic":
                select = magic[random.randint(0,magic_count)]
                if select not in slots and select[0] not in player.magics:
                    choosing = False

            else:
                select = item[random.randint(0,item_count)]
                if select not in slots: #You are allowed to have multiple of the same item in your inventory, but they still do not appear in the shop twice
                    choosing = False

        slots.append(select)

    repeat = True
    
    while repeat == True:
        print("DREAD SHRINE\n\nYour aspiring champion "+player.name+" kneels before a shrine dedicated to you and humbly asks for boons.\nHere, the aspirant exchanges "+colour.GOLD+"Favour"+colour.END+" for gifts.")
        print("Four gifts are available to choose from. Choose which one to bestow upon "+player.name+" - provided they have enough "+colour.GOLD+"Favour"+colour.END+".\n\n")

        print_shop(slots, categories, True)

        try:
            print(player.name+" currently has "+colour.GOLD+str(player.favour)+colour.END+" Favour.")
            choice = input("Select any of the gifts above to purchase, or type \"n\" if you are done. ")

            if choice == "n":
                repeat = False
                    
            else:
                choice = int(choice)
                choice -= 1

                if ((categories[choice] == "melee" and player.favour < slots[choice][7])
                        or (categories[choice] == "ranged" and player.favour < slots[choice][6])
                        or (categories[choice] == "magic" and player.favour < slots[choice][6])
                        or (categories[choice] == "item" and player.favour < slots[choice][4])):
                    input(player.name+" does not have enough "+colour.GOLD+"Favour"+colour.END+" for the "+slots[choice][0]+"! ")
                else:
                    cont = acquire(slots[choice],categories[choice])
                    if cont == True:
                        input(player.name+" has acquired the "+player.wep.name+". ")
                
        except:
            input("Invalid input! ")

        clear()

def acquire(slot,cat):
    #This is a little messy and repeats sometimes but it is what it is
    if cat == "melee":  #Player will always have a melee weapon, so always ask for confirmation
        input("Taking the "+slot[0]+" will replace the currently equipped "+player.wep.name+".\nThe "+player.wep.name+"'s stats are listed below for comparison.\n")
        display_melee(player)
        
        approve = input("Are you sure you want to buy the "+slot[0]+"? ")
        approve = approve.lower()
        if approve == "y" or approve == "yes":
            pick_melee(slot)
            cont = True
        else:
            cont = False
        
    elif cat == "ranged" and not player.ranged.name == "":  #Only ask for confirmation if player has a ranged weapon
        input("Taking the "+slot[0]+" will replace the currently equipped "+player.ranged.name+".\nThe "+player.ranged.name+"'s stats are listed below for comparison.\n")
        display_ranged(player)

        approve = input("Are you sure you want to buy the "+slot[0]+"? ")
        approve = approve.lower()
        if approve == "y" or approve == "yes":
            pick_ranged(slot)
            cont = True
        else:
            cont = False
    

    return cont


def pick_melee(equip):
    player.wep.name = equip[0]
    player.wep.light_dmg = equip[1]
    player.wep.heavy_dmg = equip[2]
    player.wep.light_cost = equip[3]
    player.wep.heavy_cost = equip[4]
    player.wep.crit_chance = equip[5]
    player.wep.crit_bonus = equip[6]

def pick_ranged(equip):
    player.ranged.name = equip[0]
    player.ranged.dmg = equip[1]
    player.ranged.cost = equip[2]
    player.ranged.ammo = equip[3]
    player.ranged.max_ammo = equip[3]
    player.ranged.crit_chance = equip[4]
    player.ranged.crit_bonus = equip[5]


###PRINTING FUNCTIONS
    
#Display stats of weapons
def display_melee(guy):
    print("\tLight Attack Damage: "+colour.RED+str(guy.wep.light_dmg)+colour.END)
    print("\tLight Attack Energy Cost: "+colour.BLUE+str(guy.wep.light_cost)+colour.END)
    print("\tHeavy Attack Damage: "+colour.RED+str(guy.wep.heavy_dmg)+colour.END)
    print("\tHeavy Attack Energy Cost: "+colour.BLUE+str(guy.wep.heavy_cost)+colour.END)
    print("\tCritical Strike Chance: "+colour.GOLD+str(guy.wep.crit_chance)+"%"+colour.END)
    print("\tCritical Damage Bonus: "+colour.RED+str(guy.wep.crit_bonus)+"%"+colour.END)

def display_ranged(guy):
    print("\tDamage: "+colour.RED+str(guy.ranged.dmg)+colour.END)
    print("\tEnergy Cost: "+colour.BLUE+str(guy.ranged.cost)+colour.END)
    print("\tAmmunition: "+colour.CYAN+str(guy.ranged.ammo)+colour.END+"/"+colour.CYAN+str(guy.ranged.max_ammo)+colour.END)
    print("\tCritical Shot Chance: "+colour.GOLD+str(guy.ranged.crit_chance)+"%"+colour.END)
    print("\tCritical Damage Bonus: "+colour.RED+str(guy.ranged.crit_bonus)+"%"+colour.END)

def print_shop(slots, categories, showcost):   #This can't use the display_X functions because they display from the Char class and not lists, so they're incompatible
    for x in range (0,len(slots)):
        g = 6   #the position that favour cost is stored in
        
        print(str(x+1)+". "+slots[x][0], end="")

        #Compare slots list to categories list to display information correctly
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

        #this is a long one
        elif categories[x] == "magic":
            if slots[x][1] == "plasma":
                print(" (Plasma Magic)")
            elif slots[x][1] == "shadow":
                print(" (Shadow Magic)")
            elif slots[x][1] == "plague":
                print(" (Plague Magic)")
            elif slots[x][1] == "frost":
                print(" (Frost Magic)")
            elif slots[x][1] == "heal":
                print(" (Healing Magic)")
            else:
                print(" (Shield Magic)")
                
            if slots[x][1] == "plasma" or slots[x][1] == "shadow" or slots[x][1] == "plague" or slots[x][1] == "frost":
                print("\tDamage: "+colour.RED+str(slots[x][2])+colour.END)
            elif slots[x][1] == "heal":
                print("\tHealing: "+colour.GREEN+str(slots[x][2])+colour.END)
            else:
                print("\tArmour: "+colour.PURPLE+str(slots[x][2])+colour.END)

            if slots[x][4] > 0:
                print("\tDamage over Time: "+colour.RED+str(slots[x][4])+colour.END)
                print("\tDamage over Time Duration: "+colour.RED+str(slots[x][5])+colour.END+" turns")

        #another long one
        else:
            g = 4
            if slots[x][1] == "armour":
                print(" (Armour)")
            else:
                print(" (Item)")

            if slots[x][1] == "dmg":
                print("\tDamage: "+colour.RED+str(slots[x][2])+colour.END)
            elif slots[x][1] == "heal":
                print("\tHealing: "+colour.GREEN+str(slots[x][2])+colour.END)
            elif slots[x][1] == "energy":
                print("\tEnergy Restored: "+colour.BLUE+str(slots[x][2])+colour.END)
            elif slots[x][1] == "armour":
                print("\tArmour: "+colour.PURPLE+str(slots[x][2])+colour.END)
            else:
                print("\tFavour Gain: "+colour.GOLD+str(slots[x][2])+colour.END)

            if slots[x][3] > 0:
                print("\tArmour Efficiency Added: "+colour.PURPLE+str(slots[x][3])+"%"+colour.END)

        if showcost == True:
            print("\tFavour Cost: "+colour.GOLD+str(slots[x][g])+colour.END)

        print("\n")


###GAME START
clear() #For some reason this has to be here in order to make text colours work on the start screen
print("Welcome to "+colour.GOLD+"War of the Champions"+colour.END+", a turn-based roguelike battle game where you are a Dread Titan nurturing a prospective champion by testing their resolve against many enemies.")
player_name = input("\nBefore your champion can go to battle, they must first have a name. Many champions abandon their old names and take up new ones upon swearing themselves to a Titan.\n\nWhat shall your champion be known as? ")
if len(player_name) < 3:
    print("")
    while len(player_name) < 3:
        player_name = input("Your champion's name must be at least three letters long. ")
player_race = choose_race()
player = Char(player_name,player_race)
player_stat_setup(player)
input("\nAnd so, "+player.name+" the "+player.race+" enters the fray. ")
clear()
weapon_select()
shop()
