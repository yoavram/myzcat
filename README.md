# myzcat
## An example Python project

[![Build Status](https://travis-ci.org/yoavram/myzcat.svg?branch=master)](https://travis-ci.org/yoavram/myzcat)

This is an example of a Python project.

The structure of the project is:

```
.
├── build
│   ├── bdist.macosx-10.9-x86_64
│   └── lib
│       ├── myzcat
│       │   ├── __init__.py
│       │   ├── cli.py
│       │   └── gzip_reader.py
│       └── tests
│           ├── __init__.py
│           ├── test_cli.py
│           └── test_gzip_reader.py
├── dist
│   ├── myzcat-0.1.0-py3-none-any.whl
│   └── myzcat-0.1.0.tar.gz
├── myzcat
│   ├── __init__.py
│   ├── cli.py
│   └── gzip_reader.py
├── myzcat.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── entry_points.txt
│   ├── requires.txt
│   └── top_level.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── test_cli.py
    └── test_gzip_reader.py
```

- The package source code is contained in `myzcat`.
  - `gzip_reader.py` has a single function that given a filename, opens it, decompresses the gzip compression, and returns the content as a string.
  - `cli.py` leverages `gzip_reader.py` to create a CLI using [`click`](http://click.pocoo.org), which allows to view gzipped text files from the command line by calling `myzcat <filename>`.
- The tests are in `tests` and can be run with `nose tests` after installing `nosetests` (`pip install nose`) or using `python setup.pt test`.
  - `__init__.py` defines utility functions for the tests
  - `test_gzip_reader.py` tests `gzip_reader.py`
  - `test_cli.py` tests `cli.py`
- `setup.py` is the package installer:
  - to install run `python setup.py install`
  - to install in developer mode, so that every change you make to the code will be reflected in the installed package, run `python setup.py develop`.
- `myzcat.egg-info` is the result of running `python setup.py install` and contains package definitions
- `dist` contains package distribution files, the results of running `python setup.py sdist bdist_wheel`
- `build` contains files related to building the package into a distributable file

Additional `setup.py` tasks can be found in the [docs](https://packaging.python.org) or if you use _PyCharm_, in the `Tools` menu, under `Run setup.py task...`.

## Dependencies

- To install, you might need `setuptools`
- To run, you will need `click`
- To test, you'll need to install `nose` or `py.test`
- To build a wheel file you will need `wheel`
