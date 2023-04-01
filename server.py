import socket
import time

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8001              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.bind((HOST, PORT))
        s.listen(1)
        
        conn, addr = s.accept()
        
        try:
            with conn:
                print('Connected by', addr)
                
                c = 1
                while True:
                    
                    conn.sendall(f'{c}\n'.encode('utf-8'))
                    
                    time.sleep(c)
                    c += 1
        
        
        except Exception as e:
            print(type(e), e.args)
            conn.close()