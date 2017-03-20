# -*- coding: utf-8 -*-
import click

import myzcat


@click.command()
@click.argument('filename', 
	type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True))
@click.version_option(version=myzcat.__version__)
def main(filename):
	try:
		click.echo(myzcat.gzip_reader.read_gzip_file(filename))
	except OSError as e:
		raise click.FileError(filename, str(e))


if __name__ == '__main__':
    main()