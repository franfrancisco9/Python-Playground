FROM python:3.10-slim

WORKDIR /app

ARG task1a="/Task 1A"
ARG task1b="/Task 1B"

ADD .${task1a}/caesar .
ADD .${task1b}/main.py .

COPY .${task1b}/requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["/app/main.py"]

