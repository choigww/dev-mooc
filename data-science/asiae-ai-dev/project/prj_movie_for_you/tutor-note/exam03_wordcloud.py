#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
import matplotlib as mpl
from matplotlib import font_manager, rc

fontpath = '../malgun.ttf'
font_name = font_manager.FontProperties(
    fname=fontpath).get_name()
rc('font', family=font_name)
mpl.font_manager._rebuild()

df = pd.read_csv(
    './crawling/cleaned_movie_review_2019_3.csv')
movie_index = 6
words = df.review[movie_index].split(' ')

worddict = collections.Counter(words)
print(worddict)

stopwords = ['배우','영화','감독','출연','리뷰','보기','연출',
            '개봉']

wordcloud_img = WordCloud(
        background_color='white',
        max_words=2000,
        font_path=fontpath
        ,stopwords=stopwords
    ).generate(df.review[movie_index])


# In[57]:


plt.figure(figsize=(8,8))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.title(df.title[movie_index], size=25)
plt.show()


# In[ ]:




