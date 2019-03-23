import create_paths
import random

def main(four_paths,player,rolled):
    return(four_paths)

# setting variables
p0=["p0c0", "p0c1", "p0c2", "p0c3"]
p1=["p1c0", "p1c1", "p1c2", "p1c3"]
p2=["p2c0", "p2c1", "p2c2", "p2c3"]
p3=["p3c0", "p3c1", "p3c2", "p3c3"]

four_paths=create_paths.main()
player=2
rolled=6

dice_min=1
dice_max=6

p0_finished_coins_counter=0
p1_finished_coins_counter=0
p2_finished_coins_counter=0
p3_finished_coins_counter=0

if(player==0):
    coins_to_move=p0
elif(player==1):
    coins_to_move=p1
elif(player==2):
    coins_to_move=p2
else:
    coins_to_move=p3

# spawning the first player since they were the first to roll a six in main.py
path_to_move_in=four_paths[player]
first_spot=str(next(iter(path_to_move_in.keys())))
path_to_move_in[first_spot]=coins_to_move[0]


# while a player has not won
while(p0_finished_coins_counter!=4 and p1_finished_coins_counter!=4 and p2_finished_coins_counter!=4 and p3_finished_coins_counter!=4):

    path_to_move_in=four_paths[player]
    player, rolled = roll(player)

    if(rolled==6):
        # if our player's path is completely empty, we want to just spawn in one coin
        if(all(value is None for value in path_to_move_in.values())):
            first_spot=str(next(iter(path_to_move_in.keys())))
            path_to_move_in[first_spot]=coins_to_move[0]
            coins_to_move[0]=None
        # if player rolled a six and path is not empty, then we check for how many coins are on the path
        # TODO if only one, then we move that one
        # TODO if greater than 1, we let the player decided which one to move
        # TODO if greater than 1 and have option to kill, present options to console
        else:
            print("fill code here")
    else: # if player did not roll a 6
        # circling players from 0 - 3
        if player > 2:
            player=0
        else:
            player+=1
            
    # TODO must print out any killing of other player coins to the console
    
    # TODO a temporary break to the loop
    print("a player won. not really")
    p0_finished_coins_counter=4
    


print(path_to_move_in)

# we want to roll over and over again for each player and handle each player's roll result differently, depending on their board situation
def roll(player):
    roll_result=random.randint(dice_min, dice_max)
    
    return(player, roll_result)