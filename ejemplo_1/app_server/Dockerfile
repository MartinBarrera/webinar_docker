FROM python:3.7

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
CMD gunicorn --bind 0.0.0.0:5000 --workers 2 server:app