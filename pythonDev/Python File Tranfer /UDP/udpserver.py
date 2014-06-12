import socket
import sys
import hashlib

idx=0
naklist=[]
k=0

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
	print 'Failed to create socket'
	sys.exit()
s.bind(('192.168.5.65',7000))
f=open('mysong.mp3','w')
ack='1'
nak='0'
address=None

print 'Listening...'
while 1:
	d=s.recvfrom(32)
	md5check=d[0]
	addr=d[1]
	d=s.recvfrom(125)
	msg=d[0]
	addr=d[1]
	if not msg:
		break
	md5ServerCheck = hashlib.md5()
	md5ServerCheck.update(msg)

	if md5ServerCheck.digest() == md5check and idx % 125 !=0:
		f.seek(idx*125)
		f.write(msg)
		s.sendto(ack , addr)
		address = addr
	if idx % 125 ==0 :
		naklist.append(idx)
		s.sendto(nak,addr)
	idx=idx+1

for iterator in naklist:
	print iterator,
	s.sendto(str(iterator), address)
	d=s.recvfrom(32)
	md5check=d[0]
	d=s.recvfrom(125)
	data=d[0]
	address=d[1]
	md5ServerCheck = hashlib.md5()
	md5ServerCheck.update(data)
	if md5ServerCheck.digest() == md5check:
		f.seek(iterator*125)
		f.write(data)
		s.sendto(ack, d[1])
		print 'is right'
	else:
		s.sendto(nak , d[1])
		s.append(iterator)
		print 'is wrong'		
s.sendto('', address)

s.close()
f.close()