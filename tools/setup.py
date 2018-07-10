#!/usr/bin/env python
# Copyright (c) 2018 G Adam Cox. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
_setup.py_

"""

from setuptools import setup, find_packages

from adstk.__info__ import __version__

setup_args = {
    'description': "Adam's Data Science Toolkit",
    'include_package_data': True,
    'install_requires': [],
    'name': 'adstk',
    'version': __version__,
    'author': 'gadamc',
    'author_email': 'gadamc@gmail.com',
    'url': 'https://github.com/gadamc/datachallenges/adstk',
    'packages': ['adstk'],
    'classifiers': [
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: Apache Software License',
          'Topic :: Software Development :: Libraries',
          'Development Status :: 2 - Pre-Alpha',
          'Programming Language :: Python :: 3.6'
      ]
}

setup(**setup_args)
