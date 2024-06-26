from fastapi import Depends
from uuid import UUID
from app.models.task_m import Task
from app.reps.task_repo import TaskRepo


class TaskServ:
    task_repo: TaskRepo
    def __init__(self, task_repo: TaskRepo = Depends(TaskRepo)) -> None:
        self.task_repo = task_repo

    def get_tasks(self) -> list[Task]:
        return self.task_repo.get_tasks()
    def create_task(self, task:Task) -> Task:
        return self.task_repo.create_task(task)
    def get_task_by_id(self, id: UUID) -> Task:
        return self.task_repo.get_task_by_id(id)

    def delete_task_by_id(self, id: UUID) -> Task:
        return self.task_repo.delete_task_by_id(id)

    def get_task_by_name(self, name: str) -> list[Task]:
        return self.task_repo.get_tasks_by_name(name)