from ..enums.item_type_enum import ItemTypeEnum
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
            raise ParamNotValidated("agency", "Must have 4 digits")
        self.account = account
        self.current_balance = current_balance
    

    @staticmethod
    def validateAgency(agency: str) -> bool:
        if agency.__len__ != 4: 
            return False
        
        return True