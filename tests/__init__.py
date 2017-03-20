# -*- coding: utf-8 -*-
import tempfile
import gzip


def temp_compress(filename):
    """Given a filename, compresses the file to a temporary file

    :param filename: input file to compress
    :return: filename of temporary compressed file and a string of the decompressed content
    """
    _, temp_filename = tempfile.mkstemp(suffix='.gz')
    with open(filename, 'rt') as fin, gzip.open(temp_filename, 'wt') as fout:
        content = fin.read()
        fout.write(content)
    return temp_filename, content