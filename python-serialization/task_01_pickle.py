#!/usr/bin/env python3
"""pickle serialization"""

import pickle
from pathlib import Path


class CustomObject:
    def __init__(self, name, age, is_student):
        """init method"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print method"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize method"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(self, filename):
        """deserialize method"""
        file_path = Path(filename)
        if file_path.is_file():
            with open(filename, "rb") as f:
                return pickle.load(f)
        return None
