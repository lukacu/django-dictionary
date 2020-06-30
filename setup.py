# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from os.path import join, dirname, abspath, isfile

this_directory = abspath(dirname(__file__))
install_requires = []
if isfile(join(this_directory, "requirements.txt")):
    with open(join(this_directory, "requirements.txt"), encoding='utf-8') as f:
        install_requires = f.readlines()

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
    install_requires=install_requires,
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
