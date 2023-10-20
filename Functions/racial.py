from Functions.visual import clear
from Functions.visual import colour

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

def race_stat_setup(guy):  #Separate function to avoid clutter - also used later for assigning racial stats for opponent
    if guy.race == "Orc":
        guy.health = 120
        guy.max_health = 120
        guy.energy = 110
        guy.max_energy = 110
        guy.arm_eff = 20
        guy.max_eff = 40

    elif guy.race == "Elf":
        guy.health = 90
        guy.max_health = 90
        guy.max_armour = 90
        guy.e_regen = 6

    elif guy.race == "Limka":
        guy.health = 80
        guy.max_health = 80
        guy.max_armour = 70
        guy.max_eff = 60
        guy.e_regen = 7
        guy.dodge = 6