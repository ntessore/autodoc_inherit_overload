Sphinx: Render inherited overloads with autodoc
===============================================

This extension works around a small issue in Sphinx where autodoc does not show
inherited `@overload` signatures, by manually resolving overloads during the
[`autodoc-process-signature`] event.  Dynamically, the overloads for a function
can only be obtained using the [`typing.get_overloads()`] function, which was
introduced in Python 3.11.  The latter is therefore a hard requirement.


Installation
------------

For testing, you can install the `sphinxcontrib.autodoc_inherit_overload`
package from pip:

```
pip install sphinxcontrib.autodoc_inherit_overload
```

When adding the package to your dependencies, make sure you guard against
incorrect Python versions:

```
sphinxcontrib.autodoc_inherit_overload; python_version>='3.11'
```

The same applies to loading the extension in your `conf.py`:

```py
extensions = [
    # your extensions
    ...
]
if sys.version_info >= (3, 11):
    extensions += ['sphinxcontrib.autodoc_inherit_overload']
```

[`autodoc-process-signature`]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#event-autodoc-process-docstring
[`typing.get_overloads()`]: https://docs.python.org/3/library/typing.html#typing.get_overloads
