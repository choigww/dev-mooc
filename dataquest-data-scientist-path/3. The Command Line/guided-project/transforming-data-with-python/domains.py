import pandas as pd
import read

stories_df = read.load_data()

print(stories_df['url'].value_counts()[:100])