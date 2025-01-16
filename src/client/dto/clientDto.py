import strawberry

from src.client.types.creditEnums import CreditRiskProfileEnum


@strawberry.type
class ClientDto:
    id: int
    firstName: str
    lastName: str
    email: str
    phone: str
    auth0Id: str
    age: int
    status: bool
    riskProfile: CreditRiskProfileEnum
    borrowingCapacity: int