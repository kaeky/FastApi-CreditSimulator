from typing import Type

from sqlalchemy.orm import Session

from src.client.dto.clientInput import ClientInput
from src.client.entities.clientEntity import ClientEntity


class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    def createClient(self, client: ClientInput):
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client

    def findAll(self) -> list[Type[ClientEntity]]:
        return self.db.query(ClientEntity).all()