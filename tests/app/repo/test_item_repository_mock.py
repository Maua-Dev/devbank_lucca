from src.app.entities.item import Item
from src.app.errors.entity_errors import ParamNotValidated
from  src.app.repo.items_repository_mock import ItemRepositoryMock

class Test_ItemRepositoryMock:
    def test_get_all_items(self):
        repo = ItemRepositoryMock()

        items = repo.get_all_items()

        expected_items = repo.items

        assert expected_items == items