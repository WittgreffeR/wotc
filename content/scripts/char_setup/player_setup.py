import random
from typing import Iterable

from ..visual import colour, clear

from ..values.values import Char, Values, MeleeWep
from .race_setup import char_setup_from_race
from ..shop.display import display_melee_weapon


def setup_player(values: Values) -> Char:
    player = char_setup_from_race(_set_name_dialog(), _choose_race_dialog())

    input(f"\nAnd so, {player.name} the {player.race} enters the fray. ")
    clear()

    return _select_first_melee_weapon(player, values)


def _set_name_dialog() -> str:
    player_name = input("\nBefore your champion can go to battle, they must first have a name. Many champions abandon their old names and take up new ones upon swearing themselves to a Titan.\n\nWhat shall your champion be known as? ")

    if len(player_name) < 3:
        print("")
        while len(player_name) < 3:
            player_name = input("Your champion's name must be at least three letters long. ")

    return player_name


def _choose_race_dialog() -> str:
    player_race = ""

    while player_race == "":
        clear()
        print(f"""As a Dread Titan, you can draw from any of the mortal races to create a new champion.\n
        {colour.GOLD}Humans{colour.END} are mundane and average, but are great in numbers and are known for their tenacity and adaptability.\n
        {colour.GOLD}Orcs{colour.END} are strong and hardy, but their intimidating size also makes them an easy target.\n
        {colour.GOLD}Elves{colour.END} are slender and a little frail, but are blessed with magic and impressive stamina.\n
        {colour.GOLD}Limkas{colour.END} are small in stature, but are agile and nimble.\n
        """)
        player_race = input("What race does your champion hail from? ")
        player_race = player_race.lower()

        if player_race == "human" or player_race == "humans" or player_race == "man" or player_race == "men" or player_race == "mankind" or player_race == "humanity":
            print("\nHumans have no special buffs or debuffs; they have 100 health, 100 energy and regenerate 5 energy per turn.")
            player_race = "Human"
            player_race = _confirm_race(player_race)
            
        elif player_race == "orc" or player_race == "orcs" or player_race == "orcish":
            print("\nOrcs have a higher health of 120 and a higher energy of 110, and regenerate 5 energy per turn as normal. However, their armour efficiency is reduced by 10% and cannot go above 40%, and their starting dodge chance is reduced to 3%.")
            player_race = "Orc"
            player_race = _confirm_race(player_race)

        elif player_race == "elf" or player_race == "elves" or player_race == "elvish" or player_race == "elfkin" or player_race == "elfkind":
            print("\nElves have a lower health of 90 and a lower maximum armour of 90. However, they regenerate 6 energy per turn rather than 5, and all magic costs 25% less energy to use.")
            player_race = "Elf"
            player_race = _confirm_race(player_race)

        elif player_race == "limka" or player_race == "limkas" or player_race == "limkian":
            print("\nThe small Limkas have a lower health of 80 and a lower maximum armour of 70. However, they regenerate 7 stamina per turn rather than 5, their armour efficiency can go up to 60%, and they have an increased starting dodge chance of 6%.")
            player_race = "Limka"
            player_race = _confirm_race(player_race)

        else:
            player_race = ""
            input("\nInput not recognised. ")

    return player_race


def _confirm_race(race: str) -> str:
    confirm = input(f"\nAre you sure you want to continue as a {race}? ")
    confirm = confirm.lower()

    if confirm == "yes" or confirm == "y":
        return race
        
    else:
        return ""


def _select_first_melee_weapon(player: Char, values: Values) -> Char:
    drawn_weps = _draw_first_melee_weapons(values)

    while not player.melee_weapon:
        print(f"Before your champion spends {colour.GOLD}Favour{colour.END} to acquire boons, they must first select a starting melee weapon from three choices.\n\n")

        for wep in range(0,len(drawn_weps)):
            _print_out_weapon_stats(wep, drawn_weps[wep])

        try:
            choice = int(input("Please choose a weapon from one of the above. "))

            player.melee_weapon = drawn_weps[choice-1]

            input(f"{player.name} now wields the {player.melee_weapon.name}. ")

        except:
            input("Invalid input! ")

        clear()

    return player


def _draw_first_melee_weapons(values: Values) -> Iterable["MeleeWep"]:
    drawn_weps = []

    while len(drawn_weps) < 3:
        select = random.choice(values.melee_weapons)
        if select not in drawn_weps:
            drawn_weps.append(select)
    
    return drawn_weps


def _print_out_weapon_stats(wep: int, weapon: MeleeWep) -> None:
    print(f"{wep+1}. {weapon.name}")
    display_melee_weapon(weapon)
    print("\n")
