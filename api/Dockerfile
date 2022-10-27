FROM osgeo/gdal:ubuntu-small-3.4.1

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        python3-pip

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .