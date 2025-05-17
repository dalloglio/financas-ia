FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PIP_NO_CACHE_DIR=off

CMD ["python", "/app/src/main.py"]
