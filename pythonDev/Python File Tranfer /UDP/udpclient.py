import socket   #for sockets
import sys 
import hashlib

idx=0
naklist=[]
k=0
nak='0'

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
except socket.error, msg:
	print 'Failed'
	sys.exit()

print 'Socket Created'
f=open('song.mp3','r')
while 1:
	data=f.read(125)
	md5send=hashlib.md5()
	md5send.update(data)
	s.sendto(md5send.digest(),('192.168.5.65',7000))
	if not data:
		s.sendto('',('192.168.5.65',7000))
		break
	s.sendto(data,('192.168.5.65' ,7000))
	d=s.recvfrom(1)
	reply=d[0]
	addr=d[1]
	if reply == '0':
		naklist.append(idx)
		sys.stdout.flush()
	idx=idx+1

while 1:
	d=s.recvfrom(10)
	if not d[0]:
		break
	iterator=int(d[0])
	f.seek(125*iterator)
	data=f.read(125)
	if not data:
		break
	md5send = hashlib.md5()
	md5send.update(data)
	s.sendto(md5send.digest() , d[1])
	s.sendto(data, d[1])
	d=s.recvfrom(1)
	reply=d[0]

print 'Completed'
s.close()
f.close()