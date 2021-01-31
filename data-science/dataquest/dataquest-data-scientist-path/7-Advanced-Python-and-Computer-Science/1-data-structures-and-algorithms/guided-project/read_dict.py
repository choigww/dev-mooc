import csv
import read

aviation_data = read.aviation_data

aviation_list = read.aviation_list

aviation_dict_list = []
colnames = []

for i, av_line in enumerate(aviation_data):
    split = av_line[0].split(' | ')
    if i != 0:
        row_dict = {k:v for (k,v) in zip(colnames, split)}
        aviation_dict_list.append(row_dict)
        
    else:
        colnames = av_line[0].split(' | ')

lax_dict = []

for av_dict in aviation_dict_list:
    
    if av_dict['Accident Number'] == 'LAX94LA336':
        lax_dict.append(av_dict)
        
print(lax_dict)     