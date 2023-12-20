import random
from typing import Iterable, Union

from ..visual import colour, clear
from ...config.settings import MAX_MAGICS, MAX_ITEMS
from ..values.values import Char, Values, MeleeWep, RangedWep, Magic, Item
from ..display.service import display_boons
from ..display.specific import (
    display_melee_weapon,
    display_ranged_weapon,
    display_magic,
    display_item,
    display_item_type
)


def set_boon_categories() -> Iterable:
    categories = []

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
    
    return categories


def set_available_boons(player: Char, values: Values, categories: Iterable) -> Iterable:
    boons = []

    for x in range(0,4):
        while True:
            if categories[x] == "melee":
                select = random.choice(values.melee_weapons)
                if select not in boons and select != player.melee_weapon:
                    break

            elif categories[x] == "ranged":
                select = random.choice(values.ranged_weapons)
                if select not in boons and select != player.ranged_weapon:
                    break
            
            elif categories[x] == "magic":
                select = random.choice(values.magics)
                if select not in boons and select not in player.magics:
                    break
            
            elif categories[x] == "item":
                select = random.choice(values.items)
                if select not in boons and select not in player.items:
                    break
        
        boons.append(select)
    
    return boons


def handle_shop_choice(player: Char, boon: Union[MeleeWep,RangedWep,Magic,Item]) -> Char:
    if boon.favour_cost > player.favour:
        input(f"{player.cost} does not have enough {colour.GOLD}Favour{colour.END} for the {boon.name}! ")
        return player

    if type(boon) is MeleeWep:
        if _confirm_melee_replacement(player, boon):
            player.melee_weapon = boon

    elif type(boon) is RangedWep:
        if player.ranged_weapon:
            if _confirm_ranged_replacement(player, boon):
                player.ranged_weapon = boon
        else:
            player.ranged_weapon = boon
    
    elif type(boon) is Magic:
        if len(player.magics) == MAX_MAGICS:
            player.magics = _confirm_magic_replacement(player, boon)
        else:
            player.magics.append(boon)
    
    elif type(boon) is Item:
        if len(player.items) == MAX_ITEMS:
            player.items = _confirm_item_replacement(player, boon)
        else:
            player.items.append(boon)

    return player


def _confirm_melee_replacement(player: Char, boon: MeleeWep) -> bool:
    print(f"Buying the {boon.name} will replace the currently equipped {boon.name}.\nThe {player.melee_weapon.name}'s stats are listed below for comparison.\n")
    display_melee_weapon(player.melee_weapon)

    if _weapon_confirm_replace(boon.name):
        return True

    return False


def _confirm_ranged_replacement(player: Char, boon: RangedWep) -> bool:
    print(f"Buying the {boon.name} will replace the currently equipped {boon.name}.\nThe {player.ranged_weapon.name}'s stats are listed below for comparison.\n")
    display_ranged_weapon(player.ranged_weapon)

    if _weapon_confirm_replace(boon.name):
        return True

    return False


def _weapon_confirm_replace(name: str) -> bool:
    approve = input(f"\nAre you sure you want to buy the {name}? ")
    approve = approve.lower()

    if approve == "y" or approve == "yes":
        return True

    return False


def _confirm_magic_replacement(player: Char, boon: Magic) -> Iterable[Magic]:
    clear()
    print(f"{player.name} is trying to acquire a new magical technique, but they already have the maximum of {MAX_MAGICS}. One must be discarded to continue.")
    print(f"The technique {player.name} is trying to acquire is:\n")
    print(f"{boon.name} ({boon.type} Magic)")
    display_magic(boon)
    print(f"\nThe techniques {player.name} already has are:\n")
    display_boons(player.magics)

    discard = input("Choose the number of the technique to discard, or type anything else to cancel. ")
    try:
        player.magics.pop(int(discard)-1)
        player.magics.append(boon)
    except:
        pass

    return player.magics


def _confirm_item_replacement(player: Char, boon: Item) -> Iterable[Item]:
    clear()
    print(f"{player.name} is trying to acquire a new item, but they already have the maximum of {MAX_ITEMS}. One must be discarded to continue.")
    print(f"The item {player.name} is trying to acquire is:\n")
    print(f"{boon.name} ({display_item_type(boon)})")
    display_item(boon)
    print(f"\nThe items {player.name} already has are:\n")
    display_boons(player.items)

    discard = input("Choose the number of the item to discard, or type anything else to cancel. ")
    try:
        player.items.pop(int(discard)-1)
        player.items.append(boon)
    except:
        pass

    return player.items
