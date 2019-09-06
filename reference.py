"""Ten plik nie jest przeznaczony do bezposredniego uzywania, ma tylko sluzyc jako punkt odniesienia :)"""
from sqlalchemy import Integer, Boolean, Text, DateTime, Date, Column, String, Numeric, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Auction(Base):
    """Proto-klasa aukcji, pokazujaca wszystkie przydatne na co dzien typy"""
    id = Column(Integer, primary_key=True)
    is_suspended = Column(Boolean, default=False, nullable=False)
    starting_price = Column(Numeric, nullable=False)
    title = Column(String(80), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    ends_at = Column(DateTime, nullable=False)
    shipping_date = Column(Date)


"""Relacje - 1 do 1"""
class Parent(Base):
    __tablename__ = 'parent'

    id = Column(Integer, primary_key=True)
    child = relationship("Child", uselist=False, backref="parent")


class Child(Base):
    __tablename__ = 'child'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", backref="child")


"""Relacja 1 do wielu"""
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))


"""Relacja wiele do wielu"""
association_table = Table('association', Base.metadata,
    Column('parent_id', Integer, ForeignKey('parent.id')),
    Column('child_id', Integer, ForeignKey('child.id'))
)


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", secondary=association_table)


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
