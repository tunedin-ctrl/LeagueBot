from src.error_handler.api_error import InputError

""" Stub test"""
def echo(value):
    """ stub method """
    if value == 'echo':
        raise InputError('Input cannot be echo')
    return value
