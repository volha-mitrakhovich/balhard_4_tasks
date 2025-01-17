from tasks.dict_tasks.create_with_kv import save_user


def test_save_user(new_dict):
    data_to_insert = {
        'login': 'user_login',
        'name': 'user_name',
        'age': 30
    }
    some_dict = {}
    result = save_user(some_dict, data_to_insert)
    assert isinstance(result["login"], dict)
    assert result["login"] == {
        'name': 'user_name',
        'age': 30
    }
