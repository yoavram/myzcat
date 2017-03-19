# -*- coding: utf-8 -*-
import logging
import os

from .version import __version__
from .gzip_reader import read_gzip_file
from . import cli


logger = logging.getLogger()
handler = logging.FileHandler(
	os.path.join(os.getcwd(), "myzcat.log"))
handler.setFormatter(logging.Formatter(
	'%(asctime)s %(name)-12s %(levelname)-8s %(message)s'))
logger.addHandler(handler)
debug_level = logging.INFO
if os.environ.get("MYZCAT_DEBUG", "false").lower() == 'true':
	debug_level = logging.DEBUG
logger.setLevel(debug_level)


