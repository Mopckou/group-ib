from src.helper import INTERFACE, VkConnector, TwConnector


class CONNECTOR(INTERFACE):

    def __init__(self, vk_api, twitter_api):
        self.vk_api = vk_api
        self.twitter_api = twitter_api
        self.proxies = []
        self.use_proxy = False

    def add_proxies(self, proxies):
        self.proxies = proxies

    def get_profile(self):
        vk_profile = self.vk_api.get_profile()
        tw_profile = self.twitter_api.get_profile()

        return self.merge(vk_profile, tw_profile)

    def get_friends(self):
        vk_friends = self.vk_api.get_friends()
        tw_friends = self.twitter_api.get_friends()

        return self.merge(vk_friends, tw_friends)

    def get_wall(self):
        vk_wall = self.vk_api.get_wall()
        tw_wall = self.twitter_api.get_wall()

        return self.merge(vk_wall, tw_wall)

    def merge(self, obj1, obj2):
        return