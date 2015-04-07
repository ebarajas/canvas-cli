import click

@click.group()
def canvas():
    pass

@canvas.command()
def config():
    click.echo('Hello from Config!')

canvas.add_command(config)
