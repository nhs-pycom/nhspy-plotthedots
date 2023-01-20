"""
Template of setup.py.

See https://github.com/NHSDigital/rap-community-of-practice/blob/main/python/project-structure-and-packaging.md
"""

from setuptools import find_packages, setup

setup(
    name='nhspy-plotthedots',
    packages=find_packages(),
    version='0.1.0',
    description='Python SPC chart tool',
    author='NHS_Python_Community',
    license='',
    setup_requires=['pytest-runner','flake8'],
    tests_require=['pytest'],
)
