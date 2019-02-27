FROM python:alpine3.7
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev
ADD app.py /facility-scoring/
ADD /templates/app.html /facility-scoring/templates/
ADD /templates/site.html /facility-scoring/templates/
RUN pip install Flask Flask-SQLAlchemy psycopg2
EXPOSE 80
CMD python3 ./facility-scoring/app.py
