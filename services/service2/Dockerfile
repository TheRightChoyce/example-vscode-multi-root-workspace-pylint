# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

# Install pipenv
RUN pip install pipenv

# Set project/working directory
ENV SRC_DIR /usr/local/src/service2/src
WORKDIR ${SRC_DIR}

# Copy Pipefile * .lock file into prod directory
COPY Pipfile Pipfile.lock ${SRC_DIR}/

# Copy all the local files as well
COPY src/* ${SRC_DIR}/

# Send print and log statements directly to stdout
ENV PYTHONUNBUFFERED=1

# Install packages with pipenv
RUN pipenv install --system --deploy

# Run our server command
CMD [ "python3", "server.py"]
