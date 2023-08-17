from src.app.entities.item import Item
import pytest
from src.app.errors.entity_errors import ParamNotValidated

class testItem: 
    def testItem(self):
        item = Item("Lucca", "4598", "00392-4", 100.0)

        assert item.name == "Lucca"
        assert item.agency == "4598"
        assert item.account == "00392-4"
        assert item.current_balance == 100.0

