FROM python:3.11.4-slim

RUN apt-get update -y && \
    apt-get upgrade -y

WORKDIR /techblog 

COPY ./requirements.txt /techblog/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./* /techblog

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]