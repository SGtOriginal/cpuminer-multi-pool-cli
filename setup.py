from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cpuminer-multi-poo-cli',
    version='0.1.0',
    description='Command line interface for cpuminer-multi for pool selection',
    long_description=readme,
    author='Benno Müller',
    author_email='software@befrish.de',
    url='https://github.com/Befrish/cpuminer-multi-pool-cli',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)