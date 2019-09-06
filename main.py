from db import engine, Base, with_session
from services import example_service


def create_schema():
    Base.metadata.create_all(engine)


def teardown_schema():
    Base.metadata.drop_all(engine)


@with_session
def insert_initial_data(session):
    print('Insert initial data', session)


if __name__ == '__main__':
    create_schema()
    try:
        insert_initial_data()
        # Call your services!
        example_service(example_argument=123)
    finally:
        teardown_schema()
