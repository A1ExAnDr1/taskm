from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Body
from app.models.task_m import Task
from app.models.user_m import User
from app.services.task_serv import TaskServ



tasks_router = APIRouter(prefix='/tasks', tags=['TASKS'])

tasks_service = Annotated[TaskServ, Depends(TaskServ)]

@tasks_router.get('/')
def get_tasks(
   service: tasks_service
):
   return service.get_tasks()

@tasks_router.post('/create_task')
def create_task(
   task: Task,
   service: tasks_service
):
   try:
       service.create_task(task)
       return task.dict()
   except:
       raise HTTPException(418, 'Errrrrorrre')
