from ..errors.entity_errors import ParamNotValidated
from typing import Dict, Tuple
from ..enums.users_enum import BankOperationType

class User: 
    name: str
    agency: str
    account: str
    current_balance: float
    timestamp = float
    type = BankOperationType
    value = float

    def __init__(self, name: str = None, agency: str = None, account: str = None, current_balance: float = None,
                timestamp: float = None, type: BankOperationType = None, value: float = None):
        
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
        
        self.timestamp = timestamp
        if not self.validate_timestamp(timestamp):
            raise ParamNotValidated("timestamp", "error")
    
        self.type = type
        if not self.validate_type(type):
            raise ParamNotValidated("type", "invalid")
        
        self.value = value
        if not self.validate_value(value):
            raise ParamNotValidated("value", "invalid")

    @staticmethod
    def validateAgency(agency: str) -> bool:
        if agency == None:
            if type(agency) != str:
                if len(agency) > 4:
                    return False
        
        return True
    
    @staticmethod
    def validateAccount(account : str) -> bool:
        if account == None: 
            if type(account) != str:
                if account[5] != "-":
                    return False
            
        return True 
    
    @staticmethod
    def validate_current_balance(current_balance) -> bool:
        if current_balance == None:
            if type(current_balance) != float:
                return False
        
        return True
    
    @staticmethod
    def validate_timestamp(timestamp) -> bool:
        if timestamp == None:
            if type(timestamp) != float:
                return False
            
        return True
    
    @staticmethod
    def validate_type(type: BankOperationType) -> Tuple[bool, str]:
        if type == None:
            if type(type) != BankOperationType:
                return False
             
        return True
    
    @staticmethod
    def validate_value(value) -> bool:
        if value == None:
            if type(value) != float:
                return False
            
        return True
    
    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp,
            "type": self.type,
            "value": self.value
        }

     