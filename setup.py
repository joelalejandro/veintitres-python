from setuptools import setup

setup(name='veintitres',
      version='0.0.1',
      description='A Python library for interacting with 23andme.com''s API.',
      url='http://github.com/joelalejandro/veintitres-python',
      author='Joel A. Villarreal Bertoldi',
      author_email='joel.a.villarreal@gmail.com',
      license='MIT',
      packages=['veintitres'],
      install_requires=[
          'requests'
      ],
      zip_safe=False)
