#!/usr/bin/env python3
"""task 02 requests"""

import requests
import csv


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    status_code = r.status_code
    print(f"Status Code: {status_code}")
    r.raise_for_status()
    data = r.json()
    for post in data:
        print(post["title"])


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    r.raise_for_status()
    data = r.json()
    field_names = ["id", "title", "body"]
    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=field_names,
            extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)
