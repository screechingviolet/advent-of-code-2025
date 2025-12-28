invalid = 0

with open("day2.txt", "r") as file:
	for line in file:
		ranges = line.split(",")
		for rg in ranges:
			nums = rg.split("-")
			for i in range(int(nums[0]), int(nums[1])+1):
				str_ver = str(i)
				for repeat_len in range(1, len(str_ver)):
					if len(str_ver)%repeat_len != 0:
						continue
					repeat_str = str_ver[:repeat_len]
					is_valid = False
					for start in range(0, len(str_ver), repeat_len):
						# print(str_ver[start:start+repeat_len] + " " + repeat_str)
						if str_ver[start:start+repeat_len] != repeat_str:
							# print("hi")
							is_valid = True
							break
					if not is_valid:
						# print(i)
						invalid += i
						break

				# if str_ver[:len(str_ver)//2] == str_ver[len(str_ver)//2:]:
				# 	invalid += i

print(invalid)