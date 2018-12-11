#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
protob= ['RPA']
print(proto)
proto.append('dns') # this line will add 'dns' to the end of our list
protoa.append('dns') # this line will add 'dns' to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print (proto)
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
print (protoa)
proto3= [21, 15, 26, 9 ] # adding fun line
print (proto3)
print(proto)
protoa.append('hi') # this line will add hi to the end of our list
print(protoa)
protob.append('Jay loves RPA')
print(protob)
