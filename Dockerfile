FROM python:3.10.9-alpine3.17

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY ./entrypoint.sh /
EXPOSE 8000

ENTRYPOINT ["sh", "/entrypoint.sh"]

