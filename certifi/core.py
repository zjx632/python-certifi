# -*- coding: utf-8 -*-

"""
certifi.py
~~~~~~~~~~

This module returns the installation location of cacert.pem.
"""
import os


def where():
    f = os.path.dirname(__file__)
    
    if os.path.exists(os.path.join(f, 'cacert.pem')):
        return os.path.join(f, 'cacert.pem')
    else:
        return os.path.join(f, '../..', 'cacert.pem')
    
