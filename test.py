import time
import subprocess
import tempfile
import os
import time
import tempfile
import subprocess
# from http.server import HTTPServer, BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


class HTTPRequestHandler(BaseHTTPRequestHandler):

    # GET Method
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        f = tempfile.TemporaryFile()
        p = subprocess.Popen(['top'], stdout=f)
        time.sleep(2)
        p.terminate()
        p.wait()
        f.seek(0)
        chunk = f.read()
        f.close()
        self.wfile.write(chunk)


if __name__ == "__main__":
    httpd = HTTPServer(('', 8000), HTTPRequestHandler)
    print("Listening at port", 8000)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped")

# f = tempfile.TemporaryFile()
# p = subprocess.Popen(['top'], stdout=f)
# time.sleep(2)
# p.terminate()
# p.wait()
# f.seek(0)
# print(f.read().decode())
# f.close()
