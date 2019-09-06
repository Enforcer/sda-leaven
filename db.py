import functools

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings

dsn = f'mysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}/{settings.DB_NAME}'
engine = create_engine(dsn, echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()


def with_session(fun):
    @functools.wraps(fun)
    def wrapped(*args, **kwargs):
        if 'session' in kwargs:
            return fun(*args, **kwargs)

        session = Session()
        try:
            result = fun(*args,  session=session, **kwargs)
            session.commit()
            return result
        except:
            session.rollback()
            raise

    return wrapped
