# -*- coding: utf-8 -*-
from bot import VKBot

if __name__ == '__main__':
    with open(".token") as f:
        token = f.read()

    bot = VKBot(token=token)
    bot.run()