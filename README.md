# template_api - API

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