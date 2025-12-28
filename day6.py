with open("day6.txt", "r") as file:
	lines = [line.replace('\n', '') for line in file]
	print([len(line) for line in lines])
	nums = []
	op = ""
	ans = 0
	for i in range(len(lines[0])):
		if all(lines[j][i] == ' ' for j in range(len(lines))):
			# calc last val
			# print(nums)
			# print(op)
			if op == '+':
				ans += sum(nums)
			elif op == '*':
				temp = 1
				for val in nums:
					temp *= val
				ans += temp
			nums = []
			op = ""
		else:
			if lines[-1][i] == '+':
				op = '+'
			elif lines[-1][i] == '*':
				op = '*'

			num = ""
			for j in range(len(lines)-1):
				num += lines[j][i]
			if num != "":
				nums.append(int(num))
	# calc last val
	if op == '+':
		ans += sum(nums)
	elif op == '*':
		temp = 1
		for val in nums:
			temp *= val
		ans += temp
	nums = []
	op = ""
	print(ans)


	# vals = []
	# for line in file:
	# 	vals.append([])
	# 	for item in line.split(" "):
	# 		stripped = item.strip()
	# 		if stripped != "":
	# 			vals[-1].append(stripped)
	# 	print(len(vals[-1]))
	# 	print(line)
	# ans = 0
	# for i in range(len(vals[0])):
	# 	if vals[4][i] == '+':
	# 		ans += int(vals[0][i]) + int(vals[1][i]) + int(vals[2][i]) + int(vals[3][i])
	# 	else:
	# 		ans += int(vals[0][i]) * int(vals[1][i]) * int(vals[2][i]) * int(vals[3][i])
	# print(ans)
