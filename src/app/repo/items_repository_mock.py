from ..repo.items_repository_interface import IItemRepository
from ..entities.item import Item
from typing import List

class ItemRepositoryMock(IItemRepository):
    items: list[Item]

    def __init__(self):
        self.items = [
            Item("Lucca", "1503", "00253-2", current_balance = 1000.0),
            Item("Pedro", "2604", "01243-7", current_balance = 2000.0),
            Item("Thiago", "5412", "19450-0", current_balance = 500.0),
            Item("Rodrigo", "8965", "98215-3", current_balance = 900.0),
        ]   
        
    def get_all_items(self) -> List[Item]:
        return self.items