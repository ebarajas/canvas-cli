
from setuptools import setup, find_packages

setup(
    name='canvas-cli',
    version='0.1',
    author='Ernesto Barajas',
    author_email='ernestobarajas@utexas.edu',
    description=("A command line interface for the Canvas Learning Management System"),
    url="https://github.com/ebarajas/canvas-cli"
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests',
        'urllib3', 
        'pyopenssl',
        'ndg-httpsclient',
        'pyasn1',
        'tabulate',
        'python-dateutil'
    ],
    entry_points='''
        [console_scripts]
        canvas=canvas.canvas:canvas
    ''',
)

