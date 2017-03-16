# -*- coding: utf-8 -*-
import difflib
import tempfile
import gzip


def diff(s1, s2):
    """Compare two strings.

    :param s1, s2: two strings to compare
    :return: a string that represents the diff between the input strings
    """
    return ''.join(difflib.ndiff(
        s1.splitlines(keepends=True),
        s2.splitlines(keepends=True)
    ))


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