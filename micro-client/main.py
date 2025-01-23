from fastapi import FastAPI


from src.auth.middlewares.jwt_strategy import JWTStrategy
from src.config.router import register_routers
from src.libs.auth0_lib import Auth0Lib
auth0Lib = Auth0Lib()

app = FastAPI()

app.include_router(register_routers())
app.add_middleware(JWTStrategy, auth0Lib=auth0Lib)