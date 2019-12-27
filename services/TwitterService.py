import os
import tweepy
import requests

CONSUMER_KEY = os.environ.get("CONSUMER_KEY", "BStFXJbScjS0gbNSRFp2ZAVal")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET", "lQNj9xi0r99XoID6J2I5sRJK9CS6iYJg6xiAnx73nZyRoDDCva")
ACCESS_TOKEN_KEY = os.environ.get("ACCESS_TOKEN_KEY", "1210293320162959360-0rfLNv01nk5xqsdiuD4YKkvzCHW5jc")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET", "0IOeTbiXNw0WmTbRAu9lHW5JeEKkCpHbf9ss6anzf0jtJ")


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