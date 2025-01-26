import re
import tweepy
from telethon import TelegramClient, events

# Replace these with your credentials
API_ID = 29199461
API_HASH = '5d5c0797293505649aaa30aa8d1af14a'
SESSION_NAME = 'auto_buy_session'

# Twitter credentials
TWITTER_API_KEY = 'LimdXnhuXXgGC4IkXwMQ49Vt6'
TWITTER_API_SECRET = 'wVJ8LSa3UiyhtROtlHpciFSdg8BnOM3rVeZG5G5EKLwTcXTUFt'
TWITTER_ACCESS_TOKEN = '1878805655211159552-f9RRNgOf9wXWT4pdjEjr57rFwN2DXt'
TWITTER_ACCESS_TOKEN_SECRET = 'C3ReRKNxZjsAI9HghxyyiMWpYLp9dW5wtP8Jl48hnQmab'

# List of source group IDs
SOURCE_GROUP_IDS = ['@buybotttttt', '@buybottttt']  # Add more groups as needed
TROJAN_BOT_ID = '@bonkbot_bot'
TARGET_TWITTER_USER = 'godofhell__'  # Replace with the Twitter username

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# Set up Twitter API client
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

# Function to forward tweets to Telegram
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.screen_name == TARGET_TWITTER_USER:
            message_text = status.text
            client.send_message(TROJAN_BOT_ID, message_text)
            print(f"Forwarded tweet to Telegram: {message_text}")

# Start streaming tweets from the specified user
def start_stream():
    listener = MyStreamListener()
    stream = tweepy.Stream(auth=twitter_api.auth, listener=listener)
    stream.filter(follow=[str(twitter_api.get_user(TARGET_TWITTER_USER).id)])

def main():
    print("Starting the Telegram client...")
    with client:
        print("Listening for new messages...")
        start_stream()
        client.run_until_disconnected()

if __name__ == "__main__":
    main()
