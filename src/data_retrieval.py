from reddit_api import RedditAPI
import numpy as np
import pandas as pd
# get data
def get_data(post_url):
    try:
        reddit_api = RedditAPI(post_url)
        # get post info and comments
        post_info = reddit_api.get_post_info()
        comments_info = reddit_api.get_comments()
        #Create df
        df_post_info = pd.DataFrame(post_info, index=range(1, 2))
        index_comments = range(1, len(comments_info["body"])+1)
        df_comments_info = pd.DataFrame(comments_info, index=index_comments)
        df_post_info.to_csv('../data/post_info.csv')
        df_comments_info.to_csv('../data/comments_info.csv')
    except Exception as e:
        print(e)

    
