def matrix_search(mat, n, input_x): 
	i = 0
	j = n - 1
	while ( i < n and j >= 0 ): 
		if (mat[i][j] == input_x ):
			return str("Found at "+ str([i+1,j+1]))
		if (mat[i][j] > input_x ): 
			j = j - 1
		else: 
			i = i + 1
	return "Element not found"

matrix = [ 	[10,20,30], 
        	[16,26,35], 
        	[27, 29, 37, 48], 
        	[32, 33, 39, 50] ] 

input_x = raw_input("Enter element in matrix : \n") 
print matrix_search(matrix, 3, int(input_x)) 
