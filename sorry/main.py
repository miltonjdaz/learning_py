import random
import create_paths
import movement

dice_min=1
dice_max=6

starting_roller=random.randint(0, 3)

# this function rolls a die until a player rolls a six. 
# It returns that player as an integer between [0,3]

def first_six(starting_roller):
    player_counter = starting_roller
    roll_result = random.randint(dice_min, dice_max)
    
    # if this roll is not 6, we roll until it is a 6 and keep track of the player rolling each time with player_counter
    
    while roll_result != 6:
        # uncomment following two lines to see every roll
        print("Player {0} rolls a {1}.".format(player_counter+1,roll_result))
        print("So next player rolls.")
        roll_result=random.randint(dice_min, dice_max)
        if player_counter > 2:
            player_counter=0
        else:
            player_counter+=1
    return player_counter

# this method returns a list of player turn orders

def get_turn_order(counter):
    player_list_ordered=[]
    for i in range(0,4):
        if counter > 2:
            player_list_ordered.append(3)
            counter=0
        else:
            player_list_ordered.append(counter)
            counter+=1
    return player_list_ordered

# storing the first player as an int 

first_player=first_six(starting_roller) # first roller to get six

# getting a list of the order of turns by player

turn_order=get_turn_order(first_player)
print("")
print("Because player {} rolled the first six, the order of turns will be: ".format(first_player+1))
turn_order_1based=[x+1 for x in turn_order]
print(turn_order_1based)

# Roll dice until the first player spawns. 

first_spawn=first_six(first_player)
print("")
print("Within this order of turns, the first one to roll a six and spawn, is player {}.".format(first_spawn+1))


pathlist=create_paths.main() # four empty dicts the first time this is called

pathlist=movement.main(pathlist,first_spawn,6)
print("")
print(pathlist[first_spawn])




# ex: if first_six() returns 0 then pathlist[0] is the dictionary you want to populate their first spot with p1[0] in the value spot. Not the key.


# TODO Roll dice until everyone spawns. 

# Move previously spawned coins across dictionaries while remaining players are rolling die for spawn


# to see player 4 path:


# TODO print out board from data structures

# TODO create movement method which depends on dice rolls

# TODO 

# Everytime a new position is taken by a coin, we can check the other three dictionaries values for the same position key.
# If there is a coin there, it gets knocked out of the game.
# After adding that logic, we have to also add options like: 
# You have two coins, moving the first one will kill p2's coin, do you wish to move it or move your other coin