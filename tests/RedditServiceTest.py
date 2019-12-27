import unittest
from services.RedditService import RedditService


class RedditServiceTest(unittest.TestCase):
    def setUp(self):
        self.reddit_service = RedditService()

    def testRedditConnection(self):
        reddit = self.reddit_service.reddit_api_auth()
        self.assertIsNotNone(reddit)

    def testGetSubreddit(self):
        python_subreddit = self.reddit_service.get_subreddit("python")
        self.assertIsNotNone(python_subreddit)

    def testGetSubredditTopPosts(self):
        top_posts = self.reddit_service.get_subreddit_top_posts("python", "all", 5)
        self.assertIsNotNone(top_posts)

    def testGetSubredditHotPosts(self):
        hot_posts = self.reddit_service.get_subreddit_hot_posts("python", 5)
        self.assertIsNotNone(hot_posts)
