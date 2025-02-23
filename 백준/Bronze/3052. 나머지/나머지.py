arr = []

new_arr = []

for _ in range(10):

	arr.append(int(input()))	

for ele in arr:

	new_arr.append(ele % 42)

	

print(len(set(new_arr)))