def paths_from_to(start, end, neighbors):
	visited = set()
	visited.add(start)
	ans = 0
	visitstk = [start]
	while len(visitstk) != 0:
		top = visitstk[-1]
		visited.add(top)
		visitstk.pop()
		if top in neighbors:
			for neighbor in neighbors[top]:
				if neighbor == end:
					print(ans)
					ans += 1
				# elif neighbor != start:
				else:
					visitstk.append(neighbor)
	return ans

ans = 0
maybes = 0
paths_current_count = {}
paths_meeting_cond_to_out = {}
neighbors = {}

def sophisticated_and_dp(visitstk):
	global paths_current_count
	global paths_meeting_cond_to_out
	# need to pass it out instead of passing it in
	# i.e. return {x, y, z, w} based on node x to out
	# then parent can take that based on if it is dac/fft or any other node (then the stats would just add up)
	top = visitstk
	paths_current_count[top[0]] = [0, 0, 0, 0] # none, just dac, just fft, both
	if top[0] in neighbors:
		for neighbor in neighbors[top[0]]:
			if neighbor == "out":
				paths_current_count[top[0]][0] += 1
			else:
				if neighbor not in paths_meeting_cond_to_out:
					sophisticated_and_dp([neighbor])
				for i in range(4):
					paths_current_count[top[0]][i] += paths_meeting_cond_to_out[neighbor][i]

	if top[0] == "fft":
		paths_meeting_cond_to_out[top[0]] = [0, 0, paths_current_count[top[0]][0]+paths_current_count[top[0]][2], paths_current_count[top[0]][1]+paths_current_count[top[0]][3]]
	elif top[0] == "dac":
		paths_meeting_cond_to_out[top[0]] = [0, paths_current_count[top[0]][0]+paths_current_count[top[0]][1], 0, paths_current_count[top[0]][2]+paths_current_count[top[0]][3]]
	else:
		paths_meeting_cond_to_out[top[0]] = paths_current_count[top[0]]

with open("day11.txt", "r") as file:
	for line in file:
		contents = line.split(":")
		for neighbor in contents[1].strip().split(" "):
			if contents[0] not in neighbors:
				neighbors[contents[0]] = [neighbor]
			else:
				neighbors[contents[0]].append(neighbor)

	sophisticated_and_dp(["svr", False, False])
	print(paths_current_count["svr"][3])

	# ===========================================

	# can either do dac --> fft or fft --> dac
	# can revisit?
	# print(paths_from_to("svr", "dac", neighbors))
	# print(paths_from_to("dac", "fft", neighbors))
	# print(paths_from_to("fft", "out", neighbors))

	# print(paths_from_to("you", "out", neighbors))
	# ans = 0
	# maybes = 0
	# visitstk = [["svr", False, False]]
	# while len(visitstk) != 0:
	# 	top = visitstk[-1]
	# 	visitstk.pop()
	# 	if top[0] in neighbors:
	# 		for neighbor in neighbors[top[0]]:
	# 			if neighbor == "out":
	# 				maybes += 1
	# 				if top[2] == True:
	# 					print("HIII")
	# 				if maybes%1000000 == 0:
	# 					print(maybes)
	# 					print(top)
	# 				if top[1] and top[2]:
	# 					print("Found ending path")
	# 					ans += 1
	# 			else:
	# 				if neighbor == "svr":
	# 					print("back here...")
	# 				if neighbor == "akv":
	# 					print("HELLO THERE")
	# 				visitstk.append([neighbor, (top[1] or neighbor == "dac"), (top[2] or neighbor == "fft")])
	# print(maybes)
	# print(ans)

	
