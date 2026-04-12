from app.db.database import SessionLocal
from app.repositories import paciente_repository
from app.schemas.paciente_schema import PacienteCreate
from fastapi import HTTPException
from app.utils.redis_client import redis_client

def crear_paciente(paciente: PacienteCreate):
    db = SessionLocal()

    existente = paciente_repository.get_by_email(db, paciente.email)

    if existente:
        raise HTTPException(status_code=400, detail="Paciente ya existe")

    nuevo = paciente_repository.create(db, paciente.dict())
    db.close()
    return nuevo


def listar_pacientes():
    db = SessionLocal()
    pacientes = paciente_repository.get_all(db)
    db.close()
    return pacientes


def bloquear_cita(paciente_id: str, horario: str):
    key = f"paciente:{paciente_id}:horario:{horario}"

    lock = redis_client.set(key, "LOCK", nx=True, ex=300)

    if not lock:
        raise HTTPException(
            status_code=400,
            detail="El paciente ya tiene una cita en ese horario"
        )

    return True