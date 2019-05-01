FROM python:3.8.0a3-alpine3.9

RUN pip install flask couchdb

COPY *.py /
WORKDIR /
CMD python -m app
