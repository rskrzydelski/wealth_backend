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
# TODO: grab these via python os.environ
ENV PORT=8888

# set default enviroment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# install enviroment dependencies
RUN pip3 install --upgrade pip

# install requirements.txt
RUN pip3 install -r requirements.txt

# install custom python libs
# mongomarket lib
RUN cd mongomarket-lib/ && python3 setup.py sdist bdist_wheel && pip install dist/mongomarket-lib-0.0.1.tar.gz
# coinmarketcapscrapper lib
RUN cd coinmarketcapscrapper-lib/ && python3 setup.py sdist bdist_wheel && pip install dist/coinmarketcapscrapper-lib-0.0.1.tar.gz
# alphavantage lib
RUN cd alphavantage-lib/ && python3 setup.py sdist bdist_wheel && pip install dist/alphavantage-lib-0.0.1.tar.gz

EXPOSE 8888

CMD ./process_runner.sh $PORT
