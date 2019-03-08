"""
This file creates 4 dictionaries which define the paths for each of the four players.

Assuming a player is facing up, the path follows this amount of steps.
    # adding up the spots for path. It is 55 regular + 6 final
    # 5 up 
    # 1 left
    # 1 up
    # 5 left
    # 2 up
    # 5 right
    # 1 up
    # 1 right
    # 5 up
    # 2 right
    # 5 down
    # 1 right
    # 1 down
    # 5 right
    # 2 down
    # 5 left
    # 1 down
    # 1 left
    # 5 down
    # 1 left
    # 6 up
"""
def main():
    paths=[]
    for i in range(0,4):
        path={}

        # TODO you can add 14 and append to spawn_points 
        # in each i for the outer for loop
        # spawn points append spawn_points[i-1]+14
        spawn_points=[0,14,28,42]
        for i in spawn_points:
            spawn_points.append(spawn_points[i-1]+14)
            return spawn_points
        # there are 14 spots between each spawn point
        # p2: 14 - 55 then 0 - 13 then the last 6 spots for p2
        # and so on for p3 and p4.
        # adding 55 to each value in spawn_points to get a ending point before the final 6 spots
        # ex: new_list = [x+1 for x in my_list]
        ending_points=[x+55 for x in spawn_points]
        custom_range=range(spawn_points[i],ending_points[i])

        for j in custom_range:
            if i == 0 or j < 55:
                # player one needs no number manipulation
                key_j='spot_{}'.format(j)
                path[key_j]=None
            # around to 0 after reaching 55
            # players 2,3, and 4 need their path to loop back 
            elif j >= 55:
                # in order to loop back around from 54 to 0
                # here, we format the key string to use j minus
                # the last number of the first i=0 loop custom_range

                # for example, once j gets to 55 on i=1, we want the key
                # string to say 0, so we subtract 55 AKA ending_points[0] from j
                key_j='spot_{}'.format(j-ending_points[0])
                path[key_j]=None

        final_spots_range=range(0,6)
        for k in final_spots_range:
            key_k = 'p{0}_final_spot_{1}'.format(i+1,k)
            path[key_k]=None
        paths.append(path)
    return paths


        


    
