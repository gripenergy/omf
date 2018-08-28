#!/usr/bin/env python
# Script to start a web server for easier circuitjs1 testing.

from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import http.server
import socketserver
import webbrowser

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
webbrowser.open_new('http://localhost:8000')
httpd.serve_forever()

