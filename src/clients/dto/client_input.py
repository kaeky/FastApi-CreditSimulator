from pydantic import BaseModel

from src.clients.types.creditEnums import CreditRiskProfileEnum

class ClientInput(BaseModel):
    firstName: str
    lastName: str
    email: str
    phone: str
    auth0Id: str
    age: int
    status: bool
    riskProfile: CreditRiskProfileEnum
    borrowingCapacity: int