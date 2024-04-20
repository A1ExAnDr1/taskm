import sys
import pytest
import uuid
from pathlib import Path
from typing import Annotated


from fastapi import Depends
from app.models.task_m import Task
from app.reps.task_repo import TaskRepo
from app.services.task_serv import TaskServ
from sqlalchemy.orm import Session
from app.database import get_db
#

def test_task_repo():
  repo = TaskRepo()
  tasks = repo.get_tasks()
  assert isinstance(tasks, list)
  task = repo.create_task(Task(id=str(uuid.uuid4()), name='test', task_user=str(uuid.uuid4())))
  assert isinstance(task.id, uuid.UUID)
  assert task.name == 'test'
  assert isinstance(task.task_user, uuid.UUID)