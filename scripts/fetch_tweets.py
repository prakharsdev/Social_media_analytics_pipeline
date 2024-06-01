import tweepy
import snowflake.connector
import os

def fetch_tweets():
    auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET_KEY'))
    auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
    api = tweepy.API(auth)

    tweets = api.home_timeline(count=100, tweet_mode="extended")
    data = [(tweet.id_str, tweet.created_at, tweet.full_text) for tweet in tweets]

    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT')
    )

    cs = conn.cursor()
    cs.execute("CREATE OR REPLACE TABLE twitter_data (id STRING, created_at TIMESTAMP, text STRING)")
    cs.executemany("INSERT INTO twitter_data VALUES (%s, %s, %s)", data)
    cs.close()
    conn.close()

if __name__ == "__main__":
    fetch_tweets()
