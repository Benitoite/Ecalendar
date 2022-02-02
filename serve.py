from gevent.pywsgi import WSGIServer
from app import app

http_server = WSGIServer(('192.168.1.157', 5001), app, keyfile='/etc/letsencrypt/live/17230.ddns.net/privkey.pem', certfile='/etc/letsencrypt/live/17230.ddns.net/cert.pem')
http_server.serve_forever()
