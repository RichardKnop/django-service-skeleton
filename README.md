django-service-skeleton
=======================

A sample Django application with a clean structure.
All apps live inside apps directory. Settings are inside proj/settings.
A proj/settings/local.py file defines environment specific settings.
This can be used as a starting point when building a RESTful web service.

Setup
-----

Create a virtual environment:

```
virtualenv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Create a local.py file and insert correct configuration details:

```
cp djangoserviceskeleton/proj/settings/local.example.py djangoserviceskeleton/proj/settings/local.py
nano cp djangoserviceskeleton/proj/settings/local.py
```

Run the migrations:

```
python djangoserviceskeleton/manage.py migrate
```

Run tests:

```
python djangoserviceskeleton/manage.py test
```