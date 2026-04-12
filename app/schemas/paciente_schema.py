from pydantic import BaseModel, EmailStr

class PacienteCreate(BaseModel):
    nombre: str
    email: EmailStr

class PacienteResponse(BaseModel):
    id: str
    nombre: str
    email: str

    class Config:
        from_attributes = True