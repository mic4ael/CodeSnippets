#!/usr/bin/env python

import click


class TranslationFetcher(object):
    def __init__(self, files):
        self._files = files

    def run(self):
        click.clear()


@click.command()
@click.option('files', '--file', '-f', help='path to the file with a list of words to be translated', multiple=True)
def main(files):
    instance = TranslationFetcher(files)
    instance.run()


if __name__ == '__main__':
    main()
