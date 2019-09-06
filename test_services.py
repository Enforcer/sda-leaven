import pytest

from db import dsn, Base
from models import UselessModel
from services import example_service


@pytest.fixture(scope='session')
def sqlalchemy_manage_db():
    return True


@pytest.fixture(scope='session')
def sqlalchemy_connect_url():
    return dsn + '_test'


@pytest.fixture(scope='session', autouse=True)
def tables(engine, db_schema):
    Base.metadata.create_all(engine)


def test_example_service(dbsession):
    assert dbsession.query(UselessModel).count() == 0
    some_number = 2

    example_service(example_argument=some_number, session=dbsession)

    assert dbsession.query(UselessModel).one().number == some_number
