from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import DateTime, Integer, String
from sqlalchemy.orm import relationship, backref
from db import Base


class SystemItem(Base):
    __tablename__ = 'system_items'

    id = Column(String, primary_key=True, nullable=False, index = True)
    type = Column(String, nullable = False)
    url = Column(String, nullable=True, default=None)
    parentId =  Column(String, ForeignKey('system_items.id'), nullable=True)
    size = Column(Integer, nullable=False, default = 0)
    date = Column(DateTime(timezone=True), nullable=False)

    children = relationship('SystemItem', backref=backref('parent', remote_side='SystemItem.id'))


class SystemItemHistory(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(String, ForeignKey('system_items.id'), nullable=False)
    date = Column(DateTime, nullable =False)
