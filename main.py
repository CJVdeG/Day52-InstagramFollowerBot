# Imports
from bot import InstaFollower
import time

# TODO: Insert which Instagram account you want to follow, e.g.:
ig_account = 'aiartmagnet'

# TODO: Instantiate the bot
bot = InstaFollower()

# TODO: Login to Instagram
bot.login()

# TODO: Navigate to the Instagram page > open Followers popup
time.sleep(5)
bot.find_followers(username=ig_account)

while True:
    bot.scroll_down()
    time.sleep(2)
    bot.follow()
