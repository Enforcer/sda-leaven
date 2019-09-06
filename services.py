from db import with_session
from models import UselessModel


@with_session
def example_service(example_argument: int, session=None):
    print(example_argument, session)
    session.add(UselessModel(number=example_argument))
