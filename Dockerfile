FROM amd64/python:3.10-slim

WORKDIR /flask_resterant

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    pip install Flask Flask-RESTful Flask-SQLAlchemy Flask-Cors Flask-Login Flask-WTF WTForms wtforms.validators email_validator psycopg2-binary

COPY . .

CMD python server.py



