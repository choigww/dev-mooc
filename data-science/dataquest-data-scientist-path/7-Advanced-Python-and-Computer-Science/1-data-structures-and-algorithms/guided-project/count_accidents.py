import read

aviation_list = read.aviation_list

aviation_dict_list = read.aviation_dict_list


def concat_state(string):
    return string.split('-')[1].upper()

# count accidents using aviation_list

count_accidents = {}

for i, avl in enumerate(aviation_list[1:]):
    
    if avl[5] ==  'United States':
        try:
            state = concat_state(avl[4])
        except:
            state = 'None'

        if state in count_accidents:
            count_accidents[state] += 1
        else:
            count_accidents[state] = 1

            
count_accidents_sorted = [(k, v) for (k,v) in count_accidents.items()]
count_accidents_sorted.sort(key=lambda x: x[1], reverse=True)

print('Top 5 US States with the most aviation accidents')
print(count_accidents_sorted[:5])




