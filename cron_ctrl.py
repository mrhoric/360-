#!/usr/bin/python

import os,re,sys

def ctrl_cron(job,ctrl):
    try:
        cronfile = open(r'/etc/crontab','r')
        content = ''
        for i in cronfile.readlines():
            if i.find(" "+job) != -1:
                if ctrl == "--start":
                    i = re.sub('^#','',i)
                elif ctrl == "--stop":
                    i = "#" + i
                elif ctrl == "--list": 
                    print i
            content += i
        cronfile.close()
        cronfile = open(r'/etc/crontab','w')
        cronfile.write(content)
        cronfile.close()
        os.system("crontab /etc/crontab")
    except Exception,e:
        print e


if __name__ == '__main__':
    ctrl_cron(sys.argv[1],sys.argv[2])
