# Foodie
Local Market app for HackYeah.

## Requirements
To work with this repo you should have preinstalled:
* Docker Desktop
* Serverless Framework
* Node Package Manager
* Make

## Setup
Create app in Serverless dashboard and set
 `service`, `app` and `org` in Serverless config file
```
nano serverless.yml
```

Fill in secrets
```
cp .env.sample .env && nano .env
```

Set the same secrets in Serverless Dashboard
```
make db
```

Install deployment deps
```
make install-deps
```

## Development

For local development
```
make rebuild
```

For Django shell
```
make shell
```

For running migrations
```
make migrate
```

## Deployment

For remote deployment
```
make deploy
```

For remote migrations
```
make remote-migrate
make remote-migrate-logs
```
