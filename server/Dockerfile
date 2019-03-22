FROM python:3.7-alpine
MAINTAINER xlui <liuqi0315@gmail.com>
COPY . /data
WORKDIR /data
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ENTRYPOINT ["python", "manage.py", "runserver", "--host", "0.0.0.0"]
