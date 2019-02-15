# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    readme = f.read()

with open(os.path.join(os.path.dirname(__file__), 'LICENSE')) as f:
    license = f.read()

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    version = f.read()


def import_requirements():
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        return content


setup(
    name='ensembl_prodinf',
    version=version,
    description='Core libraries for Ensembl Production infrastructure services',
    long_description=readme,
    author='Dan Staines, Thomas Maurel, Marc Chakiachvili',
    author_email='dstaines@ebi.ac.uk, maurel@ebi.ac.uk, mchakiachvili@ebi.ac.uk',
    url='https://github.com/Ensembl/ensembl-prodinf-core',
    license=license,
    install_requires=import_requirements(),
    packages=find_packages(exclude=('tests', 'docs'))
)
