from python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8000

# Create directories app_home and static directories
ENV HOME=/app
ENV APP_HOME=/app/web
RUN mkdir $HOME
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
RUN chmod 777 $APP_HOME

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD pytest -s
