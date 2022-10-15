#!/usr/bin/python3
# Script to select special characters
spec = "`~!@#$%^&*()_-+=[{]}:;\"'<,>.?/"
num = len(spec)
maxRoll = 3 * num - 1
print("Roll twice. Max is: ", maxRoll)
while True:
	line = input("Roll: ").strip()
	if "q" == line:
		break

	roll = int(line) % num
	print(spec[roll])
