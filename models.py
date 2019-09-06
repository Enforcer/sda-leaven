from sqlalchemy import Column, Integer

from db import Base


class UselessModel(Base):
    __tablename__ = 'useless_models'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)

