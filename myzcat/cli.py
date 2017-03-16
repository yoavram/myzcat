# -*- coding: utf-8 -*-
import click
from myzcat import gzip_reader


@click.command()
@click.argument('filename', type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True))
def main(filename):
    click.echo(gzip_reader.read_gzip_file(filename))

if __name__ == '__main__':
    main()