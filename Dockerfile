FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV FLASK_APP main.py 

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0"]
