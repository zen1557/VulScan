#!/usr/bin/python

import socket
import os
import sys

def retBanner(ip,port):
    try:
            socket.setdefaulttimeout(2)
            s = socket.socket()
            s.connect((ip,port))
            banner = s.recv(1024)
            return banner
    except:
            return

def checkVulns(banner, filename):
    f = open(filename, "r")
    for line in f.readline():
        if line.strip("\n") in banner:
            print '[+] Server is vulnerable: ' + banner.strip("\n")

def main():
        if len(sys.argv) == 2:
            filename = sys.argv[1]
            if not os.path.isfile(filename):
                print '[-] File Doesnt Exist!'
                exit(0)
            if not os.access(filename, os.R_OK):
                print '[-] Access Denied'
                exit(0)
        else:
            print '[-] Usuage: ' + str(sys.argv[0]) + " <vuln filename>"
            exit(0)
        portlist = [21,22,23,25,80,110,443,445,543]
        for x in range(129,134): 
            ip  = "192.168.54." + str(x)
            for port in portlist:
                banner = retBanner(ip,port)
                if banner:
                    print '[+] ' + ip + "/" + str(port) + " : " + banner
                    checkVulns(banner,filename)                






main()        