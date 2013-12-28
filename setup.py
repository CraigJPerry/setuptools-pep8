#!/usr/bin/env python
# encoding: utf-8


"""pep8 command for setuptools"""

from setuptools import setup, find_packages


__version__ = '0.9.0'
README = open('README.rst').read()
NEWS = open('NEWS.rst').read()
REQUIREMENTS = open('requirements.txt').readlines()


setup(
    name='setuptools-pep8',
    version=__version__,
    description=__doc__,
    long_description=README + '\n\n' + NEWS,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    entry_points={
        "distutils.commands": [
            "pep8 = setuptools_pep8.setuptools_command:Pep8Command",
        ]
    },

    author='Craig J Perry',
    author_email='craigp84@gmail.com',
    url='https://github.com/CraigJPerry/setuptools-pep8',
    license='BSD',
    keywords='pep8 setuptools command',
    classifiers=[
        "Topic :: Documentation",
        "Framework :: Setuptools Plugin",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: BSD License',
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)

