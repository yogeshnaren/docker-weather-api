# Docker Container for Weather Forecast REST Dynamic UI.
_Full Python 3 Docker Container Image that encapsulates full REST API Webservice and UI with graphs for Weather Forecast._

_Yahoo Weather API is used for current weather forecast_

### AIM:
Creating a docker image compressed file for running Weather API UI on a single instance.

### WORKING:

#### Weather Information Graph:
Weather information is forecasted for 6 days including the specified date in the date picker. 
The information is plotted in a graph powered by CanvasJS. Date is retrieved from Django database and current forecast is powered by Yahoo Weather API.

### STEPS FOR CREATING A DOCKER CONTAINER IMAGE:

A directory “Docker Workspace” is created in the system 
```
$cd Docker\ Workspace
$git clone https://github.uc.edu/bundeyyn/dynamicUI-weather-forecast.git
$cd dynamicUI-weather-forecast
$vi Dockerfile
```
*Dockerfile:*

```
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
```

```
$docker build -t dynamic-rest-ui .
$docker run -p 80:8080 dynamic-rest-ui
```
```
$docker images
$docker save -o dynamic-rest-ui.tar dynamic-rest-ui
```

To retrieve, load and run:
```
$docker load -i dynamic-rest-ui.tar
$docker run -p 80:8080 dynamic-rest-ui
```


### TECHNOLOGIES USED:

* Programming language : Python
* Container :     Docker
* Framework :  		Django Rest Framework
* WebAPI : 			Swagger
* DB     : 			SQLite (Django Internal)
* Dynamic UI : Javascript, jQuery
* Graph Plotting  : CanvasJS


### LINKS:
 
* "docker_image_url": 	"https://s3.us-east-2.amazonaws.com/dynamic-rest-ui-docker-image/dynamic-rest-ui.tar",
* "doc_url"  : 	"https://github.uc.edu/bundeyyn/docker-django-weather-api/blob/master/README.md"
