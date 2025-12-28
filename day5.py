with open("day5.txt", "r") as file:
	ranges = []
	fresh_ingreds = []
	for line in file:
		split_line = line.split("-")
		if len(split_line) == 2:
			ranges.append([int(item.strip()) for item in split_line])
		elif split_line[0].strip() != "":
			fresh_ingreds.append(int(split_line[0].strip()))
	
	ingreds = 0
	ranges = sorted(ranges)
	# print(ranges)
	last_begin = -1
	longest_endpoint = -1
	for i, rnge in enumerate(ranges):
		if i == 0 or (i != 0 and rnge[0] > longest_endpoint):
			if i != 0:
				# print(last_begin)
				# print(ranges[i-1][1])
				ingreds += longest_endpoint-last_begin+1
			last_begin = rnge[0]
			longest_endpoint = rnge[1]
		else:
			longest_endpoint = max(longest_endpoint, rnge[1])
	ingreds += longest_endpoint - last_begin + 1
	print(ingreds)


	# ingreds = 0
	# for ingred in fresh_ingreds:
	# 	is_fresh = False
	# 	for rnge in ranges:
	# 		if ingred >= rnge[0] and ingred <= rnge[1]:
	# 			is_fresh = True
	# 	if is_fresh:
	# 		ingreds += 1
	# print(ingreds)