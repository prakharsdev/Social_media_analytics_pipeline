FROM python:3.8-slim

COPY scripts/ /scripts
RUN pip install tweepy snowflake-connector-python

CMD ["python", "/scripts/fetch_tweets.py"]
