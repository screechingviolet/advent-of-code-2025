def parent(x, pars):
	if pars[x] == x:
		return x
	else:
		pars[x] = parent(pars[x], pars)
		return pars[x]

def merge(x, y, pars, size, num_groups):
	if not same_group(x, y, pars):
		root_x = parent(x, pars)
		root_y = parent(y, pars)
		pars[root_x] = root_y
		size[root_y] += size[root_x]
		num_groups -= 1
	return num_groups

def same_group(x, y, pars):
	return parent(x, pars) == parent(y, pars)

with open("day8.txt", "r") as file:
	coords = []
	for line in file:
		splitsplat = line.split(",")
		coords.append([int(item.strip()) for item in splitsplat])
	matrix = [[-1 for i in coords] for j in coords]
	for i, fst in enumerate(coords):
		for j, snd in enumerate(coords):
			matrix[i][j] = (fst[0]-snd[0])**2 + (fst[1]-snd[1])**2 + (fst[2]-snd[2])**2
	# print(matrix)
	how_many_top = 1000
	pars = [i for i in range(len(coords))]
	size = [1 for i in coords]
	num_groups = len(coords)
	# for rep in range(how_many_top):
	while num_groups != 1:
		# if (rep%100 == 0):
		# 	print(rep)
		min_dist = float("inf")
		rel_i = -1
		rel_j = -1
		for i in range(len(coords)):
			for j in range(i+1, len(coords)):
				if matrix[i][j] < min_dist:
					rel_i = i
					rel_j = j
					min_dist = matrix[i][j]
		# print(size)
		matrix[rel_i][rel_j] = float("inf")
		num_groups = merge(rel_j, rel_i, pars, size, num_groups)
	print(coords[rel_i], coords[rel_j])

	for i in range(len(coords)):
		parent(i, pars)
		
	for i in range(len(coords)):
		if i not in pars:
			size[i] = 0

	size.sort()
	print(size[-1]*size[-2]*size[-3])

