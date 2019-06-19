class MyOAuthHandler:

    def set_access_token(self, *args, **kwargs):
        print('token is accessed')


class MyApi:

    def get_user(self, *args, **kwargs):
        return UserModel(33333, 'vasya')


class UserModel:

    def __init__(self, id, screen_name):
        self.id = id
        self.screen_name = screen_name

    @staticmethod
    def friends():
        return [
            UserModel(12345, 'friend1'), UserModel(54321, 'friend2'), UserModel(213, 'friend3')
        ]
