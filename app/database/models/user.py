from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String, unique=False, index=True)
    email = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True, index=True)
    cnpj = Column(String, unique=True, index=True)
    chave_pix = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    reset_pin = Column(String, nullable=True)
    reset_pin_expiration = Column(DateTime, nullable=True)
    journeys = relationship("Journey", back_populates="user")
    payments = relationship("Payment", back_populates="user")
    hourly_rates = relationship("HourlyRate", back_populates="user")
    extra_expenses = relationship("ExtraExpense", back_populates="user")