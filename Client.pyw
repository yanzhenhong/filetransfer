#-*- coding:gb2312 -*-
import socket
import sys

if __name__ == '__main__':
    sock = socket.socket()
    filename=sys.argv[1]
    sock.connect(('192.168.110.132',31000))
    print('connect ok')
    sock.send((filename).encode())
    sock.send(('\n').encode())
    print('send filenane')
    filesize = ''
    while True:
        data = sock.recv(1).decode()
        filesize += data
        if filesize.find('\n') > 0 :
            filesize = filesize.replace('\n','')
            filesize = filesize.strip()
            break
    print("filesize:"+filesize)
    output = open(filename, 'wb')
    b_recvfinish = False
    len = 0
    while len < int(filesize) :
        data = sock.recv(1)
        len += 1
        output.write(data)
    output.close()
    sock.close()


