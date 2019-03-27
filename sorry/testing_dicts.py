import create_paths
# this script checks out how to loop dictionaries and how we can use the string keys and values in movement.py

four_paths=create_paths.main()
first_path=four_paths[0]

first_spot=str(next(iter(first_path.keys())))
first_path[first_spot]="coin0"

first_path["spot_49"]="coin1"
rolled=2 

coin_count=0
coins_on_board=[]
for k, v in first_path.items():
    if v!=None:
        coin_count+=1
        coins_on_board.append(k) # keeping a list of dictionary keys with coins in them for single player
# print(coint_count)

furthest_coin_key=coins_on_board[-1]
print(furthest_coin_key)

furthest_coin_value=first_path[furthest_coin_key]
print(furthest_coin_value)



first_path[furthest_coin_key]=None # empty out the furthest spot
print(first_path[furthest_coin_key])
# str(next(iter(path_to_move_in.keys())))
