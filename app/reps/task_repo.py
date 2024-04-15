import traceback
from sqlalchemy.orm import Session
from uuid import UUID, uuid4

from app.database import get_db
from app.models.task_m import Task
from app.models.user_m import User
from app.schemas.character import Character as DBCharacter

class TaskRepo:
  db: Session

  def __init__(self):
      self.db = next(get_db())

  def __map_to_model(self, task: DBTask) -> Task:
      result = Task.model_validate(task, strict=False)
      return result

  def __map_to_schema(self, task: Task) -> DBTask:
      data = dict(task)
      return DBTask(**data)

  def get_tasks(self) -> list[Task]:
      return [self.__map_to_model(c) for c in self.db.query(DBTask).all()]

  def create_task(self, task: Task) -> Task:
      try:
          task.id = uuid4()
          db_task = self.__map_to_schema(task)
          self.db.add(db_task)
          self.db.commit()
          return self.__map_to_model(db_task)
      except:
          traceback.print_exc()
          raise KeyError
