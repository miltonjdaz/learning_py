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

# we want to roll over and over again for each player and handle each player's roll result differently, depending on their board situation


# while a player has not won
while(p0_finished_coins_counter!=4 and p1_finished_coins_counter!=4 and p2_finished_coins_counter!=4 and p3_finished_coins_counter!=4):

    def roll(player):
        roll_result=random.randint(dice_min, dice_max)
        return(player, roll_result)

    path_to_move_in=four_paths[player]
    player, rolled=roll(player)

    if(rolled==6):
        # if our player's path is completely empty, we want to just spawn in one coin
        if(all(value is None for value in path_to_move_in.values())):
            first_spot=str(next(iter(path_to_move_in.keys())))
            path_to_move_in[first_spot]=coins_to_move[0]
            coins_to_move[0]=None # coin has moved to the board/path/dictionary
        # if player rolled a six and path is not empty
        # then we check for how many coins are on the path
        else:
            coin_count=0
            for i in path_to_move_in.values():
                if isinstance(path_to_move_in[i], list):
                    count+=len(path_to_move_in[i])
        
        player=player # a trivial line to show that rolling a 6, lets the same player roll again

        # TODO must print out any killing of other player coins to the console
        # TODO if only one, then we move that one
        # TODO if greater than 1, we let the player decided which one to move
        # TODO if greater than 1 and have option to kill, present options to console
    
    # TODO once a player does not roll a 6, player ++ to move on to the next player
    else: # if player did not roll a 6
        # if the board is empty, nothing happens here
        if(all(value is None for value in path_to_move_in.values())):
            print("Player {} rolled a {}, but the board is empty.".format(player+1, rolled))
        else: # if board is not empty and player rolled != 6
            
            # we check how many coins are on the board
            coin_count=0
            coins_on_board=[]
            for k, v in path_to_move_in.items():
                if v!=None:
                    coin_count+=1
                    # TODO use following line's list to check against possible killing of other player coins
                    coins_on_board.append(k) # keeping a list of dictionary keys with coins in them for single player
                
            # TODO allow the player to choose which coin to move ahead
            # for now, we force player to move furthest coin disregarding eveything else
            furthest_coin_key=coins_on_board[-1]
            furthest_coin_value=path_to_move_in[furthest_coin_key]
            path_to_move_in[furthest_coin_key]=None # empty out the furthest spot

            # TODO move furthest coin value into a new furthest_coin_key 
            # which is = to rolled+(previous)furthest coin key
            # TODO using this for loop: for k, v in first_path.items()
            # we will check for when a key is equal to the furthest coin key
            # if it is, we move start a counter and once the counter = amount rolled
            # then we stick the value in this new, further long, key
            
            # we also need to check for final spots when moving forward.


        # circling players from 0 - 3
        if player > 2:
            player=0
        else:
            player+=1
            
    # TODO a temporary break to the loop
    print("a player won. not really")
    p0_finished_coins_counter+=1
    



