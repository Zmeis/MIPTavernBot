# -*- coding: utf-8 -*-
from t_vk_api import VKBot
from random import randint


# example function:
# def example(message, vk):
#     """
#     :param message: message container, contains informations about user_id, text, status etc
#     :param vk: API
#     :return: nothing
#     """
#     vk.messages.send(user_id=message.user_id, message="Some text")


def start(message, vk):
    vk.messages.send(user_id=message.user_id, message=u"Начнем, пожалуй")


def random_habrahabr(message, vk):
    vk.messages.send(user_id=message.user_id, message=u'https://habrahabr.ru/post/' + str(randint(100, 200000)) + u'/')


if __name__ == '__main__':
    queryset = [[[u"Погнали", u"погнали", u"лол", u"Лол"], start], [[u"Хабрахабр", ], random_habrahabr]]
    # if you want use bot by community token
    bot = VKBot(token=)
    # if you want use bot by your account
    # bot = VKBot(log='your_login', passwd='your_passwd')
    bot.run(query=queryset)