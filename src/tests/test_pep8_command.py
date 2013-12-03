#!/usr/bin/env python
# encoding: utf-8


import unittest
import setuptools
from os.path import abspath, join, dirname
from setuptools_pep8.setuptools_command import Pep8Command
import subprocess


FIXTURES_DIR = abspath(join(dirname(__file__), "fixtures"))


class SetupCfgDirectives(unittest.TestCase):

    def test_case_is_setup_correctly(self):
        self.assertTrue(issubclass(Pep8Command, setuptools.Command))

    def test_can_use_excludes_parameter_in_setup_cfg(self):
        cmdline = ['python', 'setup.py', 'pep8']
        output = subprocess.check_output(cmdline, stderr=subprocess.STDOUT, cwd=FIXTURES_DIR)
        self.assertNotIn("excdir", output)
        self.assertIn("incdir", output)


if __name__ == '__main__':
    unittest.main()
