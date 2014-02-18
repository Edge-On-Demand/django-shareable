#!/usr/bin/env python
from setuptools import setup, find_packages

import django_social_share

setup(
    name = "django-social-share",
    version = django_social_share.__version__,
    description = "Templatetags for 'tweet this' and 'share on facebook'",
    packages = find_packages(),
    package_data = {
        'django_social_share': [
            'templates/*.*',
            'templates/*/*.*',
            'templates/*/*/*.*',
            'static/*.*',
            'static/*/*.*',
            'static/*/*/*.*',
        ],
    },
    url = 'https://github.com/chrisspen/django-social-share',
    license = 'MIT',
    author = 'Chris Spencer',
    author_email = 'chrisspen@gmail.com',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: LGPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe = False,
    install_requires = ['Django>=1.4.0'],
)
