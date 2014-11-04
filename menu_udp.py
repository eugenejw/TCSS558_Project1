import cmd
import logging
import os
import sys
from datetime import datetime

class UDP_Client(cmd.Cmd):
    """Simple command processor example."""

    port = 9999
    hostname = 'localhost'
    network = 'socket.AF_INET, socket.SOCK_STREAM'

    def do_port(self, customized_port):
        """set port
        of the client"""
        if customized_port:
           self.port = customized_port
        else:
            print 'Invalid Syntax! Try {port argument1}'

    def do_hostname(self, customized_name):
        """set hostname
        of the client"""
        if customized_name:
           self.hostname = customized_name
        else:
            print 'Invalid Syntax! Try {hostname argument1}'

    def do_hostname(self, customized_network):
        """set hostname
        of the client"""
        if customized_network:
           self.network = customized_network
        else:
            print 'Invalid Syntax! Try {network argument1}'

    def do_GET(self, person):
        """GET [person]
        GET the phone number of this person"""
        if person:
           os.system('python client_udp.py %s %d GET %s' %(self.hostname, int(self.port),person))
        else:
            print 'Invalid Syntax! Try {GET argument1}'

    def do_QUERY(self, line):
        """QUERY [no argument]
        Query all data in DB"""

        os.system('python client_udp.py %s %d QUERY all' %(self.hostname, int(self.port)) )


    def do_PUT(self, person_number):
        """PUT [person number] 
        Add key/value to DB"""
        if person_number:
           os.system('python client_udp.py %s %d PUT %s'%(self.hostname, int(self.port),person_number))
        else:
            print 'Invalid Syntax! Try {PUT argument1 argument2}'


    def do_DELETE(self, person):
        """DELETE [person]
        Delete the key [person] and its value in DB"""
        if person:
           os.system('python client_udp.py %s %d DELETE %s' %(self.hostname, int(self.port), person))
        else:
            print 'Invalid Syntax! Try {DELETE argument1}'

    def do_exit(self, line):
        print "[{0}]Shutting the Client down...".format(str(datetime.now()))
        print "[{0}]Client has been shut down...".format(str(datetime.now()))
        logging.info("[{0}]Client is gracefully shut down.".format(str(datetime.now())))
        return True

if __name__ == '__main__':
    logging.basicConfig(filename='client_udp.log', level=logging.INFO)
    logging.info('[INFO][%s]:Client Started.' %str(datetime.now()))
    print "[TEST][{0}]Start to pre-populating the following 5 pairs of data when Client is up.".format(str(datetime.now()))
    logging.info("[TEST][{0}]Start to pre-populating the following 5 pairs of data when Client is up".format(str(datetime.now())))
    UDP_Client().do_PUT("person1 number1")
    UDP_Client().do_PUT("person2 number2")
    UDP_Client().do_PUT("person3 number3")
    UDP_Client().do_PUT("person4 number4")
    UDP_Client().do_PUT("person5 number5")
    print "[TEST][{0}]Get value from each pair.".format(str(datetime.now()))
    logging.info("[TEST][{0}]Get value from each pair.".format(str(datetime.now())))
    UDP_Client().do_GET('person1')
    UDP_Client().do_GET('person2')
    UDP_Client().do_GET('person3')
    UDP_Client().do_GET('person4')
    UDP_Client().do_GET('person5')
    print "[TEST][{0}]Clensing the pre-populated pairs.".format(str(datetime.now()))
    logging.info("[TEST][{0}]Clensing the pre-populated pairs of data.".format(str(datetime.now())))
    UDP_Client().do_DELETE('person1')
    UDP_Client().do_DELETE('person2')
    UDP_Client().do_DELETE('person3')
    UDP_Client().do_DELETE('person4')
    UDP_Client().do_DELETE('person5')

#   doing initial setup of ports, hostname, and instance
    UDP_Client().port = 9999
    UDP_Client().hostname = 'localhost'
    UDP_Client().instance = 'SOCK_STREAM'

    print "\n"
    print "*** Welcome to TCSS558 Group7 Project1 *** \n"
    print "***                                    *** \n"    
    print "***     Input cmd or help or exit      *** \n"    
    print "***                                    *** \n"    
    print "****************************************** \n"    

    print "[INFO]By default the client is using <localhost>:<port-9999> via UDP"    
    print "[INFO]To customize them, use cmd <port>, <hostname>, and <network>"

    UDP_Client().cmdloop()
