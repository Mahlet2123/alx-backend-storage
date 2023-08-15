#!/usr/bin/env python3
""" 11-schools_by_topic.py module """


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    _docs = list(mongo_collection.find(
            {"topics": topic}
            ))
    return _docs
