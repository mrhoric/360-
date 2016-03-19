#!/usr/bin/python
import socket,threading

host = socket.gethostname()
port = 4000
maxclient = 40
bufsize = 1024
ERRORPATH = '/var/log/guide_server_error.log'
VALUEPATH = '/var/guide_value'

def ReadValue():
    cdic = {}
    f = open(VALUEPATH,'r')
    for i in f.readlines():
        tmp = i.split('=')
        cdic[tmp[0]] = tmp[1].replace('\n','')
    return cdic

def NetDeal(c,cdic):
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
    try:
        cdic = ReadValue()
        s = socket.socket()
        s.bind((host,port))
        s.listen(maxclient)
        while 1:
            c,addr = s.accept()
            if c:
                t = threading.Thread(target=NetDeal,args=(c,cdic))
                t.start()

    except Exception,e:
        f = open(ERRORPATH,'a+')
        print e 
        f.writelines(str(e) + '\n')
