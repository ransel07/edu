import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("data.pr4e.org", 80))
cmd = b'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'

sock.send(cmd)

while True:
    line = sock.recv(512)
    if len(line) < 1:
        break
    print(line.decode(),end='')

sock.close()

