FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd -r app && useradd -r -g app app

COPY --chown=app:app . ./

USER app

# CMD exec gunicorn --bind :80 --log-level info --workers 1 --threads 8 --timeout 0 app:server
CMD python app.py
