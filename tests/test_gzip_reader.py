# -*- coding: utf-8 -*-
import gzip
import os
import tempfile
from unittest import TestCase, main

import myzcat
from tests import diff, temp_compress


class GzipReaderTestCase(TestCase):
    def setUp(self):
        self.filename, self.string = temp_compress(__file__)

    def tearDown(self):
        os.remove(self.filename)

    def test_read_gzip_file(self):
        string = myzcat.read_gzip_file(self.filename)
        assert self.string == string, diff(self.string, string)
