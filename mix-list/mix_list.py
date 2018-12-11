#!/usr/bin/env python3
##creating a list
my_list = [ "192.168.0.5", 5060, "UP" ]
##returning the IP address to list
print("The first item in the list (IP): " + my_list[0] )
##return the port 5060
print("The second item in the list (port): " + str(my_list[1]) )
##return last item in the list
print("The last item in the list (state): " + my_list[2] )
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
##When I ssh into IP addresses 10.0.0.1 or 10.20.30.1 I am unable to ping ports 5060, 80, or 55.