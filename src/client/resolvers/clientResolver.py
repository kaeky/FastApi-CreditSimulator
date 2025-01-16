
import strawberry

from src.client.dto.clientDto import ClientDto
from src.client.services.clientService import ClientService


@strawberry.type
class ClientResolver:

    def __init__(self, clientService: ClientService):
        self.clientService = clientService

    @strawberry.field
    def getClients(self) -> list[ClientDto]:
        return self.clientService.getClients()