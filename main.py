from db import Session, engine, Base


def create_schema():
    Base.metadata.create_all(engine)


def teardown_schema():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    create_schema()
    try:
        # insert_initial_data()
        pass
    finally:
        teardown_schema()
