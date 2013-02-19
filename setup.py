#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='hc',
    version='2.0',
    description="",
    author="HospitalityClub",
    author_email='hello@cem-yildiz.com',
    url='',
    packages=find_packages(),
    package_data={'hc': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)