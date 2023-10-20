from Functions.visual import colour

def melee(guy):
    print("\tLight Attack Damage: "+colour.RED+str(guy.wep.light_dmg)+colour.END)
    print("\tLight Attack Energy Cost: "+colour.BLUE+str(guy.wep.light_cost)+colour.END)
    print("\tHeavy Attack Damage: "+colour.RED+str(guy.wep.heavy_dmg)+colour.END)
    print("\tHeavy Attack Energy Cost: "+colour.BLUE+str(guy.wep.heavy_cost)+colour.END)
    print("\tCritical Strike Chance: "+colour.GOLD+str(guy.wep.crit_chance)+"%"+colour.END)
    print("\tCritical Damage Bonus: "+colour.RED+str(guy.wep.crit_bonus)+"%"+colour.END)

def ranged(guy):
    print("\tDamage: "+colour.RED+str(guy.ranged.dmg)+colour.END)
    print("\tEnergy Cost: "+colour.BLUE+str(guy.ranged.cost)+colour.END)
    print("\tAmmunition: "+colour.CYAN+str(guy.ranged.ammo)+colour.END+"/"+colour.CYAN+str(guy.ranged.max_ammo)+colour.END)
    print("\tCritical Shot Chance: "+colour.GOLD+str(guy.ranged.crit_chance)+"%"+colour.END)
    print("\tCritical Damage Bonus: "+colour.RED+str(guy.ranged.crit_bonus)+"%"+colour.END)

def magic_name(mage):
    if mage[1] == "plasma":
        print(" (Plasma Magic)")
    elif mage[1] == "shadow":
        print(" (Shadow Magic)")
    elif mage[1] == "plague":
        print(" (Plague Magic)")
    elif mage[1] == "frost":
        print(" (Frost Magic)")
    elif mage[1] == "heal":
        print(" (Healing Magic)")
    else:
        print(" (Shield Magic)")

def magic_stats(mage):  
    if mage[1] == "plasma" or mage[1] == "shadow" or mage[1] == "plague" or mage[1] == "frost":
        print("\tDamage: "+colour.RED+str(mage[2])+colour.END)
    elif mage[1] == "heal":
        print("\tHealing: "+colour.GREEN+str(mage[2])+colour.END)
    else:
        print("\tArmour: "+colour.PURPLE+str(mage[2])+colour.END)

    if mage[4] > 0:
        print("\tDamage over Time: "+colour.RED+str(mage[4])+colour.END)
        print("\tDamage over Time Duration: "+colour.RED+str(mage[5])+colour.END+" turns")

def item_name(thing):
    if thing[1] == "armour":
        print(" (Armour)")
    else:
        print(" (Item)")

def item_stats(thing):
    if thing[1] == "dmg":
        print("\tDamage: "+colour.RED+str(thing[2])+colour.END)
    elif thing[1] == "heal":
        print("\tHealing: "+colour.GREEN+str(thing[2])+colour.END)
    elif thing[1] == "energy":
        print("\tEnergy Restored: "+colour.BLUE+str(thing[2])+colour.END)
    elif thing[1] == "armour":
        print("\tArmour: "+colour.PURPLE+str(thing[2])+colour.END)
    else:
        print("\tFavour Gain: "+colour.GOLD+str(thing[2])+colour.END)

    if thing[3] > 0:
        print("\tArmour Efficiency Added: "+colour.PURPLE+str(thing[3])+"%"+colour.END)