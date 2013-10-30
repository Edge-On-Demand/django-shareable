import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
requirements = []

setup(
    name = "django-social-share",
    version = "0.2.2",
    description = "Templatetags for 'tweet this' and 'share on facebook'",
    long_description = read('README.rst'),
    url = 'https://github.com/chrisspen/django-social-share',
    license = 'MIT',
    author = 'Chris Spencer',
    author_email = 'chrisspen@gmail.com',
    packages = find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires = requirements,
    test_suite = "nose.collector",
)
