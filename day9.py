with open("day9.txt", "r") as file:
	coords = []
	all_x_coords = []
	# all_y_coords = []
	for line in file:
		splitsplat = line.split(",")
		coords.append([int(item) for item in splitsplat])
		all_x_coords.append(coords[-1][0])
		all_x_coords.append(coords[-1][1])
	print(len(coords))
	all_x_coords.sort()
	# all_y_coords.sort()
	# max_area = 0
	# for val in coords:
	# 	for val2 in coords:
	# 		max_area = max(max_area, (abs(val[0]-val2[0])+1)*(abs(val[1]-val2[1])+1))
	# print(max_area)

	idx = 0
	compress_x = {}
	decompress_x = {}
	for item in all_x_coords:
		if item in compress_x:
			continue
		else:
			compress_x[item] = idx
			decompress_x[idx] = item
			idx += 1

	# idx = 0
	# compress_y = {}
	# decompress_y = {}
	# for item in all_y_coords:
	# 	if item in compress_y:
	# 		continue
	# 	else:
	# 		compress_y[item] = idx
	# 		decompress_y[idx] = item
	# 		idx += 1
	print(compress_x)
	# print(compress_y)

	grid = [['.' for j in range(idx)] for i in range(idx)]
	for i, coord in enumerate(coords):
		before = coords[(i-1)%len(coords)]
		# after = coords[(i+1)%len(coords)]
		if coord[1] == before[1]:
			for k in range(compress_x[coord[0]], compress_x[before[0]], 1 if coord[0] < before[0] else -1):
				grid[compress_x[coord[1]]][k] = 'X'
		else:
			for j in range(compress_x[coord[1]], compress_x[before[1]], 1 if coord[1] < before[1] else -1):
				grid[j][compress_x[coord[0]]] = 'X'
		

		grid[compress_x[coord[1]]][compress_x[coord[0]]] = '#'

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] != '.':
				continue

			# print("still here", i, j)

			still_valid = False
			for k in range(i, -1, -1):
				# print(k, j)
				if grid[k][j] == 'X' or grid[k][j] == '#':
					still_valid = True
					break
			if not still_valid:
				continue

			# print("still here")

			still_valid = False
			for k in range(i, idx):
				if grid[k][j] == 'X' or grid[k][j] == '#':
					still_valid = True
					break
			if not still_valid:
				continue

			# print("still here")

			still_valid = False
			for k in range(j, -1, -1):
				if grid[i][k] == 'X' or grid[i][k] == '#':
					still_valid = True
					break
			if not still_valid:
				continue

			# print("still here")

			still_valid = False
			for k in range(j, idx):
				if grid[i][k] == 'X' or grid[i][k] == '#':
					still_valid = True
					break
			if not still_valid:
				continue

			# print("still here")

			grid[i][j] = 'X'

	# for i in range(len(grid)):
	# 	for j in range(len(grid[i])):
	# 		print(grid[i][j], end="")
	# 	print("")

	max_rect = 0

	for coord1 in coords:
		for coord2 in coords:
			# check rectangle
			i_direction = 1 if coord1[1] < coord2[1] else -1
			j_direction = 1 if coord1[0] < coord2[0] else -1
			invalid = False
			for i in range(compress_x[coord1[1]], compress_x[coord2[1]]+i_direction, i_direction):
				for j in range(compress_x[coord1[0]], compress_x[coord2[0]]+j_direction, j_direction):
					if grid[i][j] != 'X' and grid[i][j] != '#':
						invalid = True
						break
			if invalid:
				continue

			max_rect = max(max_rect, (abs(coord1[0]-coord2[0])+1)*(abs(coord1[1]-coord2[1])+1))


	print(max_rect)
