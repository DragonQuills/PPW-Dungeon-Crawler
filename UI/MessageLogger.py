'''
A Singleton message logger to track and display
messages to the text box

Code to make this a singleton is from here:
https://python-patterns.guide/gang-of-four/singleton/
'''

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

    def add_message(self, message):
        self.messages.append(message)

    def print_message(self):
        print(self.messages)
