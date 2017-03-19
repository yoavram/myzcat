# -*- coding: utf-8 -*-
import logging
import warnings

import click

import myzcat


@click.command()
@click.argument('filename', 
	type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True))
@click.version_option(version=myzcat.__version__)
def main(filename):
	logging.info("{} started with filename {}".format(myzcat.__name__, filename))
	try:
		click.echo(myzcat.gzip_reader.read_gzip_file(filename))
	except OSError as e:
		err = click.FileError(filename, str(e))
		logging.error(str(err))
		raise err
	else:
		logging.debug('Reading {} succeeded'.format(filename))


if __name__ == '__main__':
    main()