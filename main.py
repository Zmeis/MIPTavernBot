# -*- coding: utf-8 -*-
from bot import VKBot
import json

try:
    with open("users.json") as f:
        users = json.load(f)
except:
    with open("users.json", "w") as f:
        users = {}

if __name__ == '__main__':
    with open(".token") as f:
        token = f.read()

    bot = VKBot(users = users, token=token)
    bot.run()