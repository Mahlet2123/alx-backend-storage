#!/usr/bin/env python3
""" 10-update_topics.py module """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name """
    updated_doc = mongo_collection.update_many(
            {"name": "Holberton school"},
            {"$set": {"topics": topics}}
            )
    return updated_doc
