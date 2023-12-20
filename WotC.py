from content.scripts.visual import clear, colour

from content.scripts.values.initialise_values import initialise_values

from content.scripts.char_setup import setup_player, create_opp
from content.scripts.shop.service import shop


values = initialise_values()

### GAME START ###

clear() # For some reason this has to be here in order to make text colours work on the start screen
print(f"Welcome to {colour.GOLD}War of the Champions{colour.END}, a turn-based roguelike battle game where you are a Dread Titan nurturing a prospective champion by testing their resolve against many enemies.")

player = setup_player(values)



### CORE GAMEPLAY LOOP ###

while player.health > 0:
    player = shop(player, values)

    opp = create_opp(values)

    #Do the battle
