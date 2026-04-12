from sqlalchemy.orm import Session
from app.models.paciente import Paciente

def get_by_email(db: Session, email: str):
    return db.query(Paciente).filter(Paciente.email == email).first()

def create(db: Session, paciente_data):
    paciente = Paciente(**paciente_data)
    db.add(paciente)
    db.commit()
    db.refresh(paciente)
    return paciente

def get_all(db: Session):
    return db.query(Paciente).all()