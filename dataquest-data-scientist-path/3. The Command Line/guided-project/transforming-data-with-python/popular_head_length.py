import pandas as pd
import read

stories_df = read.load_data()

stories_df['head_len'] = stories_df['headline'].apply(lambda x: len(str(x)))

#print(stories_df[['headline','head_len']].iloc[:5])

stories_sorted_upvote = stories_df.sort_values(by='upvotes', ascending=False)

print(stories_sorted_upvote['head_len'][:10]\
      .value_counts())