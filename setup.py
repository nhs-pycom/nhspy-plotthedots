"""
Template of setup.py.

See https://github.com/NHSDigital/rap-community-of-practice/blob/main/python/project-structure-and-packaging.md
"""

from setuptools import find_packages, setup

setup(
    name='nhspy-plotthedots',
    packages=find_packages(),
    version='0.1.6',
    description='Python SPC chart tool',
    author='NHS Python Community',
    license='MIT',
    setup_requires=['pytest-runner','flake8'],
    tests_require=['pytest'],
)
