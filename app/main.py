import asyncio
from fastapi import FastAPI, Depends, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import app.rabbitmq as rabbitmq
from app.endpoints.task_rout import tasks_router


app = FastAPI(title="Tasks Service", prefix='/api')


@app.on_event('startup')
def startup():
 loop = asyncio.get_event_loop()
 asyncio.ensure_future(rabbitmq.consume(loop))

app.include_router(tasks_router, prefix='/api')
