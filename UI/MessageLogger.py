'''
A Singleton message logger to track and display
messages to the text box

Code to make this a singleton is from here:
https://python-patterns.guide/gang-of-four/singleton/
'''
from definitions import *

class MessageLogger():
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
            cls.messages = []
        return cls._instance

    def draw(self, starting_x, starting_y, message_margin):
        for i in range(0, len(self.messages)):
            arcade.draw_text(self.messages[i], starting_x, starting_y - (i * message_margin), arcade.color.COPPER, message_margin)

    def push_message(self, message):
        print(MAX_MESSAGES_ON_SCREEN)
        if len(self.messages) < MAX_MESSAGES_ON_SCREEN:
            print("addign message")
            self.messages.append(message)
        else:
            print("Popping message")
            self.messages.pop(0)
            self.messages.append(message)
