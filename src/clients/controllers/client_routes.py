from fastapi import APIRouter
from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.clients.dto.client_dto import ClientDto
from src.clients.dto.client_input import ClientInput
from src.clients.services.clientService import ClientService
from src.config.database import getDb

router = APIRouter()

class ClientRoutes:

    def __init__(self):
        self.router = APIRouter()
        self._registerRoutes()

    def _registerRoutes(self):
        self.router.get("/", response_model=List[ClientDto])(self.getClients)
        self.router.post("/", response_model=ClientDto)(self.createClient)

    def getClients(self, db: Session = Depends(getDb)) -> List[ClientDto]:
        clientService = ClientService(db)
        return clientService.getClients()

    def createClient(self, client: ClientInput, db: Session = Depends(getDb)) -> ClientDto:
        clientService = ClientService(db)
        print(client)
        return clientService.createClient(client)


# Instancia del controlador y exposición del enrutador
clientRoutes = ClientRoutes()
router = clientRoutes.router