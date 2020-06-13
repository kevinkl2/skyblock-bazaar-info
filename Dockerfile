FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN cd /usr/local/bin
RUN ln -s /usr/bin/python3 python
RUN pip3 install --upgrade pip
COPY . /app
WORKDIR /app/flask
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]