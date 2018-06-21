#-- setup.py --

'''
'''

from setuptools import setup

#----------------------------------------------------------------------------------------------#

options = dict(
    name                    = 'master',
    packages                = ['master'],

    version                 = '0.0.0',
    description             = "",
    long_description        = __doc__,
    license                 = "MIT License",

    url                     = 'https://github.com/philipov/python-plugins-demo',
    author                  = 'Philip Loguinov',
    author_email            = 'philipov@gmail.com',

    zip_safe                = True,
    include_package_data    = True,

    install_requires = [
        'powertools',
    ],
    classifiers = [
        'Programming Language :: Python :: 3.6'
    ],


)

#########################
if __name__ == "__main__":
    setup(**options)

#----------------------------------------------------------------------------------------------#
