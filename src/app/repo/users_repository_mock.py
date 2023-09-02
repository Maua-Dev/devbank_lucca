from .users_repository_interface import UUserRepository
from ..entities.item import User
from typing import List

class UserRepositoryMock(UUserRepository):
    users: list[User]

    def __init__(self):
        self.users = [
            User("Lucca", "1503", "00253-2", current_balance = 1000.0, timestamp = 400.0, type = "deposit", value = 300.0),
            User("Pedro", "2604", "01243-7", current_balance = 2000.0, timestamp = 1000.0, type = "withdraw", value = 500.0),
            User("Thiago", "5412", "19450-0", current_balance = 500.0, timestamp = 200.0, type = "deposit", value = 600.0),
            User("Rodrigo", "8965", "98215-3", current_balance = 900.0, timestamp = 600.0, type = "withdraw", value = 150.0)
        ]   
        
    def get_all_users(self) -> List[User]:
        return self.users