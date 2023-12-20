from typing import Iterable

from ..visual import clear, colour
from ..values.values import Char, Values
from ..display.service import display_boons

from .backend import set_boon_categories, set_available_boons, handle_shop_choice


def shop(player: Char, values: Values) -> Char:
    return _shop_interface(player, _generate_boons(player, values))


def _generate_boons(player: Char, values: Values) -> Iterable:
    return set_available_boons(player, values, set_boon_categories())


def _shop_interface(player: Char, boons: Iterable) -> Char:
    while True:
        print(f"DREAD SHRINE\n\nYour aspiring champion {player.name} kneels before a shrine dedicated to you and humbly asks for boons.\nHere, the aspirant can exchange {colour.GOLD}Favour{colour.END} for gifts.")
        print(f"Four gifts are available to choose from. Choose which one to bestow upon {player.name} - provided they have enough {colour.GOLD}Favour{colour.END}.\n\n")

        display_boons(boons, True)

        try:
            print(f"{player.name} currently has {colour.GOLD}{player.favour}{colour.END} Favour.")
            choice = input("Select any of the gifts above to purchase, or type \"n\" if you are done. ").lower()

            if choice == "n":
                input(f"Now equipped for battle, {player.name} seeks out an opponent... ")
                break

            else:
                player = handle_shop_choice(player, boons[int(choice)-1])

        except:
            input("Invalid input! ")
    
    return player
