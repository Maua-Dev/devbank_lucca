from src.app.entities.item import User
from src.app.errors.entity_errors import ParamNotValidated

class Test_Item: 
    def test_user(self):
        users = User("Lucca", "5454", "00392-4", 100.0, 1000.0, "deposit", 200.0)

        assert users.name == "Lucca"
        assert users.agency == "5454"
        assert users.account == "00392-4"
        assert users.current_balance == 100.0
        assert users.timestamp == 1000.0
        assert users.type == "deposit"
        assert users.value == 200.0

    def test_to_dict(self):
        users = User("Lucca", "7658", "93875-6", 100.0, 300.0, 'deposit', 150.0)

        assert users.to_dict() == {'name': 'Lucca', 'agency':'7658', 'account': '93875-6', 'current_balance': 100.0, 'timestamp': 300.0, 'type': 'deposit', 'value': 150.0}
        
    
