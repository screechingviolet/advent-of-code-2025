with open("day7.txt", "r") as file:
	beam_indices = {}
	ans = 0
	for line in file:
		new_ver = beam_indices.copy()
		for i, char in enumerate(line):
			if char == 'S':
				new_ver[i] = 1 # ways to reach this beam
			elif char == '^' and i in beam_indices and beam_indices[i] > 0:
				if i+1 not in new_ver:
					new_ver[i+1] = beam_indices[i]
				else:
					new_ver[i+1] += beam_indices[i] # this can't apply yet
				if i-1 not in new_ver:
					new_ver[i-1] = beam_indices[i]
				else:
					new_ver[i-1] += beam_indices[i]
				new_ver[i] = 0
				ans += 1
		beam_indices = new_ver.copy()
	print(ans)
	print(beam_indices)
	ans = 0
	for key, val in beam_indices.items():
		ans += val
	print(ans)