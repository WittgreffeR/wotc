from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class Values:
    male_names: Iterable[str]
    female_names: Iterable[str]
    melee_weapons: Iterable["MeleeWep"]
    ranged_weapons: Iterable["RangedWep"]
    magics: Iterable["Magic"]
    items: Iterable["Item"]


@dataclass
class EquipmentBase:
    name: str
    favour_cost: int


@dataclass
class Item(EquipmentBase):
    dmg: Optional[int] = None
    heal: Optional[int] = None
    energy: Optional[int] = None
    armour: Optional[int] = None
    favour_gain: Optional[int] = None
    armour_eff: Optional[int] = None


@dataclass
class Magic(EquipmentBase):
    type: str   # Types of damaging magic: plasma, shadow, plague, frost
    cost: int
    dmg: Optional[int] = None
    heal: Optional[int] = None
    armour: Optional[int] = None
    dot: Optional[int] = None
    dot_duration: Optional[int] = None


@dataclass
class WeaponBase(EquipmentBase):
    crit_chance: int
    crit_bonus: int


@dataclass
class MeleeWep(WeaponBase):
    light_dmg: int
    heavy_dmg: int
    light_cost: int
    heavy_cost: int


@dataclass
class RangedWep(WeaponBase):
    dmg: int
    cost: int
    ammo: int = 0
    max_ammo = ammo
    ban: Optional[str] = None


@dataclass
class Char:
    health: int
    max_health: int
    armour: int
    max_armour: int
    arm_eff: int    #Armour efficiency in percent
    max_eff: int    #Maximum armour efficiency
    energy: int
    max_energy: int
    energy_regen: int
    dodge: int      #Dodge chance in percent
    favour: int

    melee_weapon: MeleeWep
    ranged_weapon: RangedWep

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.magics = []
        self.items = []
