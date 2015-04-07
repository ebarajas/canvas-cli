import os
import json

def getKey():
    configpath = getConfigPath()
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

def getConfigPath():
    return os.path.expanduser('~') + "/.canvas.json"
