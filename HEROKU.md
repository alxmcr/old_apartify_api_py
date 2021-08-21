# Heroku

## Create an app

```bash
heroku create

```
-> Example: `apartify-api-py.herokuapp.com`

## Heroku Enviroment Variables

**Project name**: `apartify-api-py`

```bash
heroku config:set ALLOWED_HOSTS=apartify-api-py.herokuapp.com
heroku config:set CORS_ALLOWED_ORIGINS=the-apartify-app.netlify.app
heroku config:set DJANGO_SETTINGS_MODULE=apartify_api_py.settings.heroku
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set WEB_CONCURRENCY=1
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