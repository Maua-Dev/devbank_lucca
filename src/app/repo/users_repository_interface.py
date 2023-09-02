from abc import ABC, abstractmethod
from typing import List
from ..entities.item import User

class UUserRepository(ABC):

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

