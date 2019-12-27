import unittest
from services.TwitterService import TwitterService


class TwitterServiceTest(unittest.TestCase):
    def setUp(self):
        self.twitter_service = TwitterService()

    def testTwitterConnection(self):
        twitter = self.twitter_service.twitter_api_auth()
        self.assertIsNotNone(twitter)

    def testPublishingTweet(self):
        pass

    def testPublishingTweetWithMedia(self):
        pass
