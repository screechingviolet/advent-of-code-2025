ans = 0
with open("day3.txt", "r") as file:
	for line in file:
		liine = line.strip()
		idx_in_line = 0
		val = ""
		for digit in range(12, 0, -1):
			curr_max = "0"
			max_idx = -1
			while idx_in_line < len(liine)-digit:
				if liine[idx_in_line] > curr_max:
					curr_max = liine[idx_in_line]
					max_idx = idx_in_line
				idx_in_line += 1
			if int(liine[idx_in_line]) > int(curr_max):
				curr_max = liine[idx_in_line]
				max_idx = idx_in_line
			# print(liine[idx_in_line] + " AND " + curr_max)
			idx_in_line = max_idx+1
			val += curr_max
		ans += int(val)
		# print(val)

		# curr_max = 0
		# for i, fst in enumerate(line):
		# 	for j in range(i+1, len(line)):
		# 		if int(fst + line[j]) > curr_max:
		# 			curr_max = int(fst+line[j])
		# ans += curr_max

		# suffix_max = [line[len(line)-1] for i in range(len(line))]
		# for i in range(len(line)-2, -1, -1):
		# 	suffix_max[i] = max(suffix_max[i+1], line[i])
		# for i in range(0, len(suffix_max)):
		# 	if line[i] == suffix_max[0]:
		# 		print(int(suffix_max[0]+suffix_max[i+1]))
		# 		ans += int(suffix_max[0]+suffix_max[i+1])
print(ans)