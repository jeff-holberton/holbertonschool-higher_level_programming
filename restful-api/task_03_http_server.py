#!/usr/bin/env python3
"""task 03 http server"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyServer(BaseHTTPRequestHandler):
    """MyServer class"""

    def do_GET(self):
        if self.path == "/":
            status_code = 200
            body = b"Hello, this is a simple API!"
            content_type = "text/plain; charset=utf-8"
        elif self.path == "/data":
            status_code = 200
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            body = json.dumps(data).encode("utf-8")
            content_type = "application/json"
        elif self.path == "/status":
            body = b"OK"
            status_code = 200
            content_type = "text/plain; charset=utf-8"
        elif self.path == "/info":
            status_code = 200
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            body = json.dumps(data).encode("utf-8")
            content_type = "application/json"
        else:
            status_code = 404
            content_type = "text/plain; charset=utf-8"
            body = b"Endpoint not found"

        content_length = len(body)
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", content_length)
        self.end_headers()

        self.wfile.write(body)


server = HTTPServer(("localhost", 8000), MyServer)
print("Starting server on http://localhost:8000")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nStopping server.")
    server.server_close()
