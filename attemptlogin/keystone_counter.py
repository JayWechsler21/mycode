#!/usr/bin/env python3
# parse keystone.common.wsgi and return number of failed login attempts
loginsuccess = 0 
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')
keystone_file_lines=keystone_file.readlines()
for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginsuccess += 1 # this is the same as loginsuccess = loginsuccess + 1
print('The number of successful log in attempts is ' + str(loginsuccess))
