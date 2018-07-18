# !/usr/bin/env python

import time
from distutils.core import setup

setup(
    name='SrMoura',
    version=time.strftime('%Y.%m.%d.%H.%M.%S', time.gmtime(1520986859.625666)),
    description='Srmoura.',
    author='Gabriel Moura',
    author_email='develop@srmoura.com.br',
    license="Custom",
    long_description='SrMoura.',
    url='https://github.com/srmoura/Arch',
    py_modules=['SrMoura']
)
