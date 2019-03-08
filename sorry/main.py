import random
import create_paths

p1 = ["c1", "c2", "c3", "c4"]
p2 = ["c1", "c2", "c3", "c4"]
p3 = ["c1", "c2", "c3", "c4"]
p4 = ["c1", "c2", "c3", "c4"]

dice_min=1
dice_max=6

roll_result=random.randint(dice_min, dice_max)

# this returns 4 dictionaries for 4 player paths from another file
pathlist=create_paths.main()

# to see player 4 path:
print(pathlist[3])
# TODO print out board from data structures

# TODO create movement method which depends on dice rolls

# TODO 

# Everytime a new position is taken by a coin, we can check the other three dictionaries values for the same position key.
# If there is a coin there, it gets knocked out of the game.
# After adding that logic, we have to also add options like: 
# You have two coins, moving the first one will kill p2's coin, do you wish to move it or move your other coin