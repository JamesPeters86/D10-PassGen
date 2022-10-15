#!/usr/bin/python3
import sys
filename = "english3.txt"
if len(sys.argv) == 2:
	filename = sys.argv[1]

fptr = open(filename, "r")

#count the lines and lengths
cnt = 0
lengs = [0] * 40
while True:

	line = fptr.readline()
	if "" == line:
		break
	line = line.strip()
	lengs[len(line)] += 1
	cnt = cnt+1

print("There are " + str(cnt) + " words")
cum = 0
for idx, leng in enumerate(lengs):
	cum = cum + leng
	if leng != 0:
		print(idx, leng, cum)

