import random

from content.scripts.visual import clear, colour

from content.scripts.values.values import Char
from content.scripts.values.initialise_values import initialise_values

from content.scripts.char_setup.player_setup import setup_player


values = initialise_values()


##SHOP
def weapon_select():    #Selecting weapon for the first time
    drawn_weps = []

    #Randomly select 3 melee weapons and ensure that duplicates cannot be drawn
    while len(drawn_weps) < 3:
        select = random.choice(melee_weps)
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
            sh.pick_melee(drawn_weps[choice])
            
            input(player.name+" now wields the "+player.wep.name+". ")
            
        except:
            input("Invalid input! ")
            
        clear()

def shop(guy):
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
                select = random.choice(melee_weps)
                if select not in slots and select[0] != guy.wep.name:
                    choosing = False
                    
            elif categories[x] == "ranged":
                select = random.choice(ranged_weps)
                if select not in slots and select[0] != guy.ranged.name:
                    choosing = False

            elif categories[x] == "magic":
                select = random.choice(magic)
                if select not in slots and select[0] not in guy.magics:
                    choosing = False

            else:
                select = random.choice(item)
                if select not in slots: #You are allowed to have multiple of the same item in your inventory, but they still do not appear in the shop twice
                    choosing = False

        slots.append(select)

    repeat = True
    
    while repeat == True:
        print("DREAD SHRINE\n\nYour aspiring champion "+guy.name+" kneels before a shrine dedicated to you and humbly asks for boons.\nHere, the aspirant can exchange "+colour.GOLD+"Favour"+colour.END+" for gifts.")
        print("Four gifts are available to choose from. Choose which one to bestow upon "+guy.name+" - provided they have enough "+colour.GOLD+"Favour"+colour.END+".\n\n")

        sh.print_shop(slots, categories, True)

        try:
            print(guy.name+" currently has "+colour.GOLD+str(guy.favour)+colour.END+" Favour.")
            choice = input("Select any of the gifts above to purchase, or type \"n\" if you are done. ")

            if choice == "n":
                repeat = False
                input("Now equipped for battle, "+guy.name+" seeks out an opponent... ")
                
            else:
                choice = int(choice)
                choice -= 1

            if ((categories[choice] == "melee" and guy.favour < slots[choice][7])
                    or (categories[choice] == "ranged" and guy.favour < slots[choice][6])
                    or (categories[choice] == "magic" and guy.favour < slots[choice][6])
                    or (categories[choice] == "item" and guy.favour < slots[choice][4])):
                input(guy.name+" does not have enough "+colour.GOLD+"Favour"+colour.END+" for the "+slots[choice][0]+"! ")
            else:
                cont = sh.acquire(slots[choice],categories[choice], guy)
                if cont == True:
                    input(guy.name+" has acquired the "+slots[choice][0]+". ")
                    slots.pop(choice)
            
        except:
            input("Invalid input! ")

        clear()

###SET UP OPPONENT FOR BATTLE
#Generate basics
def create_opp():
    #Generate name - first decide whether male or female
    pick_gender = random.randint(1,3)
    
    if pick_gender < 3: #2/3 chance to be male
        opp_name = random.choice(male_names)
    else:   #1/3 chance to be female
        opp_name = random.choice(female_names)

    #Generate race
    #This is not a random 1/4 chance but rather is weighted (both for gameplay and lore reasons); you are most likely to see humans
    pick_race = random.randint(1,10)

    if pick_race in range(1,4): #40%
        opp_race = "Human"
    elif pick_race in range(5,6):  #20%
        opp_race = "Orc"
    elif pick_race in range(7,8):  #20%
        opp_race = "Elf"
    else:                       #20%
        opp_race = "Limka"

    return opp_name, opp_race

#Assign ranged weapon to opp
def generate_ranged(guy, wep):
    #3/4 chance to have a ranged weapon, 1/4 chance to not have one (function does nothing in this case)
    roll = random.randint(1,4)
    if roll < 4:
        while guy.ranged.name == "":
            pick_wep = random.choice(wep)
            if pick_wep[7] == "free":   #Only assign ranged weapon to opp if it's not banned for opps
                sh.pick_ranged(pick_wep, guy)

#Assign magic to opp
def generate_magics(guy, mag):
    #Weighted chance to generate magic; most likely to have two
    roll = random.randint(1,10)

    if roll in range(1,3):  #30%
        roll_magic = 1
    elif roll in range(4,8):    #50%
        roll_magic = 2
    else:                   #20%
        roll_magic = 3

    for x in range(1,roll_magic):   #Ensure no duplicate magic
        while True:
            pick_magic = random.choice(mag)
            if pick_magic not in guy.magics:
                break
        guy.magics.append(pick_magic)



### GAME START ###

clear() # For some reason this has to be here in order to make text colours work on the start screen
print(f"Welcome to {colour.GOLD}War of the Champions{colour.END}, a turn-based roguelike battle game where you are a Dread Titan nurturing a prospective champion by testing their resolve against many enemies.")
player_name = input("\nBefore your champion can go to battle, they must first have a name. Many champions abandon their old names and take up new ones upon swearing themselves to a Titan.\n\nWhat shall your champion be known as? ")
if len(player_name) < 3:
    print("")
    while len(player_name) < 3:
        player_name = input("Your champion's name must be at least three letters long. ")

player = setup_player(player_name)

input(f"\nAnd so, {player.name} the {player.race} enters the fray. ")
clear()

weapon_select()


### CORE GAMEPLAY LOOP ###
while player.health > 0:
    shop(player)

    #Set up opponent
    opp_name, opp_race = create_opp()
    opp = Char(opp_name, opp_race)
    r.race_stat_setup(opp)

    #Opponent max energy is always reduced by 10
    opp.max_energy -= 10
    opp.energy -= 10
    
    sh.pick_melee(random.choice(melee_weps), opp)  #Randomly choose melee weapon - this doesn't need a function
    opp.wep.crit_chance -= 1    #Critical chance for opps is always reduced by 1
    if opp.wep.crit_chance < 1: #However base crit chance can never be lower than 1%
        opp.wep.crit_chance = 1
    
    generate_ranged(opp, ranged_weps)   #Randomly choose a non-banned ranged weapon, 25% chance for no ranged

    generate_magics(opp, magic)    #Randomly generate 1-3 magic techniques

    #Do the battle
