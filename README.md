
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

## Endpoints

- `/countries`
- `/countries/:pk`
- `/states`
- `/states/:pk`
- `/cities`
- `/cities/:pk`
- `/cities_hall`
- `/cities_hall/:pk`
- `/neighborhoods`
- `/neighborhoods/:pk`
- `/features`
- `/features/:pk`
- `/outdoor_spaces`
- `/outdoor_spaces/:pk`
- `/investments`
- `/investments/:pk`
- `/apartments`
- `/apartments/:pk`
- `/photos`
- `/photos/:pk`
- `/floor_plans`
- `/floor_plans/:pk`
- `/attracts`
- `/outdoors`
- `/invests`
  
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
python manage.py makemigrations
python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

Create an administrator

```bash
python manage.py createsuperuser
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

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`ALLOWED_HOSTS`

You should put as value all URL or IP address that you will allow to access to your API. 

`DJANGO_SETTINGS_MODULE`

What is the configuration that you would like to use: `apartify_api_py.settings.heroku` (Heroku) or `apartify_api_py.settings.dev` (Development).

`SECRET_KEY`

Django's secret key.

`DATABASE_URL`

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

![Admin cities](https://res.cloudinary.com/images-alex-projects/image/upload/v1628913261/Portfolio/appartify-assets/backend-api/apartify-endpoint-cities-admin_l2hjjv.png)

![Endpoint cities](https://res.cloudinary.com/images-alex-projects/image/upload/v1628913151/Portfolio/appartify-assets/backend-api/apartify-endpoint-cities_zivy3m.png)


  
## Demo

[https://apartify-api-py.herokuapp.com/cities](https://apartify-api-py.herokuapp.com/cities)

  
## Authors

- [Alejandro M. Coca Rojas (@alxmcr)](https://www.github.com/alxmcr)

  
## Feedback

If you have any feedback, please reach out to us at amcocarojas@gmail.com.

  