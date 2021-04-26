# myzcat
## An example Python project

[![Build Status](https://travis-ci.org/yoavram/myzcat.svg?branch=master)](https://travis-ci.org/yoavram/myzcat)

This is an example of a Python project.

The structure of the project is:

```
.
├── LICENCE.txt
├── MANIFEST.in
├── README.md
├── build
│   ├── bdist.macosx-10.7-x86_64
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
│   ├── myzcat-0.1.2-py3-none-any.whl
│   └── myzcat-0.1.2.tar.gz
├── myzcat
│   ├── __init__.py
│   ├── cli.py
│   ├── gzip_reader.py
│   └── version.py
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
  - `version.py` contains the version info in a single variable, `__version__`.
- The tests are in `tests` and can be run with `nosetests tests` after installing `nose` or by calling `python setup.pt test`.
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
- To test, you'll need to install `nose`; for a test coverage report also install `coverage`
- To build a wheel binary distribution, you will need `wheel`

## Installing

You can [download the code as a ZIP file](https://github.com/yoavram/myzcat/archive/master.zip) or clone it with git using `git clone https://github.com/yoavram/myzcat.git`. 

If you downloaded a ZIP file extract it and open a terminal window in the extracted folder.
If you cloned the repository, open a terminal folder in the repository folder.

Then run `pip install .` (with a dot at the end) to install the package, or `pip install -e .` to install it in developer mode. You can also do the same actions with `python setup.py install` and `python setup.py develop`, but then you must install dependencies on your own.

You can also install directly from GitHub without downloading or cloning using `pip install git+https://github.com/yoavram/myzcat.git`.

## Developing

When continuing development, it is best to install in developer/editing mode (`pip install -e .` or `python setup.py develop`) so that any changes in the source code are reflected when importing the package in Python.

## Versioning

The package version is set in `myzcat/version.py` and is imported in `__init__.py` to the package namespace. 

From `setup.py`, the version is evaluated by reading `myzcat/version.py` and executing the code.

For other methods of versioning Python packages, see the [packaging docs](https://packaging.python.org/single_source_version/#single-sourcing-the-version).

## Packaging & Distributing

To distribute the package, run `python setup.py sdist bdist_wheel` to create a source distribution (`sdist`) and a wheel binary distribution (`bdist_wheel)`); the latter requires the `wheel` package to be installed.

To upload the package to [PyPI](http://pypi.python.org), register a username and password, install `twine`, then use `twine upload dist/*`.

You can also setup your own repository (instead of using PyPI) with [pypiserver](https://pypi.org/project/pypiserver/).

To install `pypi-server` and setup a local folder for the packages:
```
python -m pip install pypiserver  
mkdir ~/mypypi   
```
To start the server without authentication on localhost with port 8080:
```
pypi-server -p 8080 -P . -a . ~/mypypi &
```
To upload the package with `twine`:
```
twine upload dist/* --repository-url http://localhost:8080
```
To install the package from the local repository:
```
python -m pip install -i http://localhost:8080/simple myzcat
```


## Testing

The easiest way to test the app is to call 
```
nosetests tests
```

If you want a test coverage report, run:
```
nosetests tests --with-coverage --cover-package=myzcat
```

Additional tests should be added in the `tests` folder. 
Follow the same format as in the existing files, only functions with names starting with `test` will be used as tests.

## Logging

See the [logging](https://github.com/yoavram/myzcat/tree/logging) branch.