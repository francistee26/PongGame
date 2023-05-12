#!/usr/bin/env python

from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='PongGame',
      version='0.1',
      description='Pong Game to test portability',
      author='Francis Tholley',
      author_email='francis.tholley@scranton.edu',
      url='',
      packages=['Pong Game'],
      install_requires=requirements
      )
