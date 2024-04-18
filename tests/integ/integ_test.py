import sys
from app.models.task_m import Task
from app.reps.task_repo import TaskRepo
import uuid
import pytest

BASE_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / 'services/app'))
#sys.path.append(str(BASE_DIR / 'movies_service/app'))
def test_task_repo():
 repo = TaskRepo()
 tasks = repo.get_tasks()
 assert isinstance(tasks, list)
 task = repo.create_task(Task(id=str(uuid.uuid4()), name='test', task_user=str(uuid.uuid4())))
 assert isinstance(task.id, uuid.UUID)
 assert character.name == 'test'
 assert isinstance(task.task_user, uuid.UUID)