import enum

import strawberry
from sqlalchemy import Column, Integer, String, DateTime, func, Boolean, Enum

from src.client.types.creditEnums import CreditRiskProfileEnum
from src.config.database import Base



class ClientEntity(Base):
    __tablename__ = 'dim_client'

    id = Column(Integer, primary_key=True)
    firstName = Column(String(255))
    lastName = Column(String(255))
    email = Column(String(255))
    phone = Column(String(255))
    auth0Id = Column(String(255))
    age = Column(Integer)
    status = Column(Boolean)
    riskProfile = Column(Enum(CreditRiskProfileEnum))
    borrowingCapacity = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
