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
        data = {"Name": self.name,
                "Age": self.age,
                "Is Student": self.is_student
                }
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

    @classmethod
    def deserialize(self, filename):
        """deserialize method"""
        file_path = Path(filename)
        if file_path.is_file:
            with open(filename, "rb") as f:
                data = pickle.load(f)
            name = data["Name"]
            age = data["Age"]
            is_student = data["Is Student"]
            return CustomObject(name, age, is_student)
        return None
