# mini-compose

A tiny subset of [Docker Compose](https://docs.docker.com/compose/) built on top of [Docker SDK](https://docker-py.readthedocs.io/en/stable/index.html).

## In a nutshell

Given a `mini-compose.yml` file like this:

```yaml
services:
  app:
    image: app:latest
    environment:
      - DB_ADDRESS
    ports:
      - 8000:80
```

Executing `mini-compose up` in the same directory as the file will:

- create a new bridge network
- start a container in the network running the image `app:latest`
- make the container reachable using the network alias `app`
- map the container port 80 to host port 8000
- pass the DB_ADDRESS environment variable from host to container

## Limitations

This tool supports only a tiny subset of Docker Compose features like:

- defining containers
- exposing container ports on the host
- passing environment variables to containers

There is no support for volumes for example.

## Disclaimer

This probably goes without saying, but you should _not_ use this for production. This was done just to take a peek at the Docker SDK.
