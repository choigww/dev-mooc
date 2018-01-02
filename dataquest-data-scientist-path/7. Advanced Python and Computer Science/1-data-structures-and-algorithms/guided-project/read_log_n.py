import csv
import math
import read

aviation_data = read.aviation_data

aviation_list = read.aviation_list

def format_year(string):
    return string[3:5]

upper_bound = len(aviation_list) - 1
lower_bound = 0

target = 'LAX94LA336'
guess_index = math.floor((upper_bound + lower_bound)/2)

target_year = format_year(target)
year = format_year(aviation_list[guess_index][2])

# check the direction from where to approach the target
# this value will be referenced for 2nd loop
# less -> more : 1
# more -> less : 0
direction = 0
if target_year > year:
    direction = 1

# first while loop
while (year != target_year) and (upper_bound >= lower_bound):
    
    if year > target_year:
        lower_bound += 1
    else:
        upper_bound -= 1
        
    guess_index = math.floor((upper_bound + lower_bound)/2)
    year = format_year(aviation_list[guess_index][2])
    
    
acc = aviation_list[guess_index][2]

while (year == '94') and (acc != target):
    
    if direction:
        guess_index += 1
    else:
        guess_index -= 1
    
    acc = aviation_list[guess_index][2]
    
# check the result from second loop
if acc == target:
    print('found')
    print(aviation_list[guess_index])
else:
    print(-1)
