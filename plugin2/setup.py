#-- setup.py --

''' Long Description for Plugin 2
'''

from setuptools import setup

#----------------------------------------------------------------------------------------------#

options = dict(
    name                    = 'plugin2',
    packages                = ['plugin2'],

    version                 = '0.0.0',
    description             = "",
    long_description        = __doc__,
    license                 = "MIT License",

    url                     = 'https://github.com/philipov/python-plugins-demo',
    author                  = 'Philip Loguinov',
    author_email            = 'philipov@gmail.com',

    zip_safe                = True,
    include_package_data    = True,

    entry_points = {
        'master.plugins' : 'plugin2 = plugin2'
    },
    install_requires = [
        'powertools',
        'master',
    ],
    classifiers = [
        'Programming Language :: Python :: 3.6'
    ],


)

#########################
if __name__ == "__main__":
    setup(**options)

#----------------------------------------------------------------------------------------------#
