import socket

s = socket.socket()
host = '0.0.0.0'
port = 12345
s.bind((host, port))

s.listen(5)

c, addr = s.accept()
print("Connection established from: ", addr)

st = "Thank you for connecting"

c.send(st.encode('utf-8'))

while True:
    print(c.recv(1024))

