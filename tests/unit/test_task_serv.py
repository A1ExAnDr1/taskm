from app.models.task_m import Task
from app.models.user_m import User
import uuid

def test_task_model():
 task = Task(id=str(uuid.uuid4()), name='test',task_user=str(uuid.uuid4()))
 assert isinstance(task.id, uuid.UUID)
 assert character.name == 'test'
 assert isinstance(task_user.id, uuid.UUID)


def test_user_model():
 user = Equipment(id=str(uuid.uuid4()), name='test')
 assert isinstance(user.id, uuid.UUID)
 assert equipment.name == 'test'
