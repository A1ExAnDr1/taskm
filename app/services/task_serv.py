from fastapi import Depends

from app.models.task_m import Task
from app.reps.task_repo import TaskRepo


class TaskServ:
    task_repo: TaskRepo

def __init__(self, task_repo: TaskRepo = Depends(TaskServ)) -> None:
        self.task_repo = task_repo

def get_tasks(self) -> list[Task]:
    return self.task_repo.get_tasks()

def create_task(self, task:Task) -> Task:
    return self.task_repo.create_task(task)

