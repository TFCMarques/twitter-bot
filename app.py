import logging
from services.TwitterService import TwitterService
from services.RedditService import RedditService

logging.basicConfig(level=logging.INFO)
twitter_service = TwitterService()
reddit_service = RedditService()

# top_memes = reddit_service.get_subreddit_top_posts(subreddit='memes', time='day', limit=5)

# for count, meme in enumerate(top_memes, 1):
#     msg = f"Today's #{count} {meme.title} - u/{meme.author}"
#     twitter_service.publish_tweet_with_media(message=msg, media_url=meme.url)
#     logging.info(f"Tweeting meme #{count} of the day.")

tweets = twitter_service.get_tweets(search_query="memes", max_tweets=1000)
twitter_service.favorite_selected_tweets(tweets=tweets)
