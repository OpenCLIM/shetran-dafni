FROM python:slim

RUN mkdir /src

WORKDIR /src

COPY cobres-model cobres-model
COPY shetran-linux run.py ./

RUN chmod +x shetran-linux

CMD python run.py
