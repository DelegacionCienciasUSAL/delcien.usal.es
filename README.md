# delcien.usal.es
Code repository for the web page of the student delegation of the Science Faculty from the University of Salamanca.

## 1. Setup
Project development is based on [docker-compose]( https://docs.docker.com/compose ). 
It is required to have [Python3](https://www.python.org/) installed for the initial configuration and docker-compose for the deploy of
the web page.

Upon start two different conatiners are created: one for the client and one for the server; each of them with 
their separate dependencies.

This helps managing one's machine, avoiding having to install globally depencies for each project or having conflicting
installations of the same software.

### 2. Development
Firstly run ```python3 configureWebPage.py``` to provide the platform a valid email, password and secret key for 
the webpage. After that, and once you have [docker-compose]( https://docs.docker.com/compose ) installed, it is only needed 
to run the following command to have both client and server up and running:
```
$ docker-compose up
```
Client site is available at __port 8000__ and the server at __port 80__. This setup is done for the server to be asked for
the page and serve static files directly, and redicrect the rest of requests to the container with the gunicorn workers 
reunning the Django platform.

*Be sure to remove the database file before rebuilding as it will have conflicts when trying to create a new superuser.*


## 3. Build
```$ docker-compose up --build``` will recreate the containers if changes to the platform or the Docker/Docker-compose files
are made. This is not needed if changes are made to the templates or static files; however static files will need for a 
re-collection of the static files:
```
docker exec delcienusales_delcien_1[id of the container] python src/manage.py collectstatic --noinput
```

