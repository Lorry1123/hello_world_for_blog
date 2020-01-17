FROM python:3.8-slim

ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

ADD . /code
WORKDIR /code

CMD ["python", "app.py"]

EXPOSE 8080