import socket
import io
import traceback
import logging
import sys
from datetime import datetime

logging.basicConfig(filename='client_udp.log', level=logging.INFO)
#logging.info('[INFO][%s]:Client Started.' %str(datetime.now()))
HOST = sys.argv[1]
PORT = int(sys.argv[2])#"localhost", 9999
data = " ".join(sys.argv[3:])

# Create a socket (SOCK_STREAM means a UDP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Communicate with server
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")
    print "[{0}]Sent:{1}".format(str(datetime.now()),data)
    logging.info("[INFO][{0}]Requesting --> {1}".format(str(datetime.now()),data))
    received = sock.recv(1024)
    print "[{0}]Received:{1}".format(str(datetime.now()),received)
    logging.info("[INFO][{0}]Received --> {1}".format(str(datetime.now()),received))
    
except Exception, err:
    print "[ERROR][{0}]Error Communicating with the server. Check log for detailed info!".format(str(datetime.now()),sys.exc_info()[0])
    logging.info("[ERROR][{0}]Error Connecting the server -- {1} Check Server Please!".format(str(datetime.now()),sys.exc_info()[0]))
    logging.info("[ERROR][DETAIL]{0}".format(traceback.format_exc()))

finally:
    sock.close()
    exit()



