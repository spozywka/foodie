# Foodie
Local Market app for HackYeah.

## Requirements
To work with this repo you should have preinstalled:
* Docker Desktop
* Serverless Framework
* Node Package Manager

## Setup
Fill in secrets
```
cp .env.sample .env && nano .env
```

Install deployment deps
```
npm i
```

## Usage

For local development
```
docker-compose up -d
```

For remote deployment
```
serverless deploy
```
