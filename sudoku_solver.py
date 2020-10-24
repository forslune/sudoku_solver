import math
input = [[0,0,0,0,0,0,0,0,0],
		 [0,0,1,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [1,0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0,0],
		 [7,8,9,0,0,0,0,1,0],
		 [3,4,5,0,1,0,0,0,0],
		 [0,1,2,0,0,0,0,0,0]]

print(input[1])
print(input[1][1])
print(input[1][:]-input[1][2])




def fill(input):
	for i in range(9):
		for j in range(9):
			for k in range(9):
				if input[i][j]==0:
					input[i][j]=k+1
				if input[i][j]==input[i] | input[i][j]==input[j] | input[i][j]==input[i][j]:
					print('hej')

	