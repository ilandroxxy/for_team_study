"""В этом файле содержится весь текст для бота"""


import random




class ForUser():
    def __init__(self, messege):
        self.messege = messege

    """Текст для кнопки старт"""
    @staticmethod
    def push_command_start(self):
        text = f'Добро пожаловать, {self.from_user.first_name}!'
        return text

    """Текст для выдачи айдишника пользователю"""
    @staticmethod
    def push_command_getmyid(self):
        text = f'ID: `{self.chat.id}`'
        return text

    """Текст для команды help"""
    @staticmethod
    def push_command_help(self):
        text = ('/start - запуск бота и приветствие пользователя\n'
                '/help - вывод списка команд\n'
                '/getmyid - команда для вывода айди пользователя\n'
                '/contactgithub - открой мой GitHub\n'
                '/contacttg - открой мой Telegram')
        return text

    """Текст для ответа на бред"""
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

    """Текст для ключевого слова #help и т.д."""
    @staticmethod
    def push_text_help(self):
        text = 'Админ уведомлён'
        return text

    """Текст для кнопки пересылки"""
    @staticmethod
    def push_ikbtext_getmyid(self):
        text = 'Переслать вашему репетитору'
        return text

    """Так же ответ на ключевое слово"""
    @staticmethod
    def get_messege_text(self):
        text = 'хуй'
        return text


    @staticmethod
    def messege_answer(self):
        text = 'Dota2'
        return text

    """Ключевое слово"""
    @staticmethod
    def get_trash(self):
        text = ('#help', 'pamagi', 'nado ochen')
        return text

    """Перечень команд"""
    # @staticmethod
    # def get_help_text(self):
    #     answer = ('/start - запуск бота и приветствие пользователя\n'
    #             '/help - вывод списка команд\n'
    #             '/getmyid - команда для вывода айди пользователя\n'
    #             '/contactgithub - открой мой GitHub\n'
    #             '/contacttg - открой мой Telegram')
    #     return answer

    """Попытка реализации команды help"""
    @staticmethod
    def push_text_toadmin(self):
        text = 'Введите обращение'
        return text


    @staticmethod
    def push_command_contact(self):
        text = 'Мои контакты'
        return text


    @staticmethod
    def push_ikbtext_contact_github(self):
        text = 'Мой GitHub'
        return text

    @staticmethod
    def push_ikbtext_contact_tg(self):
        text = 'Мой Telegram'
        return text


    @staticmethod
    def help_handlers(self, mess):
        text = f'#help пользователь ввёл обращение: {mess}'
        return text




class ForAdmin():
    def __init__(self, messege):
        self.messege = messege

    """Текст для админа"""
    @staticmethod
    def send_help_self(self, mess):
        text = f'#help Пользователь: @{self.from_user.username}\n' \
               f'Пишет: {mess}'
        return text