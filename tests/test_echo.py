""" Stub tests """
import pytest
from src.echo import echo
from src.error import error

def test_echo():
    """ Stub test method"""
    assert echo("123") == "123", "123 == 123"
    assert echo("abc") == "abc", "abc == abc"

def test_echo_except():
    with pytest.raises(error.InputError):
        echo("echo")