import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print("Connection established from: ", addr)

    st = input("Thank you for connecting")
    with gzip.open(fn+".gz","wb") as f_out:
        f_out.write(write(bytes(st, 'UTF-8')))
    c.send(st)
    input()
    c.close()
