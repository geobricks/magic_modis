from setuptools import setup
from setuptools import find_packages

setup(
    name='magic_modis',
    version='0.1.1',
    author='Guido Barbaglia',
    author_email='guido.barbaglia@gmail.com',
    packages=find_packages(),
    install_requires=[

    ],
    url='http://pypi.python.org/pypi/MagicMODIS/',
    license='LICENSE.txt',
    description='Magic MODIS module.',
    long_description=open('README.md').read()
)