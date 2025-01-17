from sqlalchemy.orm import Session
from typing import List

from src.clients.dto.client_dto import ClientDto
from src.clients.dto.client_input import ClientInput
from src.clients.entities.client_entity import ClientEntity


class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    def createClient(self, client: ClientInput):
        clientData = ClientEntity(**client.dict())
        self.db.add(clientData)
        self.db.commit()
        self.db.refresh(clientData)
        return clientData

    def findAll(self) -> List[ClientDto]:
        clients = self.db.query(ClientEntity).all()
        return [ClientDto.from_entity(client) for client in clients]