FROM python:3.11.4-slim

RUN apt-get update -y && \
    apt-get upgrade -y

WORKDIR /techblog 

COPY ./requirements.txt /techblog/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./* /techblog

CMD ["python3", "main.py"]