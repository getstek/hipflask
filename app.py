#!/usr/bin/env python

from flask import Flask
import socket
app = Flask(__name__)

ip_address = socket.gethostbyname(socket.gethostname())
docker_hostname = socket.gethostname()

@app.route('/')
def index():
    return 'Python Flask Dockerized! \n' + 'Version: v2 \n' + 'IPv4 address: \n' + str(ip_address) + '\n' + 'Container hostname: \n \t' + str(docker_hostname)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(8350))
