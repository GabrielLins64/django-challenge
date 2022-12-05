# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/
RUN apt-get update
RUN apt-get install -y dos2unix
RUN dos2unix /code/init/entrypoint.sh
RUN chmod +x /code/init/entrypoint.sh
CMD [ "sh", "/code/init/entrypoint.sh" ]
