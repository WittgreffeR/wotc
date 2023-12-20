from ..values.values import Char


def char_setup_from_race(name: str, race: str) -> Char:
    if race == "Human":
        return Char(
            name=name,
            race=race,
            magics=[],
            items=[],
            health=100,
            health_max=100,
        )
    elif race == "Orc":
        return Char(
            name=name,
            race=race,
            magics=[],
            items=[],
            health=120,
            health_max=120,
            energy=110,
            energy_max=110,
            armour_eff=20,
            armour_eff_max=40,
        )
    elif race == "Elf":
        return Char(
            name=name,
            race=race,
            magics=[],
            items=[],
            health=90,
            health_max=90,
            armour_max=90,
            energy_regen=6,
        )
    elif race == "Limka":
        return Char(
            name=name,
            race=race,
            magics=[],
            items=[],
            health=80,
            health_max=80,
            armour_max=70,
            armour_eff_max=60,
            energy_regen=7,
            dodge=6,
        )
    else:
        raise RuntimeError("Invalid race given to race_stat_setup function")