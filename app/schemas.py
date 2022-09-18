from datetime import datetime
from enum import Enum
from lib2to3.pgen2.token import OP
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi import Query


class SystemItemType(str, Enum):
    FILE = 'FILE'
    FOLDER = 'FOLDER'


class SystemItemImport(BaseModel):
    id: str
    type: SystemItemType
    url: Optional[str] = Field(default=None, max_length=255)
    parentId: Optional[str] = Field(default=None)
    size: Optional[int] = Field(default = 0, ge=0)
    date: Optional[datetime]

    class Config:
        orm_mode=True


class Udpates(BaseModel):
    item_id: str
    date: datetime

    class Config:
        orm_mode=True
