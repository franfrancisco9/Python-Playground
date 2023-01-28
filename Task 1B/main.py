import http.server
import socketserver
import subprocess
# set command to ruyn the caesar program
cmd = "python3 .."  + r'"\Task 1A\caesar"'

PORT = 8000

class GetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            #explain how to use the program
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("Usage: YOUR_URL/caesar/[encrypt/decrypt]?message=[message]", "utf-8"))

        # check if the url is encrypt or decrypt
        elif self.path.startswith("/caesar/encrypt"):
            # get the message
            message = self.path.split("=")[1]
            # run the caesar program
            output = subprocess.check_output(cmd + " encrypt " + message, shell=True)
            # send the message back to the user
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            message= b'You send to encrypt:\n' + message.encode() + b'\n and the result is:\n' + output
            self.wfile.write(message)
        elif self.path.startswith("/caesar/decrypt"):
            # get the message
            message = self.path.split("=")[1]
            # run the caesar program
            output = subprocess.check_output(cmd + " decrypt " + message, shell=True)
            # send the message back to the user
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            message= b'You send to decrypt:\n' + message.encode() + b'\n and the result is:\n' + output
            self.wfile.write(message)
        else:
            # send error message
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("404 Not Found", "utf-8"))

Handler = GetHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

