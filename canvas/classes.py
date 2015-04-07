import click
import json
import requests
from utils import getKey
from tabulate import tabulate

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
