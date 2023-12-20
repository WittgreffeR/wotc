from dataclasses import dataclass
from typing import Any, Iterable, Optional


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
    dot: Optional[int] = None   # Damage Over Time
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
    name: str
    race: str

    health: int
    health_max: int

    # Equipment
    magics: Iterable[Any]
    items: Iterable[Any]
    melee_weapon: Optional[RangedWep] = None
    ranged_weapon: Optional[RangedWep] = None

    # Values with defaults
    armour: int = 0
    armour_max: int = 100
    armour_eff: int = 30
    armour_eff_max: int = 50
    dodge: int = 4
    favour: int = 20
    energy: int = 100
    energy_max: int = 100
    energy_regen: int = 5
