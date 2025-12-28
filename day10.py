with open("day10.txt", "r") as file:
	ans = 0
	for line in file:
		desiredconfig = 0
		buttonoptions = []
		joltagereqs = []
		acc = ""
		for char in line:
			if char == ')':
				starting = 0
				for num in acc.split(","):
					starting |= (1 << int(num))
				buttonoptions.append(starting)
				acc = ""
			elif char == "}":
				joltagereqs = [int(item) for item in acc.split(',')]
				acc = ""
			elif char == "]":
				starting = 0
				for i, char2 in enumerate(acc):
					if char2 == '#':
						starting |= (1 << i)
				desiredconfig = starting
				acc = ""
			elif char != " " and char != "{" and char != "(" and char != "[":
				acc += char
		
		# ============== PART 1 ==============
		# currmin = None
		# for i in range(2**(len(buttonoptions))):
		# 	curr = 0
		# 	popcount = 0
		# 	for j in range(len(buttonoptions)):
		# 		if i & (1 << j):
		# 			popcount += 1
		# 			curr ^= buttonoptions[j]
		# 	if (curr == desiredconfig):
		# 		if currmin == None or popcount < currmin:
		# 			currmin = popcount
		# ans += currmin

		# print(bin(desiredconfig))
		# print([bin(item) for item in buttonoptions])
		# print(currmin)
	print(ans)