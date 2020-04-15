import pytest
from UI.MessageLogger import MessageLogger
from definitions import *

def test_messagelogger_is_singleton():
    with pytest.raises(RuntimeError):
        m1 = MessageLogger()
    m2 = MessageLogger.instance()
    m3 = MessageLogger.instance()
    assert(m2 is m3)

# Assuming the limit is above 2 which it should always be
def test_push_message_under_limit():
    m = MessageLogger.instance()
    m.push_message("test1")
    m.push_message("test2")
    assert(m.messages == ["test1", "test2"])


def test_push_message_over_limit():
    m = MessageLogger.instance()
    correct_list = []
    for i in range(0, MAX_MESSAGES_ON_SCREEN + 1):
        m.push_message("test" + str(i))
        if i > 0:
            correct_list.append("test" + str(i))

    assert(m.messages == correct_list)
