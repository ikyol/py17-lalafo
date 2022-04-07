FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFED=1

RUN mkdir /app-py17

WORKDIR /app-py17

RUN apt update

RUN pip install --upgrade pip

COPY requirements.txt /app-py17/

RUN pip install -r requirements.txt

COPY . /app-py17/

CMD ["python", "manage.py"]