import read
from collections import Counter

data = read.load_data()
data_ = data[data['headline'].notnull()]

headlines = ' '.join(data_['headline'])
headlines = headlines.lower()\
.replace('(','')\
.replace(')','')\
.replace('?','')

head_split = headlines.split(' ')

c = Counter(head_split)
print(c.most_common(100))