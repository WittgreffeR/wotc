from .values import Values, Item, Magic, MeleeWep, RangedWep
from ..file_service.service import read_file_as_list, read_file_as_classes

def initialise_values() -> Values:
    dir = "content/data"

    return Values(
        male_names=read_file_as_list(f"{dir}/names/male_names.txt"),
        female_names=read_file_as_list(f"{dir}/names/female_names.txt"),
        melee_weapons=read_file_as_classes(f"{dir}/weapons/melee.txt", MeleeWep),
        ranged_weapons=read_file_as_classes(f"{dir}/weapons/ranged.txt", RangedWep),
        magics=read_file_as_classes(f"{dir}/weapons/magic.txt", Magic),
        items=read_file_as_classes(f"{dir}/weapons/item.txt", Item)
    )
