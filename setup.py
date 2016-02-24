# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='mx_datagenerator',
      version='0.4.0',
      description='Generador de datos específicamente creado para México',
      url='https://github.com/ericking97/MX_datagen.git',
      author='ericking97',
      author_email='ericking97@hotmail.com',
      license='MIT',
      packages=find_packages(),
      data_files=[('mx_datagen/data_source/', ['mx_datagen/data_source/CP.json'])],
      zip_safe=False)
