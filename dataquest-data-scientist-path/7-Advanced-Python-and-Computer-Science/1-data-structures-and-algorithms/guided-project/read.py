import pandas as pd
import csv

f = open('AviationData.txt', 'r',encoding='utf-8')

reader = csv.reader(f)

aviation_data = []
for line in reader:
    
    summed = ''
    for l in line:
        summed += l.replace(',','')
        summed += '-'
        
    aviation_data.append([summed])
    
aviation_list = []
for i, av in enumerate(aviation_data):
    #print(i)
    if i != 0:
        split = av[0].split(' | ')
        aviation_list.append(split[:-1])
    
    else:
        aviation_list.append(av[0].split(' | ')[:-1])


lax_code = []
for avl in aviation_list:
    for avl_component in avl:
        if avl_component == 'LAX94LA336':
            lax_code.append(avl)
                         

aviation_dict_list = []
colnames = []

for i, av_line in enumerate(aviation_list):
    split = av_line
    if i != 0:
        row_dict = {k:v for (k,v) in zip(colnames, split)}
        aviation_dict_list.append(row_dict)
        
    else:
        colnames = av_line