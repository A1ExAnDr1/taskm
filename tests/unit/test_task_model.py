from app.services.task_serv import TaskServ
from app.reps.task_repo import TaskRepo
from app.models.task_m import Task
import uuid
from unittest.mock import Mock
from app.models.task_m import Task
from app.models.user_m import User
import uuid


def test_task_model():
 task = Task(id=str(uuid.uuid4()), name='test', task_user=str(uuid.uuid4()))
 assert isinstance(task.id, uuid.UUID)
 assert task.name == 'test'
 assert isinstance(task.task_user, uuid.UUID)


def test_user_model():
 user = User(id=str(uuid.uuid4()), name='test')
 assert isinstance(user.id, uuid.UUID)
 assert user.name == 'test'