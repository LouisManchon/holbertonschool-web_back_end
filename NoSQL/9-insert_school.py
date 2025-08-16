#!/usr/bin/env python3
"""
chnage all topics of a document
"""


def insert_school(mongo_collection, **kwargs):
    """
    change all topics
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
