from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table, UniqueConstraint, func
from sqlalchemy.orm import relationship
from db import Base


class UselessModel(Base):
    __tablename__ = 'useless_models'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)


students_courses_table = Table(
    'students_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id')),
    UniqueConstraint('student_id', 'course_id', name='unique_enrollmen_1')
)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    student_no = Column(String(80), nullable=False, unique=False)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    courses = relationship(
        "Course",
        secondary=students_courses_table,
    )


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    exam_type = Column(String(20), nullable=False)
    enrolled_no = Column(Integer, nullable=False)
    students = relationship(
        "Student",
        secondary=students_courses_table,
    )


class Grade(Base):
    __tablename__ = 'grades'
    student_id = Column(
        Integer,
        ForeignKey('students.id'),
        nullable=True,
        primary_key=True,
    )
    course_id = Column(
        Integer,
        ForeignKey('courses.id'),
        nullable=True,
        primary_key=True,
    )
    created_at = Column(DateTime, nullable=False)
    grade = Column(Integer, nullable=False)

