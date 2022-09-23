### Development

Build the images and spin up the containers:

```sh
$ docker-compose up -d --build
```

Test it out:

1. [http://fastapi.localhost:8008/](http://fastapi.localhost:8008/)
1. [http://fastapi.localhost:8081/](http://fastapi.localhost:8081/)

### Production

Update the domain in *docker-compose.prod.yml*, and add your email to *traefik.prod.toml*.

Build the images and run the containers:

```sh
$ docker-compose -f docker-compose.prod.yml up -d --build
```


### Access PG Admin

Access the PG Admin dashboard:

1. [http://localhost:15432/](http://localhost:15432/)

Login using the email and password specified on the docker-compose file.

To connect to the database register a new server.

The host will be the name given to the DB docker container on the docker-compose file. Use the port, user, password, and db specified for the Posgress.