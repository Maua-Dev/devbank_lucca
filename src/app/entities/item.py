from ..errors.entity_errors import ParamNotValidated

class Item: 
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str = None, agency: str = None, account: str = None, current_balance: float = None):
        self.name = name

        self.agency = agency
        if not self.validateAgency(agency):
            raise ParamNotValidated("agency", "invalid")
        
        self.account = account
        if not self.validateAccount(account):
            raise ParamNotValidated("account", "invalid")
    
        self.current_balance = current_balance
        if not self.validate_current_balance(current_balance):
            raise ParamNotValidated("current balance", "invalid")
    
    @staticmethod
    def validateAgency(agency: str) -> bool:
        if type(agency) != str:
            return False
        
        return True
    
    @staticmethod
    def validateAccount(account : str) -> bool:
        if type(account) != str:
                return False
        
        return True 
    
    @staticmethod
    def validate_current_balance(current_balance) -> bool:
        if type(current_balance) != float:
            return False
        
        return True