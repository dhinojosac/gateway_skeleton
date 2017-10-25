#!/usr/bin/env python 
# Diego Hinojosa Cordova
# 25-Oct-2017
# Gateway Skeleton
# This program is a server, that opens a new thread for each new client.
 
import os 
import time
import socket 
import threading 
import SocketServer 
 
SERVER_HOST = 'localhost' 
SERVER_PORT = 5005 # tells the kernel to pickup a port dynamically 
BUF_SIZE    = 1024 
 
 
def client(ip, port, message): 
    """ A client to test threading mixin server"""     
    # Connect to the server 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.connect((ip, port)) 
    try: 
        sock.sendall(bytes(message)) 
        response = sock.recv(BUF_SIZE) 
        print ("Client received: %s" %response) 
    finally: 
        sock.close() 
 
 
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler): 
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.

    Inherits request, client_address, server
    """
    def handle(self): 
        # self.request is the TCP socket connected to the client
        print "[+] You have a new client on port %s" % (self.client_address[1])
        data = self.request.recv(1024) 
        print "[+] data incomming: %s" % (data)
        # Add the function you want here.
        cur_thread = threading.current_thread() 
        response = "Welcome, you are over a "+"%s: %s" %(cur_thread.name, data) 
        self.request.sendall(bytes(response)) 

    def finish(self):
        print "[!] Finish connection with a client on port %s" % (self.client_address[1])
 
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer): 
    """ Nothing to add here, inherited everything necessary from parents """ 
    pass 

class mExcept(Exception):
    """ Custom exception """
    pass
 
 
if __name__ == "__main__": 
    # Create the server, binding to localhost on port SERVER_PORT
    server   = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler) 
    ip, port = server.server_address # retrieve ip address 
 
    # Create a thread and activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server_thread = threading.Thread(target=server.serve_forever) 

    # Exit the server thread when the main thread exits 
    server_thread.daemon = True  # Don't hang on exit
    server_thread.start() 

    print ("[+] Server loop running on thread: %s in %s:%s"  % (server_thread.name,ip,port) )

    # test while for serve forever
    try:
        while True:
            time.sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        # Server cleanup 
        server.shutdown() 