
from sqlalchemy.orm import Session
from src.clients.dto.client_dto import ClientDto
from src.clients.dto.client_input import ClientInput
from src.clients.repositories.client_repository import ClientRepository



class ClientService:
    def __init__(self, db: Session):
        self.clientRepository = ClientRepository(db)

    def getClients(self) -> list[ClientDto]:
        return self.clientRepository.findAll()

    def createClient(self, client: ClientInput):
        return self.clientRepository.createClient(client)

