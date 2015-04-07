import click
import json
import os

@click.group()
def canvas():
    pass

@canvas.command(help='Set up JSON config file')
@click.option('--key', type=unicode, help='API Key from Canvas')
@click.option('--name', type=unicode, help='Your name, self-explanatory')
def config(key, name):

    # check if config file exists
    # if exists, load into dict
    # if not, create empty dict with keys and dump
    config = {}
    configpath = os.path.expanduser('~') + "/.canvas.json"
    if os.path.exists(configpath):
        click.echo('Config file exists at ' + configpath)
        with open(configpath, 'r') as f:
            config = json.load(f)
    else:
        click.echo('Config file does not exist')
        config['key'] = ''
        config['name'] = ''
        click.echo('Config file created at ' + configpath)
    
    # check if options were provided

    if key:
        config['key'] = key
    if name:
        config['name'] = name

    with open(configpath, 'w') as f:
        json.dump(config,f)

@click.group()
def classes():
    pass

@classes.command()
def all():
    config = {}
    configpath = os.path.expanduser('~') + "/.canvas.json"
    if not os.path.exists(configpath):
        click.echo('''
            config file not found.
            run 'canvas config --help' for more information 
        ''')

def getKey():
    configpath = os.path.expanduser('~') + "/.canvas.json"
    if not os.path.exists(configpath):
        click.echo('''
            config file not found.
            run 'canvas config --help for more information
        ''')
    config = {}
    with open(configpath, 'r') as f:
        config = json.load(configpath)
    if not config['key']:
        click.echo('''
            API key not set. 
            run 'canvas config --help for more information
        ''')
        sys.exit(-1)

canvas.add_command(config)
canvas.add_command(classes)
