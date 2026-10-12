#!/usr/bin/env python3
"""basic serialization"""

import json


def serialize_and_save_to_file(data="", filename=""):
    """serialize and save to file function"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename=""):
    """load and deserialize function"""
    with open(filename, 'r') as f:
        obj = json.load(f)
    return obj
