# xip
Resolves the External IP using a default URL

xIP.exe v2.4 - Resolve your eXternal IP address : (c)gfragkos 2012

usage: xip [url]
   without parameters       Resolves External IP using a default URL*
   url*                     i.e. http://www.example.com/myip.php
                            The URL is expected to be a continuous stream of
                            characters without any spaces, nor within quotes.
                            The given URL must point at a webpage which is
                            capable of resolving and displaying your IP address.
   -x                       Display LAN IP Address


It is very usuful to have a quick and convinient way to display the External IP (WAN)
from the command line, without having to use your webbrowser. I made two version, 
one to be run under Windows (xip.exe) and one for Linux (xip.py) using Python. 

