FROM python:3.12.4-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python -m pip install --upgrade pip

COPY requirements/base.txt requirements/base.txt
COPY src/apps/consumers/notifier src/apps/consumers/notifier
COPY src/contexts/notifications src/contexts/notifications
COPY src/contexts/shared src/contexts/shared

RUN pip install -r src/apps/consumers/notifier/requirements/base.txt

ENV PYTHONPATH=/usr/src/app:$PYTHONPATH

CMD ["python", "src/apps/consumers/notifier/main.py"]
