FROM python:3.12.4-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python -m pip install --upgrade pip

COPY requirements/base.txt requirements/base.txt
COPY src/apps/webhooks src/apps/webhooks
COPY src/contexts/notifications src/contexts/notifications
COPY src/contexts/shared src/contexts/shared

RUN pip install -r src/apps/webhooks/requirements/base.txt

ENV PYTHONPATH=/usr/src/app:$PYTHONPATH

CMD ["uvicorn", "src.apps.webhooks.src.main:app", "--host", "0.0.0.0", "--port", "8000"]
