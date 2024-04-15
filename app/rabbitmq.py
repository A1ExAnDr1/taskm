import json
import traceback
from asyncio import AbstractEventLoop
from aio_pika.abc import AbstractRobustConnection
from aio_pika import connect_robust, IncomingMessage

from app.settings import settings
from app.services.task_serv import TaskServ
from app.reps.task_repo import TaskRepo
from app.models.task_m import Task
from uuid import UUID

async def process_created_task(msg: IncomingMessage):
 try:
     data = json.loads(msg.body.decode())
     task = Task(
         id=UUID(data['id']),
         name=data['name'],
         task_user=data['id']
     )
     repo = TaskRepo()
     created_task = repo.create_task(task)
     await msg.ack()
     return created_task
 except:
     traceback.print_exc()
     await msg.ack()

async def process_get_task(msg: IncomingMessage):
 try:
     repo = TaskRepo()
     tasks = repo.get_tasks()
     await msg.ack()
     return tasks
 except:
     await msg.ack()



async def consume(loop: AbstractEventLoop) -> AbstractRobustConnection:
   connection = await connect_robust(settings.amqp_url, loop=loop)
   channel = await connection.channel()

   order_created_queue = await channel.declare_queue('created_task_queue', durable=True)
   order_paid_queue = await channel.declare_queue('get_tasks_queue', durable=True)

   await order_created_queue.consume(process_created_task())
   await order_paid_queue.consume(process_get_task())
   print('Started RabbitMQ consuming...')

   return connection
