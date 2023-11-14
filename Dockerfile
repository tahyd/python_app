FROM python:3.6-slim
COPY ./app.py /deploy/
COPY ./app1.py /deploy/
COPY ./app2.py /deploy/
COPY ./app3.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./model_pickle /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 8081
ENTRYPOINT ["python", "app.py"]