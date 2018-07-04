import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
import json

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
    users = {}

    def __init__(self, token, users = None):
        """
        Run authorization methods

        :param token: your community token
        """
        if users is None:
            with open("users.json", "w") as f:
                pass
        else:
            self.users = users
        self.vk_session = vk_api.VkApi(token=token)
        self.vk = self.vk_session.get_api()
        self.session = requests.session()
        self.upload = VkUpload(self.vk_session)
        self.long_poll = VkLongPoll(self.vk_session)


    def broadcast_message(self, uid, message):
        message = f'{uid}: {message}'
        for user in self.users:
            if uid != user:
                self.vk.messages.send(user_id=user, message=message)

    def run(self):
        """
        Main bot`s cycle.
        """
        for event in self.long_poll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.user_id not in self.users:
                    print(self.users)
                    self.users[str(event.user_id)] = None
                    with open("users.json", "w") as f:
                        json.dump(self.users, f)
                self.broadcast_message(str(event.user_id), event.text)