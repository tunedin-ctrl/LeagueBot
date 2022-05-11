from src.error import InputError

""" Stub test"""
def echo(value):
    """ stub method """
    if value == 'echo':
        raise InputError('Input cannot be echo')
    return value
