FROM clojure:tools-deps

WORKDIR /app

COPY . /app

RUN clojure -m cljs.main --optimizations advanced --output-dir static/cljs -c todo.core

FROM ubuntu:18.04

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

COPY --from=0 /app/static/cljs /static/cljs

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENV FLASK_APP main.py 

EXPOSE 3000

CMD [ "flask", "run", "--host=0.0.0.0", "-p", "3000"]
