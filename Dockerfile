FROM python:alpine3.7
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev
ADD app.py /facility-scoring/
COPY templates /facility-scoring/templates/
COPY static /facility-scoring/static/
ENV FS_DB="postgres://doadmin:m2udda79zsz7fb6o@db-rankings-postgresql-lon-do-user-1289704-0.db.ondigitalocean.com:25060/rankings?sslmode=require"
RUN pip install Flask Flask-SQLAlchemy psycopg2 twilio
EXPOSE 8080
CMD python3 ./facility-scoring/app.py
