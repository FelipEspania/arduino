#!/usr/bin/env python
#!/usr/bin/python
# coding: utf-8

import pip

def install(package):
        pip.main(['install', package])
        
install('certifi')
install('requests')
install('pyserial')
