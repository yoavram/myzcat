# -*- coding: utf-8 -*-
import os
from unittest import TestCase, main

from click.testing import CliRunner

import myzcat
from tests import diff, temp_compress


class GzipReaderTestCase(TestCase):
    def setUp(self):
        self.filename, self.string = temp_compress(__file__)

    def tearDown(self):
        os.remove(self.filename)

    def test_main(self):
        runner = CliRunner()
        result = runner.invoke(myzcat.cli.main, [self.filename])
        assert result.exit_code == 0
        string = result.output[:-1] # without the final EOL inserted
        assert self.string == string, diff(self.string, string)
