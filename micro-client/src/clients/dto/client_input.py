from pydantic import BaseModel, Field, EmailStr, validator
from src.clients.types.creditEnums import CreditRiskProfileEnum
import re

class ClientInput(BaseModel):
    firstName: str = Field(..., min_length=1, max_length=50, description="El nombre no puede estar vacío.")
    lastName: str = Field(..., min_length=1, max_length=50, description="El apellido no puede estar vacío.")
    email: EmailStr = Field(..., description="Debe proporcionar un correo electrónico válido.")
    phone: str = Field(..., pattern=r"^\d+$", description="El número de teléfono debe contener solo números.")
    age: int = Field(..., ge=18, le=120, description="La edad debe estar entre 18 y 120 años.")
    status: bool
    riskProfile: CreditRiskProfileEnum
    borrowingCapacity: int = Field(..., ge=0, description="La capacidad de endeudamiento debe ser mayor o igual a 0.")
    password: str

    @validator("password")
    def validate_password(cls, value):
        passwordPattern = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).{8,}$")
        if not passwordPattern.match(value):
            raise ValueError(
                "La contraseña debe tener al menos 8 caracteres, incluyendo una mayúscula, una minúscula, un número y un carácter especial."
            )
        return value