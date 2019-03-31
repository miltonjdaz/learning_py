import create_paths
# this script checks out how to loop dictionaries and how we can use the string keys and values in movement.py

four_paths=create_paths.main()
path_to_move_in=four_paths[0]

first_spot=str(next(iter(path_to_move_in.keys())))
path_to_move_in[first_spot]="coin0"

path_to_move_in["spot_49"]="coin1"
rolled=6

coin_count=0
coins_on_board=[]
for k, v in path_to_move_in.items():
    if v!=None:
        coin_count+=1
        coins_on_board.append(k) # keeping a list of dictionary keys with coins in them for single player
# print(coint_count)

furthest_coin_key=coins_on_board[-1]
coin_to_move=""
movement_counter=0
for k, v in path_to_move_in.items():
	# once we finally come across the furthest coin
	# we store in coin_to_move var and empty out the dict value (v)
	if k==furthest_coin_key:
		print(k, v)
		coin_to_move=v
		path_to_move_in[k]=None
	else:
		v=v # trivial line which explains that nothing happens
	# if we already moved the coin out to be moved forward
	if path_to_move_in[furthest_coin_key]==None and movement_counter<rolled:
		movement_counter+=1
		print(movement_counter)
	# if we have looped around enough times to catch the rolled amount
	elif movement_counter==rolled:
		path_to_move_in[k]=coin_to_move
		rolled=0 # breaks out of these conditionals because movement counter will never equal 0
	else:
		path_to_move_in[k]=path_to_move_in[k]
print(path_to_move_in)


# this function should be working correctly
path_to_move_in=four_paths[1]
def path_is_empty(path_to_move_in):
    if(all(value is None for value in path_to_move_in.values())):
        return True
    else:
        return False

print(path_is_empty(path_to_move_in))