#!/usr/bin/env python
#
# Codeship-YAML, YAML configuration file support for Codeship.
# Copyright (C) 2016  Painless Software <info@painless.software>
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
    'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Build Tools',
]


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import shlex
        import sys
        import tox
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


class Clean(TestCommand):
    def run(self):
        from os import system
        system('find . -type f -name *.pyc -exec rm -v {} \;')
        system('find . -type d -name __pycache__ -exec rm -rv {} \;')
        system('find . -type d -name .tox  -exec rm -rv {} \;')
        system('find . -type d -name build -exec rm -rv {} \;')
        system('find . -type d -name dist  -exec rm -rv {} \;')
        system('find . -type d -name .eggs -exec rm -rv {} \;')
        system('find . -type d -name *.egg-info  -exec rm -rv {} \;')


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
    keywords='continuous integration, continuous delivery, '
             'devops, build server, infrastructure, tools',

    classifiers=CLASSIFIERS,
    install_requires=read_file('requirements.txt'),
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    zip_safe=False,

    tests_require=['tox'],
    cmdclass={
        'clean': Clean,
        'test': Tox,
    },
    entry_points={
        'console_scripts': [
            'codeship-yaml = codeship_yaml.main:main',
        ],
    },
)
