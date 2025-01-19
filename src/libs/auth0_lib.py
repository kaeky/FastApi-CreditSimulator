import requests
from cachetools import TTLCache

from src.clients.dto.client_dto import ClientDto
from src.clients.dto.client_input import ClientInput
from src.config.auth0 import auth0Config

class Auth0Lib:
    def __init__(self):
        # Configura un caché con un TTL de 24 horas
        self.cache = TTLCache(maxsize=100, ttl=24 * 60 * 60)

    def _request(self, method, url, data=None, headers=None):
        headers = headers or {}
        full_url = f"{auth0Config['domain']}{url}"

        try:
            response = requests.request(method, full_url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise

    def _getApiToken(self):
        # Verifica si el token está en la caché
        token = self.cache.get('access-token')
        if token:
            return token

        # Solicita un nuevo token
        form = {
            "grant_type": "client_credentials",
            "client_id": auth0Config['clientApiClient'],
            "client_secret": auth0Config['clientApiSecret'],
            "audience": auth0Config['audience'],
        }

        body = self._request("POST", "/oauth/token", data=form, headers={
            "Content-Type": "application/json",
        })

        token = body.get("access_token") if body else None
        if token:
            self.cache['access-token'] = token
        return token

    def createUser(self, client):
        accessToken = self._getApiToken()
        if not accessToken:
            return None

        form = {
            "email": client.email,
            "given_name": client.firstName,
            "family_name": client.lastName or " ",
            "name": f"{client.firstName} {client.lastName}",
            "password": client.password,
            "connection": "Username-Password-Authentication",
        }

        return self._request("POST", "/api/v2/users", data=form, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {accessToken}",
        })

    def changeUserPassword(self, client, password):
        access_token = self._getApiToken()
        if not access_token:
            return None

        form = {
            "password": password,
            "connection": "Username-Password-Authentication",
        }

        return self._request("PATCH", f"/api/v2/users/auth0|{client['auth0Id']}", data=form, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        })

    def updateUser(self, clientInput: ClientInput, client: ClientDto):
        access_token = self._getApiToken()
        if not access_token:
            return None

        form = {
            "email": clientInput.email,
            "given_name": clientInput.firstName,
            "family_name": clientInput.lastName or " ",
            "name": f"{clientInput.firstName} {clientInput.lastName}",
            "connection": "Username-Password-Authentication",
        }

        return self._request("PATCH", f"/api/v2/users/auth0|{client.auth0Id}", data=form, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        })

    def findUserByEmail(self, email):
        access_token = self._getApiToken()
        if not access_token:
            return None

        return self._request("GET", f"/api/v2/users-by-email?email={email}", headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        })
