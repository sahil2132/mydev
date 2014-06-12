import socket
import sys

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
	print 'Failed to create socket'
	sys.exit()
s.bind(('localhost',7000))
f=open('myGOT.mp4','w')
send_msg='.'
print 'Listening...'
s.listen(2)
conn , addr = s.accept()
while 1:
	msg=conn.recv(1024*1024)
	if not msg:
		break
	f.write(msg)
	conn.send(send_msg)
conn.close()
s.close()