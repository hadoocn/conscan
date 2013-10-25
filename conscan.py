#!/usr/bin/python

## import modules
try:
	import argparse
	import httplib
	import sys
	from modules import concrete

except Exception, error:
	print error
	sys.exit(1)

## Banner
def banner():
	print """
//========================================================================\\\\
||                                                                        ||
|| TITLE                                                                  ||
|| Concrete CMS blackbox vulnerability scanner              	          ||
||                                                                        ||
|| VERSION                                                                ||
|| 0.5                                                                    ||
||                                                                        ||
|| AUTHOR                                                                 ||
|| TheXero | thexero@nullsecurity.net                                     ||
||                                                                        ||
|| WEBSITE                                                                ||
|| www.thexero.co.uk | www.nullsecurity.net                               ||
||                                                                        ||
\\\\========================================================================//
    """

## Argument Parser
def arg_parser():
	parser = argparse.ArgumentParser(add_help=True,
	epilog='Example: ./%(prog)s -t https://www.thexero.co.uk:8443/concrete/ -e')

	parser.add_argument('-t', dest='target', help='Target IP / Domain', required='yes')
	parser.add_argument('-e', action='store_true', help='Perform enumeration')

	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit(2)

	args = parser.parse_args()
	target = args.target


	if target.startswith("https://"):
		ssl = True
		target = target[8:]

	elif target.startswith("http://"):
		ssl = False
		target = target[7:]

	else:
		ssl = False

	if "/" in target:
		temp = target.split("/")
		target = temp[0]

#		length = len(temp)		
#		length = length 

		temp = temp[1:]

		dir = '/'
		for item in temp:
			dir = dir + item + '/' 

	else:
		dir = '/'	

	if args.e:
        	enumerate = True
	else:
        	enumerate = False

	concrete.detect(target, dir, ssl)
	
	if enumerate == True:
		concrete.enumerate(target, dir, ssl)


## Program startup
if __name__ == '__main__':

	banner()
	arg_parser()
	sys.exit(0)

