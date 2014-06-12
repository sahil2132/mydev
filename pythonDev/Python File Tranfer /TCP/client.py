import socket   #for sockets
import sys 

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('localhost',7000)) 
except socket.error, msg:
	print 'Failed'
	sys.exit()

print 'Socket Created'
f=open('got.mp4','r')
while 1:
	data=f.read(1024*1024)
	if not data:
		s.send('')
		break
	s.send(data) 
	reply=s.recv(1)
	print reply,
	sys.stdout.flush()
s.close()