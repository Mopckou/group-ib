from datetime import date
import vk_api
import tweepy
from src.config import login, password
from src.objects import USER, FRIEND, POST
from src.my_mock import MyOAuthHandler, MyApi, UserModel
from vk_api.exceptions import ApiError


class INTERFACE:

    def get_profile(self, *args, **kwargs):
        pass

    def get_friends(self, *args, **kwargs):
        pass

    def get_wall(self, *args, **kwargs):
        pass


class VkConnector(INTERFACE):

    def __init__(self, login, password):
        self.__session = vk_api.VkApi(login, password)
        self.__session.auth()
        self.__api = self.__session.get_api()

    def get_profile(self, user_id):
        try:
            u = self.__api.users.get(user_id=user_id, fields='sex, screen_name')
        except ApiError:
            return []

        return self.to_users(u)

    def get_friends(self, user_id):
        try:
            u = self.__api.friends.get(user_id=user_id, fields='sex, screen_name')
        except ApiError:
            return []

        return self.to_friends(u)

    def get_wall(self, owner_id=0):
        try:
            w = self.__api.wall.get(owner_id=-owner_id)
        except ApiError:
            return []

        return self.to_posts(w)

    @staticmethod
    def to_posts(w):
        posts = [POST(e['post_type'], e['text'], e['date'], 'vk') for e in w['items']]

        return posts

    @staticmethod
    def to_users(u):
        print(u)
        users = []

        for e in u:
            users.append(
                USER(
                    e['id'],
                    e['first_name'],
                    e['last_name'],
                    e['sex'],
                    e['screen_name'] if hasattr(e, 'screen_name') else ''
                )
            )

        return users

    @staticmethod
    def to_friends(u):
        friends = []

        for e in u['items']:
            friends.append(
                FRIEND(
                    e['id'],
                    e['first_name'],
                    e['last_name'],
                    e['sex'],
                    e['screen_name'] if hasattr(e, 'screen_name') else ''
                       )
            )

        return friends


class TwConnector(INTERFACE):

    def __init__(self, access_token, access_token_secret, consumer_key, consumer_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.__api = tweepy.API(auth)

    def get_profile(self, screen_name):
        u = self.__api.get_user(screen_name)

        return self.to_user(u)

    def get_friends(self, screen_name):
        u = self.__api.get_user(screen_name)
        f = u.friends()

        return self.to_friends(f)

    @staticmethod
    def to_user(model):
        user = USER(model.id, None, None, None, model.screen_name)
        return user

    @staticmethod
    def to_friends(f):
        friends = []

        for i in f:
            friends.append(
                FRIEND(i.id, None, None, None, i.screen_name)
            )

        return friends


if __name__ == '__main__':
    import mock
    tweepy.OAuthHandler = mock.Mock(return_value=MyOAuthHandler())
    tweepy.API = mock.Mock(return_value=MyApi())

    t = TwConnector('', '', '', '')
    friends = t.get_friends('1')

    for i in friends:
        print(i)

    v = VkConnector(login, password)

    w = v.get_profile(86529522)
    for i in w:
        print(i)



