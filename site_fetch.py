#!/usr/bin/env python
import urllib  						#import the lib to open arbitary resources by URL
import re      						#import the regex lib
import time
import socket						#import classes that calls OS socket APIs
from urllib import FancyURLopener

class colors:						#class to display output in different colors
        def __init__(self):
                self.green = "\033[92m"
                self.blue = "\033[94m"
                self.bold = "\033[1m"
                self.yellow = "\033[93m"
                self.red = "\033[91m"
                self.end = "\033[0m"
color = colors()							#creating object for class colors

class UserAgent(FancyURLopener):			#class to define user agent of the fetching agent
	version = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'

useragent = UserAgent()

class HTTP_HEADER:							#assigning the host and server using predefine class
    HOST = "Host"
    SERVER = "Server"

def siteInfo(url):							#class to fetch the web server experiment
	# This function will print the server headers such as WebServer OS & Version
	print color.bold+" \n  Detecting the backend Technologies."+color.end
	opener = urllib.urlopen(url)				#defining opener object for the urllib to open the URL
	if opener.code == 200:												#checking the opener code -
		 print color.green+"  Status code: 200 OK"+color.end 			#if code=200 the web site can be reached
	if opener.code == 404:												#if code=404 page cannot be found
		 print color.red+"  Page was not found! Please check the URL \n"+color.end
		 exit()
	Server = opener.headers.get(HTTP_HEADER.SERVER)
	# HOST will split the HostName from the URL
	Host = url.split("/")[2]											#split the URL on 2nd '/' i.e http://
	print color.green+"  Host: " + str(Host) +color.end
	ip = socket.gethostbyname(str(Host))									#detecting the ip address of the website using socket-gethostbyname()
	print color.green+"  IP Addres: "+ ip +color.end
	print color.green+"  WebServer: " + str(Server) +color.end
	for item in opener.headers.items():											#deteting the php version of the webserver
	    for powered in item:
		sig = "x-powered-by"
		if sig in item:
		    print color.green+ "  " + str(powered).strip() + color.end
