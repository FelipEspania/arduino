#!/usr/bin/env python
#!/usr/bin/python
# coding: utf-8

import pip


def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('certifi')
install_and_import('requests')
install_and_import('pyserial')
