from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from db import Base


__tablename__ = 'useless_models'
class UselessModel(Base):
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    student_no = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    exam_type = Column(String, nullable=False)
    enrolled_no = Column(String, nullable=False)

class Grade(Base):
    __tablename__ = 'grades'
    student_id = Column(Integer, ForeignKey('students.id'), nullable=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=True)
    created_at = Column(DateTime, nullable=False)
    grade = Column(Integer, nullable=False)
