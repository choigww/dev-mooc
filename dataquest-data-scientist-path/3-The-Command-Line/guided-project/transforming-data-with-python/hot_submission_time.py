import pandas as pd
import read

stories_df = read.load_data()

#print(stories_df['submission_hour'].dtype)
#print(stories_df['upvotes'].dtype)

stories_df['upvotes_int'] = stories_df['upvotes'].apply(int)

hot_submission_time = stories_df.groupby('submission_hour')['upvotes_int'].mean()

print(hot_submission_time.sort_values(ascending=False))