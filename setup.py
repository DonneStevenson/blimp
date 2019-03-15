from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    readme=readme_file.read()
    
setup(
    name='blimp',
    version='0.0.1',
    author='DBStevenson',
    author_email='stevensondb95@gmail.com',
    description='Do multiple k fold cross validations of sklearn and keras models',
    url='https://github.com/DonneStevenson/blimp',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        ],
    )