#!/usr/bin/env python3
""" 9-insert_school.py module """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    attrs = kwargs
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
