FROM python:3.10-buster

WORKDIR /app

# dockerizeをインストール
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY requirements.txt .

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

COPY . .

EXPOSE 8000

# dockerizeを使ってMySQLが利用可能になるまで待機し、その後uvicornでAPIサーバーを起動
CMD sh -c "dockerize -wait tcp://mysql:3306 -timeout 60s && uvicorn main:app --host 0.0.0.0 --port 8000"
