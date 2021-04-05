import pkg_resources
import os

# check if the requirements are satifiered
try:
    pkg_resources.require(open("./requirements.txt", "r").readlines())
except:
    os.system("python -m pip install -r requirements.txt")

from Bot import *

Bot = InstagramBot("usrname", "pw")
Bot.login()

pickle.dump([], open("error_log.txt", "wb"))
# reset the error_log data

# Bot.reset_data(data="posts")
# Bot.reset_data(data="storys")

Bot.check_storys()
# check all storys of people you follow

Bot.check_posts(name="jetsetsam_")
# check posts of users by they usrname

Bot.search_hashtag("free", mode="collect")
# check hashtags by their name
# you could either like or collect the posts