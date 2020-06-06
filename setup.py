# -*- coding: utf-8 -*-
"""Setup.py for the dungeons project."""
from setuptools import find_packages, setup

install_requirements = [
    'pygame',
]

setup_requirements = []

test_requirements = [
    'pytest==5.4.1',
]

setup(
    name='dungeons',
    version='0.0.0',
    packages=find_packages(),
    url='https://github.com/gagelarsen/dungeons',
    license='',
    author='glarsen',
    author_email='gagelarsen53@gmail.com',
    description='A dungeon crawler generator',
    long_description=__doc__,
    setup_requires=setup_requirements,
    install_requires=install_requirements,
    tests_require=test_requirements,
)
