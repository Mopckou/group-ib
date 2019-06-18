import vk_api


class INTERFACE:

    def get_profile(self):
        pass

    def get_friends(self):
        pass

    def get_wall(self):
        pass


class VkConnector(INTERFACE):

    def __init(self, login, password):
        self.session = vk_api.VkApi(login, password)
        self.session.auth()

    def get_profile(self):
        return

    def get_friends(self):
        return

    def get_wall(self):
        return


class TwConnector(INTERFACE):

    def get_profile(self):
        return

    def get_friends(self):
        return

    def get_wall(self):
        return


class USER:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class POST:

    def __init__(self):
        pass


if __name__ == '__main__':
    session = vk_api.VkApi('', '')
    session.auth()
    tools = vk_api.VkTools(session)
    t = tools.get_all('users.get', 10, {'user': [1459679], 'fields': ['sex']})
    print(t)