import pytest

from db import dsn, Base
from models import UselessModel, Student, Course
from services import example_service, enrolling_course


@pytest.fixture(scope='session')
def sqlalchemy_manage_db():
    return True


@pytest.fixture(scope='session')
def sqlalchemy_connect_url():
    return dsn + '_test'


@pytest.fixture(scope='session', autouse=True)
def tables(engine, db_schema):
    Base.metadata.create_all(engine)


# def test_example_service(dbsession):
#     assert dbsession.query(UselessModel).count() == 0
#     some_number = 2
#
#     example_service(example_argument=some_number, session=dbsession)
#
#     assert dbsession.query(UselessModel).one().number == some_number


def test_enrolling(dbsession):
    student = Student(student_no='AZB123', first_name='John', last_name='Doe')
    course = Course(name='Maths', exam_type='speaking', enrolled_no=0)
    dbsession.add(student)
    dbsession.add(course)
    dbsession.flush()

    enrolling_course(course.id, student.id, session=dbsession)

    assert course.enrolled_no == 1

