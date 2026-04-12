from sqlalchemy import Column, String
from app.db.database import Base
import uuid

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)