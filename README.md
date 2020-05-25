# Devops

## Installation

Make sure Docker is installed and running and run :

```bash
docker-compose build
docker-compose up
```

## Endpoints

Data REST API: http://localhost:3000

Dashboard UI: http://localhost:8080

## Jenkins (CI/CD)

```bash
docker network create jenkins
docker volume create jenkins-certs
docker volume create jenkins-data

docker container run
  --name jenkins
  --rm
  --detach
  --privileged
  --network jenkins
  --network-alias docker
  --env DOCKER_TLS_CERTDIR=/certs
  --volume jenkins-certs:/certs/client
  --volume jenkins-data:/var/jenkins_home
  --publish 2376:2376
  docker:dind

  docker container run
  --name jenkins-blueocean
  --rm
  --detach
  --network jenkins
  --env DOCKER_HOST=tcp://docker:2376
  --env DOCKER_CERT_PATH=/certs/client
  --env DOCKER_TLS_VERIFY=1
  --publish 8080:8080
  --publish 50000:50000
  --volume jenkins-certs:/certs/client:ro
  --volume jenkins-data:/var/jenkins_home
  jenkinsci/blueocean
```

```bash

```

## Team

- Alexandre Suchot ([AlexSuchot](https://github.com/AlexSuchot))
- Corentin Guillard ([CorentinGlrd5](https://github.com/CorentinGlrd5))
- Marceau David ([marceaudavid](https://github.com/marceaudavid))

```

```
