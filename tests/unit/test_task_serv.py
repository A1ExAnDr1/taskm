from app.models.task_m import Task
from app.models.user_m import User
import uuid
from app.services.task_serv import TaskServ
from app.reps.task_repo import TaskRepo
from app.models.task_m import Task
import uuid
from unittest.mock import Mock
def test_task_service():
 repo = Mock(spec=TaskRepo)
 service = TaskServ(repo)

 task = Task(id=str(uuid.uuid4()), name='test', task_user=str(uuid.uuid4()))

 # Mocking the behavior of the repo
 repo.create_task.return_value = task
 repo.get_tasks.return_value = [task]

 # Testing create_task method
 created_task = service.create_task(task)
 assert created_task == task

 # Testing get_tasks method
 tasks = service.get_tasks()

 assert len(tasks) == 1
 assert tasks[0].id == created_task.id
 assert tasks[0].name == created_task.name
 assert tasks[0].task_user == created_task.task_user
