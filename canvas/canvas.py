import click
import json
import os
import urllib3


import classes
import utils

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
    
    if os.path.exists(utils.getConfigPath()):
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





canvas.add_command(config)
canvas.add_command(classes.classes)
