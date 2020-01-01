import praw


class RedditService:
    def __init__(self, client_id, client_secret, reddit_username, reddit_password, user_agent):
        self.reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, username=reddit_username,
                                  password=reddit_password, user_agent=user_agent)

    def get_subreddit(self, subreddit: str):
        return self.reddit.subreddit(subreddit)

    def get_subreddit_top_posts(self, subreddit: str, time: str, limit: int):
        subreddit = self.reddit.subreddit(subreddit)
        return subreddit.top(time_filter=time, limit=limit)

    def get_subreddit_hot_posts(self, subreddit: str, limit: int):
        subreddit = self.reddit.subreddit(subreddit)
        return subreddit.hot(limit=limit)