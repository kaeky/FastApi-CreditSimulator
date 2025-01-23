from sqlalchemy.orm import Session
from typing import List

from src.clients.dto.client_dto import ClientDto
from src.clients.dto.client_input import ClientInput
from src.clients.entities.client_entity import ClientEntity


class ClientRepository:
    def __init__(self, db: Session):
        self.db = db

    def createClient(self, client: ClientInput, auth0Id: str) -> ClientDto:
        clientData = ClientEntity(**client.dict(exclude={"password"}))
        clientData.auth0Id = auth0Id
        self.db.add(clientData)
        self.db.commit()
        self.db.refresh(clientData)
        return ClientDto.from_entity(clientData)

    def findAll(self) -> List[ClientDto]:
        clients = self.db.query(ClientEntity).all()
        return [ClientDto.from_entity(client) for client in clients]

    def getByAuth0Id(self, auth0Id: str) -> ClientDto:
        client = self.db.query(ClientEntity).filter(ClientEntity.auth0Id == auth0Id).first()
        return ClientDto.from_entity(client) if client else None

    def updateClient(self, clientInput: ClientInput, client: ClientDto, auth0Id: str) -> ClientDto:
        clientData = self.db.query(ClientEntity).filter(ClientEntity.id == client.id).first()
        clientInputDict = clientInput.dict(exclude={"password"})
        clientInputDict['auth0Id'] = auth0Id
        for key, value in clientInputDict.items():
            setattr(clientData, key, value)
        self.db.commit()
        self.db.refresh(clientData)
        return ClientDto.from_entity(clientData)