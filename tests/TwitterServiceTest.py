import os
import logging
import unittest
from services.TwitterService import TwitterService

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN_KEY = os.environ.get("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")


class TwitterServiceTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.twitter = TwitterService(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                                      access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)

    def testTwitterConnection(self):
        self.assertIsNotNone(self.twitter)

    def testPublishingTweet(self):
        pass

    def testPublishingTweetWithMedia(self):
        self.twitter.publish_tweet_with_media("Test", "https://images.pexels.com/photos/3154302/pexels-photo-3154302."
                                                      "jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940")

    def testGetTweetsContent(self):
        tweets = self.twitter.get_tweets(search_query="memes", max_tweets=100)
        self.assertIsNotNone(tweets)

    def testFavoriteSetOfTweets(self):
        tweets = self.twitter.get_tweets(search_query="memes", max_tweets=100)
        self.twitter.favorite_selected_tweets(tweets=tweets)
