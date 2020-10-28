# base image
FROM python:3.8

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# create and set working directory
RUN mkdir /wealthy
WORKDIR /wealthy

# add current directory code to working directory
COPY . /wealthy/

# set project enviroment variables
# grab these via python os.environ
ENV PORT=8888

# set default enviroment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# install enviroment dependencies
RUN pip3 install --upgrade pip

# copy and install requirements.txt
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

# install market-data mongodb handler
RUN cd market-data/ && pip3 install .

EXPOSE 8888

CMD ./process_runner.sh $PORT
