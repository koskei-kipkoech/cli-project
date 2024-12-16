from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class TM(Base):
    __tablename__ = 'tms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    students = relationship("Student", back_populates="tms")

    def __repr__(self):
        return f'TM(id={self.id}, name="{self.name}", email="{self.email}")'
    

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    tm_id = Column(Integer, ForeignKey("tms.id"))

    tm = relationship("TM", back_populates="students")

    def __repr__(self):
        return f'Student(id={self.id}, name="{self.name}", age={self.age}, tm_id={self.tm_id})'
