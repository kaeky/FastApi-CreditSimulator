from pydantic import BaseModel

from src.clients.types.creditEnums import CreditRiskProfileEnum

class ClientDto(BaseModel):
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

    @classmethod
    def from_entity(cls, entity):
        return cls(
            id=entity.id,
            firstName=entity.firstName,
            lastName=entity.lastName,
            email=entity.email,
            phone=entity.phone,
            auth0Id=entity.auth0Id,
            age=entity.age,
            status=entity.status,
            riskProfile=entity.riskProfile.name if entity.riskProfile else None,
            borrowingCapacity=entity.borrowingCapacity,
        )
