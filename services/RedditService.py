import os
import praw

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDDIT_USERNAME = os.environ.get("REDDIT_USERNAME")
REDDIT_PASSWORD = os.environ.get("REDDIT_PASSWORD")
USER_AGENT = os.environ.get("USER_AGENT")


class RedditService:
    @staticmethod
    def reddit_api_auth():
        auth = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, password=REDDIT_PASSWORD,
                           user_agent=USER_AGENT, username=REDDIT_USERNAME)
        return auth

    def get_subreddit(self, subreddit: str):
        reddit = self.reddit_api_auth()
        return reddit.subreddit(subreddit)

    def get_subreddit_top_posts(self, subreddit: str, time: str, limit: int):
        reddit = self.reddit_api_auth()
        subreddit = reddit.subreddit(subreddit)
        return subreddit.top(time_filter=time, limit=limit)

    def get_subreddit_hot_posts(self, subreddit: str, limit: int):
        reddit = self.reddit_api_auth()
        subreddit = reddit.subreddit(subreddit)
        return subreddit.hot(limit=limit)