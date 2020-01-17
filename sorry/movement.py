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

def set_coins(player):
    if(player==0):
        return p0
    elif(player==1):
        return p1
    elif(player==2):
        return p2
    else:
        return p3

coins_to_move=set_coins(player)


# spawning the first player since they were the first to roll a six in main.py

path_to_move_in=four_paths[player]
first_spot=str(next(iter(path_to_move_in.keys())))
path_to_move_in[first_spot]=coins_to_move[0]
print("Player {} has rolled the first 6 and spawned.".format(player))



def path_is_empty(path_to_move_in):
    if(all(value is None for value in path_to_move_in.values())):
        return True
    else:
        return False

# this function moves the furthest coin in a dictionary forward the amount passed into the first
# parameter which is called, rolled.

def move_forward(rolled, path_to_move_in):
    
    # we check how many coins are on the board
    
    coin_count=0
    coins_on_board=[]
    coin_to_move=""
    movement_counter=0

    for k, v in path_to_move_in.items():
        if v!=None:
            coin_count+=1
            # TODO use following line's list to check against possible killing of other player coins
            coins_on_board.append(k) # keeping a list of dictionary keys with coins in them for single player
    
    # TODO Allow player to choose which coin to move. 
    # Currently assuming they want to move the furthest
    # which is = to rolled+(previous)furthest coin key
    
    furthest_coin_key=coins_on_board[-1]

    for k, v in path_to_move_in.items():
        # once we finally come across the furthest coin
        # we store in coin_to_move var and empty out the dict value (v)
        if k==furthest_coin_key:
            coin_to_move=v
            path_to_move_in[k]=None
        else:
            v=v # trivial line which explains that nothing happens
        # if we already moved the coin out to be moved forward
        if path_to_move_in[furthest_coin_key]==None and movement_counter<rolled:
            movement_counter+=1
        # if we have looped around enough times to catch the rolled amount
        elif movement_counter==rolled:
            # TODO check if movement will run out of spots and then move next furthest if so
            path_to_move_in[k]=coin_to_move
            rolled=0 # breaks out of these conditionals because movement counter will never equal 0
        else:
            path_to_move_in[k]=path_to_move_in[k]
    return path_to_move_in

def roll(player):
    roll_result=random.randint(dice_min, dice_max)
    return(roll_result)

def spawn(path_to_move_in, coins_to_move):
    
    # TODO Check if this spot is empty first, to see if an option to kill exists.
    
    first_spot=str(next(iter(path_to_move_in.keys())))
    flag=0
    
    for i in range(0,4):
        if coins_to_move[i]!=None and flag==0: # checks for very first coin that is not empty in coin list for player
            path_to_move_in[first_spot]=coins_to_move[i]
            coins_to_move[i]=None # coin has moved to the board/path/dictionary
            print("Player {} has rolled a {} with an empty board and spawned.".format(player, rolled))
            flag=1 # forces conditional to only be used once.
    return path_to_move_in, coins_to_move

# we want to roll over and over again for each player and handle each player's roll result differently, depending on their board situation
# while a player has not won

loops_to_test=30

while(p0_finished_coins_counter!=loops_to_test and p1_finished_coins_counter!=loops_to_test and p2_finished_coins_counter!=loops_to_test and p3_finished_coins_counter!=loops_to_test):

    # resetting the player, amount rolled, and coins to move at the beginning of every while loop
    path_to_move_in=four_paths[player]
    rolled=roll(player)
    coins_to_move=set_coins(player)

    if(rolled==6):
        
        # if our player's path is completely empty, we want to just spawn in one coin
        
        if(path_is_empty(path_to_move_in)==True):
            path_to_move_in, coins_to_move=spawn(path_to_move_in, coins_to_move)
        
        # if player rolled a six and path is not empty
        
        else:
            print("Congrats! Player {} has rolled a 6 and already has at least one coin on the board.".format(player))
            print("Would you like to spawn a new coin? If no, your furthest coin moves ahead.")
            answer=input("Y/N: ")
            if(answer=="y" or answer=="Y"):
                path_to_move_in, coins_to_move=spawn(path_to_move_in, coins_to_move)
            elif(answer=="n" or answer=="N"):
                # move a coin - do not spawn new one
                path_to_move_in=move_forward(rolled, path_to_move_in)
        
        player=player # a trivial line to show that rolling a 6, lets the same player roll again

        # TODO must print out any killing of other player coins to the console
        # TODO if only one, then we move that one
        # TODO if greater than 1, we let the player decided which one to move
        # TODO if greater than 1 and have option to kill, present options to console
    
    
    # TODO once a player does not roll a 6, player ++ to move on to the next player
    
    else: # if player did not roll a 6
        # if the board is empty, nothing happens here
        if(path_is_empty(path_to_move_in)==True):
            print("Player {} rolled a {}, but the board is empty.".format(player, rolled))
        else: # if board is not empty and player rolled != 6
            path_to_move_in=move_forward(rolled, path_to_move_in)
            
        # circling players from 0 - 3
        if player > 2:
            player=0
        else:
            player+=1
            
    # TODO a temporary break to the loop
    
    p0_finished_coins_counter+=1


# print(four_paths[0])
# print("")
# print(four_paths[1])
# print("")
# print(four_paths[2])
# print("")
# print(four_paths[3])
