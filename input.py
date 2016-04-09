#!/usr/bin/env python

import re
import urllib
from site_fetch import *
from vulnerability import *

def inputUrl():
	url = raw_input(color.bold+"  Enter the URL to scan: "+color.end)
	siteInfo(url)

	while(1):
		if "?" in url:
			print color.bold+"\n  Press 1 for Checking SQL Injection Vulnerability"+color.end
			print color.bold+"  Press 2 for Checking Cross-Site Scripting Vulnerability"+color.end
			print color.bold+"  Press 3 for Checking Remote Code Execution Vulnerability"+color.end
			print color.red+"  Press any other key to Exit"+color.end

			option = int(input("Enter Choice: "))
			if(option==1):
				sqliExploit(url)
			elif(option==2):
				xssExploit(url)
			elif(option==3):
				remoteCodeExec(url)
			else:
				exit(1)

		else:
			print color.red +"\n [Warning] "+ color.end + color.bold+"%s"%url +color.end + color.red +" is not a valid URL"+color.end
			print color.red +" [Warning] Enter a full URL like http://yoursite.com/page.php?id=value \n"+ color.end
			exit()


inputUrl()
