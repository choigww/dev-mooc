import pandas as pd
from dateutil.parser import parse as dateparser

def load_data():
    stories = pd.read_csv('hn_stories.csv')
    stories.columns = ['submission_time', 'upvotes', 'url', 'headline']
    
    stories['submission_time'] = stories['submission_time'].apply(dateparser)
    
    stories['submission_hour'] = stories['submission_time'].apply(lambda x: x.hour)

    stories['upvotes_int'] = stories['upvotes'].apply(int)

    return stories