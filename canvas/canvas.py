import click
import json
import requests
import os
import urllib3
from tabulate import tabulate

import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

@click.group()
def canvas():
    pass

@canvas.command(help='Set up JSON config file')
@click.option('--key', type=unicode, help='API Key from Canvas')
@click.option('--name', type=unicode, help='Your name, self-explanatory')
@click.option('--display/--no-display', default=False, help='Display config values. Default false')
def config(**kwargs):

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

    if kwargs['key']:
        config['key'] = kwargs['key']
    if kwargs['name']:
        config['name'] = kwargs['name']

    if kwargs['display']:
        for k in config:
            click.echo('{0}: {1}'.format(k, config[k]))

    with open(configpath, 'w') as f:
        json.dump(config,f)

@click.group()
def classes():
    pass

@classes.command()
def all():
    key = getKey()
    j = requests.get('https://canvas.instructure.com/api/v1/courses?access_token=' + key).json()
    table = tabulate([(d['course_code'], d['name']) for d in j]) 
    click.echo(table)  

@classes.command()
def favs():
    key = getKey()
    j = requests.get('https://canvas.instructure.com/api/v1/users/self/favorites/courses?access_token=' + key).json()
    table = tabulate([d['id'], d['course_code'], d['name']] for d in j)   
    click.echo(table)

def getKey():
    configpath = os.path.expanduser('~') + "/.canvas.json"
    if not os.path.exists(configpath):
        click.echo('''
            config file not found.
            run 'canvas config --help for more information
        ''')
    config = {}
    with open(configpath) as f:
        config = json.load(f)
    if not config['key']:
        click.echo('''
            API key not set. 
            run 'canvas config --help for more information
        ''')
        exit(-1)
    return config['key']

canvas.add_command(config)
canvas.add_command(classes)
