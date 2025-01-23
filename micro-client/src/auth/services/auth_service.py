from sqlalchemy.orm import Session

from src.auth.dto.jwt_dto import auth0PayloadDto
from src.clients.dto.client_dto import ClientDto
from src.clients.services.client_service import ClientService
from src.libs.auth0_lib import Auth0Lib


class AuthService:
    def __init__(self, db: Session, auth0Lib: Auth0Lib):
        self.db = db
        self.clientService = ClientService(db, auth0Lib)
    def validateUserFromAuth0Payload(self, auth0Payload: auth0PayloadDto) -> ClientDto:
        auth0Id = auth0Payload['sub'].split("|")[1]
        user = self.clientService.getByAuth0Id(self.db, auth0Id)
        return user