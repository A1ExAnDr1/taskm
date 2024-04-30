FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

#COPY ./ent.sh /code/ent.sh

#RUN chmod +x ./ent.sh
RUN pip install keycloak
#ENTRYPOINT ["sh","ent.sh"]
EXPOSE 80

CMD ["python", "servtwo.py"]