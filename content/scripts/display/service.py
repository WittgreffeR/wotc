from typing import Any, Iterable, Optional, Union

from ..visual import colour
from ..values.values import MeleeWep, RangedWep, Magic, Item

from .backend import(
    display_melee_weapon,
    display_ranged_weapon,
    display_magic,
    display_item,
    display_item_type
)


def display_boons(boons: Iterable[Any], show_favour_cost: Optional[bool] = False) -> None:
    for x in range (0,len(boons)):
        _display_boon(x, boons[x], show_favour_cost)


def _display_boon(count: int, boon: Union[MeleeWep,RangedWep,Magic,Item], show_favour_cost: bool) -> None:
    print(f"{count}. {boon.name}", end="")

    if type(boon) is MeleeWep:
        print(" (Melee Weapon)")
        display_melee_weapon(boon)

    elif type(boon) is RangedWep:
        print(" (Ranged Weapon)")
        display_ranged_weapon(boon)

    elif type(boon) is Magic:
        print(f" ({boon.type} Magic)")
        display_magic(boon)

    elif type(boon) is Item:
        print(f" ({display_item_type()})")
        display_item(boon)

    if show_favour_cost:
        print(f"\tFavour Cost: {colour.GOLD}{boon.favour_cost}{colour.END}")

    print("\n")
