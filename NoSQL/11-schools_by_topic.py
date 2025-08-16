#!/usr/bin/env python3
"""
reutrn a list of havuing a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    return a list which having a specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
