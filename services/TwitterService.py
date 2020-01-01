import os
import tweepy
import logging
import requests
from PIL import Image
from tweepy import Cursor
from tweepy.error import TweepError


class TwitterService:
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)

        self.twitter = tweepy.API(auth)

    def publish_tweet(self, message: str):
        self.twitter.update_status(message)

    def publish_tweet_with_media(self, message: str, media_url: str):
        filename = 'temp.jpg'
        max_size = 3072
        response = requests.get(media_url, stream=True)

        if response.status_code == requests.codes.ok:
            with open(filename, 'wb') as file:
                for chunk in response:
                    file.write(chunk)

            while os.path.getsize(filename) > max_size * 1024:
                logging.info(f"Image file size is too big: {round(os.path.getsize(filename)/1024)}kb.")
                image = Image.open(filename)
                image.save(filename, optimize=True, quality=45)
                logging.info(f"Image file size reduced: {round(os.path.getsize(filename)/1024)}kb.")

            self.twitter.update_with_media(filename, status=message)
            os.remove(filename)
        else:
            print("Unable to download image")

    def favorite_tweet(self, tweet_id: int):
        self.twitter.create_favorite(tweet_id)

    def get_tweets(self, search_query: str, max_tweets: int):
        tweets = Cursor(self.twitter.search, q=search_query).items(max_tweets)
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
