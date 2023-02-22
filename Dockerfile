FROM python:3.10-slim

WORKDIR /app

ARG task1a="/Task 1A"
ARG task1b="/Task 1B"
ARG task2="/Task 2"

ADD .${task1a}/caesar .
ADD .${task1b}/main.py .
ADD .${task2}/find_island .

COPY .${task1b}/requirements.txt .

RUN pip install -r requirements.txt
RUN ["chmod", "+x", "./caesar"]
RUN ["chmod", "+x", "./find_island"]

EXPOSE 8000

ENTRYPOINT ["/app/main.py"]

