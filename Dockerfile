FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
ENTRYPOINT ["python", "app.py", "runserver", "--host=0.0.0.0", "--port=5000"]