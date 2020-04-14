import pytest
from UI.MessageLogger import MessageLogger

def test_messagelogger_is_singleton():
    with pytest.raises(RuntimeError):
        m1 = MessageLogger()
    m2 = MessageLogger.instance()
    m3 = MessageLogger.instance()
    assert(m2 is m3)
