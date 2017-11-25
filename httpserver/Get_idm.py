import requests
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import subprocess

def start(port, callback):
    def handler(*args):
        CallbackServer(callback, *args)
    server = HTTPServer(('', int(port)), handler)
    server.serve_forever()

class CallbackServer(BaseHTTPRequestHandler):
    def __init__(self, callback, *args):
        self.callback = callback
        BaseHTTPRequestHandler.__init__(self, *args)

    
    def do_GET(self):
        #parsed_path = urlparse.urlparse(self.path)
        #query = parsed_path.query
        self.send_response(200)
        self.end_headers()
        '''
        cmd='ls -l'
        try:
            res = subprocess.check_output(cmd.split(" "))
        except:
            print("error")
        return res
        '''
        #result = self.callback(query)
        result = self.callback
        #result = self.exe_scan()
        #message = '\r\n'.join(result)
        #self.wfile.write(message)
        self.wfile.write(result)
        return
