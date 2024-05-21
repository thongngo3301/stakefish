# App Development

Firstly, I updated the original `swagger.json`file with `/`, `/health` and `/metrics` path definitions. To faster my development process, I used `swagger-codegen-cli` to generate the base structure of the service.


# Local Testing

We will use `docker compose` to spin up the local environment for testing
```
docker compose up --build -d
```

# Helm Chart
I create a Helm chart for the application. For Prometheus and Redis, I wrap their existing Helm charts as sub-charts. Doing this will help the version maintenance become individually between services and we don't need to re-invent the wheel.

# CI Pipeline

I created the GitHub Actions pipeline to build the application image as well as the Helm charts to deploy the application yet also Prometheus and Redis instances

# DockerHub and ArtifactHub
Docker image:
```
docker pull thongngo3301/stakefish
```
Helm chart:
```
helm repo add thongngo https://thongngo3301.github.io/stakefish
helm search repo thongngo
```

# Further Implementation
I have not had enough time to create a production-ready chart which can have few more components. For example, I want to integrate with HashiCorp Vault via `vault-secrets-operator` so that our application can retrieve the database credentials dynamically from Vault. We don't need to store and rotate the database credentials manually anymore.
