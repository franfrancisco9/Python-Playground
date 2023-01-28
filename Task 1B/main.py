#!/usr/bin/env python
from simple_http_server import server, route
import socketserver
import subprocess
# set command to ruyn the caesar program
cmd = "./caesar"

PORT = 8000

@route("/")
def index():
    return "<!DOCTYPE html><html><body><h1>Usage: /caesar/[encrypt/decrypt]?message=[message]</h1></body></html>"

@route("/caesar/encrypt", method="GET")
def encrypt(message):
    output = subprocess.check_output(cmd + " encrypt " + message, shell=True)
    return "<!DOCTYPE html><html><body><h1>You sent to encrypt:</h1><p>" + message + "</p><h1>The result is:</h1><p>" + output.decode() + "</p></body></html>"

@route("/caesar/decrypt", method="GET")
def decrypt(message):
    output = subprocess.check_output(cmd + " decrypt " + message, shell=True)
    return "<!DOCTYPE html><html><body><h1>You sent to decrypt:</h1><p>" + message + "</p><h1>The result is:</h1><p>" + output.decode() + "</p></body></html>"

server.start(port = PORT)