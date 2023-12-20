import random

from content.scripts.visual import clear, colour

from content.scripts.values.values import Char
from content.scripts.values.initialise_values import initialise_values

from content.scripts.char_setup import setup_player, create_opp


values = initialise_values()


##SHOP
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



### GAME START ###

clear() # For some reason this has to be here in order to make text colours work on the start screen
print(f"Welcome to {colour.GOLD}War of the Champions{colour.END}, a turn-based roguelike battle game where you are a Dread Titan nurturing a prospective champion by testing their resolve against many enemies.")

player = setup_player(values)


### CORE GAMEPLAY LOOP ###

while player.health > 0:
    player = shop(player, values)

    opp = create_opp(values)
    
    sh.pick_melee(random.choice(melee_weps), opp)  #Randomly choose melee weapon - this doesn't need a function
    opp.wep.crit_chance -= 1    #Critical chance for opps is always reduced by 1
    if opp.wep.crit_chance < 1: #However base crit chance can never be lower than 1%
        opp.wep.crit_chance = 1

    generate_ranged(opp, ranged_weps)   #Randomly choose a non-banned ranged weapon, 25% chance for no ranged

    generate_magics(opp, magic)    #Randomly generate 1-3 magic techniques

    #Do the battle
