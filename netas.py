#!/usr/bin/env python

from colorama import Fore,Back,init
import os
import sys
import re
import time

banner = r'''

 _   _      _
| \ | | ___| |_ __ _ ___
|  \| |/ _ \ __/ _` / __|
| |\  |  __/ || (_| \__ \
|_| \_|\___|\__\__,_|___/
	       3P1C /\ V1.0
	'''

def op():
    return "\n1) Whois      2) DNS Lookup\n3) Traceroute      4) Telnet\n5) Ping      6) Exit"
try:    
    print Fore.CYAN+banner   
    print Fore.MAGENTA+op(),"\n--------------+-++-----------"
    user = raw_input(Fore.CYAN+"[i] Choose Info :~# ") 
    if int(user) == 1:
        whois = raw_input(Fore.GREEN+" [i] Domain ~# ")
        init()
        if re.findall('https',whois) :
            os.system('whois '+whois[8:])
        elif re.findall('http',whois):
            os.system('whois '+whois[7:])
        else:
            os.system('whois '+whois)
        
    elif int(user) == 2:
        dns = raw_input(Fore.GREEN+" [i] Hostname ~# ")
        init()
        dotted = dns.count(".")
        if dotted == True:
            os.system("dig "+dns)
        else:
            print " [!] Please Enter Hostname or Website"

    elif int(user)== 3:
        how = raw_input(Fore.GREEN+"[i] Host or Website ~# ")
        init()
        os.system('traceroute '+how)
    elif int(user) == 4:
        telnt = raw_input(Fore.GREEN+" [i] IP Address ~# ")
        if re.findall('.',telnt) == True:
            port = raw_input(" [i] Port ~# ")
            init()
            if port  < 2:
                os.system('telnet '+telnt+port)
    elif int(user) == 5:
        png = raw_input(Fore.GREEN+'Host ~# ')
        init()
        os.system('ping -c 11 '+png)
    elif int(user) == 6:
        print Fore.BLUE+'Exit.....'
        time.sleep(1)
        sys.exit()
    else:
        print Fore.RED+'Wrong Input' 

    init() 
except:
    print "[!] Try Again.." 
    time.sleep(2)
    sys.exit() 
init()
    












