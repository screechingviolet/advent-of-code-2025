def num_hashes(shape):
	count = 0
	for line in shape:
		count += line.count('#')
	return count



with open("day12.txt", "r") as file:
	shapes = []
	shapes_count = []
	appendingshape = False
	curr_shape = []
	# dimensions = {}
	def_impossible = 0
	possible_ans = 0
	for line in file:
		if line.strip() == "":
			appendingshape = False
			if curr_shape != []:
				shapes.append(curr_shape)
				shapes_count.append(num_hashes(curr_shape))
				curr_shape = []
			continue

		split_by_colon = line.split(":")
		if appendingshape:
			curr_shape.append(line.strip())
		elif len(split_by_colon) > 1:
			if "x" not in split_by_colon[0]:
				assert not appendingshape
				appendingshape = True
			else:
				# activate PHASE 2
				dimensions = [int(item) for item in split_by_colon[0].strip().split("x")]
				reqs = [int(item) for item in split_by_colon[1].strip().split(" ")]
				if sum([reqs[i]*shapes_count[i] for i in range(len(reqs))]) > dimensions[0]*dimensions[1]:
					def_impossible += 1
					continue

				# actually check


	print(def_impossible)
	print(possible_ans)

