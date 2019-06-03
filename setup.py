#!/usr/bin/env python

import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = 's3-app'
DESCRIPTION = 's3-app'
URL = 'https://github.com/plavreshin/s3-app'
EMAIL = ''
AUTHOR = ''
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.0.1'

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


# Where the magic happens:
setup(
    name="s3-app",
    version="0.0.1",
    description="",
    long_description="long_description",
    long_description_content_type='text/markdown',
    author="",
    author_email="",
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    entry_points={
        'console_scripts': ['app=app:main.cli'],
    },
    install_requires=[
        "botocore>=1.12.91,<1.12.92", 
        "aiobotocore==0.10.2", 
        "boto3==1.9.91",
        "click"],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "pytest-runner",
            "black",
            "flake8",
            "mypy",
            "isort",
            "autoflake",
        ]
    },
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
