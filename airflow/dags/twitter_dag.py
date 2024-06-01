from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import tweepy
import snowflake.connector
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='A simple Twitter data pipeline',
    schedule_interval=timedelta(days=1),
)

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

fetch_tweets_task = PythonOperator(
    task_id='fetch_tweets',
    python_callable=fetch_tweets,
    dag=dag,
)
