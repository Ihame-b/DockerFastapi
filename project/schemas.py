from pydoc import describe
from turtle import title
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class BookPublic(BaseModel):
    id: UUID
    title: str
    description: str
    condition: bool
    created_at: datetime
    


class BookCreate(BaseModel):
    title: str = Field(..., max_length=399)
    describe: str = Field(..., max_length=399)