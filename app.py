from services.TwitterService import TwitterService
from services.RedditService import RedditService

twitter_service = TwitterService()
reddit_service = RedditService()

top_memes = reddit_service.get_subreddit_top_posts(subreddit='memes', time='day', limit=5)

for count, meme in enumerate(top_memes, 1):
    message = f"Today's #{count} {meme.title} - u/{meme.author}"
    twitter_service.publish_tweet_with_media(message, meme.url)
