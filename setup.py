#! /usr/bin/env python
"""
Setup for mwa-calplots
"""
import os
import sys
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    """Read a file"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    """Get the version number of AegeanTools"""
    import calplots
    return calplots.__version__


reqs =['numpy>=1.16',
       'matplotlib>=2.1.0',
       'astropy>=2.0.2',
       'six>=1.11']


setup(
    name="mwa-calplots",
    version=get_version(),
    author="Paul Hancock",
    author_email="Mr.Paul.Hancock@gmail.com",
    description="MWA convenience plotting tool.",
    url="https://github.com/MWATelescope/mwa-calplots",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=['calplots'],
    scripts=['scripts/aocal_plot.py'],
    install_requires=reqs,
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'nose']
)
