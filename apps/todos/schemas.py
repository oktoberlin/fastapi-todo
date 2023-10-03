from typing import Union

from pydantic import BaseModel


class TodosBase(BaseModel):
    title: str
    description: Union[str, None] = None

class TodoCreate(TodosBase):
    pass


class Todos(TodosBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
