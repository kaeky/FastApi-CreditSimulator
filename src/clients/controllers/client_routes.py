from fastapi import APIRouter, HTTPException
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from src.auth.middlewares.current_user_decorator import currentUser
from src.auth.middlewares.jwt_strategy import JWTStrategy
from src.clients.dto.client_dto import ClientDto
from src.clients.dto.client_input import ClientInput
from src.clients.services.client_service import ClientService


from src.config.database import getDb
from src.libs.auth0_lib import Auth0Lib

router = APIRouter()
auth0Lib = Auth0Lib()

class ClientRoutes:

    def __init__(self):
        self.router = APIRouter()
        self._registerRoutes()

    def _registerRoutes(self):
        self.router.get("/", response_model=List[ClientDto], dependencies=[Depends(currentUser)])(self.getClients)
        self.router.post("/", response_model=ClientDto)(self.createClient)
        self.router.get("/profile", response_model=ClientDto)(self.getClient)

    def getClients(self, db: Session = Depends(getDb)) -> List[ClientDto]:
        try:
            clientService = ClientService(db, auth0Lib)
            return clientService.getClients()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error inesperado: {e}")

    def getClient(self, db: Session = Depends(getDb)) -> ClientDto:
        clientService = ClientService(db, auth0Lib)
        return clientService.getClients()

    def createClient(self, client: ClientInput, db: Session = Depends(getDb)) -> ClientDto:
        try:
            clientService = ClientService(db, auth0Lib)
            return clientService.createClient(client)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error inesperado: {e}")


# Instancia del controlador y exposición del enrutador
clientRoutes = ClientRoutes()
router = clientRoutes.router