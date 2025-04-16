# models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    skills = Column(String)  # comma-separated

    courses = relationship("Course", back_populates="job")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey('jobs.id'))
    title = Column(String)
    url = Column(String)

    job = relationship("Job", back_populates="courses")
