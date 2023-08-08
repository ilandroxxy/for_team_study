import random

class ForUser():
    def __init__(self, message):
        self.message = message

    @staticmethod
    def push_command_start(self):
        text = f'Добро пожаловать, {self.from_user.first_name}!'
        return text

    @staticmethod
    def push_command_getmyid(self):
        text = f'Вот ваш ID: `{self.chat.id}`'
        return text

    @staticmethod
    def push_trash(self):
        answer = ('Что тут вообще происходит?',
                  'Что здесь происходит?',
                  'Что тут происходит?',
                  'Что тут вообще творится?',
                  'Что здесь вообще происходит?',
                  'Что здесь творится?',
                  'Что тут вообще творится?',
                  'Что здесь происходит?',
                  'Что тут происходит?',
                  'Что здесь вообще творится?')
        return random.choice(answer)


class ForAdmin():
    def __init__(self, message):
        self.message = message

    @staticmethod
    def send_help_forward(self, mess):
        text = f'#help Пользователь: @{self.from_user.username}\n' \
               f'Пишет сообщение: {mess}'
        return text