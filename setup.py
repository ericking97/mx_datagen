# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(name='mx_datagenerator',
      version='0.4.6',
      description='Generador de datos específicamente creado para México',
      url='https://github.com/ericking97/MX_datagen.git',
      author='ericking97',
      author_email='ericking97@hotmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'python-dateutil',
      ],
      include_package_data=True,
      zip_safe=False)
