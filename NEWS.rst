News
====

0.9.0
-----

*Release date: 29-Dec-2013*

Final major release before v1.0 (project goes into maint mode).

**Contains non-backwards-compatable changes!**

Bugfixes:

* Resolves clash with setuptools Command --verbose flag

Features:

* All pep8 cmdline options can now be specified on the ``python
  setup.py pep8`` command line
* pep8 return code is propagated to the ``python setup.py`` command
  return code

Non-Functional Changes:

* Drastic simplification of pep8 setuptools Command implementation
* Minor changes to testing code (adopt usage of process return code)

Backwards Incompatable Changes:

* --pep8-output option has been removed. Replace usage of this with
  shell redirection.
* --check-dirs option has been removed. Replace usage of this with
  pep8's --exclude option.

Any users wishing to retain these features are advised to stay on
version 0.2.0.

0.2.0
-----

*Release date: 28-Dec-2013*

* Stable build, promoted minor version. No functional changes.

0.1.7
-----

*Release date: 28-Dec-2013*

* Enabled Travis-CI integration testing
* Configured auto upload from Travis -> PyPI for tagged releases
* Minor formatting tweaks

0.1.6
-----

*Release date: Not released*

* Minor tweak to .rst syntax, fix rendering issues on PyPI

0.1.5
-----

*Release date: 3-Dec-2013*

* Bugfix: missing NEWS.rst in manifest

0.1.4
-----

*Release date: 3-Dec-2013*

* @yoloseem fixed indentation bug
* Fixed setup.cfg parsing of include / exclude directives

0.1.3
-----

*Release date: 6-Oct-2013*

* Fixed github issue #1: Setting pep8 directives in setup.cfg doesn't work
* Exposed --check-dirs= option to control which modules are checked
* Fixed incorrect handling of stdout/stderr when redirecting pep8 output to a file

0.1.2
-----

*Release date: 4-Oct-2013*

* Fork of https://github.com/johnnoone/setuptools-lint
* Adds in config parsing from setup.cfg
* Semantic versioning

