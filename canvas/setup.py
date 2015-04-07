from setuptools import setup

setup(
    name='canvas',
    version='0.1',
    py_modules=['canvas'],
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
        canvas=canvas:canvas
    ''',
)

