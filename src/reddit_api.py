# Importing libraries :
import praw
import json
import datetime
class RedditAPI:
    # init
    def __init__(self, post_url):
        user_agent = 'PostAnalytics'
        credentials_file = 'credentials.json'
        with open(credentials_file) as file :
            credentials = json.load(file)
        client_id = credentials['client_id']
        client_secret = credentials['client_secret'] 
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret = client_secret,
            user_agent=user_agent)
        self.post_url = post_url

    # connect to post
    def _connect_post(self):
        try:
            # connect to the post
            self.submission = self.reddit.submission(url=self.post_url)
            # return true if connected
            return True
        # return error if an error occured
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return False

    # get post info
    def get_post_info(self):
        if self._connect_post():
            # Get post info
            post_info = {
                'Title': self.submission.title,
                'Author': str(self.submission.author),
                'Score': self.submission.score,
                'Number of comments ': self.submission.num_comments,
                'URL': self.submission.url
            }
            # return post info
            return post_info
        else:
            print("Failed to connect to the post !")
            return None
    # get comments
    def get_comments(self,is_get_replies = False):
        if self._connect_post():
            # Dict to save comments
            data_comments = dict(body=[],score=[],created=[])
            # if is_get_replies = True then get all replies
            if is_get_replies : 
                limit = None
            else:
                limit = 0
            # Retrieve the comments
            self.submission.comments.replace_more(limit=limit)
            comments = self.submission.comments.list()
            for comment in comments :
                # save comments
                data_comments['body'].append(comment.body)
                data_comments['score'].append(comment.score)
                # convert unix timestamp in seconds to strftime format
                dt_object = datetime.datetime.fromtimestamp(comment.created)
                data_comments['created'].append(dt_object.strftime("%Y-%m-%d %H: %M: %S"))
            # return comments
            return data_comments
        else:
            print("Failed to connect to the post !")
            return None

