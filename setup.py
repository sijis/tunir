#!/usr/bin/env python
"""Tunir project"""
import sys
from setuptools import find_packages, setup


requirements = [
    'apache-libcloud',
    'paramiko',
    'pycrypto',
    'systemd-python',
    'typing',
]

if sys.version_info.major != 3:
    requirements.append(['mock'])

setup(name = 'tunir',
    version = '0.16',
    description = "Simple testing system.",
    long_description = "A simple testing system which can be maintained.",
    platforms = ["Linux"],
    author="Kushal Das",
    author_email="kushaldas@gmail.com",
    url="http://tunir.rtfd.org",
    license = "GPLv2+",
    install_requires=requirements,
    packages=find_packages(),
    data_files=[('share/tunir',
                  ['examples/default.json', 'examples/multihost.txt', 'examples/multihost.cfg',
                    'examples/default.txt', 'examples/vgt.json', 'examples/vgt.txt']),
        ('share/man/man8/', ['tunir.8'])],
    entry_points = {
          'console_scripts': [
              'tunir = tunirlib:startpoint'
          ]
      }
    )
