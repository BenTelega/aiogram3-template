FROM python:3.9.16-slim-buster

WORKDIR /app

COPY . . 

RUN pip install poetry
RUN poetry install 

WORKDIR /app/src

CMD [ "poetry", "run", "python", "app.py" ]