FROM ubuntu:20.10

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py ./
COPY templates ./templates

ENV FLASK_APP app.py

EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]