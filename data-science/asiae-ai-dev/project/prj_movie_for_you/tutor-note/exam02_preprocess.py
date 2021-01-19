import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('./crawling/movie_review_2019_3.csv',index_col=0)
stopwords = pd.read_csv('../datasets/stopwords.csv', index_col=0)
stopwords = list(stopwords.stopword)
temp_stopwords = ['배우','영화','감독','출연',
                  '리뷰','보기','연출','개봉']
stopwords += temp_stopwords
okt = Okt()
cleaned_sentences = []
for sentence in df.review:
    print('.',end='')
    sentence = re.sub('[^가-힣]', ' ', sentence)
    token = okt.pos(sentence)
    df_token = pd.DataFrame(token, columns=['word', 'class'])
    df_cleaned_token = df_token[(df_token['class'] == 'Noun') |
                                (df_token['class'] == 'Verb') |
                                (df_token['class'] == 'Adjective')]

    words = []
    for word in df_cleaned_token['word']:
        if len(word) > 1:
            if word not in stopwords:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
df['cleaned_review'] = cleaned_sentences
print(df.head())
df = df[['title', 'cleaned_review']]


one_sentences = []
for title in df['title'].unique():
    temp = df[df['title']==title]['cleaned_review']
    if len(temp) > 100:
        temp = temp[:100]
    one_sentence = ' '.join(list(temp))
    one_sentences.append(one_sentence)
df_one_sentences = pd.DataFrame({'title':df['title'].unique(), 'review':one_sentences})
print(df_one_sentences.head())
print(df_one_sentences.info())

df_one_sentences.to_csv('./crawling/cleaned_movie_review_2019_3.csv')


