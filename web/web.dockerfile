FROM python:3
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
COPY startWeb.sh /startWeb.sh
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir /static
RUN mkdir /src
VOLUME /src/

EXPOSE 8000


ENTRYPOINT ["sh", "startWeb.sh"]
