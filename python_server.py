import SimpleHTTPServer
import SocketServer
import os

PORT = 8000

web_dir = os.path.join(os.path.dirname(__file__), 'www')
os.chdir(web_dir)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

try:
  print "serving at port", PORT
  httpd.serve_forever()
except KeyboardInterrupt:
  print('\ninterrupted!')
  httpd.server_close()
