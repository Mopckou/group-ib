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
        self.vk_api = self.vk_api.get_profile()
        self.twitter_api = self.twitter_api.get_profile()

    def get_friends(self):
        pass

    def get_wall(self):
        pass

