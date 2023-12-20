from ..visual import colour
from ..values.values import MeleeWep, RangedWep, Magic, Item


def display_melee_weapon(boon: MeleeWep) -> None:
    print(f"\tLight Attack Damage: {colour.RED}{boon.light_dmg}{colour.END}")
    print(f"\tLight Attack Energy Cost: {colour.BLUE}{boon.light_cost}{colour.END}")
    print(f"\tHeavy Attack Damage: {colour.RED}{boon.heavy_dmg}{colour.END}")
    print(f"\tHeavy Attack Energy Cost: {colour.BLUE}{boon.heavy_cost}{colour.END}")
    print(f"\tCritical Strike Chance: {colour.GOLD}{boon.crit_chance}%{colour.END}")
    print(f"\tCritical Damage Bonus: {colour.RED}{boon.crit_bonus}%{colour.END}")


def display_ranged_weapon(boon: RangedWep) -> None:
    print(f"\tDamage: {colour.RED}{boon.dmg}{colour.END}")
    print(f"\tEnergy Cost: {colour.BLUE}{boon.cost}{colour.END}")
    print(f"\tAmmunition: {colour.CYAN}{boon.max_ammo}{colour.END}")
    print(f"\tCritical Shot Chance: {colour.GOLD}{boon.crit_chance}%{colour.END}")
    print(f"\tCritical Damage Bonus: {colour.RED}{boon.crit_bonus}%{colour.END}")


def display_magic(boon: Magic) -> None:
    if boon.dmg:
        print(f"\tDamage: {colour.RED}{boon.dmg}{colour.END}")

    if boon.heal:
        print(f"\Healing: {colour.GREEN}{boon.heal}{colour.END}")

    if boon.armour:
        print(f"\Armour: {colour.PURPLE}{boon.armour}{colour.END}")

    if boon.dot:
        print(f"\Damage over Time: {colour.RED}{boon.dot}{colour.END}")
        print(f"\Damage over Time Duration: {colour.RED}{boon.dot_duration}{colour.END} turns")

    print(f"\tEnergy Cost: {colour.BLUE}{boon.cost}{colour.END}")


def display_item(boon: Item) -> None:
    if boon.dmg:
        print(f"\tDamage: {colour.RED}{boon.dmg}{colour.END}")

    if boon.heal:
        print(f"\Healing: {colour.GREEN}{boon.heal}{colour.END}")

    if boon.energy:
        print(f"\Energy Restored: {colour.BLUE}{boon.energy}{colour.END}")

    if boon.armour:
        print(f"\Armour: {colour.PURPLE}{boon.armour}{colour.END}")

    if boon.armour_eff:
        print(f"\Armour Efficiency Added: {colour.PURPLE}{boon.armour_eff}%{colour.END}")
    
    if boon.favour_gain:
        print(f"\Favour Gain: {colour.GOLD}{boon.favour_gain}{colour.END}")


def display_item_type(boon: Item) -> str:
    if boon.armour:
        return "Armour"
    return "Item"
