# Imports
from bot import InstaFollower
import time

# TODO: Instantiate the bot
bot = InstaFollower()

# TODO: Login to Instagram
bot.login()

# TODO: Navigate to the Instagram page > open Followers popup
time.sleep(5)
bot.find_followers(username='ai_artimagecreator')

while True:
    bot.scroll_down()
    time.sleep(2)
    bot.follow()
    # bot.scroll_down()

