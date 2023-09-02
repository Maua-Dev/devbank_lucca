from src.app.entities.item import Item
from src.app.errors.entity_errors import ParamNotValidated
from  src.app.repo.users_repository_mock import UserRepositoryMock

class Test_ItemRepositoryMock:
    def test_get_all_users(self):
        repo = UserRepositoryMock()

        User = repo.get_all_users()

        expected_users = repo.users

        assert expected_users == User