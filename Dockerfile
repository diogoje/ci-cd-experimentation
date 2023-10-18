FROM python:alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install .

CMD ["python3", "app"]
