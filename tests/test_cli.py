# -*- coding: utf-8 -*-
import os
from unittest import TestCase, main

from click.testing import CliRunner

import myzcat
from tests import temp_compress


class CliTestCase(TestCase):
    def setUp(self):
        self.filename, self.string = temp_compress(__file__)

    def tearDown(self):
        os.remove(self.filename)

    def test_main(self):
        self.maxDiff = None
        runner = CliRunner()
        result = runner.invoke(myzcat.cli.main, [self.filename])
        self.assertEquals(result.exit_code, 0)
        string = result.output[:-1] # without the final EOL inserted
        self.assertEquals(string, self.string)

    def test_file_not_found(self):
        runner = CliRunner()
        result = runner.invoke(myzcat.cli.main, ['not_really_a_file.txt.gz'])
        self.assertNotEquals(result.exit_code, 0)

