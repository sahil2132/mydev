
def check(b,p,q,idx):
	for i in range(0,9):
		if b[i][q] == idx:
			return False
	for j in range(0,9):
		if b[p][j] == idx:
			return False
	row = int(p/3)
	col = int(q/3)
	for i in range(row*3,row*3+3):
		for j in range(col*3,col*3+3):
			if b[i][j] == idx:
				return False
	return True

def findEmpty(a):
	for i in range(0,9):
		for j in range(0,9):
			if a[i][j] == 0:
				return (i,j)
	return (-1,-1)


def sudoku(b):
	(i,j)=findEmpty(b)
	if j == -1:
		return True
	for idx in range(1,10):
		if check(b,i,j,idx):
			b[i][j]=idx
			if sudoku(b):
				return True
			else:
				b[i][j]=0
		if idx == 9:
			return False
	return True

a=[[3, 0, 6, 5, 0, 8, 4, 0, 0],
   [5, 2, 0, 0, 0, 0, 0, 0, 0],
   [0, 8, 7, 0, 0, 0, 0, 3, 1],
   [0, 0, 3, 0, 1, 0, 0, 8, 0],
   [9, 0, 0, 8, 6, 3, 0, 0, 5],
   [0, 5, 0, 0, 9, 0, 6, 0, 0],
   [1, 3, 0, 0, 0, 0, 2, 5, 0],
   [0, 0, 0, 0, 0, 0, 0, 7, 4],
   [0, 0, 5, 2, 0, 6, 3, 0, 0]]

print a
print 'Solving........'

if sudoku(a):
	print 'Solution Found'
	print a