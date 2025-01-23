from sqlalchemy import Column, Integer, String, DateTime, func, Boolean, Enum, Index

from src.clients.types.creditEnums import CreditRiskProfileEnum
from src.config.database import Base



class ClientEntity(Base):
    __tablename__ = 'dim_client'

    id = Column(Integer, primary_key=True)
    firstName = Column(String(255), nullable=False)
    lastName = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(255), nullable=True)
    auth0Id = Column(String(255), unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    status = Column(Boolean, default=True, nullable=False)
    riskProfile = Column(Enum(CreditRiskProfileEnum), nullable=True)
    borrowingCapacity = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        Index('idx_email', 'email'),
        Index('idx_auth0Id', 'auth0Id'),
    )

