import os
import time
import tempfile
import subprocess
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def _writeheaders(self):
        self.send_response(200)
        self.send_header('Connection', 'keep-alive')
        self.send_header('Content-Type', 'text/event-stream')
        self.end_headers()

    # GET Method
    def do_GET(self):
        if self.path == '/top':
            self._writeheaders()
            while True:
                f = tempfile.TemporaryFile()
                p = subprocess.Popen(['top'], stdout=f)
                time.sleep(2)
                p.terminate()
                p.wait()
                f.seek(0)
                chunk = f.read()
                f.close()
                self.wfile.write(
                    'id: 1\ndata: {}\ndata:\n\n'.format(chunk))
        else:
            # prepend the filename with current filepath
            path = os.getcwd() + '/index.html'
            with open(path) as indexHtml:
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(indexHtml.read().encode())


if __name__ == "__main__":
    httpd = HTTPServer(('', 8000), HTTPRequestHandler)
    print("Listening at port", 8000)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped")
