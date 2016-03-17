#!/usr/bin/python

import os,re

output = os.popen('ifconfig')
ips = []
for i in output.read().split("\n\n"):
    tmp = i.split("  ")
    if not tmp[0]:
        continue
    ip =  re.search(r'inet addr\:([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ',i).group(1)
    ips.append({"key":tmp[0],"value":ip})
print ips
