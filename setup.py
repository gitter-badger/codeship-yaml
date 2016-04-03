#!/usr/bin/env python
#
# Codeship-YAML, YAML configuration file support for Codeship.
# Copyright (C) 2016  Painless Software, Peter Bittner <peter@painless.software>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os.path import abspath, dirname, join
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import codeship_yaml as package
import sys

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Software Development :: Build Tools',
]


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def read_file(*pathname):
    with open(join(dirname(abspath(__file__)), *pathname)) as f:
        return f.read()


setup(
    name='codeship-yaml',
    version=package.__version__,
    author=package.__author__,
    author_email=package.__author_email__,
    maintainer=package.__maintainer__,
    maintainer_email=package.__maintainer_email__,
    url=package.__url__,
    license=package.__license__,

    description=package.__doc__.strip(),
    long_description=read_file('README.rst'),
    keywords='continuous integration, continuous delivery, devops, build server, infrastructure, tools',

    classifiers=CLASSIFIERS,
    install_requires=read_file('requirements.txt'),
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    zip_safe=False,

    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    entry_points={
        'console_scripts': [
            'codeship-yaml = codeship_yaml.main:main',
        ],
    },
)