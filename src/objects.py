from datetime import date


class USER:

    def __init__(self, id, first_name, last_name, sex, screen_name=''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.screen_name = screen_name

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and self.sex == other.sex \
                and self.screen_name == other.screen_name

    def __str__(self):
        return 'USER < first name= %s, last name= %s, sex= %s, screen name= %s>' % (self.first_name, self.last_name,
                                                                        self.sex_translate(self.sex), self.screen_name)

    @staticmethod
    def sex_translate(sex):
        return 'famale' if sex == 1 else 'male'


class FRIEND(USER):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        s = super().__str__()
        return s.replace('USER', 'FRIEND')


class POST:

    def __init__(self, type, text, date, source):
        self.type = type
        self.text = text
        self.date = date
        self.source = source

    def __eq__(self, other):
        return self.type == other.type and self.text == other.text and self.date == other.date

    def __str__(self):
        return 'POST < type= %s, date= %s, source= %s, text= %s >' % (self.type, date.fromtimestamp(self.date),
                                                                      self.source, self.text)

