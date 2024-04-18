import traceback
from sqlalchemy.orm import Session
from uuid import UUID, uuid4

from app.database import get_db
from app.models.task_m import Task
from app.models.user_m import User
from app.schems.task_s import Task as DBTask

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

  def get_task_by_id(self, id: UUID) -> Task:
      db_task = self.db.query(DBTask).filter_by(id=id).first()
      if db_task is not None:
          return self.__map_to_model(db_task)
      else:
          # You may want to handle this scenario differently based on your requirements
          raise KeyError("Task not found with the provided ID")

  def delete_task_by_id(self, id: UUID) -> Task:
      db_task = self.db.query(DBTask).filter_by(id=id).first()
      if db_task:
          self.db.delete(db_task)
          self.db.commit()
      else:
          raise KeyError("Task not found with the provided ID")

  def get_tasks_by_name(self, name: str) -> list[Task]:
      db_tasks = self.db.query(DBTask).filter(DBTask.name == name).all()
      return [self.__map_to_model(db_task) for db_task in db_tasks]