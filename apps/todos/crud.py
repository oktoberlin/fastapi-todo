from sqlalchemy.orm import Session

from apps.todos import models, schemas

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todos).offset(skip).limit(limit).all()


def create_user_todo(db: Session, todos: schemas.TodoCreate, user_id: int):
    db_todo = models.Todos(**todos.model_dump(), user_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
