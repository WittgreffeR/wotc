import random
from typing import Iterable, Optional

from ..values.values import Char, Values, RangedWep, Magic
from .race_setup import char_setup_from_race


def create_opp(values: Values) -> Char:
    opp = char_setup_from_race(
        _create_opp_name(values),
        _create_opp_race()
    )

    opp.energy -= 10
    opp.energy_max -= 10

    return _assign_opp_weapons(opp, values)


def _create_opp_name(values: Values) -> str:
    if random.randint(1,3) < 3: #2/3 chance to be male
        return random.choice(values.male_names)
    else:   #1/3 chance to be female
        return random.choice(values.female_names)


def _create_opp_race() -> str:
    pick_race = random.randint(1,10)

    # This is not equal because for lore reasons you are most likely to see humans
    if pick_race in range(1,4):     #40%
        return "Human"
    elif pick_race in range(5,6):   #20%
        return "Orc"
    elif pick_race in range(7,8):   #20%
        return "Elf"
    else:                           #20%
        return "Limka"


def _assign_opp_weapons(opp: Char, values: Values) -> Char:
    opp.melee_weapon = random.choice(values.melee_weapons)
    opp.ranged_weapon = _create_opp_ranged(values)
    opp.magics = _create_opp_magics(values)

    return opp


def _create_opp_ranged(values: Values) -> Optional[RangedWep]:
    if random.randint(1,4) < 4: # There is a 1/4 chance to not have a ranged wep
        while True:
            ranged_weapon = random.choice(values.ranged_weapons)
            if not ranged_weapon.ban:
                break
        return ranged_weapon
    return


def _create_opp_magics(values: Values) -> Iterable[Magic]:
    magics = []
    for x in range(1,_roll_opp_magic_chance()):
        magics.append(_add_unique_magic(magics, values))

    return magics


def _roll_opp_magic_chance() -> int:
    #Weighted chance to generate magic; most likely to have two
    roll = random.randint(1,10)

    if roll in range(1,3):      #30%
        return 1
    elif roll in range(4,8):    #50%
        return 2
    else:                       #20%
        return 3


def _add_unique_magic(magics: Iterable, values: Values) -> Magic:
    while True:
        magic = random.choice(values.magics)

        if magic not in magics:
            break

    return magic
