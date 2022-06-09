from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Tuple

from typing_extensions import Self


class GSIServer(HTTPServer):
    def __init__(self: Self, server_address: Tuple[str, int], token: str, RequestHandler) -> None:
        super(GSIServer, self).__init__(server_address, RequestHandler)

        self.auth_token = token
        self.setup_logger()

    def setup_logger(self):
        pass

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_header('Content-type', 'text/html')
        self.send_response(200)
        self.end_headers()

server = GSIServer(('localhost', 3000), 'no_password', RequestHandler)
print('Starting server')

try:
    server.serve_forever()
except (KeyboardInterrupt, SystemExit):
    print('Ending server')
    server.server_close()