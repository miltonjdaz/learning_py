import random

p1 = ["c1", "c2", "c3", "c4"]
p2 = ["c1", "c2", "c3", "c4"]
p3 = ["c1", "c2", "c3", "c4"]
p4 = ["c1", "c2", "c3", "c4"]

dice_min = 1
dice_max = 6

roll_result = random.randint(dice_min, dice_max)

"""
res = {}
for j in xrange(10):
    key_j = 'key_{}'.format(j)  # a string depending on j
    res[key_j] = j**2
"""

# TODO create paths for all players
# while loop. While the counter is < 55, starting from 0, add up the index
while: 

# p2: 14 - 55 then 0 - 13 then p2final path
# and so on for p3 and p4.
pathcounter = 55


# adding up the spots for path. It is 55 regular + 6 final
p1_path = {}

# these are regular path
for i in range(0,55): 
    key_i = 'spot_{}'.format(i)
    p1_path[key_i]=None
    print(key_i)

for i in range(0,7):
    key_i = 'p1_final_spot_{}'.format(i)
    p1_path[key_i]=None #f for final. f1 for final1
    print(key_i)
print(p1_path)

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



# TODO print out board from data structures

# TODO create movement method which depends on dice rolls

# TODO 