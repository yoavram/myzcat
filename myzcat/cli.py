# -*- coding: utf-8 -*-
import click
import myzcat


@click.command()
@click.argument('filename', 
	type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True))
@click.version_option(version=myzcat.__version__)
def main(filename):
    click.echo(myzcat.gzip_reader.read_gzip_file(filename))

if __name__ == '__main__':
    main()