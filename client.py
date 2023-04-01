import socket

HOST = 'localhost'
PORT = 8001
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.settimeout(5)
    s.setblocking(True)
    
    s.connect((HOST, PORT))
    
    fd = s.makefile()
    
    for line in fd:
        print(repr(line))