#!/usr/bin/python
import time

timewait = 3
lastinfo = {}
LOGPATH = "/var/log/sysinfo_recorder.log"
ERRORPATH = "/var/log/sysinfo_recorder_error.log"

def GetCpuInfo():
    f = open('/proc/stat','r')
    c = f.readlines()[0].replace('  ',' ')
    c = c.replace('\n','').split(' ')
    totalcput = int(c[1]) + int(c[2]) + int(c[3]) + int(c[4]) + \
        int(c[5]) + int(c[6]) + int(c[7]) + int(c[8]) + int(c[9])  
    return {'user':c[1],'nice':c[2],'system':c[3],'idle':c[4],'iowait':c[5],\
        'irq':c[6],'softirq':c[7],'stealstolen':c[8],'guest':c[9],'total':totalcput}


def CalcUse(linfo,ninfo):
    total = int(ninfo['total']) - int(linfo['total'])
    idle =  int(ninfo['idle']) - int(linfo['idle'])
    iowait = int(ninfo['iowait']) - int(linfo['iowait'])
    user = int(ninfo['user']) - int(linfo['user'])
    system = int(ninfo['system']) - int(linfo['system'])
    return {'cpuuse':(total-idle)/total*100, 'iowait':iowait/total*100, 'user':user/total*100, 'system':system/total*100}


def writelog(cdata):
    f = open(LOGPATH,'a+')
    s = "cpuu: %s  iowait: %s  user: %s  system: %s\n" %(cdata['cpuuse'],cdata['iowait'],cdata['user'],cdata['system'])
    f.writelines(s)

if __name__ == "__main__":
    while 1:
        try:
            if not lastinfo:
                lastinfo = GetCpuInfo()
                time.sleep(timewait)
            nowinfo = GetCpuInfo()
            time.sleep(timewait)
            cdata = CalcUse(lastinfo,nowinfo)
            lastinfo = nowinfo
            writelog(cdata)
        except Exception,e:
            log = open(ERRORPATH,'a+')
            print e
            log.writelines(str(e)+'\n')
