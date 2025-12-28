adjust = 50
ans = 0
change = -1

with open("day1.txt", "r") as file:
	for line in file:
		# print(adjust)
		change = int(line[1:])
		if line[0] == 'R':
			if change < 100-adjust:
				# doesn't wrap around
				pass
			else:
				# wraps to 0
				ans += 1 + max(0, ((change-(100-adjust))//100))
				# print("ans: " + str(ans))
			adjust = (adjust+change)%100
		elif line[0] == 'L':
			if change < adjust:
				# doesn't wrap around
				pass
			else:
				# wraps to 0
				ans += (1 if adjust != 0 else 0) + max(0, ((change-(adjust))//100))
				# print("ans: " + str(ans))
			adjust = (adjust-change)%100
		# if adjust == 0:
		# 	ans += 1

print("ans: " + str(ans))