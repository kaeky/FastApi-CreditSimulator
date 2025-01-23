from decouple import config

auth0Config = {
    "domain": config("AUTH0_DOMAIN").rstrip("/"),
    "clientId": config("AUTH0_CLIENT_ID"),
    "clientApiClient": config("AUTH0_API_CLIENT_ID"),
    "clientApiSecret": config("AUTH0_API_CLIENT_SECRET"),
    "audience": config("AUTH0_AUDIENCE"),
}
