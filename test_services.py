import pytest

from db import dsn, Base
from models import UselessModel, Student, Course, Grade
from services import example_service, enrolling_course, awarding_grade


@pytest.fixture(scope='session')
def sqlalchemy_manage_db():
    return True


@pytest.fixture(scope='session')
def sqlalchemy_connect_url():
    return dsn + '_test'


@pytest.fixture(scope='session', autouse=True)
def tables(engine, db_schema):
    Base.metadata.create_all(engine)


@pytest.fixture(autouse=True)
def use_transaction(transaction):
    pass

def test_example_service(dbsession):
    assert dbsession.query(UselessModel).count() == 0
    some_number = 2

    example_service(example_argument=some_number, session=dbsession)

    assert dbsession.query(UselessModel).one().number == some_number


@pytest.fixture()
def student(dbsession):
    student_instance = Student(student_no='AZB123', first_name='John', last_name='Doe')
    dbsession.add(student_instance)
    dbsession.flush()
    return student_instance


@pytest.fixture()
def course(dbsession):
    course_instance = Course(name='Maths', exam_type='speaking', enrolled_no=0)
    dbsession.add(course_instance)
    dbsession.flush()
    return course_instance


def test_enrolling(dbsession, student, course):
    enrolling_course(course.id, student.id, session=dbsession)

    assert course.enrolled_no == 1
    assert len(course.students) == 1


def test_enrolling_twice(dbsession, student, course):
    enrolling_course(course.id, student.id, session=dbsession)

    with pytest.raises(Exception):
        enrolling_course(course.id, student.id, session=dbsession)


def test_awarding_grade(dbsession, student, course):
    grade = 5
    awarding_grade(course.id, student.id, grade, session=dbsession)

    saved_grade = dbsession.query(Grade).filter(
        (Grade.student_id == student.id)
        & (Grade.course_id == course.id)
    ).one()
    assert saved_grade.grade == grade
    assert student.grades_avg == grade


def test_awarding_student_avg(dbsession, student, course):
    grade = 3
    awarding_grade(course.id, student.id, grade, session=dbsession)

    assert student.grades_avg == grade
