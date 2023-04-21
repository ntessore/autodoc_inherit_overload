"""Sphinx extension to render inherited overloads with autodoc."""

__version__ = '2023.4'

from typing import get_overloads
from sphinx.util.inspect import signature, stringify_signature


def autodoc_inherit_overload(app, what, name, obj, options, sig, ret_ann):
    '''Callback function to provide overloaded signatures.'''
    if what in ('function', 'method') and callable(obj):
        overloads = get_overloads(obj)
        if overloads:
            kwargs = {}
            if app.config.autodoc_typehints in ('none', 'description'):
                kwargs['show_annotation'] = False
            if app.config.autodoc_typehints_format == 'short':
                kwargs['unqualified_typehints'] = True
            type_aliases = app.config.autodoc_type_aliases
            bound_method = what == 'method'
            sigs = []
            for overload in overloads:
                overload_sig = signature(overload, bound_method=bound_method,
                                         type_aliases=type_aliases)
                sigs.append(stringify_signature(overload_sig, **kwargs))
            return '\n'.join(sigs), None


def setup(app):
    '''Initialise the extension.'''
    app.connect('autodoc-process-signature', autodoc_inherit_overload)
