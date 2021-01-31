FROM python:3.6.12-slim

USER root

WORKDIR /vercode

COPY requirements.txt requirements.txt
COPY gunicorn.conf.py gunicorn.conf.py
COPY run.py run.py
# docker pull alpine/opencv:latest
# apk --update add --no-cache python3 python3-dev py3-pip
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# pip install Cython numpy
# && yum install mesa-libGL.x86_64 -y
RUN apt update && apt install -y libgl1-mesa-glx libglib2.0-dev\
    && pip install --upgrade pip -i https://mirrors.cloud.tencent.com/pypi/simple\
    && pip install --no-cache-dir scikit-build gunicorn gevent -i https://mirrors.cloud.tencent.com/pypi/simple \
    && pip install --no-cache-dir -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple 

EXPOSE 4006
CMD ["gunicorn", "run:app", "-c", "./gunicorn.conf.py"]