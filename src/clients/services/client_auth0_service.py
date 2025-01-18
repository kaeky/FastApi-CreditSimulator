import requests

from src.clients.dto.client_input import ClientInput
from src.libs.auth0_lib import Auth0Lib


class ClientAuth0Service:
    def __init__(self, auth0Lib: Auth0Lib):
        self.auth0Lib = auth0Lib

    def createUser(self, client: ClientInput):
        try:
            user = self.auth0Lib.createUser(client)
            return user
        except requests.exceptions.RequestException as e:
            raise ValueError("No se pudo crear el usuario en Auth0.") from e