=========================
 Setuptools pep8 command
=========================

Based on https://github.com/johnnoone/setuptools-pylint

This package exposes the `pep8`_ style guide checker as a
sub-command of setup.py::

    $ cat setup.cfg
    ...
    [pep8]
    ignore=E225
    ...
    $ python setup.py pep8

This invokes ``pep8`` and applies any configuration from your
``setup.cfg`` file's ``[pep8]`` section.

.. _`pep8` : http://pypi.python.org/pypi/pep8

