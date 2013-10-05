#!/usr/bin/env python
# encoding: utf-8


"""pep8 command for setuptools"""


from setuptools import setup, find_packages
import sys, os


VERSION = '0.1.3'
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


setup(name='setuptools-pep8',
    version=VERSION,
    description=__doc__,
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Topic :: Documentation",
        "Framework :: Setuptools Plugin",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: BSD License',
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='pep8 setuptools command',
    author='Craig J Perry',
    author_email='craigp84@gmail.com',
    url='https://github.com/CraigJPerry/setuptools-pep8',
    license='BSD',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=['pep8'],
    entry_points={
        "distutils.commands": [
            "pep8 = setuptools_pep8.setuptools_command:Pep8Command",
        ]
    }
)

