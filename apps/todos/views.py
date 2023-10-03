from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from . import crud, models, schemas
from core.settings import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{user_id}/todos/", response_model=schemas.Todos)
def create_todo_for_user(
    user_id: int, todos: schemas.TodoCreate, db: Session = Depends(get_db)
):
    return crud.create_user_todo(db=db, todos=todos, user_id=user_id)


@router.get("/todos/", response_model=List[schemas.Todos])
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos