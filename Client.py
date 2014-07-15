import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect(('192.168.56.1', port))
print(s.recv(1024))
s.close
