import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import requests

class VKBot:
    """
    VKBot object
    """
    vk = None
    vk_session = None
    session = None
    upload = None
    long_poll = None
    event = None
    users = set()

    def __init__(self, token):
        """
        Run authorization methods.
        To choose login type enter token or your login and password.
        How to get token: https://vk.com/dev/bots_docs

        :param token: your community token
        """
        self.vk_session = vk_api.VkApi(token=token)
        self.vk = self.vk_session.get_api()
        self.session = requests.session()
        self.upload = VkUpload(self.vk_session)
        self.long_poll = VkLongPoll(self.vk_session)


    def broadcast_message(self, message):
        for user in self.users:
            self.vk.messages.send(user_id=user, message=message)

    def run(self):
        """
        Main bot`s cycle.
        """
        for event in self.long_poll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.user_id not in self.users:
                    self.users.add(event.user_id)
                self.broadcast_message(event.text)