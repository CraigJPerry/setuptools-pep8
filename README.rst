Setuptools pep8 command
=======================

.. image:: https://travis-ci.org/CraigJPerry/setuptools-pep8.png?branch=master
   :target: https://travis-ci.org/CraigJPerry/setuptools-pep8
.. image:: https://pypip.in/d/setuptools-pep8/badge.png
   :target: https://pypi.python.org/pypi/setuptools-pep8

Based on https://github.com/johnnoone/setuptools-pylint

This package exposes the `pep8`_ style guide checker as a
sub-command of setup.py::

    $ cat setup.py
    ...
        setup(
            name='your project',
            setup_requires=['setuptools-pep8']
        )
    ....
    $ cat setup.cfg
    ...
    [pep8]
    ignore=E225
    ...
    $ python setup.py pep8
    running pep8
    ./setup.py:41:1: W391 blank line at end of file

This invokes ``pep8`` and applies any configuration from your
``setup.cfg`` file's ``[pep8]`` section.

It skips packages named "test" or "tests".

.. _`pep8` : http://pypi.python.org/pypi/pep8

