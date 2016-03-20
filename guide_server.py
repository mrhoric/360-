#!/usr/bin/python
import socket,threading,signal,errno

host = socket.gethostname()
port = 4000
maxclient = 40
bufsize = 1024
ERRORPATH = '/var/log/guide_server_error.log'
VALUEPATH = '/var/guide_value'
cdic = {}

def SigDeal(a,b):
    global cdic
    cdic = ReadValue() 

def ReadValue():
    cdic = {}
    try:
        f = open(VALUEPATH,'r')
        for i in f.readlines():
            tmp = i.split('=')
            cdic[tmp[0]] = tmp[1].replace('\n','')
    except IOError,e:
        f = open(ERRORPATH,'a+')
        f.writelines('ValueFile:'+str(e)+'\n')
    return cdic

def NetDeal(c):
    global cdic
    while 1:
        data = c.recv(bufsize)
        if not data:
            break
        if not cdic.has_key(str(data)):
            c.send('Null')
        else:
            c.send(cdic[str(data)])
    c.close()

if __name__ == '__main__':
    cdic = ReadValue()
    s = socket.socket()
    s.bind((host,port))
    s.listen(maxclient)
    signal.signal(signal.SIGUSR1,SigDeal)
    while 1:
        try:
            c,addr = s.accept()
            if c:
                t = threading.Thread(target=NetDeal,args=(c,))
                t.start()
        except Exception,e:
            if e.errno == errno.EINTR:
                continue
            f = open(ERRORPATH,'a+')
            print e 
            f.writelines(str(e) + '\n')
