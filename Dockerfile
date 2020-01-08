FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

ENV UWSGI_CHEAPER 8
ENV UWSGI_PROCESSES 16
ENV UWSGI_INI /app/uwsgi.ini

WORKDIR /app

# 更换源
COPY ./pip.conf /root/.pip/pip.conf

# 安装依赖
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtion \
    && echo "Asia/Shanghai" > /etc/timezone