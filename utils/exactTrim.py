#!/usr/bin/python3
import sys
cnt = 7
filename = "english3.txt","r"
if len(sys.argv) > 1:
	cnt = int(sys.argv[1])

if len(sys.argv) == 3:
	filename = sys.argv[2]

fptr = open(filename)

#count the lines and lengths
lengs = [0] * 40
while True:

	line = fptr.readline()
	if "" == line:
		break

	line = line.strip()
	if len(line) == cnt:
		print(line)

