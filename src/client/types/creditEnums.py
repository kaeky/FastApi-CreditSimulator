import strawberry
from enum import Enum

@strawberry.enum
class CreditRiskProfileEnum(Enum):
    AAA = 'AAA'
    AA = 'AA'
    A = 'A'
    BBB = 'BBB'