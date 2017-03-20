# -*- coding: utf-8 -*-
import gzip
import os
import tempfile
from unittest import TestCase, main

import myzcat
from tests import temp_compress


class GzipReaderTestCase(TestCase):
	def setUp(self):
		self.filename, self.string = temp_compress(__file__)

	def tearDown(self):
		os.remove(self.filename)

	def test_read_gzip_file(self):
		self.maxDiff = None
		string = myzcat.read_gzip_file(self.filename)
		self.assertEquals(string, self.string)
