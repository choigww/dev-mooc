import pandas as pd
import read
from matplotlib import pyplot as plt

stories_df = read.load_data()

tot_upvotes_over_time = stories_df.groupby('submission_time')['upvotes_int'].sum()

print(tot_upvotes_over_time)

tot_upvotes_over_time.plot()
plt.show()
