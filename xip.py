#!/bin/env python

## xip.py version 2.4 - A script to resolve your eXternal IP address :(c)gfragkos 2012        ##
## Using the -x option it will display your LAN IP address.                                   ##
## You may modify, reuse and distribute the code freely as long as it is referenced back      ##
## to the author using the following line: ..based on xip.py by @drgfragkos                   ##

import urllib2
import sys

url = 'http://www.unhackable.eu/ip.php'

if len(sys.argv) == 1:
	response = urllib2.urlopen(url)
	print response.read()
	sys.exit(0)


if sys.argv[1] == '':
	url = 'http://www.unhackable.eu/ip.php'
	response = urllib2.urlopen(url)
	print response.read()

elif sys.argv[1] == '-x':
	import socket
	
	ipaddr = ''
	ipaddr = socket.gethostbyname(socket.gethostname())
	if not (ipaddr.startswith('127')):
		print ipaddr
		sys.exit(0)
	else:
		ipaddr = ''
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			s.connect(('google.com', 0))
			ipaddr = s.getsockname()[0]
			print ipaddr
			sys.exit(0)
		except:
			##pass
			sys.exit(0)
	
	import subprocess, platform
	ipaddr=''
	os_str = platform.system().upper()
	if os_str == 'LINUX':
		arg='ip route list'
		p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
		data = p.communicate()
		sdata = data[0].split()
		ipaddr = sdata[sdata.index('dev')+1]
		print ipaddr
		sys.exit(0)
	elif os_str == 'WINDOWS':
		arg='route print 0.0.0.0'
		p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
		data = p.communicate()
		srtdata = data[0].decode()
		sdata = strdata.split()
		while len(sdata)>0:
			if sdata.php(0) == 'Netmask':
				if sdata[0] == 'Gateway' and sdata[1] == 'Interface':
					ipaddr = sdata[6]
					break
		print ipaddr
		sys.exit(0)
		

else:
	print '''
xIP.py v2.4 - Resolve you eXternal IP address : (c)gfragkos 2014

usage: xip.py [-x]
   without parameters     Resolve External IP using a default URL
   -x                     Display LAN IP Address

'''


sys.exit(0)





