from typing import List

from pydantic import BaseModel
from apps.todos.schemas import Todos
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Todos] = []

    class Config:
        from_attributes = True
