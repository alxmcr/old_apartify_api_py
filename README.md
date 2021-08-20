
# Apartify API REST

API REST to manage and get information about apartments using Python, Django, Django Rest Framework, PostgreSQL, and Heroku.

## Features

- Django Admin
- Database: PostgreSQL
- Models
- Migrations
- Fixtures
- URLS (and operations like `GET`, `POST`, `PUT`, and `DELETE`)
- Enabled CORS
- Django Admin filters

## Endpoints `/v2`

- `/v2/countries`
- `/v2/countries/:pk`
- `/v2/states`
- `/v2/states/:pk`
- `/v2/cities`
- `/v2/cities/:pk`
- `/v2/cities_hall`
- `/v2/cities_hall/:pk`
- `/v2/neighborhoods`
- `/v2/neighborhoods/:pk`
- `/v2/features`
- `/v2/features/:pk`
- `/v2/outdoor_spaces`
- `/v2/outdoor_spaces/:pk`
- `/v2/investments`
- `/v2/investments/:pk`
- `/v2/apartments`
- `/v2/apartments/:pk`
- `/v2/photos`
- `/v2/photos/:pk`
- `/v2/floor_plans`
- `/v2/floor_plans/:pk`
- `/v2/attracts`
- `/v2/outdoors`
- `/v2/invests`
  
## Lessons Learned

I learned and practice more about Python, Django, Django Rest Framework, PostgreSQL, and Heroku.

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/alxmcr/apartify_api_py
```

Go to the project directory

```bash
  cd apartify_api_py
```

Install Python packages

```bash
  pip install -r requirements.txt
```

Make & Run Migrations

```bash
# (optional) If you modify the migration
python manage.py makemigrations
# create tables & relationships
python manage.py migrate
```

Run fixtures

```bash
python manage.py loaddata fixtures/countries
python manage.py loaddata fixtures/states
python manage.py loaddata fixtures/cities
python manage.py loaddata fixtures/cities_hall
python manage.py loaddata fixtures/neighborhoods
python manage.py loaddata fixtures/features
python manage.py loaddata fixtures/outdoor_spaces
python manage.py loaddata fixtures/investments
python manage.py loaddata fixtures/apartments
python manage.py loaddata fixtures/photos
python manage.py loaddata fixtures/floor_plans
python manage.py loaddata fixtures/attracts
python manage.py loaddata fixtures/outdoors
python manage.py loaddata fixtures/invests
```

Start the server

```bash
python manage.py runserver
```

Create an administrator (If you want to use Djando admin site `/admin`)

```bash
python manage.py createsuperuser
```
  
## Environment Variables

To run this project, you will need to add the following environment variables.

`ALLOWED_HOSTS`

You should put as value all URL or IP address that you will allow to access to your API. 

`CORS_ALLOWED_ORIGINS`

List of origins authorized to make requests. For example: `the-apartify-app.netlify.app`.

`DJANGO_SETTINGS_MODULE`

What is the configuration that you would like to use: `apartify_api_py.settings.heroku` (Heroku) or `apartify_api_py.settings.dev` (Development).

`SECRET_KEY`

Django's secret key.

`DATABASE_URL`
(optional: It could be provided by Heroku)

PostgreSQL's url (or other database engine)

(specially in Heroku) `WEB_CONCURRENCY`

How many dynos do you use for your API?

  
## Tech Stack

- `python`: 3.9.6
- `django`: 3.2.6
- `djangorestframework`: 3.12.4
- `django-environ-2`: 2.1.0
- `psycopg2`: 2.9.1
- `gunicorn`: 20.1.0
- `dj_database_url`: 0.5.0
- `whitenoise`: 5.3.0
- `colorama`: 0.4.4
- `django-cors-headers`: 3.8.0
- `django-filter`: 2.4.0

  
## Screenshots

![Django admin](https://res.cloudinary.com/images-alex-projects/image/upload/v1628912993/Portfolio/appartify-assets/backend-api/django-admin-apartify_tulaqa.png)

![Admin Apartments](https://res.cloudinary.com/images-alex-projects/image/upload/v1629502178/Portfolio/appartify-assets/backend-api/django-admin-apartments_infu7t.png)

![Endpoint Apartments](https://res.cloudinary.com/images-alex-projects/image/upload/v1629502177/Portfolio/appartify-assets/backend-api/endpoint-apartments_xt6ham.png)


  
## Demo

[https://apartify-api-py.herokuapp.com/cities](https://apartify-api-py.herokuapp.com/cities)

  
## Authors

- [Alejandro M. Coca Rojas (@alxmcr)](https://www.github.com/alxmcr)

  
## Feedback

If you have any feedback, please reach out to me at amcocarojas@gmail.com.

  