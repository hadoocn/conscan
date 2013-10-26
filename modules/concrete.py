#!/usr/bin/python

import httplib, string, sys
from modules import cmsvulns

bold = '\033[1m'
normal = '\033[0m'

## Dection function
def detect(target, dir, ssl):
    try:
        if ssl == True: ## Enables SSL
            conn = httplib.HTTPSConnection(target)
            conn.request("GET", dir)
            response = conn.getresponse()
            data = response.read()
            conn.close()

        else: ## Uses plain-text HTTP
            conn = httplib.HTTPConnection(target)
            conn.request("GET", dir)
            response = conn.getresponse()
            data = response.read()
            conn.close()

        for line in string.split(data, '\n'):
            if 'generator' in line:
                ver = line.split("\"")
                version = ver[3].split(" ")

		if version[0] == 'concrete5':
            		if version.count(1) == 2:
				print "Found", version[0], "at version", version[2], "via generator tag"
                    		cmsvulns.vulncheck(version[2])
				break
			else:
				print "Found", version[0],  "installation"
		    		break
		else:
		    print "Not running concrete5!"
		    sys.exit(0)


	if not "/concrete/css/" in data:
		print "concrete5 installation not detected"
		sys.exit(0)

    except Exception, IndexError:
	pass

    except Exception, error:
	print error
	sys.exit(1)


def enumerate(target, dir, ssl):
	
	fullpath(target, dir, ssl)


def fullpath(target, dir, ssl):
	try:

        	if ssl == True: ## Enables SSL
            		conn = httplib.HTTPSConnection(target)
            		conn.request("GET", dir + "concrete/blocks/content/editor_config.php")
            		response = conn.getresponse()
            		data = response.read()
            		conn.close()

        	else: ## Uses plain-text HTTP
            		conn = httplib.HTTPConnection(target)
            		conn.request("GET", dir + "concrete/blocks/content/editor_config.php")
            		response = conn.getresponse()
            		data = response.read()
            		conn.close()

		for line in string.split(data, '\n'):
			if 'Fatal error' in line:
				line = line.split(" ")
				line = line[8]
				length = len(line)
				length = length - 4
				fpd = line[3:length]

				print bold + "\nFull Path Disclosure found!\r" + normal
				print fpd + "\n"

	except Exception, error:
		print error


