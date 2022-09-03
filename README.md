# mini-compose

A tiny [Docker Compose](https://docs.docker.com/compose/)'ish container orchestrator built on top of [Docker SDK](https://docker-py.readthedocs.io/en/stable/index.html).

## In a nutshell

Given a `mini-compose.yml` file like this:

```yaml
services:
  nginx:
    image: nginx:latest
    environment:
      - API_GATEWAY
    ports:
      - 8000:80
```

Executing `poetry run mini-compose up` in the same directory as the file will:

- create a new bridge network
- start a container in the network running the image `nginx:latest`
- make the container reachable using the network alias `nginx`
- map the container port 80 to host port 8000
- pass the `API_GATEWAY` environment variable from host to container

You can also tear down the stack using `poetry run mini-compose down`.

## Installation & usage

Using [Poetry](https://python-poetry.org):

```shell
# Install dependencies
poetry install

# Start stack
poetry run mini-compose up

# Tear down stack
poetry run mini-compose down
```

You can also use the `--file` flag to specify the YAML file to use if `mini-compose.yml` is not your thing.

## Limitations

This tool supports only a tiny subset of Docker Compose features like:

- defining containers
- exposing container ports on the host
- passing environment variables to containers

There is no support for volumes for example.

## Disclaimer

This probably goes without saying, but you should _not_ use this for production. This was done just to take a peek at the Docker SDK.
