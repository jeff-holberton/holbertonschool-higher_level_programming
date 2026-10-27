#!/usr/bin/python3
"""model state"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from model_state import Base


class City(Base):
    """city class"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
