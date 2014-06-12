

import os
import hashlib

'''
try:
	f_read = open('song.mp3','r')
	f_write = open('mysong.mp3','w')
	print os.path.getsize('song.mp3')
except:
	print 'failed to getsize'
	sys.exit()
while 1:	
	data=f_read.read(1024)
	if not data:
		break
	f_write.write(data)
f_write.close()
'''
print hashlib.md5(open('sahil.txt').read()).hexdigest()
