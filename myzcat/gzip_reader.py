# -*- coding: utf-8 -*-
import gzip


def read_gzip_file(filename):
    with gzip.open(filename) as f:
        return f.read().decode('utf8')
