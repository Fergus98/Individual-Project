FROM python:3.7
WORKDIR /app
RUN apt-get update 
RUN apt-get install python3
RUN apt-get install python-pip -y
COPY ./requirements.txt /app 
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT ["/usr/local/bin/python", "app.py"]
