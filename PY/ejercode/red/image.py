import socket
import time

SERVIDOR = "data.pr4e.org"
PUERTO = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVIDOR, PUERTO))
sock.sendall(b'GET http://data.pr4e.org/conver3.jpg HTTP/1.0\r\n\r\n')
count = 0
imagen = b""

while True:
    data = sock.recv(5120)
    if len(data) < 1: break
    count =+ len(data)
    print (len(data), count)
    imagen = imagen + data
    print (imagen)

sock.close()