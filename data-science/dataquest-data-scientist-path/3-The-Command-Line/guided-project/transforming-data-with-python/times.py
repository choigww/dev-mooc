from dateutil.parser import parse as dateparser
import read

stories_df = read.load_data()

stories_df['submission_hour'] = stories_df['submission_time'].apply(dateparser)\
.apply(lambda x: x.hour)

print(stories_df['submission_hour'].value_counts)