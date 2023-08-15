#!/usr/bin/env python3
""" 8-all.py module """


def list_all(mongo_collection):
    """ lists all documents in a collection """
    ret_list = list(mongo_collection.find())
    if ret_list is None:
        ret_list = []
    return ret_list 
