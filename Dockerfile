FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# Копирование файлов alembic
COPY ./migrations /code/migrationss
COPY ./alembic.ini /code/alembic.ini
COPY ./entrypoint.sh /code/entrypoint.sh

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["sh","entrypoint.sh"]


