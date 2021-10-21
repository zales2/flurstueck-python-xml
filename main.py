from jsonType import JsonType
from aaaType import AaaType
from nasType import NasType
import click

types = { 'nas': NasType, 
    'aaa': AaaType, 
    'json': JsonType } # add new type

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('type', type=click.Choice(list(types)))
@click.argument('path')
def process(type, path):
    """ Get Flurstueck data\n
    $ python3 main.py TYPE PATH"""
    
    try:
        fluerstueck = types[type](path)
        fluerstueck.execute()
    except FileNotFoundError:
        click.echo('No such file in directory')

if __name__ == '__main__':
    process()
