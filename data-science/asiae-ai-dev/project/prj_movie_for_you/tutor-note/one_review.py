import pandas as pd

df = pd.read_csv('./crawling/cleaned_movie_review_2019_3.csv', index_col=0)
df.columns = ['title', 'review']
df.to_csv('./crawling/cleaned_movie_review_2019_3.csv')
print(df.columns)
