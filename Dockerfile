# syntax=docker/dockerfile:1

FROM python:3.8-slim-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3300

ENV FLASK_APP=src/app.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=3300"]

