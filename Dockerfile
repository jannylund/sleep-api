FROM python:3.7-alpine

ADD app /app
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app
CMD python main.py