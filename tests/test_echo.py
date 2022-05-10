""" Stub tests """
import pytest
from src.echo import echo 

def test_echo():
    """ Stub test method"""
    assert echo("123") == "123", "123 == 123"
    assert echo("abc") == "abc", "abc == abc"

def test_echo_except():
    """ Stub test method"""
    with pytest.raises(TypeError("No")):
        echo("echo")
