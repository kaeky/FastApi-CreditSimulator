import jwt
from typing import Optional
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

from src.auth.services.auth_service import AuthService
from src.config.auth0 import auth0Config
from src.config.database import SessionLocal
from src.libs.auth0_lib import Auth0Lib

class UnauthorizedException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)

def jwtFromCookieOrHeaderAsBearerToken(req: Request):
    authorization: Optional[str] = req.headers.get("Authorization")
    if authorization and authorization.startswith("Bearer "):
        return authorization.split("Bearer ")[1]

    # Intentar obtener el token desde la cookie
    cookie_header = req.headers.get("cookie", "")
    cookies = dict(cookie.split("=") for cookie in cookie_header.split("; ") if "=" in cookie)
    return cookies.get("access_token")


class JWTStrategy(BaseHTTPMiddleware):
    def __init__(self, app, auth0Lib: Auth0Lib):
        super().__init__(app)
        jwksUrl = f"{auth0Config['domain']}/.well-known/jwks.json"
        self.jwksClient = jwt.PyJWKClient(jwksUrl)
        self.auth0Lib = auth0Lib

    async def dispatch(self, request: Request, call_next):
        db = SessionLocal()
        try:
            token = jwtFromCookieOrHeaderAsBearerToken(request)
            request.state.user = None
            if token:
                try:
                    signing_key = self.jwksClient.get_signing_key_from_jwt(token).key
                except jwt.exceptions.PyJWKClientError as error:
                    raise UnauthorizedException(f"Error en la firma de la llave: {str(error)}")
                except jwt.exceptions.DecodeError as error:
                    raise UnauthorizedException(f"Error en el token: {str(error)}")

                try:
                    authService = AuthService(db, self.auth0Lib)
                    payload = jwt.decode(
                        token,
                        signing_key,
                        algorithms=['RS256'],
                        audience=auth0Config["audience"],
                        issuer=f"{auth0Config['domain']}/",
                    )
                    user = authService.validateUserFromAuth0Payload(payload)
                    request.state.user = user  # Agregar el payload al estado de la solicitud
                except Exception as e:
                    raise ValueError("Error al decodificar el token:", str(e))
        except UnauthorizedException as exc:
            return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
        except Exception as exc:
            return JSONResponse(status_code=500, content={"detail": "Unexpected server error"})
        response = await call_next(request)
        return response