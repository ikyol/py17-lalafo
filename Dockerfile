FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN mkdir /app-py17

WORKDIR /app-py17

RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt /app-py17

RUN pip install -r requirements.txt

COPY . /app-py17/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]