# APARTIFY - API REST

## Environment (Windows)

**Reference:** [How to install Django on Windows - Link](https://docs.djangoproject.com/en/3.2/howto/windows/)

```bash
py -m venv apartify_api_py
apartify_api_py/Scripts/activate.bat
```


## Setup

```bash
pip install -r requirements.txt
```

### Procfile

```
release: python manage.py migrate
web: gunicorn apartify_api_py.wsgi
```

### Make & Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```


### (optional) Development mode

```bash
python manage.py runserver --settings=apartify_api_py.settings.dev
```

### Create an administrator

```bash
python manage.py createsuperuser
```

### Fixtures

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