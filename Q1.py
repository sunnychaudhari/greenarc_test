def find_missing(elements): 
	arr = elements.split(" ")
	arr = map(int, arr)

	final_arr = []
	for k in range(min(arr), max(arr)+1):
		if k not in arr:
			final_arr.append(k)
	return final_arr


elements = raw_input("Enter elements seperated by space : \n") 
print find_missing(elements)