#!/usr/bin/env python3
"""pickle serialization"""

import pickle


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
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(self, filename):
        """deserialize method"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (OSError, EOFError, pickle.UnpicklingError):
            return None
