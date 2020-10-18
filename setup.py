# encoding: utf-8
from setuptools import setup, find_packages

SHORT = "a client for apollo 2.0, it's been reformatted!"

__version__ = "2.1.1"
__author__ = 'Lin Luo / Bruce Liu'
__email__ = '15869300264@163.com'
readme_path = 'README.md'

setup(
    name='apollo-client',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    url='',
    author=__author__,
    author_email=__email__,
    classifiers=[
        'Programming Language :: Python :: 3.5',
    ],
    include_package_data=True,
    package_data={'': ['*.py', '*.pyc']},
    zip_safe=False,
    platforms='any',

    description=SHORT,
    long_description=open(readme_path, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)
