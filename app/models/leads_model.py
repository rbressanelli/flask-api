from dataclasses import dataclass

from sqlalchemy import Column, DateTime, Integer, String

from app.configs.database import db


@dataclass
class LeadsModel(db.Model):

    id
    name: str
    email: str
    phone: str
    creation_date: DateTime
    last_visit: DateTime
    visits: int

    __tablename__ = "leads_control"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    creation_date = Column(DateTime, nullable=True)
    last_visit = Column(DateTime, nullable=True)
    visits = Column(Integer, nullable=True, default=1)
