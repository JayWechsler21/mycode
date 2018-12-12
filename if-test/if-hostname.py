#!/usr/bin/env python3

################################
#Asking what the host name is
################################
prompt_host_name_msg = "What is the hostname?"  
#################################
#typing in hostname
#################################
hostname = (input (prompt_host_name_msg))
hostname= hostname.upper()
if hostname == 'MTG':
    print('The hostname was found to be mtg')
    print('hostname matches expected config')
    print('Exiting the script.')
