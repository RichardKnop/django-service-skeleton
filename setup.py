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
        'psycopg2==2.5.1',
    ],
)
