#!/usr/bin/env python
from simple_http_server import server, route
import socketserver
import subprocess
# set command to ruyn the caesar program
cmd = "./caesar"
cmd2 = "./find_island"

PORT = 8000

@route("/")
def index():
    # create a html page with the usage of the server
    # make buttons for the island finder and a input for the caesar program with decrypt and encrypt
    # buttons

    html = """
    <!DOCTYPE html>
    <html>
    <body>
    <form action="/caesar/encrypt" method="GET">
        <input type="text" name="message" placeholder="message">
        <input type="submit" value="Encrypt">
    </form>
    <form action="/caesar/decrypt" method="GET">
        <input type="text" name="message" placeholder="message">
        <input type="submit" value="Decrypt">
    </form>
    <form action="/island_finder">
        <input type="submit" value="Island finder">
    </form>
    </body>
    </html>
    """
    return html

@route("/caesar/encrypt", method="GET")
def encrypt(message):
    output = subprocess.check_output(cmd + " encrypt " + message, shell=True)
    return "<!DOCTYPE html><html><body><h1>You sent to encrypt:</h1><p>" + message + "</p><h1>The result is:</h1><p>" + output.decode() + "</p></body></html>"

@route("/caesar/decrypt", method="GET")
def decrypt(message):
    output = subprocess.check_output(cmd + " decrypt " + message, shell=True)
    return "<!DOCTYPE html><html><body><h1>You sent to decrypt:</h1><p>" + message + "</p><h1>The result is:</h1><p>" + output.decode() + "</p></body></html>"

@route("/island_finder")
def island_finder():
    output = subprocess.check_output(cmd2, shell=True)
    # process the output so that it is readable and in a block
    output = output.decode()
    output = output.split("\n\n")
    matrix = output[0].replace("\n", "<br>")
    
    island = output[1].replace("\n", "<br>")
    # get positions of x in array
    x_pos = []
    for i in range(len(island.split())):
        if "X" in island.split()[i]:
            x_pos.append(i)
    print(x_pos)
    # add red color to the corresponding positions in matrix.split()
    matrix = matrix.split()
    for i in range(len(matrix)):
        if i in x_pos:
            matrix[i] = matrix[i].replace(str(matrix[i]), "<span style='color: red; font-size: 20px'>" + str(matrix[i]) + "</span>")
    
    matrix = " ".join(matrix)
    matrix = "<span style='font-size: 20px'>" + matrix + "</span>"

    # make X red and same size as . in the matrix
    island = island.replace("X", "<span style='color: red; font-size: 8px'>X</span>")
    # makes . in the center
    island = island.replace(".", "<span style='font-size: 20px'>.</span>")
    # show island to the right of the matrix
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <body>
    <div style="display: flex; flex-direction: row;">
        <div style="display: flex; flex-direction: column;">
            <h1>Matrix</h1>
            <p>{matrix}</p>
        </div>
        <div style="width: 50px"></div>
        <div style="display: flex; flex-direction: column;">
            <h1>Island</h1>
            <p>{island}</p>
        </div>
    </div>
    </body>
    </html>
    """
    return html

server.start(port = PORT)