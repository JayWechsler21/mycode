#!/usr/bin/env python3
## create file object in "r"ead mode
configfile = open('vlanconfig.cfg', 'r')

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## counting the number of lines in file
num_lines= sum(1 for line in open('vlanconfig.cfg'))

## display list with no '\n'
print(configlist)
message= 'Total Number of Lines ='
print(message, num_lines)


## Always close your file
configfile.close()