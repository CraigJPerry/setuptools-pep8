#!/usr/bin/env python
# encoding: utf-8


import sys
import setuptools
from distutils import log
from pep8 import StyleGuide


class Pep8Command(setuptools.Command):
    description = "run pep8 on all your modules"
    user_options = [
        ('pep8-output=', None, "output report into this file"),
    ]

    def initialize_options(self):
        self.pep8_output = None

    def finalize_options(self):
        if self.pep8_output:
            self.pep8_output = open(self.pep8_output, 'w')

    def run(self):
        if self.pep8_output:
            stdout, sys.stdout = sys.stdout, self.pep8_output
            stderr, sys.stdout = sys.stderr, self.pep8_output

        pep8style = StyleGuide(parse_argv=False, config_file=True)
        options = pep8style.options
	options.exclude.extend(['test', 'tests'])
        report = pep8style.check_files(["."])

        if options.statistics:
            report.print_statistics()
        if options.benchmark:
            report.print_benchmark()
        if report.total_errors:
            if options.count:
                log.error("Total Errors: " + str(report.total_errors))

        if self.pep8_output:
            sys.stdout = stdout
            sys.stderr = stderr
            self.pep8_output.close()

