import click
import json
import requests
from utils import getKey, convertTZ
from tabulate import tabulate

@click.group()
def hw():
	pass

@hw.command()
@click.option('--n', type=int, default=10, help='Num of assignments to display. Default: 10')
def due(n):
    key = getKey()
    j = requests.get('https://canvas.instructure.com/api/v1/users/self/todo?access_token=' + key).json()
    table = tabulate([(d['assignment']['course_id'], d['assignment']['name'], 
    	convertTZ(d['assignment']['due_at']).strftime("%b %d, %y at %I:%M%p")) for d in j])
    print table
