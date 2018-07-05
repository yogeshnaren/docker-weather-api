FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python","manage.py","makemigrations"]
CMD ["python","manage.py","migrate"]
CMD ["python","manage.py","runserver","0.0.0.0:8080"]