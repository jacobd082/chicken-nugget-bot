import os
import tweepy
from replit import db
import time
from keep_alive import keep_alive





# Create API object
#api = tweepy.API(auth)



def tweet():
  Client = tweepy.Client(bearer_token=os.environ["b_t"], consumer_key=os.environ["cons_k"], consumer_secret=os.environ["cons_s"], access_token=os.environ["a_t"], access_token_secret=os.environ["a_s"],return_type="Response", wait_on_rate_limit=False)

  value = db["n"]
  value = value + 1
  db["n"] = value
  print(value)

  tweet = ("{} pc chicken nugget".format(value))

  # Create a tweet
  #api.update_status(tweet)
  Client.create_tweet(direct_message_deep_link=None, for_super_followers_only=None, place_id=None, media_ids=None, media_tagged_user_ids=None, poll_duration_minutes=None, poll_options=None, quote_tweet_id=None, exclude_reply_user_ids=None, in_reply_to_tweet_id=None, reply_settings=None, text=tweet, user_auth=True)
  time.sleep(1800)
  new()

def new():
  tweet()

keep_alive()

tweet()
