import os
import tweepy
from tweepy import Cursor as cursor
import logging
import requests
from tweepy.error import TweepError

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN_KEY = os.environ.get("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")


class TwitterService:
    @staticmethod
    def twitter_api_auth():
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)

    def publish_tweet(self, message: str):
        twitter = self.twitter_api_auth()
        twitter.update_status(message)

    def publish_tweet_with_media(self, message: str, media_url: str):
        twitter = self.twitter_api_auth()
        filename = 'temp.jpg'
        response = requests.get(media_url, stream=True)

        if response.status_code == requests.codes.ok:
            with open(filename, 'wb') as image:
                for chunk in response:
                    image.write(chunk)

            twitter.update_with_media(filename, status=message)
            os.remove(filename)
        else:
            print("Unable to download image")

    def favorite_tweet(self, tweet_id: int):
        twitter = self.twitter_api_auth()
        twitter.create_favorite(tweet_id)

    def get_tweets(self, search_query: str, max_tweets: int):
        twitter = self.twitter_api_auth()
        tweets = cursor(twitter.search, q=search_query).items(max_tweets)
        return tweets

    def favorite_selected_tweets(self, tweets):
        successful_favorites = 0

        for tweet in tweets:
            try:
                self.favorite_tweet(tweet.id)
                logging.info(f"Favorited tweet {tweet.id}.")
                successful_favorites += 1
            except TweepError as error:
                status_code = error.response.status_code
                if status_code == 139:
                    logging.info(f"Tweet {tweet.id} is already favorited. Skipping...")
                    continue
                if status_code == 429:
                    logging.info(f"Twitter rate limit has been reached. Stopping process...")
                    break

        if successful_favorites != 0:
            logging.info(f"Successfully favorited {successful_favorites} tweets.")
        else:
            logging.info(f"Unable to favorite any tweet.")
