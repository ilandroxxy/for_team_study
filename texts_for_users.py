import random
emojis = "😅🙏😂😭😄😢😍❤️😁👍👎☺️😱😌🥳😎👾🤖💙💚💫💥💣💯💭👈👉👇"


class ForUsers():

    def __init__(self, message):
        self.message = message

    @staticmethod
    def push_command_start(self):
        hello = ('Привет', 'Доброго времени суток', 'Приветствую Вас')
        text = f'{random.choice(hello)}, {self.from_user.first_name}!'
        return text


'''
class ForCommands():
    def __init__(self, message):
        self.message = message

    @staticmethod
    def push_homework_command(self):
        text_if_pus_homework_command = 'Вот получите, <b>распишитесь</b> домашка ваша: '
        return text_if_pus_homework_command

    @staticmethod
    def push_start_command(self):
        text_if_push_start_command = f'Добро пожаловать, {self.from_user.first_name}! Получите кнопки:'
        return text_if_push_start_command


class ForMessageHandlers():

    def __int__(self, message):
        self.message = message

    @staticmethod
    def enter_message_random_emoji(self):
        text_if_enter_random_emoji = f"Получите: {random.choice(emojis)}"
        return text_if_enter_random_emoji
'''