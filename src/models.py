from sqlalchemy import Column, DateTime, Integer, String
from datetime import datetime

from database import Base


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    start_date = Column(DateTime(timezone=True), default=datetime.utcnow)
