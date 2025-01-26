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
TARGET_TWITTER_USERS = ['godofhell__']  # Add the new Twitter user here

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# Set up Twitter API client
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

# Function to forward tweets to Telegram
class MyStream(tweepy.Stream):
    def on_status(self, status):
        if status.user.screen_name in TARGET_TWITTER_USERS:
            message_text = status.text
            client.send_message(TROJAN_BOT_ID, message_text)
            print(f"Forwarded tweet to Telegram: {message_text}")

    def on_error(self, status_code):
        if status_code == 420:
            return False  # Disconnects the stream on rate limiting

# Start streaming tweets from the specified users
def start_stream():
    my_stream = MyStream(auth=twitter_api.auth)
    my_stream.filter(follow=[str(twitter_api.get_user(user).id) for user in TARGET_TWITTER_USERS])

def main():
    print("Starting the Telegram client...")
    with client:
        print("Listening for new messages...")
        start_stream()
        client.run_until_disconnected()

if __name__ == "__main__":
    main()
