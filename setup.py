# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = "django-dictionary",
    version = "0.1",
    author = "Luka Cehovin Zajc",
    description = "A Django app for community driven dictionary",
    long_description = open("README.md").read(),
    license = "MIT",
    url = "https://github.com/lukacu/django-dictionary",
    download_url = "https://github.com/lukacu/django-dictionary/archive/master.zip",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
