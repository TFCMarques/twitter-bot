import os
import logging
from services.TwitterService import TwitterService
from services.RedditService import RedditService

logging.basicConfig(level=logging.INFO)

# Twitter Environment Variables
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN_KEY = os.environ.get("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# Reddit Environment Variables
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDDIT_USERNAME = os.environ.get("REDDIT_USERNAME")
REDDIT_PASSWORD = os.environ.get("REDDIT_PASSWORD")
USER_AGENT = os.environ.get("USER_AGENT")

twitter_service = TwitterService(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                                 access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)

reddit_service = RedditService(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, reddit_username=REDDIT_USERNAME,
                               reddit_password=REDDIT_PASSWORD, user_agent=USER_AGENT)

top_memes = reddit_service.get_subreddit_top_posts(subreddit='memes', time='day', limit=5)

for count, meme in enumerate(top_memes, 1):
    msg = f"Today's #{count} {meme.title} - u/{meme.author}"
    twitter_service.publish_tweet_with_media(message=msg, media_url=meme.url)
    logging.info(f"Tweeting meme #{count} of the day.")

tweets = twitter_service.get_tweets(search_query="new year", max_tweets=1000)
twitter_service.favorite_selected_tweets(tweets=tweets)

