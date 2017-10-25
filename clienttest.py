import os 
import socket 

BUF_SIZE = 1024 

def client(ip, port, message): 
    """ A client to test threading mixin server"""  
    # Connect to the server 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.connect((ip, port)) 
    try: 
        #sock.sendall(bytes(message, 'utf-8')) 
        sock.sendall(bytes(message)) 
        response = sock.recv(BUF_SIZE) 
        print ("Client received: %s" %response) 
    finally: 
        sock.close() 



def main():
	client('localhost',5005,"hello, im client 1")

if __name__ == '__main__':
	main()