import read

aviation_list = read.aviation_list

aviation_dict_list = read.aviation_dict_list


event_date_index = aviation_list[0].index('Event Date')
total_fatal_injuries_index = aviation_list[0].index('Total Fatal Injuries')
total_serious_injuries_index = aviation_list[0].index('Total Serious Injuries')

def year_and_month(string):
    split = string.split('/')
    year = split[2]
    month = split[0]
    
    return year, month

count_injuries = {}

for avl in aviation_list[1:]:
    
    try:
        year, month = year_and_month(avl[event_date_index])
    except:
        year = avl[0][:4]
        month = avl[0][4:6]
    
    #print(year, month)
    
    tot_fatal = avl[total_fatal_injuries_index]
    tot_serious = avl[total_serious_injuries_index]
    
    injuries = 0
    try:
        injuries += int(tot_fatal)
    except:
        pass
    
    try:
        injuries += int(tot_serious)
    except:
        pass
    
    # put the data into dictionary
    
    if year in count_injuries:
        count_injuries[year][month] += injuries
    
    else:
        months = ['01', '02', '03', '04', '05', '06',
                 '07', '08', '09', '10', '11', '12']
        count_injuries[year] = {i:0 for i in months}
        count_injuries[year][month] += injuries
        
print('US Aviation Accidents in 2015.08')
print(count_injuries['2015']['08'])
