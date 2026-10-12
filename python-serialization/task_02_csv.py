#!/usr/bin/env python3
"""csv to json conversion module"""

import json
import csv


def convert_csv_to_json(filename):
    """csv to json function"""
    try:
        with open(filename, "r") as csv_file:
            data = list(csv.DictReader(csv_file))
    except (EOFError, FileNotFoundError):
        return False
    try:
        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
    except (EOFError, FileNotFoundError):
        return False
    return True
