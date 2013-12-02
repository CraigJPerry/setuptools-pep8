#!/usr/bin/env python
# encoding: utf-8


import unittest
import setuptools
from setuptools_pep8.setuptools_command import Pep8Command


class SetupCfgDirectives(unittest.TestCase):

    def test_case_is_setup_correctly(self):
        self.assertTrue(issubclass(Pep8Command, setuptools.Command))


if __name__ == '__main__':
    unittest.main()
