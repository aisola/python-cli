# Setup File for Python CLI
from distutils.core import setup

setup(
    name='Python CLI',
    version="1.0",
    author='Abram C. Isola',
    author_email='abram@isola.mn',
    packages=['cli'],
    url='https://github.com/aisola/python-cli',
    description='A small package for building command line apps in Python.',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ]
)
