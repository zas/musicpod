#!/usr/bin/env python3

import click
from musicpod.scan.scan import ScanCollection
import config

@click.command()
def scan_collection():
    sc = ScanCollection(config.MUSIC_DIR)
    try:
        sc.scan()
    except Exception:
        raise
        sys.exit(-1)

def usage(command):
    with click.Context(command) as ctx:
        click.echo(command.get_help(ctx))


if __name__ == "__main__":
    scan_collection()
    sys.exit(0)
