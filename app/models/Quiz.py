from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

# Object Relational Mapping

class Quiz(Base):
    __tablename__ = "quiz"
    quiz_id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    
    