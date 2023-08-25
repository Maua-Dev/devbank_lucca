from src.app.entities.item import Item
from src.app.errors.entity_errors import ParamNotValidated

class Test_Item: 
    def test_item(self):
        item = Item("Lucca", "65343", "00392-4", 100.0)

        assert item.name == "Lucca"
        assert item.agency == "65343"
        assert item.account == "00392-4"
        assert item.current_balance == 100.0
