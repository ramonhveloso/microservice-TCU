from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class Journey(Base):
    __tablename__ = "journeys"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)
    hours_worked = Column(Float, nullable=False)
    hourly_rate = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)
    last_modified = Column(DateTime, nullable=False)
    user = relationship("User", back_populates="journeys")