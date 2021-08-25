from internet_speed_twitter_bot import InternetSpeedTwitterBot
from password import MY_TWITTER_ACCOUNT

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider(input_message=MY_TWITTER_ACCOUNT)