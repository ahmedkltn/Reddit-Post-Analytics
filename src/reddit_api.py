# Importing libraries :
import praw


class RedditAPI:
    # init
    def __init__(self, post_url):
        user_agent = 'PostAnalytics'
        self.reddit = praw.Reddit(user_agent=user_agent)
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
