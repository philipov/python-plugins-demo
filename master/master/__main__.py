#-- master.__main__

'''
application entry point
'''

from powertools import export
from powertools import AutoLogger
log = AutoLogger()
from powertools import term

import click

#----------------------------------------------------------------------------------------------#

class MissingPlugin(Exception):
    ''' Attempted to use plugin that is not installed.'''

class MissingRequiredAttribute(Exception):
    ''' Plugin module didn't implement a required attribute.'''

#----------------------------------------------------------------------------------------------#
CONTEXT_SETTINGS = dict(help_option_names = ['-h', '--help'])

@click.command(     context_settings =  CONTEXT_SETTINGS)
@click.option(      '--verbose', '-v',  default = False,    is_flag  = True)
@click.argument(    'plugin',           default = None,     required = False)
def console( plugin, verbose ) :
    """ display the doc string of the selected plugin """

    term.init_color()

    log.print('\n', term.cyan('~~~~~~~~~~~~~~~~~~~~ '), term.pink('PYTHON PLUGINS DEMO'))

    from .plugins import (
        report_plugins,
        plugin_modules,
    )

    if verbose:
        report_plugins()

    if plugin is not None:

        ### select plugin
        if plugin not in plugin_modules:
            raise MissingPlugin(plugin)

        selected_plugin = plugin_modules[plugin]

        ### display information
        if not hasattr(selected_plugin, 'PARAMETER'):
            raise MissingRequiredAttribute(f'{plugin}.PARAMETER')

        print(f' PLUGIN:   {selected_plugin}')
        print( '__doc__:   ')
        print( selected_plugin.__doc__)
        print(f'PARAMETER: {selected_plugin.PARAMETER}')

    log.print( '\n', term.pink( '~~~~~~~~~~~~~~~~~~~~' ), term.cyan(' DONE...') )


#----------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    console()


#----------------------------------------------------------------------------------------------#
