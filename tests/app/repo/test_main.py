from src.app.main import get_all_users

class Test_main:
    def test_get_all_users(self):
        response = get_all_users()

        assert type(response) == dict
        
