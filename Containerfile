FROM --platform=linux/amd64 python:3.11.3-slim

USER root

ENV PYTHONBUFFERED=1

ENV PYTHONPATH=.

# setting up working dir

WORKDIR /usr/src/pcl

ADD src /usr/src/pcl

COPY src/requirements.txt .


# upgrade and install necessary packages

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt



# set user permissions to workdir to be non-root user

RUN chown -R 1001:1001 .

USER 1001


# port exposure for container to show website

EXPOSE 8080

ENTRYPOINT ["python", "main.py"]
