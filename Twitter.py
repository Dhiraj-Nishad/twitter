import re
import tweepy
from telethon import TelegramClient

# Replace these with your credentials
API_ID = 29199461
API_HASH = '5d5c0797293505649aaa30aa8d1af14a'
SESSION_NAME = 'auto_buy_session'

# Twitter Bearer Token
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEn9yQEAAAAAm3pKLa8OMfEqde9bSRbH3GUb0no%3Dx6HtObphKcph3iLT93gpJP6B4YSM9js6WKjSn6LO1a6xnaC8Xf'

# List of source group IDs
SOURCE_GROUP_IDS = ['@buybotttttt', '@buybottttt']  # Add more groups as needed
TROJAN_BOT_ID = '@bonkbot_bot'
TARGET_TWITTER_USERS = ['godofhell__']  # Add the new Twitter user here

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        if tweet.author.username in TARGET_TWITTER_USERS:
            message_text = tweet.text
            print(f"Forwarded tweet to Telegram: {message_text}")
            client.send_message(TROJAN_BOT_ID, message_text)

    def on_error(self, status_code):
        if status_code == 420:
            return False  # Disconnects the stream on rate limiting

def start_stream():
    my_stream = MyStream(BEARER_TOKEN)
    
    # Create rules to filter tweets from specified users
    for user in TARGET_TWITTER_USERS:
        my_stream.add_rules(tweepy.StreamRule(f"from:{user}"))

    my_stream.filter()

def main():
    print("Starting the Telegram client...")
    with client:
        print("Listening for new messages...")
        start_stream()
        client.run_until_disconnected()

if __name__ == "__main__":
    main()
