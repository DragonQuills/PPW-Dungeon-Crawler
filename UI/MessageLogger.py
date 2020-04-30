'''
A Singleton message logger to track and display
messages to the text box

Code to make this a singleton is from here:
https://python-patterns.guide/gang-of-four/singleton/
'''
from definitions import *

class MessageLogger():
    _instance = None

    # Removes init to create singleton functionality
    def __init__(self):
        raise RuntimeError('Call instance() instead')

    # This is the singleton "instance" method to get an instance of the singelton
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.messages = ["You wake up in a dungeon..."]
        return cls._instance

    def draw(self, starting_x, starting_y, message_margin):
        for i in range(0, len(self.messages)):
            # Draw messages each underneath each other
            arcade.draw_text(self.messages[i], starting_x, starting_y - (i * message_margin), arcade.color.COPPER, message_margin)

    # Adds messages up to the MAX_MESSAGES_ON_SCREEN cap, then removes the oldest message
    def push_message(self, message):
        if len(self.messages) < MAX_MESSAGES_ON_SCREEN:
            self.messages.append(message)
        else:
            self.messages.pop(0)
            self.messages.append(message)

    def clear(self):
        self.messages = ["You wake up in a dungeon..."]
