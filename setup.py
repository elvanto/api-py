from setuptools import setup


setup(name="ElvantoAPI",
      version='1.3.2',
      description='Python API Wrapper for Elvanto Systems',
      url='https://github.com/elvanto/api-py',
      author='Elvanto',
      author_email='support@elvanto.com',
      packages=['ElvantoAPI'],
      install_requires=[
          'requests'
      ],
      zip_safe=False)
