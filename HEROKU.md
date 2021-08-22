# Heroku

## Create an app

```bash
heroku create

```
-> Example: `apartify-api-py.herokuapp.com`

## Heroku Enviroment Variables

**Project name**: `apartify-api-py`

```bash
# ALLOWED_HOSTS: Without prefix http:// or https://
heroku config:set ALLOWED_HOSTS=apartify-api-py.herokuapp.com -a apartify-api-py
heroku config:set CORS_ALLOWED_ORIGINS=apartify-app.netlify.app -a apartify-api-py
heroku config:set DJANGO_SETTINGS_MODULE=apartify_api_py.settings.heroku -a apartify-api-py
heroku config:set SECRET_KEY="your-secret-key" -a apartify-api-py
heroku config:set WEB_CONCURRENCY=1 -a apartify-api-py
```

## Database

```bash
heroku addons
heroku addons:create heroku-postgresql:hobby-dev
```

## Deploy / Publish app

```bash
git push heroku main
```

## Heroku bash

```bash
heroku run bash --app apartify-api-py 
```

## Logs

```bash
heroku logs --tail
```

## Drop Heroku database

```bash
heroku pg:reset DATABASE_URL
```