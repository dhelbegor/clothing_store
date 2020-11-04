FROM python:3.7-alpine

ARG DOCKER_GROUP_ID
ARG DOCKER_USER_ID
ARG APP_ENV=dev
ENV GROUP_ID=$DOCKER_GROUP_ID USER_ID=$DOCKER_USER_ID APP_ENV=$APP_ENV

RUN mkdir -p /code/

WORKDIR /code

RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base jpeg-dev zlib-dev

RUN pip install --no-cache-dir pipenv pip setuptools -U
RUN rm -rf /var/cache/apk/*

COPY ./Pipfile ./Pipfile.lock ./

RUN pipenv install --deploy

ENTRYPOINT ["pipenv", "run"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000/tcp

HEALTHCHECK --interval=6s --timeout=3s CMD wget --quiet --tries=1 --spider http://localhost:8000/ || exit 1
