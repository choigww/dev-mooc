import csv
import read

aviation_data = read.aviation_data

aviation_list = read.aviation_list

lax_code = []
for i in range(len(aviation_list)):
    row = aviation_list[i]
    if row[2] == 'LAX94LA336':
        lax_code.append(row)
        
print(lax_code)
