FROM python:alpine3.7
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev
ADD app.py /facility-scoring/
COPY templates /facility-scoring/templates/
COPY static /facility-scoring/static/
RUN pip install Flask Flask-SQLAlchemy psycopg2
EXPOSE 8080
CMD python3 ./facility-scoring/app.py
