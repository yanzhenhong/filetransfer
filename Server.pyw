#-*- coding:gb2312 -*-
import socket
import time
import os

if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('192.168.110.132',31000))
    sock.listen(1)
    connection,address = sock.accept()
    print(address)
    while True:
        try:
            connection.settimeout(500000)
            buf = connection.recv(1024)
            filename = buf.replace('\n', '')
            print(filename)
            filesize = os.path.getsize(filename)
            print('filesize:' + str(filesize))
            connection.send(str(filesize))
            connection.send('\n')
            input = open(filename, 'rb')
            len = 0
            while len < filesize :
                byte = input.read(1)
                len += 1
                connection.send(byte)
            input.close()
            connection.send('EOF\n')
            break
        except socket.timeout:
             print('time out')
    time.sleep(1000000)
    #connection.close()

