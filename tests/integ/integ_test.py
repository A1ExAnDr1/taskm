import sys
import pytest
import uuid
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent


sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / 'app/services'))

from app.models.task_m import Task
from app.reps.task_repo import TaskRepo

def test_task_repo():
  repo = TaskRepo()
  tasks = repo.get_tasks()
  assert isinstance(tasks, list)
  task = repo.create_task(Task(id=str(uuid.uuid4()), name='test', task_user=str(uuid.uuid4())))
  assert isinstance(task.id, uuid.UUID)
  assert task.name == 'test'
  assert isinstance(task.task_user, uuid.UUID)