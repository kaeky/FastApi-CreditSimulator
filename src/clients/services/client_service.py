from http.client import HTTPException

from sqlalchemy.orm import Session
from src.clients.dto.client_dto import ClientDto
from src.clients.dto.client_input import ClientInput
from src.clients.repositories.client_repository import ClientRepository
from src.clients.services.client_auth0_service import ClientAuth0Service
from src.libs.auth0_lib import Auth0Lib


class ClientService:
    def __init__(self, db: Session, auth0Lib: Auth0Lib):
        self.clientRepository = ClientRepository(db)
        self.clientAuth0Service = ClientAuth0Service(auth0Lib)

    def getClients(self) -> list[ClientDto]:
        return self.clientRepository.findAll()

    def createClient(self, client: ClientInput) -> ClientDto:
        user = self.clientAuth0Service.createUser(client)
        idAuht0 = user["identities"][0]["user_id"]
        return self.clientRepository.createClient(client, idAuht0)

    def getByAuth0Id(self, db: Session, auth0Id: str) -> ClientDto:
        self.clientRepository = ClientRepository(db)
        return self.clientRepository.getByAuth0Id(auth0Id)

    def updateClient(self, clientInput: ClientInput, client: ClientDto) -> ClientDto:
        updateAuth0 = self.clientAuth0Service.updateClient(clientInput, client)
        idAuht0 = updateAuth0["identities"][0]["user_id"]
        return self.clientRepository.updateClient(clientInput, client, idAuht0)
