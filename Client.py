import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect(('99.108.229.133', port))
#s.connect(('192.168.1.85', port))
print(s.recv(1024))
s.close
