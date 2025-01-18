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
        result = self.clientAuth0Service.createUser(client)
        idAuht0 = result["identities"][0]["user_id"]
        return self.clientRepository.createClient(client, idAuht0)

