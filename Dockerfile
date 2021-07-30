FROM python:slim

RUN mkdir /src

WORKDIR /src

COPY shetran/shetran-linux shetran/shetran-prepare run.py ./
COPY shetran/lib /usr/lib/

RUN chmod +x shetran-linux

CMD python run.py
