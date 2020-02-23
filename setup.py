#!/usr/bin/env python

from setuptools import setup,openshift, find_packages

setup(
    name='openshift',
    author='doraly',
    url="https://github.com/dodoche/openshift-python.git/",
    packages=find_packages('selector.py'),
    description='Python sample application'
    packages=find_packages(),
)
