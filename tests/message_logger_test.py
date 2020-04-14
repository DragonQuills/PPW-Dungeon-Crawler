import pytest
from UI.MessageLogger import MessageLogger

def test_messagelogger_is_singleton():
    with pytest.raises(RuntimeError):
        m1 = MessageLogger()
    m2 = MessageLogger.instance()
    m3 = MessageLogger.instance()
    assert(m2 is m3)

def test_push_message():
    MAX_MESSAGES_ON_SCREEN = 2
    m = MessageLogger.instance()
    m.push_message("test1")
    m.push_message("test2")
    assert(m.messages == ["test1", "test2"])
    m.push_message("test3")
    assert(m.messages == ["test2", "test3"])
