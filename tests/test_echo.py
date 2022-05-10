import pytest

from src.echo import echo

def test_echo():
    assert echo("123") == "123", "123 == 123"
    assert echo("abc") == "abc", "abc == abc"

def test_echo_except():
    with pytest.raises(EOFError.mro):
        echo("echo")