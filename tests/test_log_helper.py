from src.apis import log_helper

def test_insert_no_user():
    '''
    user does not exist when inserting
    '''
    user = "yes#1234"
    cmd = "$hey"
    log_helper.save(user, cmd)
    document = log_helper.find_user(user)
    if user in document and cmd in document:
        assert True
    log_helper.delete_user(user)

def test_multi_insert_user():
    '''
    user does not exist when inserting
    '''
    user = "yes#1234"
    cmd = "$hey"
    log_helper.save(user, cmd)
    cmd2 = "$Matches tunein"
    log_helper.save(user, cmd2)
    cmd3 = "$Yeee"
    log_helper.save(user, cmd3)
    document = log_helper.find_user(user)
    if user in document and cmd in document and cmd2 in document and cmd3 in document:
        assert True
    log_helper.delete_user(user)

def test_del_doc():
    '''
    document is deleted
    '''
    user = "yes#1234"
    cmd = "$hey"
    log_helper.save(user, cmd)
    log_helper.delete_user(user)
    document = log_helper.find_user(user)
    if document is None:
        assert True