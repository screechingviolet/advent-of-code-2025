with open("day4.txt", "r") as file:
	grid = []
	for line in file:
		clean_line = line.strip()
		grid.append(list(clean_line))
	ans = 0
	change = None
	while change != 0:
		change = 0
		for i, row in enumerate(grid):
			for j, item in enumerate(row):
				if item != '@':
					continue
				count = 0
				deltas = [-1, 0, 1]
				for delta in deltas:
					for delta2 in deltas:
						if delta == 0 and delta2 == 0:
							continue
						if i+delta >= 0 and i+delta < len(grid) and j+delta2 >= 0 and j+delta2 < len(row):
							count += (1 if grid[i+delta][j+delta2] == '@' else 0)
				if count < 4:
					change += 1
					grid[i][j] = '.'
		ans += change
print(ans)