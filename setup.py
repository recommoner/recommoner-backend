from setuptools import find_packages, setup


test_requirements = [
    'pytest',
    'pytest-django',
]


setup(
    name="recommener-backend",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'argh',
        'argcomplete',
        'django==1.11',
        'django-enumfield>=1.3b2',
        'django-extensions',
        'djangorestframework==3.4.*',
        'psycopg2',
        'python-social-auth==0.2.21',
        'sqlalchemy',
    ],
    extras_require={
        'test': test_requirements,
    },
)

