from distutils.core import setup

setup(
    name='django-service-skeleton',
    version='0.0.1',
    packages=[
        'djangoserviceskeleton',
    ],
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    install_requires=[
        'South==0.8.4',
        'psycopg2==2.5.1',
    ],
)