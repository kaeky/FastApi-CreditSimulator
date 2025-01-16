from src.client.repositories.clientRepository import ClientRepository


class ClientService:
    def __init__(self, clientRepository: ClientRepository):
        self.clientRepository = clientRepository

    def getClients(self):
        return self.clientRepository.findAll()

