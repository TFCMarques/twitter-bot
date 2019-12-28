import logging
import unittest
from services.TwitterService import TwitterService


class TwitterServiceTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.twitter_service = TwitterService()

    def testTwitterConnection(self):
        twitter = self.twitter_service.twitter_api_auth()
        self.assertIsNotNone(twitter)

    def testPublishingTweet(self):
        pass

    def testPublishingTweetWithMedia(self):
        pass

    def testGetTweetsContent(self):
        tweets = self.twitter_service.get_tweets(search_query="memes", tweets_per_query=100)
        self.assertIsNotNone(tweets)

    def testFavoriteSetOfTweets(self):
        tweets = self.twitter_service.get_tweets(search_query="memes", tweets_per_query=100)
        self.twitter_service.favorite_selected_tweets(tweets=tweets)
