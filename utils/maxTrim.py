#!/usr/bin/python3
cnt = 7
filename = "english3.txt","r"
fptr = open(filename)

#count the lines and lengths
lengs = [0] * 40
while True:

	line = fptr.readline()
	if "" == line:
		break

	line = line.strip()
	if len(line) <= 2:
		continue

	if len(line) <= cnt:
		print(line)

