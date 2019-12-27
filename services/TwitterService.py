import os
import tweepy
import requests

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
        api = self.twitter_api_auth()
        api.update_status(message)

    def publish_tweet_with_media(self, message: str, media_url: str):
        api = self.twitter_api_auth()
        filename = 'temp.jpg'
        response = requests.get(media_url, stream=True)

        if response.status_code == requests.codes.ok:
            with open(filename, 'wb') as image:
                for chunk in response:
                    image.write(chunk)

            api.update_with_media(filename, status=message)
            os.remove(filename)
        else:
            print("Unable to download image")