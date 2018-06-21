#-- master.plugins

""" load plugins
"""

from powertools import AutoLogger
log = AutoLogger()
from powertools import export

import pkg_resources
from copy import copy
from contextlib import suppress

from powertools import term
from powertools.print import rprint

#----------------------------------------------------------------------------------------------#

################################
def _load_plugins():
    ''' produce a dictionary of available plugin modules '''

    try:
        plugin_modules = {
            entry_point.name : entry_point.load()
            for entry_point
            in pkg_resources.iter_entry_points( __name__ )
        }
        return plugin_modules
    except pkg_resources.DistributionNotFound as e:
        return dict()

################################
def _select_class( cls, base ):
    ''' scan all modules and pull out a name mapping of subclasses of the given type
        and adds it to the built-in subclasses
    '''
    global plugin_modules

    results = copy(base)
    for module_name, module in plugin_modules.items( ):
        for attribute, value in module.__dict__.items():
            if not attribute.startswith('_'):
                with suppress(TypeError):
                    if issubclass(value, cls) and hasattr(value, '__key__'):
                        print(value)
                        results[value.__key__] = value
    return results

#----------------------------------------------------------------------------------------------#

from .thing import Thing, Some

builtin_things = {
    'Something':    Some,
}

#----------------------------------------------------------------------------------------------#

plugin_modules      = _load_plugins()

thing_types         = _select_class( Thing, builtin_things )

#----------------------------------------------------------------------------------------------#

@export
def report_plugins():
    log.print(  term.dcyan('~~~~~~~~~~~ '), term.pink( __name__ ), ':')
    rprint( plugin_modules )

    log.print( term.dcyan( '~~~~~~~~~~~ ' ), term.pink('thing types:' ))
    rprint( thing_types )

    log.print( term.dcyan( '~~~~~~~~~~~\n' ) )

