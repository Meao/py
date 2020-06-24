# из существующего образа лёгкий линукс alpine
FROM python:alpine
# создаем и переходим в папку в образе
WORKDIR /usr/src/app
# в папку, в которую перешли, скопировать файл
COPY requirements.txt ./
# установка зависимостей для проекта из текстового файла
RUN pip install --no-cache-dir -r requirements.txt
# копировать из текущего на компе в текущий в образе
COPY . .
#
ENTRYPOINT [ "python" ]
#
CMD [ "main.py" ]


# Для сборки образа в папке 20191126_python
# запустите:
# docker build -t flask-app-demo:latest .

# Для запуска контейнера:

# docker run -d -p -rm 4321:4321 flask-app-demo
