#!/usr/bin/env python
import urllib
import re
import time
import socket
from urllib import FancyURLopener

class colors:
        def __init__(self):
                self.green = "\033[92m"
                self.blue = "\033[94m"
                self.bold = "\033[1m"
                self.yellow = "\033[93m"
                self.red = "\033[91m"
                self.end = "\033[0m"
color = colors()

class UserAgent(FancyURLopener):
	version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'

useragent = UserAgent()

class HTTP_HEADER:
    HOST = "Host"
    SERVER = "Server"

def siteInfo(url):
	# This function will print the server headers such as WebServer OS & Version
	print color.bold+" \n  Detecting the backend Technologies."+color.end
	opener = urllib.urlopen(url)
	if opener.code == 200:
		 print color.green+"  Status code: 200 OK"+color.end
	if opener.code == 404:
		 print color.red+"  Page was not found! Please check the URL \n"+color.end
		 exit()
	Server = opener.headers.get(HTTP_HEADER.SERVER)
	# HOST will split the HostName from the URL
	Host = url.split("/")[2]
	print color.green+"  Host: " + str(Host) +color.end
	ip = socket.gethostbyname(str(Host))
	print color.green+"  IP Addres: "+ ip +color.end
	print color.green+"  WebServer: " + str(Server) +color.end
	for item in opener.headers.items():
	    for powered in item:
		sig = "x-powered-by"
		if sig in item:
		    print color.green+ "  " + str(powered).strip() + color.end
