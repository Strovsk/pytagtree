from setuptools import setup, find_packages


setup(
    name='drawio_artisan',
    description='This package provides a fully resource tool to create drawio diagrams in XML format using Python and Component Tree structure',
    version='1',
    license='MIT',
    author="Thiago Santa Clara",
    author_email='strovsk@outlook.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='drawio diagrams datagrams',
    install_requires=[
          'scikit-learn',
      ],

)