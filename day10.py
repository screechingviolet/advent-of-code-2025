from scipy.optimize import linprog

with open("day10.txt", "r") as file:
	ans = 0
	for line in file:
		desiredconfig = 0
		buttonoptions = [] # become a matrix where these are the columns
		joltagereqs = [] # these are the answers
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

		# linprog
		'''
		minimize [1...1] @ x where x is a vector of button presses of each button
		such that

		A_ub @ x <= b_ub
		A_eq (matrix of effects of each button) @ x == b_eq [joltage_reqs]
		lb <= x <= ub
		'''
		c = [1 for i in buttonoptions]
		A = [[0 for j in buttonoptions] for i in joltagereqs]
		for j, opt in enumerate(buttonoptions):
			for i in range(len(joltagereqs)):
				if (1 << i) & opt:
					A[i][j] = 1

		res = linprog(c, A_eq=A, b_eq=joltagereqs, integrality=1)
		for thing in res.x:
			ans += thing
		print(res.x)
		
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