import os
from setuptools import setup, find_packages

with open('pylon/__version__.py') as fd:
    version = fd.read().split('=')[1].strip().strip("'")

with open('requirements-dev.txt') as fd:
    dev_requirements = fd.read().splitlines()

setup(
    name = "pylon",
    version = version,
    author = "Intelematics",
    license = "Apache-2.0",
    packages = find_packages(),
    #setup_requires=['pytest-runner'],
    tests_require=dev_requirements
)
