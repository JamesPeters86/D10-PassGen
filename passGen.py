#!/usr/bin/python3
import sys
filename = "tokenList"
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
	cnt += 1

#We want an even probablity distribution. 
#This will give 3 numbers that can generate each token
#For example the first token will be picked by 0, count, 2 * count
#The second token will bepickedgen by 1, count + 1, and 2 * count + 1
#If we don't throw out rolls that are higher than 3 * count,
#the first several tokens will have 4 numbers that pick and thus will 
#have a 33% higher probablity of being picked. 
maxRoll = cnt * 3 - 1

print("There are " + str(cnt) + " different tokens")
if cnt > 3333:
	print("Only the first 3333 tokens will be used.")
	cnt = 3333
print("For each token, roll a d10 4 times. For 10 enter 0.")
print("If your number is greater than", maxRoll, "start over from the first roll")
print("Enter q when done");
print("Total Digits\t","Token")

#print the tokens along with a running count of the digits
digitCount = 0
while True:
	line = input("Number: ").strip()
	if "q" == line:
		break

	number = int(line);
	if number > maxRoll:
		print("Too big, retry!")
		continue

	# use modulo to wrap back around the list
	number = (number % cnt) + 1
	fptr.seek(0)
	idx = 0
	while idx < number:
		line = fptr.readline()
		idx += 1

	line = line.strip()
	digitCount += len(line)
	print(digitCount, "\t\t", line)

