django-service-skeleton
=======================

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

Sync the database and run migrations:

```
python djangoserviceskeleton/manage.py syncdb
python djangoserviceskeleton/manage.py migrate fooservice
```

Run tests:

```
python djangoserviceskeleton/manage.py test
```