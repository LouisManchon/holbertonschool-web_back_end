#!/usr/bin/env python3
"""
chnage all topics of a document
"""


def update_topics(mongo_collection, name, topics):
    """
    change all topics of a document
    """
    return mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
