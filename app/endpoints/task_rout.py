from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Body
from app.models.task_m import Task
from app.models.user_m import User
from app.services.task_serv import TaskServ
from uuid import UUID


tasks_router = APIRouter(prefix='/tasks')

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
       raise HTTPException( 'Errrrrorrre')
@tasks_router.get('/task_by_id/{id}')
def get_task_by_id(id: UUID, service: tasks_service):
    try:
        task = service.get_task_by_id(id)
        if task:
            return task.dict()
        else:
            raise HTTPException(status_code=404, detail='Task not found')
    except:
        raise HTTPException(status_code=500, detail='Error occurred while fetching the task by ID')
@tasks_router.delete('/delete_task/{id}')
def delete_task_by_id(id: UUID, service: tasks_service):
    try:
        service.delete_task_by_id(id)
        return {"message": "Task deleted successfully"}
    except KeyError:
        raise HTTPException(status_code=404, detail='Task not found')
    except:
        raise HTTPException(status_code=500, detail='An error occurred while deleting the task')
