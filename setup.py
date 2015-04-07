
from setuptools import setup, find_packages

setup(
    name='canvas',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests',
        'urllib3', 
        'pyopenssl',
        'ndg-httpsclient',
        'pyasn1',
        'tabulate'
    ],
    entry_points='''
        [console_scripts]
        canvas=canvas.canvas:canvas
    ''',
)

