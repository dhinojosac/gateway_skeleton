#!/usr/bin/env python
import sys, os
import logging
import signal
import threading
import time
import threadingserver as ts
from configlog import configLogging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#config log and his rotation
configLogging(logger)

def service_shutdown(signal, frame):
    logger.info("Gateway program shutdown")

def main():
    # Register the signal handlers
    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)

    logger.info("Gateway program start")

     # Create the server, binding to localhost on port SERVER_PORT
    server   = ts.ThreadedTCPServer((ts.SERVER_HOST, ts.SERVER_PORT), ts.ThreadedTCPRequestHandler) 
    ip, port = server.server_address # retrieve ip address 
 
    # Create a thread and activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server_thread = threading.Thread(target=server.serve_forever) 

    # Exit the server thread when the main thread exits 
    server_thread.daemon = True  # Don't hang on exit
    server_thread.start() 

    logger.info("Server loop running on thread: %s in %s:%s"  % (server_thread.name,ip,port) )

    # test while for serve forever
    try:
        while True:
            time.sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception, e:
        logger.error('Error %s' %e)
        # Server cleanup 
        server.shutdown() 


if __name__ == '__main__':
    main()