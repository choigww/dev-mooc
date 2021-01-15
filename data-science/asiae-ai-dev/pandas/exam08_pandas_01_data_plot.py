#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import sklearn.datasets


# In[2]:


ds = sklearn.datasets.load_iris()
#print(ds)

print(ds.keys())


# In[3]:


print(ds['target_names'])
ds['target']


# In[4]:


df = pd.DataFrame(ds['data'], columns = ds['feature_names'])
df.head()


# In[5]:


# 0 : setosa, 1 : versicolor, 2 : virginica
code_species_map = dict(zip(range(3), ds['target_names']))

df['species'] = [code_species_map[c] for c in ds['target']]


# In[6]:


df.head()


# In[7]:


sums_by_species = df.groupby('species')
print(sums_by_species)


# In[8]:


# Species - target column 항목별로 instance 구분하기
# 각 항목별 DataFrame을 나누어준다.
sums_by_species = df.groupby('species')
for key, group in sums_by_species:
    print(key)
    print(type(group), group.head())


# In[ ]:





# In[9]:


# species - target column 기준으로 나눈 뒤, 각 column에 들어있는 숫자들을 합한다
sums_by_species = df.groupby('species').sum()
print(sums_by_species)

# sepal length (cm) 항목에 대해서 파이차트 생성 및 시각화
sums_by_species['sepal length (cm)'].plot(kind = 'pie', fontsize=15)
plt.ylabel('sepal length (cm)', horizontalalignment = 'right')
plt.title('Iris classified as the width of a sepal', fontsize=20)
plt.show()


# In[10]:


sums_by_species.plot(kind='pie', 
                     subplots=True, 
                     layout=(2, 2), 
                     figsize=(7, 10), 
                     legend=False)
plt.title("Total Measurements according to species, by Species")
plt.show()


# In[11]:


sums_by_species.plot(kind='bar', figsize=(10,5))
plt.title("Total Measurements according to species, by Species")
plt.show()


# In[12]:


sums_by_species.plot(kind='bar', figsize=(12,5), subplots=True, layout=(1,4))
#plt.title("Total Measurements according to species, by Species")
plt.show()


# In[13]:


# species 칼럼의 고유값에 대하여 for loop
for spec in df['species'].unique():
    
    # setosa, versicolor, virginica 각 target을 가진 instance를 dataframe으로 각각 묶어서 forspec에 저장
    forspec = df[df['species'] == spec]
    
    # forspec 데이터프레임의 petal length (cm) 칼럼에 대한 히스토그램 생성
    # alpha 설정으로 중첩내용 시각화
    forspec['petal length (cm)'].plot(kind='hist', alpha=.7, label=spec, figsize=(10,5))

# 위에서 히스토그램은 단일 canvas 위에 총 3번 그려짐

plt.legend(loc='upper right')
plt.suptitle('Histogram by petal length')
plt.show()


# In[ ]:





# In[14]:


import numpy as np
my_array = [1, 1, 1, 2, 2, 3, 3, 3, 3]
unique, count = np.unique(my_array, return_counts=True)

print('unique :', unique)
print('count :', count)
print(type(unique), type(count))


# In[15]:


np.array([1,2,3])


# In[16]:


list(set(my_array))


# In[ ]:





# In[17]:


petal_length = df['petal length (cm)']
print(type(petal_length))
print(petal_length.head())


# In[18]:


avg = petal_length.mean()
var = petal_length.var()
std = petal_length.std()
# 중위값
median = petal_length.quantile(.5)
# 1/4분위값
percentile25 = petal_length.quantile(.25)
# 3/4분위값
percentile75 = petal_length.quantile(.75)

print(avg, var, std)
print(median, percentile25, percentile75)


# In[19]:


# 1/4분위값, 3/4분위값 범위 내에서 계산한 평균값
clean_avg = petal_length[(petal_length > percentile25) & (petal_length > percentile75)].mean()
clean_avg


# In[ ]:





# In[20]:


df.describe()


# In[21]:


df.describe().T


# In[22]:


df.info()


# In[23]:


df.count()


# In[25]:


grouped = df.groupby('species')['petal length (cm)']
grouped_average = grouped.mean()
grouped_std = grouped.std()


# In[26]:


grouped_average


# In[27]:


grouped_std


# In[ ]:





# In[28]:


df.plot(kind='scatter', x='sepal length (cm)', y='sepal width (cm)')
plt.title('Length vs. Width')
plt.show()


# In[42]:


colors = ['r', 'g', 'b']
markers = ['.', '*', '^']
fig, ax = plt.subplots(1, 1)

for i, spec in enumerate(df['species'].unique()):
    ddf = df[df['species'] == spec]
    ddf.plot(kind = 'scatter',
            x = 'sepal length (cm)',
            y = 'sepal width (cm)',
            alpha = .5, s = 10*(i+1), ax=ax,
            color=colors[i], marker = markers[i],
            label=spec, figsize=(8, 4.5))

# s parameter = marker size
# alpha를 주는 이유 = 겹쳤을수록 진하게 시각화하여 구분 가능하도록

plt.legend()
plt.show()

# 판단
# setosa는 sepal length, sepal width 두 변수로도 다른 두 종류(versicolor, virginica)와 구분 가능
# 그러나 versicolor, virginica는 서로 섞여 있어서 추가적인 정보(변수) 필요함
# setosa는 뚜렷하게 sepal length - sepal width 정비례 관계를 보이고 있음


# In[ ]:





# In[46]:


from pandas.plotting import scatter_matrix
ds = sklearn.datasets.load_iris()
df2 = pd.DataFrame(ds['data'], columns = ds['feature_names'])
df2.head()

scatter_matrix(df,
               c = ds.target,
              figsize = (10, 10))
plt.show()

# 대각성분 상에 위치하는 히스토그램 = 각 변수값들의 빈도수 나타내는 히스토그램
# 대각선을 기준으로, 대각선 위 - 대각선 아래 스캐터플롯은 x, y축 대칭으로 둘 중 하나만 보면 됨.


# In[48]:


# 히트맵 - 색상의 진함으로 스캐터플롯 + 히스토그램 정보(빈도수)를 같이 전달

df.plot(kind = 'hexbin',
       x = 'sepal width (cm)',
       y = 'sepal length (cm)',
       figsize = (10, 10))


# In[ ]:





# In[ ]:





# In[ ]:




