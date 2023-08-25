from abc import ABC, abstractmethod
from typing import List
from ..entities.item import Item

class IItemRepository(ABC):

    @abstractmethod
    def get_all_items(self) -> List[Item]:
        pass